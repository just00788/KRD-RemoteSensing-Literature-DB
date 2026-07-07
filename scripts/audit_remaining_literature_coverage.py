from __future__ import annotations

import csv
import re
from collections import Counter, defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DB = ROOT / "database"
SYN = ROOT / "docs" / "literature" / "synthesis"
SKILL_SOURCE = ROOT / "docs" / "literature" / "skill_source"
READERS = ROOT / "docs" / "literature" / "readers"
CARDS = ROOT / "docs" / "literature" / "paper_cards"
EVIDENCE = ROOT / "docs" / "literature" / "evidence_maps"
RS_PROFILE = ROOT / "docs" / "literature" / "remote_sensing_journal_profile"


AUDIT_FIELDS = [
    "paper_id",
    "title",
    "year",
    "language",
    "journal_or_source",
    "doi",
    "pdf_path",
    "source_collection",
    "topic_group",
    "method_group",
    "relevance_level",
    "has_pdf",
    "has_reader",
    "has_paper_card",
    "read_in_batch_01",
    "read_in_batch_02",
    "read_in_remote_sensing_style_rereading",
    "included_in_skill_source",
    "coverage_status",
    "importance_for_skill",
    "missing_reason",
    "recommended_action",
]


TOPIC_KEYWORDS = {
    "rocky desertification classification": ["rocky_desertification", "rocky desertification", "karst rocky desertification", "石漠化"],
    "karst rocky desertification mapping": ["karst rocky desertification", "KRD", "mapping", "information extraction", "信息提取"],
    "FBR/fBR/bare-rock fraction": ["FBR", "fBR", "bare-rock", "bare rock", "bedrock fraction", "exposed bedrock", "裸岩", "基岩裸露"],
    "LSMM/SMA/MESMA": ["LSMM", "SMA", "MESMA", "spectral mixture", "linear spectral", "endmember"],
    "RF/SVM/BPNN/machine learning": ["RF", "SVM", "BPNN", "machine_learning", "machine learning", "random forest", "support vector"],
    "FCN/U-Net/DeepLabV3+/semantic segmentation": ["FCN", "U-Net", "DeepLabV3", "semantic segmentation", "segmentation", "deep_learning"],
    "DEM/topographic factors": ["DEM", "topograph", "terrain", "slope", "aspect", "elevation", "地形"],
    "GF imagery": ["GF", "Gaofen", "高分"],
    "Sentinel/Landsat imagery": ["Sentinel", "Landsat"],
    "GEE/time series": ["GEE", "Google Earth Engine", "time_series", "time series", "spatiotemporal"],
    "cross-region validation": ["cross-region", "transfer", "迁移", "spatial block", "validation"],
    "Remote Sensing journal style": ["Remote Sensing", "10.3390/rs"],
    "broader desertification": ["broader_desertification", "desertification"],
    "review papers": ["review", "综述"],
}

METHOD_KEYWORDS = {
    "LSMM": ["LSMM", "linear spectral mixture"],
    "SMA": ["SMA", "spectral mixture analysis"],
    "MESMA": ["MESMA"],
    "FCLS": ["FCLS", "fully constrained"],
    "RF": ["RF", "random forest"],
    "SVM": ["SVM", "support vector"],
    "BPNN": ["BPNN", "back propagation"],
    "CNN": ["CNN", "convolutional neural"],
    "FCN": ["FCN"],
    "U-Net": ["U-Net", "UNet"],
    "DeepLabV3+": ["DeepLabV3", "DeepLabV3+"],
    "Transformer": ["Transformer"],
    "DEM fusion": ["DEM", "terrain", "topographic"],
    "GEE": ["GEE", "Google Earth Engine"],
    "feature space": ["feature_space", "feature space"],
    "vegetation index": ["vegetation_index", "NDVI", "KNDVI"],
    "spectral index": ["spectral index", "NDRI", "SWIR", "NIR"],
    "time series": ["time_series", "time series", "spatiotemporal"],
}


