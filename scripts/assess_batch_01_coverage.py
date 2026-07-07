#!/usr/bin/env python3
"""Assess batch_01 coverage and plan batch_02 Remote Sensing reading."""

from __future__ import annotations

import csv
from collections import Counter
from datetime import datetime
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
SYNTHESIS_DIR = REPO_ROOT / "docs" / "literature" / "synthesis"
READERS_DIR = REPO_ROOT / "docs" / "literature" / "readers" / "batch_01_core"
CARDS_DIR = REPO_ROOT / "docs" / "literature" / "paper_cards" / "batch_01_core"
EVIDENCE_DIR = REPO_ROOT / "docs" / "literature" / "evidence_maps"


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def has_cjk(text: str) -> bool:
    return any("\u4e00" <= ch <= "\u9fff" for ch in text or "")


def is_remote_sensing_journal(row: dict[str, str]) -> tuple[bool, str]:
    journal = (row.get("journal_or_source") or "").strip()
    doi = (row.get("doi") or "").strip().lower()
    pdf_path = row.get("pdf_path") or ""
    title = row.get("title") or ""
    if journal == "Remote Sensing":
        return True, "journal/source is exactly Remote Sensing"
    if doi.startswith("10.3390/rs"):
        return True, "DOI prefix 10.3390/rs confirms MDPI Remote Sensing"
    if "RemoteSens_" in pdf_path and ("RemoteSens_" in pdf_path or "Remote Sensing" in title):
        return True, "PDF filename/source indicates Remote Sensing"
    return False, ""


def is_journal_uncertain(row: dict[str, str]) -> bool:
    journal = (row.get("journal_or_source") or "").strip()
    if not journal or journal.lower() in {"unknown", "core", "closely_related", "background"}:
        is_rs, _ = is_remote_sensing_journal(row)
        return not is_rs
    return False


def supports(row: dict[str, str], key: str) -> bool:
    text = " ".join(
        [
            row.get("title", ""),
            row.get("topic_group", ""),
            row.get("method_group", ""),
            row.get("relevance_to_manuscript", ""),
            row.get("key_notes", ""),
            row.get("pdf_path", ""),
        ]
    ).lower()
    checks = {
        "krd": ["rocky desertification", "karst rocky desertification", "石漠化", "desertification"],
        "fbr": ["bare_rock_fraction_fbr", "bare rock", "bedrock", "fbr", "裸岩", "基岩"],
        "lsmm": ["lsmm", "sma", "mesma", "spectral mixture"],
        "ml": ["machine_learning", "rf", "svm", "random forest", "classification"],
        "seg": ["deep_learning_segmentation", "deeplab", "u-net", "fcn", "segmentation"],
        "dem": ["dem", "topograph", "terrain", "slope", "aspect", "elevation"],
        "multi": ["sentinel", "landsat", "gf-", "gaofen", "multi-source", "remote sensing"],
        "gf_sentinel_landsat": ["gf-", "gaofen", "sentinel", "landsat"],
        "cross": ["cross-region", "transfer", "迁移"],
        "rs_style": ["remote sensing style", "10.3390/rs", "remotesens_", "remote sensing"],
    }
    return any(token in text for token in checks[key])


def md_bool(value: bool) -> str:
    return "yes" if value else "no"


def clean(value: str) -> str:
    return (value or "unknown").replace("|", "/").replace("\n", " ")


def batch_rows() -> list[dict[str, str]]:
    rows = read_csv(REPO_ROOT / "database" / "literature_database_enriched_batch_01.csv")
    return [row for row in rows if row.get("reader_path")]


