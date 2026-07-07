#!/usr/bin/env python3
"""Build an inventory for literature PDFs stored in this repository."""

from __future__ import annotations

import csv
import hashlib
import re
from collections import defaultdict
from datetime import datetime
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
PDF_ROOT = REPO_ROOT / "docs" / "literature" / "pdfs"
DATABASE_DIR = REPO_ROOT / "database"
LOG_DIR = REPO_ROOT / "logs"


def sha256_file(path: Path, chunk_size: int = 1024 * 1024) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(chunk_size), b""):
            digest.update(chunk)
    return digest.hexdigest()


def possible_year_from_filename(file_name: str) -> str:
    match = re.search(r"(19|20)\d{2}", file_name)
    return match.group(0) if match else ""


def possible_title_from_filename(file_name: str) -> str:
    stem = Path(file_name).stem
    title = re.sub(r"[_\-]+", " ", stem)
    title = re.sub(r"\s+", " ", title).strip()
    return title


def source_collection(relative_path: Path) -> str:
    parts = relative_path.parts
    if len(parts) >= 4:
        return parts[3]
    return ""


def build_inventory() -> tuple[list[dict[str, str]], list[dict[str, str]]]:
    rows: list[dict[str, str]] = []
    by_hash: dict[str, list[dict[str, str]]] = defaultdict(list)

    for pdf_path in sorted(PDF_ROOT.rglob("*.pdf")):
        stat = pdf_path.stat()
        relative = pdf_path.relative_to(REPO_ROOT)
        digest = sha256_file(pdf_path)
        row = {
            "file_name": pdf_path.name,
            "relative_path": relative.as_posix(),
            "source_collection": source_collection(relative),
            "file_size_bytes": str(stat.st_size),
            "file_size_mib": f"{stat.st_size / (1024 * 1024):.3f}",
            "modified_time": datetime.fromtimestamp(stat.st_mtime).isoformat(timespec="seconds"),
            "sha256": digest,
            "possible_year_from_filename": possible_year_from_filename(pdf_path.name),
            "possible_title_from_filename": possible_title_from_filename(pdf_path.name),
        }
        rows.append(row)
        by_hash[digest].append(row)

    duplicate_rows: list[dict[str, str]] = []
    for digest, group in sorted(by_hash.items()):
        if len(group) <= 1:
            continue
        duplicate_group_id = digest[:16]
        for index, row in enumerate(group, start=1):
            duplicate_rows.append(
                {
                    "duplicate_group_id": duplicate_group_id,
                    "duplicate_index": str(index),
                    "duplicate_count": str(len(group)),
                    **row,
                }
            )

    return rows, duplicate_rows


def write_csv(path: Path, rows: list[dict[str, str]], fieldnames: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8-sig") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def write_log(rows: list[dict[str, str]], duplicate_rows: list[dict[str, str]]) -> None:
    LOG_DIR.mkdir(parents=True, exist_ok=True)
    total_bytes = sum(int(row["file_size_bytes"]) for row in rows)
    collections: dict[str, int] = defaultdict(int)
    for row in rows:
        collections[row["source_collection"]] += 1

    lines = [
        "# PDF Inventory Log",
        "",
        f"Generated: {datetime.now().isoformat(timespec='seconds')}",
        f"PDF root: `{PDF_ROOT.relative_to(REPO_ROOT).as_posix()}`",
        f"Total PDFs: {len(rows)}",
        f"Total size MiB: {total_bytes / (1024 * 1024):.3f}",
        f"Duplicate PDF file rows: {len(duplicate_rows)}",
        f"Duplicate SHA256 groups: {len(set(row['duplicate_group_id'] for row in duplicate_rows))}",
        "",
        "## Source collections",
        "",
    ]
    for collection, count in sorted(collections.items()):
        lines.append(f"- {collection}: {count}")

    lines.extend(["", "## Duplicate groups", ""])
    if duplicate_rows:
        groups: dict[str, list[dict[str, str]]] = defaultdict(list)
        for row in duplicate_rows:
            groups[row["duplicate_group_id"]].append(row)
        for group_id, group in sorted(groups.items()):
            lines.append(f"### {group_id}")
            for row in group:
                lines.append(f"- `{row['relative_path']}`")
            lines.append("")
    else:
        lines.append("No duplicate PDFs detected by SHA256.")

    (LOG_DIR / "pdf_inventory_log.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    DATABASE_DIR.mkdir(parents=True, exist_ok=True)
    LOG_DIR.mkdir(parents=True, exist_ok=True)

    rows, duplicate_rows = build_inventory()

    inventory_fields = [
        "file_name",
        "relative_path",
        "source_collection",
        "file_size_bytes",
        "file_size_mib",
        "modified_time",
        "sha256",
        "possible_year_from_filename",
        "possible_title_from_filename",
    ]
    duplicate_fields = [
        "duplicate_group_id",
        "duplicate_index",
        "duplicate_count",
        *inventory_fields,
    ]

    write_csv(DATABASE_DIR / "pdf_inventory.csv", rows, inventory_fields)
    write_csv(DATABASE_DIR / "pdf_duplicates.csv", duplicate_rows, duplicate_fields)
    write_log(rows, duplicate_rows)

    print(f"Wrote {len(rows)} PDF inventory rows.")
    print(f"Wrote {len(duplicate_rows)} duplicate PDF rows.")


if __name__ == "__main__":
    main()
