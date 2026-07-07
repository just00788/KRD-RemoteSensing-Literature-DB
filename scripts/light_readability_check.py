#!/usr/bin/env python3
"""Create a light readability check for 15 priority literature PDFs."""

from __future__ import annotations

import csv
import re
from collections import Counter
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path

from pypdf import PdfReader


REPO_ROOT = Path(__file__).resolve().parents[1]
DATABASE_PATH = REPO_ROOT / "database" / "literature_database_cleaned.csv"
OUTPUT_CSV = REPO_ROOT / "database" / "priority_reading_list.csv"
OUTPUT_MD = REPO_ROOT / "docs" / "literature" / "synthesis" / "light_readability_check.md"


CSV_FIELDS = [
    "paper_id",
    "title",
    "year",
    "language",
    "pdf_path",
    "topic_group",
    "method_group",
    "readability_status",
    "use_nature_reader_skill",
    "reason_for_priority",
    "notes",
]


@dataclass
class CheckResult:
    row: dict[str, str]
    selected_pdf: str
    pdf_exists: bool
    first_two_pages_extractable: bool
    abstract_found: bool
    methods_found: bool
    results_found: bool
    figures_tables_found: bool
    references_found: bool
    chinese_mojibake: bool
    likely_scanned: bool
    readability_status: str
    use_nature_reader_skill: str
    reason_for_priority: str
    notes: str
    first_two_char_count: int
    sampled_char_count: int