def recommend_rows(batch_ids: set[str]) -> list[dict[str, str]]:
    rows = read_csv(REPO_ROOT / "database" / "literature_database_cleaned.csv")
    duplicate_pdf_map = {
        "KRD0016": "docs/literature/pdfs/remote_sensing_only/2014_RemoteSens_6_9895_Is_Forest_Restoration_in_the_Southwest_China_Karst_Promoted_.pdf",
        "KRD0023": "docs/literature/pdfs/remote_sensing_only/2016_RemoteSens_8_68_Quantitative_Estimation_of_Carbonate_Rock_Fraction_in_Karst_.pdf",
        "KRD0025": "docs/literature/pdfs/package_2000_2026/EN005_Analysis_of_Landsat-8_OLI_Imagery_for_Estimating_Exposed_Bed.pdf; docs/literature/pdfs/remote_sensing_only/2018_RemoteSens_10_1321_Analysis_of_Landsat-8_OLI_Imagery_for_Estimating_Exposed_Bed.pdf",
        "KRD0034": "docs/literature/pdfs/remote_sensing_only/2021_RemoteSens_13_1614_How_Can_We_Realize_Sustainable_Development_Goals_in_Rocky_De.pdf",
        "KRD0044": "docs/literature/pdfs/package_2000_2026/EN018_Spatiotemporal_Evolution_Analysis_and_Future_Scenario_Predic.pdf; docs/literature/pdfs/remote_sensing_only/2022_RemoteSens_14_292_Spatiotemporal_Evolution_Analysis_and_Future_Scenario_Predic.pdf",
        "KRD0045": "docs/literature/pdfs/remote_sensing_only/2022_RemoteSens_14_2351_The_Changes_of_Spatiotemporal_Pattern_of_Rocky_Desertificati.pdf",
        "KRD0046": "docs/literature/pdfs/package_2000_2026/EN010_Extraction_of_Rocky_Desertification_Information_in_the_Karst.pdf; docs/literature/pdfs/remote_sensing_only/2023_RemoteSens_15_3056_Extraction_of_Rocky_Desertification_Information_in_the_Karst.pdf",
        "KRD0070": "docs/literature/pdfs/package_2000_2026/EN013_Spatiotemporal_Evolution_and_Driving_Factors_of_Karst_Rocky_.pdf; docs/literature/pdfs/remote_sensing_only/2025_RemoteSens_17_2294_Spatiotemporal_Evolution_and_Driving_Factors_of_Karst_Rocky_.pdf",
    }
    already_read_equivalents = {
        # KRD0095 reader already covers this Remote Sensing article.
        "KRD0052": "KRD0095",
    }
    candidates = []
    for row in rows:
        if row.get("paper_id") in batch_ids:
            continue
        if row.get("paper_id") in already_read_equivalents and already_read_equivalents[row.get("paper_id")] in batch_ids:
            continue
        is_rs, reason = is_remote_sensing_journal(row)
        text = " ".join([row.get("title", ""), row.get("topic_group", ""), row.get("method_group", ""), row.get("pdf_path", "")]).lower()
        if not is_rs and "remotesens_" not in row.get("pdf_path", "") and not (row.get("doi", "").lower().startswith("10.3390/rs")):
            continue
        if not row.get("pdf_path") and row.get("paper_id") in duplicate_pdf_map:
            row = dict(row)
            row["pdf_path"] = duplicate_pdf_map[row["paper_id"]]
        score = 0
        for token, weight in [
            ("bare_rock_fraction_fbr", 8),
            ("bare rock", 8),
            ("bedrock", 7),
            ("rock fraction", 7),
            ("rocky_desertification_classification", 7),
            ("rocky desertification", 7),
            ("karst", 5),
            ("machine_learning", 4),
            ("classification", 4),
            ("dem", 3),
            ("topograph", 3),
            ("spatiotemporal", 3),
            ("driving", 3),
            ("sentinel", 2),
            ("landsat", 2),
        ]:
            if token in text:
                score += weight
        if row.get("pdf_path"):
            score += 5
        if row.get("doi"):
            score += 2
        candidates.append((score, reason, row))
    candidates.sort(key=lambda item: (-item[0], item[2].get("year") or "9999", item[2].get("paper_id")))
    selected = []
    seen_titles = set()
    for _, reason, row in candidates:
        key = (row.get("doi") or row.get("title") or row.get("pdf_path")).lower()
        if key in seen_titles:
            continue
        seen_titles.add(key)
        row = dict(row)
        row["_rs_reason"] = reason or "RemoteSens PDF filename/source"
        selected.append(row)
        if len(selected) == 7:
            break
    return selected