def read_csv(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        return []
    with path.open("r", encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def write_csv(path: Path, rows: list[dict[str, str]], fields: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)


def norm(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", "", (text or "").lower())


def bool_text(value: bool) -> str:
    return "yes" if value else "no"


def collect_ids(folder: Path, pattern: str) -> set[str]:
    ids: set[str] = set()
    if not folder.exists():
        return ids
    regex = re.compile(pattern)
    for path in folder.rglob("*.md"):
        match = regex.search(path.name)
        if match:
            ids.add(match.group(1))
    return ids


def collect_batch_ids(folder: Path, pattern: str, batch_name: str) -> set[str]:
    ids: set[str] = set()
    if not folder.exists():
        return ids
    regex = re.compile(pattern)
    for path in folder.rglob("*.md"):
        if batch_name.lower() not in str(path).lower():
            continue
        match = regex.search(path.name)
        if match:
            ids.add(match.group(1))
    return ids


def collect_text_mentions(folder: Path) -> str:
    chunks = []
    if folder.exists():
        for path in folder.rglob("*.md"):
            try:
                chunks.append(path.read_text(encoding="utf-8", errors="ignore"))
            except OSError:
                pass
    return "\n".join(chunks)


def parse_rs_inventory() -> list[dict[str, str]]:
    path = RS_PROFILE / "rs_only_paper_inventory.md"
    if not path.exists():
        return []
    rows = []
    for line in path.read_text(encoding="utf-8", errors="ignore").splitlines():
        if not line.startswith("| RS"):
            continue
        parts = [p.strip().strip("`") for p in line.strip("|").split("|")]
        if len(parts) < 10:
            continue
        rows.append(
            {
                "rs_id": parts[0],
                "file_name": parts[1],
                "title": parts[2],
                "year": parts[3],
                "journal_or_source": parts[4],
                "doi": parts[5],
                "pdf_path": parts[6],
                "already_read_in_batch_01": parts[7],
                "already_read_in_batch_02": parts[8],
                "reread_for_style": parts[9],
            }
        )
    return rows


def field_blob(row: dict[str, str]) -> str:
    return " ".join(
        row.get(k, "")
        for k in [
            "title",
            "translated_title",
            "journal_or_source",
            "doi",
            "topic_group",
            "method_group",
            "data_source",
            "notes",
            "source_collection",
            "source_manifest",
        ]
    )


def has_any(blob: str, words: list[str]) -> bool:
    low = blob.lower()
    return any(w.lower() in low for w in words)


def score_importance(row: dict[str, str], has_pdf: bool, has_reader: bool, style_read: bool) -> str:
    blob = field_blob(row)
    relevance = (row.get("relevance_level") or "").lower()
    topic = (row.get("topic_group") or "").lower()
    method = (row.get("method_group") or "").lower()
    title = (row.get("title") or "").lower()

    critical_hit = any(
        token in blob.lower()
        for token in [
            "karst rocky desertification",
            "rocky desertification",
            "bare-rock",
            "bare rock",
            "bedrock fraction",
            "fbr",
            "lsmm",
            "mesma",
            "deeplabv3",
            "semantic segmentation",
        ]
    )
    if "query bucket" in title or "to verify" in relevance:
        return "medium"
    if critical_hit and ("remote sensing" in blob.lower() or has_pdf or has_reader or style_read):
        return "critical"
    if any(x in topic for x in ["classification", "lsmm", "machine", "deep", "dem", "gee"]) or any(
        x in method.lower() for x in ["rf", "svm", "unet", "u-net", "deeplab", "gee", "dem", "sma", "mesma"]
    ):
        return "high"
    if "broader" in topic or "review" in topic:
        return "medium"
    return "low"


def classify_coverage(
    row: dict[str, str],
    has_pdf: bool,
    has_reader: bool,
    has_card: bool,
    style_read: bool,
) -> tuple[str, str, str]:
    metadata_status = (row.get("metadata_status") or "").lower()
    title = row.get("title", "")
    if not has_pdf and not has_reader and not has_card and not style_read:
        if "needs_manual_check" in metadata_status or "query bucket" in title.lower():
            return "needs_manual_check", "metadata requires verification or candidate bucket has no concrete PDF", "manual_check"
        return "pdf_missing", "no PDF path or local PDF was found", "manual_check"
    if has_reader:
        return "fully_read", "", "no_action_needed"
    if style_read:
        return "style_read_only", "read for Remote Sensing style but not full scientific reader", "add_to_literature_map_only"
    if has_card:
        return "paper_card_only", "paper card exists but full reader was not detected", "add_to_literature_map_only"
    if has_pdf:
        return "unread_but_indexed", "PDF exists but no reader or card was detected", "batch_03_quick_reading"
    return "metadata_only", "metadata exists but PDF and reader/card are absent", "manual_check"


def adjust_action(status: str, importance: str, has_pdf: bool) -> str:
    if status == "fully_read":
        return "no_action_needed"
    if status == "style_read_only":
        if importance in {"critical", "high"}:
            return "batch_03_quick_reading"
        return "add_to_literature_map_only"
    if status in {"pdf_missing", "needs_manual_check", "metadata_only"}:
        if importance in {"critical", "high", "medium"}:
            return "manual_check"
        return "exclude"
    if status == "unread_but_indexed":
        if importance == "critical":
            return "batch_03_full_reading"
        if importance == "high":
            return "batch_03_quick_reading"
        if importance == "medium":
            return "add_to_literature_map_only"
    return "add_to_literature_map_only"


def source_bucket(journal: str, language: str, source_collection: str) -> str:
    blob = f"{journal} {source_collection}".lower()
    if "remote sensing" in blob:
        return "Remote Sensing"
    if "ecological indicators" in blob:
        return "Ecological Indicators"
    if "scientific reports" in blob:
        return "Scientific Reports"
    if "frontiers" in blob:
        return "Frontiers"
    if any(x in blob for x in ["ieee", "isprs", "ijaeog", "international journal of applied earth"]):
        return "IEEE / ISPRS / IJAEOG"
    if (language or "").lower().startswith("chinese") and any(x in blob for x in ["cnki", "学位", "thesis", "会议", "中文"]):
        return "CNKI / thesis / Chinese conference"
    if (language or "").lower().startswith("chinese"):
        return "Chinese journals"
    return "Other"


def count_read(rows: list[dict[str, str]]) -> int:
    return sum(1 for r in rows if r["coverage_status"] in {"fully_read", "style_read_only", "paper_card_only"})


def coverage_table(rows: list[dict[str, str]], keyword_map: dict[str, list[str]]) -> list[dict[str, str]]:
    out = []
    for label, keys in keyword_map.items():
        matched = [r for r in rows if has_any(field_blob(r), keys)]
        read = [r for r in matched if r["coverage_status"] in {"fully_read", "style_read_only", "paper_card_only"}]
        unread = [r for r in matched if r not in read]
        enough = "yes" if len(read) >= 2 or (label == "Remote Sensing journal style" and len(read) >= 5) else "limited"
        if len(matched) == 0:
            enough = "no"
        gap = "no obvious gap" if enough == "yes" else "limited coverage or metadata-only evidence"
        out.append(
            {
                "label": label,
                "total": str(len(matched)),
                "read": str(len(read)),
                "unread": str(len(unread)),
                "supports_skill": enough,
                "gap": gap,
            }
        )
    return out


def md_table(headers: list[str], rows: list[list[str]]) -> str:
    lines = ["| " + " | ".join(headers) + " |", "| " + " | ".join(["---"] * len(headers)) + " |"]
    for row in rows:
        lines.append("| " + " | ".join(str(x).replace("\n", " ") for x in row) + " |")
    return "\n".join(lines)


def main() -> None:
    cleaned = read_csv(DB / "literature_database_cleaned.csv")
    enriched = read_csv(DB / "literature_database_enriched_batch_01.csv")
    enriched_by_id = {r.get("paper_id", ""): r for r in enriched}
    priority = {r.get("paper_id", ""): r for r in read_csv(DB / "priority_reading_list.csv")}
    pdf_inventory = read_csv(DB / "pdf_inventory.csv")
    pdf_paths = {r.get("relative_path", "") for r in pdf_inventory}

    reader_ids = collect_ids(READERS, r"(KRD\d+)_reader\.md")
    card_ids = collect_ids(CARDS, r"(KRD\d+)_card\.md")
    batch01_ids = collect_batch_ids(READERS, r"(KRD\d+)_reader\.md", "batch_01_core")
    batch02_ids = collect_batch_ids(READERS, r"(KRD\d+)_reader\.md", "batch_02")
    evidence_text = collect_text_mentions(EVIDENCE)
    skill_text = collect_text_mentions(SKILL_SOURCE)

    rs_rows = parse_rs_inventory()
    rs_dois = {r["doi"].lower(): r for r in rs_rows if r.get("doi")}
    rs_titles = {norm(r["title"]): r for r in rs_rows if r.get("title")}
    rs_paths = {r["pdf_path"]: r for r in rs_rows if r.get("pdf_path")}

    audit_rows: list[dict[str, str]] = []
    for row in cleaned:
        paper_id = row.get("paper_id", "")
        pdf_path = row.get("pdf_path", "")
        has_pdf = bool(pdf_path and ((ROOT / pdf_path).exists() or pdf_path in pdf_paths))
        has_reader = paper_id in reader_ids or bool(enriched_by_id.get(paper_id, {}).get("reader_path"))
        has_card = paper_id in card_ids or bool(enriched_by_id.get(paper_id, {}).get("paper_card_path"))
        read_batch01 = paper_id in batch01_ids or bool(enriched_by_id.get(paper_id, {}).get("reader_path"))
        read_batch02 = paper_id in batch02_ids

        doi = (row.get("doi") or "").lower()
        title_norm = norm(row.get("title", ""))
        style_read = False
        if doi in rs_dois:
            style_read = True
        elif title_norm in rs_titles:
            style_read = True
        elif pdf_path in rs_paths:
            style_read = True

        status, missing_reason, default_action = classify_coverage(row, has_pdf, has_reader, has_card, style_read)
        importance = score_importance(row, has_pdf, has_reader, style_read)
        action = adjust_action(status, importance, has_pdf)
        if default_action == "manual_check" and action == "exclude":
            action = default_action

        included = paper_id in evidence_text or paper_id in skill_text or has_reader or style_read

        audit_rows.append(
            {
                "paper_id": paper_id,
                "title": row.get("title", ""),
                "year": row.get("year", ""),
                "language": row.get("language", ""),
                "journal_or_source": row.get("journal_or_source", ""),
                "doi": row.get("doi", ""),
                "pdf_path": pdf_path,
                "source_collection": row.get("source_collection", ""),
                "topic_group": row.get("topic_group", ""),
                "method_group": row.get("method_group", ""),
                "relevance_level": row.get("relevance_level", ""),
                "has_pdf": bool_text(has_pdf),
                "has_reader": bool_text(has_reader),
                "has_paper_card": bool_text(has_card),
                "read_in_batch_01": bool_text(read_batch01),
                "read_in_batch_02": bool_text(read_batch02),
                "read_in_remote_sensing_style_rereading": bool_text(style_read),
                "included_in_skill_source": bool_text(included),
                "coverage_status": status,
                "importance_for_skill": importance,
                "missing_reason": missing_reason,
                "recommended_action": action,
            }
        )

    write_csv(DB / "literature_coverage_audit.csv", audit_rows, AUDIT_FIELDS)

    total = len(audit_rows)
    has_pdf_count = sum(1 for r in audit_rows if r["has_pdf"] == "yes")
    reader_count = sum(1 for r in audit_rows if r["has_reader"] == "yes")
    card_count = sum(1 for r in audit_rows if r["has_paper_card"] == "yes")
    style_count = sum(1 for r in audit_rows if r["read_in_remote_sensing_style_rereading"] == "yes")
    metadata_unread = sum(1 for r in audit_rows if r["coverage_status"] in {"metadata_only", "needs_manual_check", "pdf_missing"})
    unread_with_pdf = sum(1 for r in audit_rows if r["coverage_status"] == "unread_but_indexed")
    pdf_missing = sum(1 for r in audit_rows if r["has_pdf"] == "no")
    manual_check = sum(1 for r in audit_rows if r["recommended_action"] == "manual_check" or r["coverage_status"] == "needs_manual_check")

    language_counts = defaultdict(lambda: Counter())
    for r in audit_rows:
        lang = r["language"] or "unknown"
        language_counts[lang]["total"] += 1
        if r["coverage_status"] in {"fully_read", "style_read_only", "paper_card_only"}:
            language_counts[lang]["read"] += 1
        else:
            language_counts[lang]["unread"] += 1

    year_counts = defaultdict(lambda: Counter())
    for r in audit_rows:
        year = r["year"] or "unknown"
        year_counts[year]["total"] += 1
        if r["coverage_status"] in {"fully_read", "style_read_only", "paper_card_only"}:
            year_counts[year]["read"] += 1
        else:
            year_counts[year]["unread"] += 1

    topic_rows = coverage_table(audit_rows, TOPIC_KEYWORDS)
    method_rows = coverage_table(audit_rows, METHOD_KEYWORDS)

    source_counts = defaultdict(lambda: Counter())
    for r in audit_rows:
        bucket = source_bucket(r["journal_or_source"], r["language"], r["source_collection"])
        source_counts[bucket]["total"] += 1
        if r["coverage_status"] in {"fully_read", "style_read_only", "paper_card_only"}:
            source_counts[bucket]["read"] += 1
        else:
            source_counts[bucket]["unread"] += 1

    candidates = [
        r
        for r in audit_rows
        if r["coverage_status"] != "fully_read"
        and r["recommended_action"] in {"batch_03_full_reading", "batch_03_quick_reading", "manual_check"}
        and r["importance_for_skill"] in {"critical", "high", "medium"}
    ]
    rank_weight = {"critical": 0, "high": 1, "medium": 2, "low": 3, "irrelevant": 4}
    action_weight = {"batch_03_full_reading": 0, "batch_03_quick_reading": 1, "manual_check": 2}
    candidates.sort(
        key=lambda r: (
            action_weight.get(r["recommended_action"], 9),
            rank_weight.get(r["importance_for_skill"], 9),
            0 if r["has_pdf"] == "yes" else 1,
            r["paper_id"],
        )
    )
    key_candidates = candidates[:20]

    batch03 = [
        r
        for r in candidates
        if r["has_pdf"] == "yes"
        and r["recommended_action"] in {"batch_03_full_reading", "batch_03_quick_reading"}
    ][:8]
    decision = "Decision B"
    decision_reason = (
        "Core scientific and Remote Sensing style modules are usable, but several unread PDF-backed records remain relevant to "
        "FBR/LSMM, DEM/topography, KRD classification, and Remote Sensing KRD style. A small quick-reading batch is recommended."
    )
    if len(batch03) >= 10:
        decision = "Decision C"
        decision_reason = "Many high-priority unread PDFs remain across key themes; full batch_03 reading would be justified."
    if manual_check > total * 0.45:
        decision = "Decision D"
        decision_reason = "Metadata/manual-check burden is high enough that metadata/OCR cleanup should precede further reading."
    if not batch03 and manual_check < total * 0.25:
        decision = "Decision A"
        decision_reason = "No high-priority unread PDF-backed gap was detected."

    report = [
        "# Literature Coverage Audit Report",
        "",
        "Generated from existing metadata, readers, paper cards, evidence maps, skill source files, and Remote Sensing journal profile files. No PDFs were re-read for this audit.",
        "",
        "## 1. Total Literature Coverage",
        "",
        f"- Total literature records: {total}",
        f"- Records with PDF: {has_pdf_count}",
        f"- Records with full reader: {reader_count}",
        f"- Records with paper card: {card_count}",
        f"- Records with style rereading only or style coverage: {style_count}",
        f"- Completely unread but metadata-only/manual-check/PDF-missing records: {metadata_unread}",
        f"- Completely unread but PDF-backed records: {unread_with_pdf}",
        f"- PDF-missing records: {pdf_missing}",
        f"- Records needing manual check: {manual_check}",
        "",
        "## 2. Coverage by Language",
        "",
        md_table(
            ["language", "total", "read_or_style_covered", "unread_or_manual"],
            [[k, v["total"], v["read"], v["unread"]] for k, v in sorted(language_counts.items())],
        ),
        "",
        "## 3. Coverage by Year",
        "",
        md_table(
            ["year", "total", "read_or_style_covered", "unread_or_manual"],
            [[k, v["total"], v["read"], v["unread"]] for k, v in sorted(year_counts.items())],
        ),
        "",
        "## 4. Coverage by Topic",
        "",
        md_table(
            ["topic", "total", "read_or_style_covered", "unread", "supports_skill", "gap"],
            [[r["label"], r["total"], r["read"], r["unread"], r["supports_skill"], r["gap"]] for r in topic_rows],
        ),
        "",
        "## 5. Coverage by Method",
        "",
        md_table(
            ["method", "total", "read_or_style_covered", "unread", "supports_skill", "gap"],
            [[r["label"], r["total"], r["read"], r["unread"], r["supports_skill"], r["gap"]] for r in method_rows],
        ),
        "",
        "## 6. Coverage by Journal / Source",
        "",
        md_table(
            ["source_group", "total", "read_or_style_covered", "unread"],
            [[k, v["total"], v["read"], v["unread"]] for k, v in sorted(source_counts.items())],
        ),
        "",
        "## 7. Decision",
        "",
        f"Final decision: **{decision}**.",
        "",
        decision_reason,
        "",
        "## 8. Notes",
        "",
        "- The audit does not summarize unread paper findings.",
        "- Unread records are classified only by metadata, title, topic_group, method_group, DOI, source, and PDF availability.",
        "- Existing skill source is adequate as a draft, but final packaging should wait until the metadata/PDF mapping gap is acknowledged or cleaned.",
    ]
    (SYN / "literature_coverage_audit_report.md").write_text("\n".join(map(str, report)) + "\n", encoding="utf-8")

    key_lines = [
        "# Key Unread Papers for Possible Batch 03",
        "",
        "This list is generated from metadata and coverage status only. It does not summarize unread paper results.",
        "",
    ]
    key_lines.append(
        md_table(
            [
                "paper_id",
                "title",
                "year",
                "language",
                "journal_or_source",
                "pdf_path",
                "topic_group",
                "method_group",
                "why_important",
                "what_gap_it_fills",
                "recommended_reading_level",
            ],
            [
                [
                    r["paper_id"],
                    r["title"],
                    r["year"],
                    r["language"],
                    r["journal_or_source"],
                    r["pdf_path"],
                    r["topic_group"],
                    r["method_group"],
                    f"{r['importance_for_skill']} for skill; {r['coverage_status']}",
                    r["missing_reason"] or "adds coverage to an under-read metadata cluster",
                    "manual_check_first"
                    if r["recommended_action"] == "manual_check"
                    else ("full_reader_needed" if r["recommended_action"] == "batch_03_full_reading" else "quick_reader_needed"),
                ]
                for r in key_candidates
            ],
        )
    )
    (SYN / "key_unread_papers_for_possible_batch_03.md").write_text("\n".join(key_lines) + "\n", encoding="utf-8")

    if decision in {"Decision B", "Decision C"}:
        b_lines = [
            "# Batch 03 Recommendation",
            "",
            f"Decision: **{decision}**.",
            "",
            "Recommended reading type is quick unless the record is marked as critical and PDF-backed.",
            "",
            md_table(
                [
                    "priority_rank",
                    "paper_id",
                    "title",
                    "year",
                    "language",
                    "journal_or_source",
                    "pdf_path",
                    "why_needed",
                    "what_skill_gap_it_fills",
                    "recommended_reading_type",
                ],
                [
                    [
                        i + 1,
                        r["paper_id"],
                        r["title"],
                        r["year"],
                        r["language"],
                        r["journal_or_source"],
                        r["pdf_path"],
                        f"{r['importance_for_skill']} unread/style-only record with PDF",
                        r["missing_reason"] or "strengthens literature-map and final skill confidence",
                        "full_reader" if r["recommended_action"] == "batch_03_full_reading" else "quick_reader",
                    ]
                    for i, r in enumerate(batch03)
                ],
            ),
        ]
        (SYN / "batch_03_recommendation.md").write_text("\n".join(map(str, b_lines)) + "\n", encoding="utf-8")

    coverage_note = [
        "# Literature Map Coverage Audit",
        "",
        "## When to use this reference",
        "",
        "Use this note when deciding whether the current KRD/Remote Sensing skill source is sufficiently supported by the already-read literature, or whether claims should be phrased cautiously because they rely on metadata-only records.",
        "",
        "## Sufficiently Covered Themes",
        "",
        "- Remote Sensing journal structure and style are strongly covered by 11 style reread papers.",
        "- KRD classification and information extraction are covered by batch_01 readers and Remote Sensing style papers.",
        "- FBR/LSMM/SMA/MESMA are covered enough for core terminology and metric rules, but additional quick reading would improve confidence.",
        "- ML classification with RF/SVM is covered enough for baseline framing.",
        "",
        "## Limited Coverage Themes",
        "",
        "- DeepLabV3+, FCN, U-Net, and semantic segmentation are covered but remain a relatively small cluster.",
        "- DEM/topographic factors are covered in the scientific rules, but more unread metadata/PDF-backed records could refine ablation wording.",
        "- Cross-region transfer and spatially independent validation remain more design-driven than literature-saturated.",
        "- Chinese literature coverage includes important full readers, but many CNKI/Wanfang-style candidate buckets remain metadata-only.",
        "",
        "## Cautious Wording Required",
        "",
        "- Do not summarize findings from unread papers.",
        "- For unread papers, state only metadata-indicated themes.",
        "- Keep GF-7 stereo DEM limited to local Study Area 2 enhancement unless real results are supplied.",
        "- Keep continuous FBR and categorical classification outputs separate.",
        "",
        "## Batch 03 Recommendation",
        "",
        f"{decision}: {decision_reason}",
    ]
    (SKILL_SOURCE / "literature-map-coverage-audit.md").write_text("\n".join(coverage_note) + "\n", encoding="utf-8")

    status_note = [
        "# Coverage Audit Status",
        "",
        "The draft skill source is based on batch_01 core readers, paper cards, evidence maps, Remote Sensing journal style rereading, and generated skill_source modules.",
        "",
        f"Remaining literature coverage audit decision: **{decision}**.",
        "",
        decision_reason,
        "",
        "Because the audit decision is metadata-quality oriented, final packaging should not be treated as comprehensive until the user either accepts the current coverage limits or runs a metadata/OCR/PDF-mapping cleanup pass.",
    ]
    (ROOT / "skill_build" / "krd-remote-sensing" / "coverage_audit_status.md").write_text(
        "\n".join(status_note) + "\n", encoding="utf-8"
    )

    print(f"total={total}")
    print(f"has_pdf={has_pdf_count}")
    print(f"reader={reader_count}")
    print(f"card={card_count}")
    print(f"unread_with_pdf={unread_with_pdf}")
    print(f"style={style_count}")
    print(f"manual_check={manual_check}")
    print(f"decision={decision}")
    print(f"batch03_recommendations={len(batch03)}")


if __name__ == "__main__":
    main()