def read_rows() -> list[dict[str, str]]:
    with DATABASE_PATH.open("r", encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def has_cjk(text: str) -> bool:
    return bool(re.search(r"[\u4e00-\u9fff]", text or ""))


def priority_score(row: dict[str, str]) -> int:
    text = " ".join(
        [
            row.get("title", ""),
            row.get("topic_group", ""),
            row.get("method_group", ""),
            row.get("journal_or_source", ""),
            row.get("notes", ""),
        ]
    ).lower()
    score = 0
    weights = [
        ("bare_rock_fraction_fbr", 10),
        ("bare rock", 10),
        ("bedrock", 8),
        ("fbr", 10),
        ("lsmm_mesma_sma", 10),
        ("mesma", 10),
        ("lsmm", 10),
        ("sma", 6),
        ("rocky_desertification_classification", 9),
        ("rocky desertification", 9),
        ("karst rocky desertification", 10),
        ("machine_learning", 7),
        ("classification", 7),
        ("rf", 5),
        ("random forest", 6),
        ("svm", 6),
        ("deep_learning_segmentation", 8),
        ("deeplabv3+", 8),
        ("u-net", 7),
        ("fcn", 6),
        ("dem_topography", 6),
        ("dem", 5),
        ("topograph", 5),
        ("remote sensing", 5),
        ("remote sensing", 5),
    ]
    for needle, weight in weights:
        if needle in text:
            score += weight
    if row.get("pdf_path"):
        score += 20
    if row.get("title"):
        score += 4
    if row.get("doi"):
        score += 2
    if row.get("metadata_status") == "pdf_only":
        score -= 4
    if "review" in row.get("topic_group", ""):
        score -= 2
    return score


def priority_reason(row: dict[str, str]) -> str:
    reasons = []
    topic = row.get("topic_group", "")
    methods = row.get("method_group", "")
    title = row.get("title", "").lower()
    notes = row.get("notes", "").lower()
    combined = " ".join([topic, methods, title, notes])
    if "rocky_desertification_classification" in topic or "rocky desertification" in combined:
        reasons.append("KRD classification/information extraction")
    if "bare_rock_fraction_fbr" in topic or any(k in combined for k in ["bare rock", "bedrock", "fbr"]):
        reasons.append("FBR/bare-rock fraction")
    if any(k in methods for k in ["LSMM", "SMA", "MESMA"]) or any(k in combined for k in ["lsmm", "mesma", "spectral mixture"]):
        reasons.append("LSMM/SMA/MESMA")
    if any(k in methods for k in ["RF", "SVM", "BPNN"]) or "machine_learning" in topic:
        reasons.append("machine-learning classification")
    if any(k in methods for k in ["DeepLabV3+", "U-Net", "FCN"]) or "deep_learning_segmentation" in topic:
        reasons.append("semantic segmentation baseline/model")
    if "DEM" in methods or "dem_topography" in topic:
        reasons.append("DEM/topographic factors")
    if "remote sensing" in combined:
        reasons.append("Remote Sensing/KRD relevance")
    return "; ".join(dict.fromkeys(reasons)) or "priority selected from topic/method relevance"


def choose_pdf_path(row: dict[str, str]) -> str:
    paths = [part.strip() for part in row.get("pdf_path", "").split(";") if part.strip()]
    for relative in paths:
        if (REPO_ROOT / relative).exists():
            return relative
    return paths[0] if paths else ""


def extract_sample_text(pdf_path: Path) -> tuple[str, str, int, str]:
    reader = PdfReader(str(pdf_path))
    page_count = len(reader.pages)
    first_indexes = list(range(min(2, page_count)))
    sample_indexes = set(first_indexes)
    if page_count >= 4:
        sample_indexes.update([page_count - 2, page_count - 1])
    if page_count >= 6:
        mid = page_count // 2
        sample_indexes.update([max(0, mid - 1), mid])

    first_text_parts = []
    sample_text_parts = []
    errors = []
    for idx in sorted(sample_indexes):
        try:
            text = reader.pages[idx].extract_text() or ""
        except Exception as exc:  # pragma: no cover - depends on PDF internals
            text = ""
            errors.append(f"page {idx + 1}: {type(exc).__name__}")
        if idx in first_indexes:
            first_text_parts.append(text)
        sample_text_parts.append(text)
    return "\n".join(first_text_parts), "\n".join(sample_text_parts), page_count, "; ".join(errors)


def contains_any(text: str, patterns: list[str]) -> bool:
    return any(re.search(pattern, text, flags=re.I) for pattern in patterns)


def mojibake_detected(text: str, expected_chinese: bool) -> bool:
    if not expected_chinese:
        return False
    if "�" in text:
        return True
    suspicious = sum(text.count(ch) for ch in ["鐭", "鍖", "涓", "绌", "閬", "锛", "鏂"])
    cjk_count = len(re.findall(r"[\u4e00-\u9fff]", text))
    return suspicious >= 5 and suspicious > max(3, cjk_count // 5)


def classify_readability(
    pdf_exists: bool,
    first_two_extractable: bool,
    sampled_chars: int,
    likely_scanned: bool,
    mojibake: bool,
    has_title: bool,
) -> str:
    if not pdf_exists:
        return "pdf_missing"
    if likely_scanned:
        return "needs_ocr"
    if not first_two_extractable:
        return "needs_manual_check"
    if mojibake or sampled_chars < 1200 or not has_title:
        return "usable_with_caution"
    return "ready"


def check_row(row: dict[str, str]) -> CheckResult:
    relative_pdf = choose_pdf_path(row)
    pdf_exists = bool(relative_pdf) and (REPO_ROOT / relative_pdf).exists()
    first_text = ""
    sample_text = ""
    page_count = 0
    extraction_errors = ""

    if pdf_exists:
        try:
            first_text, sample_text, page_count, extraction_errors = extract_sample_text(REPO_ROOT / relative_pdf)
        except Exception as exc:  # pragma: no cover - depends on PDF internals
            extraction_errors = f"{type(exc).__name__}: {exc}"

    first_chars = len(first_text.strip())
    sample_chars = len(sample_text.strip())
    first_two_extractable = first_chars >= 200
    likely_scanned = pdf_exists and sample_chars < 200
    expected_chinese = row.get("language") == "Chinese" or has_cjk(row.get("title", ""))
    mojibake = mojibake_detected(first_text + "\n" + sample_text, expected_chinese)
    lower_sample = sample_text.lower()
    lower_first = first_text.lower()

    abstract_found = contains_any(lower_first, [r"\babstract\b", r"摘要"])
    methods_found = contains_any(lower_sample, [r"\bmethod(s)?\b", r"\bmaterials and methods\b", r"methodology", r"方法", r"研究方法"])
    results_found = contains_any(lower_sample, [r"\bresult(s)?\b", r"结果", r"实验结果"])
    figures_tables_found = contains_any(lower_sample, [r"\bfig(ure)?\.?\s*\d+", r"\btable\s*\d+", r"图\s*\d+", r"表\s*\d+"])
    references_found = contains_any(lower_sample, [r"\breferences\b", r"参考文献"])
    status = classify_readability(pdf_exists, first_two_extractable, sample_chars, likely_scanned, mojibake, bool(row.get("title")))
    use_reader = "yes" if status in {"ready", "usable_with_caution"} else "no"

    notes = [
        f"sampled_pages=first2+middle2+last2_or_available",
        f"page_count={page_count or 'unknown'}",
        f"first_two_chars={first_chars}",
        f"sampled_chars={sample_chars}",
        f"abstract={abstract_found}",
        f"methods={methods_found}",
        f"results={results_found}",
        f"figures_tables={figures_tables_found}",
        f"references={references_found}",
        f"chinese_mojibake={mojibake}",
        f"likely_scanned={likely_scanned}",
    ]
    if extraction_errors:
        notes.append(f"extraction_errors={extraction_errors}")
    if not row.get("title"):
        notes.append("title_missing_in_database")

    return CheckResult(
        row=row,
        selected_pdf=relative_pdf,
        pdf_exists=pdf_exists,
        first_two_pages_extractable=first_two_extractable,
        abstract_found=abstract_found,
        methods_found=methods_found,
        results_found=results_found,
        figures_tables_found=figures_tables_found,
        references_found=references_found,
        chinese_mojibake=mojibake,
        likely_scanned=likely_scanned,
        readability_status=status,
        use_nature_reader_skill=use_reader,
        reason_for_priority=priority_reason(row),
        notes=" | ".join(notes),
        first_two_char_count=first_chars,
        sampled_char_count=sample_chars,
    )


def select_priority_rows(rows: list[dict[str, str]], limit: int = 15) -> list[dict[str, str]]:
    with_pdf = [row for row in rows if row.get("pdf_path")]
    sorted_rows = sorted(with_pdf, key=lambda row: (-priority_score(row), row.get("year") or "9999", row.get("paper_id", "")))
    selected = []
    seen = set()
    for row in sorted_rows:
        key = row.get("paper_id")
        if key in seen:
            continue
        selected.append(row)
        seen.add(key)
        if len(selected) == limit:
            break
    return selected


def write_priority_csv(results: list[CheckResult]) -> None:
    rows = []
    for result in results:
        row = result.row
        rows.append(
            {
                "paper_id": row.get("paper_id", ""),
                "title": row.get("title", ""),
                "year": row.get("year", ""),
                "language": row.get("language", ""),
                "pdf_path": result.selected_pdf,
                "topic_group": row.get("topic_group", ""),
                "method_group": row.get("method_group", ""),
                "readability_status": result.readability_status,
                "use_nature_reader_skill": result.use_nature_reader_skill,
                "reason_for_priority": result.reason_for_priority,
                "notes": result.notes,
            }
        )
    with OUTPUT_CSV.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=CSV_FIELDS)
        writer.writeheader()
        writer.writerows(rows)


def yes_no(value: bool) -> str:
    return "yes" if value else "no"


def write_markdown(results: list[CheckResult]) -> None:
    status_counts = Counter(result.readability_status for result in results)
    reader_count = sum(1 for result in results if result.use_nature_reader_skill == "yes")
    lines = [
        "# Light Readability Check",
        "",
        f"Generated: {datetime.now().isoformat(timespec='seconds')}",
        "",
        "Scope: 15 priority records selected from `database/literature_database_cleaned.csv`. This is a light sampled check only; it does not create paper cards and does not summarize paper findings.",
        "",
        "## Summary",
        "",
        f"- Checked papers: {len(results)}",
        f"- ready: {status_counts.get('ready', 0)}",
        f"- usable_with_caution: {status_counts.get('usable_with_caution', 0)}",
        f"- needs_ocr: {status_counts.get('needs_ocr', 0)}",
        f"- needs_manual_check: {status_counts.get('needs_manual_check', 0)}",
        f"- pdf_missing: {status_counts.get('pdf_missing', 0)}",
        f"- Recommended for Nature Reader Skill: {reader_count}",
        "",
        "## Selection rule",
        "",
        "Priority was given to KRD classification/information extraction, FBR/bare-rock fraction, LSMM/SMA/MESMA, RF/SVM or other machine-learning classification, semantic segmentation, DEM/topographic factors, and Remote Sensing KRD papers with local PDFs.",
        "",
        "## Checked papers",
        "",
    ]
    for idx, result in enumerate(results, start=1):
        row = result.row
        title = row.get("title") or "(title missing; see filename candidate in notes)"
        lines.extend(
            [
                f"### {idx}. {row.get('paper_id', '')}: {title}",
                "",
                f"- Year: {row.get('year') or 'missing'}",
                f"- Language: {row.get('language') or 'missing'}",
                f"- PDF exists: {yes_no(result.pdf_exists)}",
                f"- PDF path: `{result.selected_pdf or 'missing'}`",
                f"- First 2 pages text extractable: {yes_no(result.first_two_pages_extractable)} ({result.first_two_char_count} chars)",
                f"- Abstract/摘要 found in first 2 pages: {yes_no(result.abstract_found)}",
                f"- Methods/方法 signal found in sampled pages: {yes_no(result.methods_found)}",
                f"- Results/结果 signal found in sampled pages: {yes_no(result.results_found)}",
                f"- Figures/Tables signal found in sampled pages: {yes_no(result.figures_tables_found)}",
                f"- References/参考文献 signal found in sampled pages: {yes_no(result.references_found)}",
                f"- Chinese mojibake detected: {yes_no(result.chinese_mojibake)}",
                f"- Likely scanned PDF: {yes_no(result.likely_scanned)}",
                f"- Readability status: `{result.readability_status}`",
                f"- Use Nature Reader Skill: `{result.use_nature_reader_skill}`",
                f"- Reason for priority: {result.reason_for_priority}",
                f"- Notes: {result.notes}",
                "",
            ]
        )
    OUTPUT_MD.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    rows = read_rows()
    selected = select_priority_rows(rows, 15)
    results = [check_row(row) for row in selected]
    write_priority_csv(results)
    write_markdown(results)

    counts = Counter(result.readability_status for result in results)
    print(f"Checked {len(results)} papers.")
    for status in ["ready", "usable_with_caution", "needs_ocr", "needs_manual_check", "pdf_missing"]:
        print(f"{status}: {counts.get(status, 0)}")
    print(f"use_nature_reader_skill=yes: {sum(1 for result in results if result.use_nature_reader_skill == 'yes')}")


if __name__ == "__main__":
    main()
