#!/usr/bin/env python3
"""Add the Wu Yongjun improved DeepLabV3+ paper without renumbering old IDs."""

from __future__ import annotations

import csv
from collections import Counter
from datetime import datetime
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
PDF_NAME = "基于改进DeepLabV3+的石漠化地区裸岩信息提取_吴永俊.pdf"
PDF_PATH = f"docs/literature/pdfs/package_2000_2026/{PDF_NAME}"
PAPER_ID = "KRD0116"
TITLE = "基于改进DeepLabV3+的石漠化地区裸岩信息提取"
AUTHOR_CANDIDATE = "吴永俊"


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def write_csv(path: Path, rows: list[dict[str, str]], fields: list[str]) -> None:
    with path.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)


def find_pdf_inventory_row() -> dict[str, str]:
    rows = read_csv(REPO_ROOT / "database" / "pdf_inventory.csv")
    for row in rows:
        if row.get("relative_path") == PDF_PATH:
            return row
    raise SystemExit(f"PDF not found in inventory: {PDF_PATH}")


def upsert_cleaned(pdf_row: dict[str, str]) -> None:
    path = REPO_ROOT / "database" / "literature_database_cleaned.csv"
    rows = read_csv(path)
    fields = list(rows[0].keys())
    new_row = {field: "" for field in fields}
    new_row.update(
        {
            "paper_id": PAPER_ID,
            "title": TITLE,
            "translated_title": "",
            "language": "Chinese",
            "year": "",
            "authors": AUTHOR_CANDIDATE,
            "journal_or_source": "",
            "doi": "",
            "url": "",
            "pdf_path": PDF_PATH,
            "sha256": pdf_row.get("sha256", ""),
            "source_collection": "package_2000_2026",
            "source_manifest": "",
            "topic_group": "deep_learning_segmentation",
            "method_group": "DeepLabV3+",
            "data_source": "",
            "relevance_level": "high",
            "open_access_status": "",
            "metadata_status": "partial",
            "notes": "Added from local PDF filename; author candidate, year, journal, and DOI need manual verification. Supports DeepLabV3+ semantic segmentation and bare-rock information extraction.",
        }
    )
    rows = [row for row in rows if row.get("paper_id") != PAPER_ID]
    rows.append(new_row)
    write_csv(path, rows, fields)


def upsert_missing_metadata() -> None:
    path = REPO_ROOT / "database" / "missing_metadata.csv"
    rows = read_csv(path)
    fields = list(rows[0].keys())
    rows = [row for row in rows if row.get("paper_id") != PAPER_ID]
    base = {field: "" for field in fields}
    base.update(
        {
            "paper_id": PAPER_ID,
            "title": TITLE,
            "language": "Chinese",
            "authors": AUTHOR_CANDIDATE,
            "pdf_path": PDF_PATH,
            "source_collection": "package_2000_2026",
            "topic_group": "deep_learning_segmentation",
            "method_group": "DeepLabV3+",
            "relevance_level": "high",
            "metadata_status": "partial",
            "notes": "Added from filename; year, journal, DOI, URL, and detailed metadata require manual verification.",
            "missing_fields": "year;doi;journal_or_source;url",
        }
    )
    rows.append(base)
    write_csv(path, rows, fields)


def upsert_priority() -> None:
    path = REPO_ROOT / "database" / "priority_reading_list.csv"
    rows = read_csv(path)
    fields = list(rows[0].keys())
    rows = [row for row in rows if row.get("paper_id") != PAPER_ID]
    rows.append(
        {
            "paper_id": PAPER_ID,
            "title": TITLE,
            "year": "",
            "language": "Chinese",
            "pdf_path": PDF_PATH,
            "topic_group": "deep_learning_segmentation",
            "method_group": "DeepLabV3+",
            "readability_status": "ready",
            "use_nature_reader_skill": "yes",
            "reason_for_priority": "新增核心论文；改进DeepLabV3+；石漠化地区裸岩信息提取；semantic segmentation support",
            "notes": "Added after batch_01_core as supplemental priority paper; metadata needs manual verification.",
        }
    )
    write_csv(path, rows, fields)


def update_overview() -> None:
    rows = read_csv(REPO_ROOT / "database" / "literature_database_cleaned.csv")
    by_year = Counter(row.get("year") or "missing" for row in rows)
    by_topic = Counter(row.get("topic_group") or "other" for row in rows)
    by_method = Counter(method for row in rows for method in (row.get("method_group") or "unknown").split(";"))
    with_pdf = [row for row in rows if row.get("pdf_path")]
    metadata_only = [row for row in rows if row.get("source_manifest") and not row.get("pdf_path")]
    chinese = [row for row in rows if row.get("language") == "Chinese" or any("\u4e00" <= c <= "\u9fff" for c in row.get("title", ""))]
    english = [row for row in rows if row.get("language") == "English"]
    missing_doi = [row for row in rows if not row.get("doi")]
    needs_check = [row for row in rows if row.get("metadata_status") in {"needs_manual_check", "partial", "pdf_only"}]

    def counter_lines(counter: Counter[str]) -> list[str]:
        return [f"- {key}: {value}" for key, value in sorted(counter.items(), key=lambda item: str(item[0]))]

    def record_lines(records: list[dict[str, str]], limit: int = 80) -> list[str]:
        if not records:
            return ["- None"]
        return [f"- {row.get('paper_id')} ({row.get('year') or 'year missing'}): {row.get('title') or row.get('notes')[:100]}" for row in records[:limit]]

    lines = [
        "# Literature Database Overview",
        "",
        f"Generated: {datetime.now().isoformat(timespec='seconds')}",
        "",
        "## Summary",
        "",
        f"- Total literature records: {len(rows)}",
        f"- Records with PDF: {len(with_pdf)}",
        f"- Metadata-only records without PDF: {len(metadata_only)}",
        f"- Chinese literature records: {len(chinese)}",
        f"- English literature records: {len(english)}",
        "",
        "## Records by year",
        "",
        *counter_lines(by_year),
        "",
        "## Records by topic_group",
        "",
        *counter_lines(by_topic),
        "",
        "## Records by method_group",
        "",
        *counter_lines(by_method),
        "",
        "## Missing DOI",
        "",
        *record_lines(missing_doi),
        "",
        "## Needs manual check or partial metadata",
        "",
        *record_lines(needs_check),
        "",
        "## Supplemental additions",
        "",
        f"- {PAPER_ID}: {TITLE}; local PDF added at `{PDF_PATH}`.",
        "",
    ]
    (REPO_ROOT / "docs" / "literature" / "synthesis" / "literature_database_overview.md").write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    if not (REPO_ROOT / PDF_PATH).exists():
        raise SystemExit(f"Missing PDF: {REPO_ROOT / PDF_PATH}")
    pdf_row = find_pdf_inventory_row()
    upsert_cleaned(pdf_row)
    upsert_missing_metadata()
    upsert_priority()
    update_overview()
    print(f"Added/updated {PAPER_ID}: {TITLE}")


if __name__ == "__main__":
    main()