def make_reports() -> dict[str, object]:
    missing = []
    required = [
        READERS_DIR,
        CARDS_DIR,
        SYNTHESIS_DIR / "batch_01_core" / "batch_01_core_synthesis.md",
        EVIDENCE_DIR,
        REPO_ROOT / "database" / "literature_database_enriched_batch_01.csv",
        REPO_ROOT / "database" / "literature_database_cleaned.csv",
        REPO_ROOT / "database" / "priority_reading_list.csv",
    ]
    for path in required:
        if not path.exists():
            missing.append(path.relative_to(REPO_ROOT).as_posix())

    rows = batch_rows()
    reader_count = len(list(READERS_DIR.glob("*_reader.md"))) if READERS_DIR.exists() else 0
    card_count = len(list(CARDS_DIR.glob("*_card.md"))) if CARDS_DIR.exists() else 0
    incomplete = [row for row in rows if row.get("full_reading_status") == "incomplete_reading"]
    manual = [row for row in rows if row.get("manual_review_needed") and row.get("manual_review_needed") != "none"]
    rs_rows = []
    non_rs_rows = []
    uncertain_rows = []
    for row in rows:
        is_rs, reason = is_remote_sensing_journal(row)
        row["_is_rs"] = md_bool(is_rs)
        row["_rs_reason"] = reason
        if is_rs:
            rs_rows.append(row)
        else:
            non_rs_rows.append(row)
        if is_journal_uncertain(row):
            uncertain_rows.append(row)

    topic_counts = {
        "rocky desertification": sum(supports(row, "krd") for row in rows),
        "FBR/fBR/bare-rock fraction": sum(supports(row, "fbr") for row in rows),
        "LSMM/SMA/MESMA": sum(supports(row, "lsmm") for row in rows),
        "machine learning": sum(supports(row, "ml") for row in rows),
        "semantic segmentation": sum(supports(row, "seg") for row in rows),
        "DEM/topography": sum(supports(row, "dem") for row in rows),
        "multi-source remote sensing": sum(supports(row, "multi") for row in rows),
        "GF/Sentinel/Landsat data": sum(supports(row, "gf_sentinel_landsat") for row in rows),
        "cross-region validation": sum(supports(row, "cross") for row in rows),
        "Remote Sensing writing style": len(rs_rows),
    }

    readiness = "mostly_sufficient"
    decision = "Decision B: small supplementary reading needed; read 5-8 more Remote Sensing papers."
    recommendations = recommend_rows({row.get("paper_id") for row in rows})

    coverage_path = SYNTHESIS_DIR / "need_for_batch_02_remote_sensing_reading.md"
    rec_path = SYNTHESIS_DIR / "batch_02_remote_sensing_recommendation.md"
    next_path = SYNTHESIS_DIR / "next_codex_task_after_batch_01.md"

    table_lines = [
        "| paper_id | title | year | journal/source | is_remote_sensing_journal | reader_status | writing_style_value |",
        "|---|---|---:|---|---|---|---|",
    ]
    for row in rows:
        style = "high" if row in rs_rows else ("medium" if supports(row, "rs_style") else "low")
        table_lines.append(
            f"| {row.get('paper_id')} | {clean(row.get('title'))} | {row.get('year') or 'unknown'} | {clean(row.get('journal_or_source'))} | {row['_is_rs']} | {row.get('full_reading_status') or 'completed'} | {style} |"
        )

    topic_lines = []
    for topic, count in topic_counts.items():
        status = "covered" if count >= 3 else ("partly covered" if count > 0 else "not covered")
        topic_lines.append(f"- {topic}: {status} ({count}/{len(rows)} batch papers).")

    writing_aspects = [
        ("Abstract", "mostly_sufficient", "5 confirmed Remote Sensing papers plus complete readers provide enough examples, but more journal-specific examples would improve confidence."),
        ("Introduction", "mostly_sufficient", "KRD/classification/FBR introductions are covered; extra RS papers can strengthen target-journal phrasing."),
        ("Methods", "mostly_sufficient", "Methods coverage is broad, but Remote Sensing-specific Materials and Methods patterns would benefit from 5-7 more papers."),
        ("Results", "mostly_sufficient", "Map/table/result organization is represented, but more RS examples are recommended."),
        ("Discussion", "insufficient", "Discussion-style evidence is less robust and should be strengthened before style profiling."),
        ("Conclusions", "mostly_sufficient", "Conclusion anchors exist, but journal-specific templates need a slightly larger sample."),
        ("Figures", "mostly_sufficient", "Figure/table captions are well represented."),
        ("Tables", "mostly_sufficient", "Accuracy/data-source tables are represented but should be compared against additional RS examples."),
        ("terminology", "mostly_sufficient", "KRD/FBR/ML/segmentation terminology is covered."),
        ("academic phrases", "insufficient", "A phrase-level journal profile needs more confirmed Remote Sensing papers."),
        ("submission checklist", "insufficient", "Submission checklist should be built after batch_02 or separate journal-profile analysis."),
    ]

    coverage = [
        "# Need for Batch 02 Remote Sensing Reading",
        "",
        f"Generated: {datetime.now().isoformat(timespec='seconds')}",
        "",
        "## 1. Batch 01 Completion Check",
        "",
        f"- planned papers: {len(rows)}",
        f"- readers generated: {reader_count}",
        f"- paper cards generated: {card_count}",
        f"- incomplete readings: {len(incomplete)}",
        f"- manual review needed: {len(manual)}",
        f"- missing critical files: {', '.join(missing) if missing else 'none'}",
        "",
        "## 2. Remote Sensing Journal Coverage",
        "",
        f"- Remote Sensing papers in batch 01: {len(rs_rows)}",
        f"- non-Remote Sensing papers: {len(non_rs_rows)}",
        f"- journal/source uncertain papers: {len(uncertain_rows)}",
        "",
        *table_lines,
        "",
        "Confirmed Remote Sensing journal papers:",
        "",
        *[f"- {row.get('paper_id')}: {row.get('title') or 'title missing'} ({row.get('year') or 'unknown'}). Evidence: {row.get('_rs_reason')}" for row in rs_rows],
        "",
        "## 3. Topic Coverage",
        "",
        *topic_lines,
        "",
        "## 4. Writing-Style Analysis Readiness",
        "",
        *[f"- {name}: {level}. {note}" for name, level, note in writing_aspects],
        "",
        f"Overall readiness judgment: `{readiness}`.",
        "",
        "## 5. Decision",
        "",
        decision,
        "",
        "Rationale: batch_01 is complete and scientifically broad, but only five papers can be confidently treated as Remote Sensing journal articles. This is enough to start orientation, but not enough for a robust phrase-level and section-level journal style profile.",
        "",
        "## 6. Recommended Next Action",
        "",
        "Run `Batch 02 Remote Sensing Full Reading` with a small supplemental set of 7 confirmed or strongly indicated Remote Sensing papers. Prioritize FBR/bare-rock fraction, KRD information extraction, spatiotemporal dynamics, driving factors, and figure/table-rich papers.",
        "",
        "Recommended list summary:",
        "",
        *[f"- {idx}. {row.get('paper_id')}: {row.get('title') or row.get('pdf_path')} ({row.get('year') or 'unknown'})" for idx, row in enumerate(recommendations, start=1)],
        "",
    ]
    coverage_path.write_text("\n".join(coverage), encoding="utf-8")

    rec_lines = [
        "# Batch 02 Remote Sensing Recommendation",
        "",
        f"Generated: {datetime.now().isoformat(timespec='seconds')}",
        "",
        "Decision: small supplementary reading is recommended because batch_01 has only five confirmed Remote Sensing journal papers.",
        "",
        "| priority_rank | paper_id | title | year | journal/source | DOI | pdf_path | topic_group | method_group | why_needed | what_gap_it_fills | whether_full_reader_needed |",
        "|---:|---|---|---:|---|---|---|---|---|---|---|---|",
    ]
    for idx, row in enumerate(recommendations, start=1):
        topic = row.get("topic_group") or "unknown"
        method = row.get("method_group") or "unknown"
        why = "confirmed/likely Remote Sensing paper not read in batch_01; useful for target-journal writing style and scientific coverage"
        if supports(row, "fbr"):
            gap = "FBR/bare-rock fraction evidence and continuous inversion framing"
        elif supports(row, "krd"):
            gap = "KRD classification/information extraction or spatial dynamics"
        else:
            gap = "Remote Sensing structure, figure/table style, and related ecological remote sensing framing"
        rec_lines.append(
            f"| {idx} | {row.get('paper_id')} | {clean(row.get('title') or row.get('pdf_path'))} | {row.get('year') or 'unknown'} | {clean(row.get('journal_or_source'))} | {row.get('doi') or 'unknown'} | `{row.get('pdf_path') or 'metadata_only'}` | {topic} | {method} | {why} | {gap} | yes |"
        )
    rec_lines.extend([
        "",
        "Notes:",
        "",
        "- Do not reread papers that already have batch_01 readers unless metadata reconciliation is needed.",
        "- For metadata-only records with duplicate PDF-only records, use the existing local PDF path when available.",
        "- The second batch should emphasize writing-style extraction in addition to scientific reading.",
    ])
    rec_path.write_text("\n".join(rec_lines), encoding="utf-8")

    next_lines = [
        "# Batch 02 Remote Sensing Full Reading",
        "",
        "This is a task draft for the next Codex run. Do not execute it from this file.",
        "",
        "## Objective",
        "",
        "Read a small supplementary set of confirmed or strongly indicated Remote Sensing papers to strengthen target-journal writing-style coverage before journal profile analysis.",
        "",
        "## Inputs",
        "",
        "- `docs/literature/synthesis/need_for_batch_02_remote_sensing_reading.md`",
        "- `docs/literature/synthesis/batch_02_remote_sensing_recommendation.md`",
        "- `database/literature_database_cleaned.csv`",
        "- `database/literature_database_enriched_batch_01.csv`",
        "- local PDFs under `docs/literature/pdfs/remote_sensing_only/` and related duplicate paths",
        "",
        "## Recommended Papers",
        "",
        *[f"{idx}. {row.get('paper_id')}: {row.get('title') or row.get('pdf_path')}" for idx, row in enumerate(recommendations, start=1)],
        "",
        "## Required Outputs",
        "",
        "- `docs/literature/readers/batch_02_remote_sensing/`",
        "- `docs/literature/paper_cards/batch_02_remote_sensing/`",
        "- `docs/literature/synthesis/batch_02_remote_sensing/batch_02_remote_sensing_synthesis.md`",
        "- `docs/literature/synthesis/remote_sensing_journal_style_input_matrix.md`",
        "- updated enriched database without overwriting batch_01 fields",
        "",
        "## Constraints",
        "",
        "- Follow `AGENTS.md`.",
        "- Do not mix continuous FBR metrics with classification metrics.",
        "- Do not claim GF-7 stereo DEM improves Area 1 to Area 2 transfer.",
        "- Preserve page/section/figure/table anchors.",
        "- Flag metadata uncertainty instead of guessing.",
    ]
    next_path.write_text("\n".join(next_lines), encoding="utf-8")

    return {
        "missing": missing,
        "planned": len(rows),
        "readers": reader_count,
        "cards": card_count,
        "incomplete": len(incomplete),
        "manual": len(manual),
        "remote_sensing": len(rs_rows),
        "non_remote_sensing": len(non_rs_rows),
        "uncertain": len(uncertain_rows),
        "readiness": readiness,
        "decision": "B",
        "recommended": len(recommendations),
        "coverage_path": coverage_path,
        "recommendation_path": rec_path,
        "next_path": next_path,
    }


def main() -> None:
    result = make_reports()
    for key, value in result.items():
        if isinstance(value, Path):
            value = value.relative_to(REPO_ROOT).as_posix()
        print(f"{key}: {value}")


if __name__ == "__main__":
    main()
