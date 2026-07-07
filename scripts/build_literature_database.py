#!/usr/bin/env python3
"""Build a structured KRD literature database from manifests and PDF inventory."""

from __future__ import annotations

import csv
import re
from collections import Counter, defaultdict
from dataclasses import dataclass, field
from datetime import datetime
from difflib import SequenceMatcher
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
PDF_INVENTORY = REPO_ROOT / "database" / "pdf_inventory.csv"
PDF_DUPLICATES = REPO_ROOT / "database" / "pdf_duplicates.csv"
MANIFEST_DIR = REPO_ROOT / "docs" / "literature" / "manifests"
SYNTHESIS_DIR = REPO_ROOT / "docs" / "literature" / "synthesis"
DATABASE_DIR = REPO_ROOT / "database"
LOG_DIR = REPO_ROOT / "logs"


CLEAN_FIELDS = [
    "paper_id",
    "title",
    "translated_title",
    "language",
    "year",
    "authors",
    "journal_or_source",
    "doi",
    "url",
    "pdf_path",
    "sha256",
    "source_collection",
    "source_manifest",
    "topic_group",
    "method_group",
    "data_source",
    "relevance_level",
    "open_access_status",
    "metadata_status",
    "notes",
]

RAW_FIELDS = [
    "raw_record_id",
    "raw_source_type",
    "source_file",
    "source_row",
    "match_key",
    *CLEAN_FIELDS,
]


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def write_csv(path: Path, rows: list[dict[str, str]], fields: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)


def first_present(row: dict[str, str], *names: str) -> str:
    for name in names:
        value = (row.get(name) or "").strip()
        if value:
            return value
    return ""


def normalize_doi(doi: str) -> str:
    doi = (doi or "").strip()
    doi = re.sub(r"^https?://(dx\.)?doi\.org/", "", doi, flags=re.I)
    doi = doi.strip().strip(".")
    return doi.lower()


def normalize_title(title: str) -> str:
    title = (title or "").lower()
    title = re.sub(r"[\W_]+", " ", title, flags=re.UNICODE)
    title = re.sub(r"\s+", " ", title).strip()
    return title


def title_similarity(a: str, b: str) -> float:
    a_norm = normalize_title(a)
    b_norm = normalize_title(b)
    if not a_norm or not b_norm:
        return 0.0
    return SequenceMatcher(None, a_norm, b_norm).ratio()


def has_cjk(text: str) -> bool:
    return bool(re.search(r"[\u4e00-\u9fff]", text or ""))


def normalize_language(value: str, title: str) -> str:
    value = (value or "").strip()
    low = value.lower()
    if low in {"en", "eng", "english"}:
        return "English"
    if low in {"cn", "zh", "chinese"}:
        return "Chinese"
    if "english" in low and "chinese" in low:
        return "English/Chinese"
    if "english" in low:
        return "English"
    if "chinese" in low:
        return "Chinese"
    if has_cjk(title):
        return "Chinese"
    return value


def normalize_relevance(value: str) -> str:
    low = (value or "").lower()
    if "very high" in low:
        return "very_high"
    if "high" in low:
        return "high"
    if "medium" in low:
        return "medium"
    if "low" in low:
        return "low"
    return value.strip()


def classify_topic(text: str) -> str:
    low = text.lower()
    if "review" in low or "综述" in text:
        return "review"
    if any(k in low for k in ["deeplab", "u-net", "unet", "fcn", "semantic segmentation", "segmentation"]):
        return "deep_learning_segmentation"
    if any(k in low for k in ["lsmm", "mesma", "spectral mixture", "sma"]):
        return "lsmm_mesma_sma"
    if any(k in low for k in ["fbr", "bare rock", "bedrock", "rock fraction"]):
        return "bare_rock_fraction_fbr"
    if any(k in low for k in ["dem", "topograph", "terrain", "slope"]):
        return "dem_topography"
    if any(k in low for k in ["gee", "google earth engine", "time series", "spatiotemporal", "temporal"]):
        return "gee_time_series"
    if any(k in low for k in ["machine learning", "random forest", " rf", "svm", "bpnn", "classification"]):
        return "machine_learning"
    if "desertification" in low and "rocky" not in low:
        return "broader_desertification"
    if "rocky desertification" in low or "karst" in low or "石漠化" in text:
        return "rocky_desertification_classification"
    return "other"


def classify_methods(text: str) -> str:
    checks = [
        ("DeepLabV3+", ["deeplabv3+", "deeplabv3", "deeplab"]),
        ("U-Net", ["u-net", "unet"]),
        ("FCN", ["fcn"]),
        ("MESMA", ["mesma", "multiple endmember"]),
        ("LSMM", ["lsmm", "linear spectral mixture"]),
        ("SMA", ["sma", "spectral mixture analysis"]),
        ("RF", ["random forest", " rf", "rf;"]),
        ("SVM", ["svm", "support vector"]),
        ("BPNN", ["bpnn", "neural network"]),
        ("feature_space", ["feature space"]),
        ("vegetation_index", ["vegetation index", "ndvi", "kndvi", "index"]),
        ("GEE", ["gee", "google earth engine"]),
        ("time_series", ["time series", "spatiotemporal", "temporal"]),
        ("DEM_ablation", ["dem", "topograph", "terrain"]),
        ("review", ["review", "综述"]),
    ]
    low = text.lower()
    found = [label for label, needles in checks if any(needle in low for needle in needles)]
    return ";".join(dict.fromkeys(found)) if found else "unknown"


def status_for(row: dict[str, str], has_pdf: bool, manifest_only: bool = False) -> str:
    if row.get("metadata_status") == "duplicate":
        return "duplicate"
    required = ["title", "year", "doi"]
    present = sum(1 for key in required if (row.get(key) or "").strip())
    if has_pdf and present == 0:
        return "pdf_only"
    if manifest_only and not has_pdf:
        return "manifest_only"
    if present == len(required):
        return "complete"
    if present >= 1:
        return "partial"
    return "needs_manual_check"


@dataclass
class Record:
    title: str = ""
    translated_title: str = ""
    language: str = ""
    year: str = ""
    authors: str = ""
    journal_or_source: str = ""
    doi: str = ""
    url: str = ""
    pdf_paths: list[str] = field(default_factory=list)
    sha256_values: list[str] = field(default_factory=list)
    source_collections: list[str] = field(default_factory=list)
    source_manifests: list[str] = field(default_factory=list)
    topic_group: str = ""
    method_group: str = ""
    data_source: str = ""
    relevance_level: str = ""
    open_access_status: str = ""
    metadata_status_override: str = ""
    notes: list[str] = field(default_factory=list)
    raw_sources: list[str] = field(default_factory=list)
    duplicate_of: str = ""

    def merge_from(self, other: "Record") -> None:
        for attr in [
            "title",
            "translated_title",
            "language",
            "year",
            "authors",
            "journal_or_source",
            "doi",
            "url",
            "topic_group",
            "method_group",
            "data_source",
            "relevance_level",
            "open_access_status",
        ]:
            if not getattr(self, attr) and getattr(other, attr):
                setattr(self, attr, getattr(other, attr))
        for attr in ["pdf_paths", "sha256_values", "source_collections", "source_manifests", "notes", "raw_sources"]:
            existing = list(getattr(self, attr))
            for value in getattr(other, attr):
                if value and value not in existing:
                    existing.append(value)
            setattr(self, attr, existing)

    def clean_row(self, paper_id: str) -> dict[str, str]:
        row = {
            "paper_id": paper_id,
            "title": self.title,
            "translated_title": self.translated_title,
            "language": self.language,
            "year": self.year,
            "authors": self.authors,
            "journal_or_source": self.journal_or_source,
            "doi": self.doi,
            "url": self.url,
            "pdf_path": "; ".join(self.pdf_paths),
            "sha256": "; ".join(self.sha256_values),
            "source_collection": "; ".join(self.source_collections),
            "source_manifest": "; ".join(self.source_manifests),
            "topic_group": self.topic_group or "other",
            "method_group": self.method_group or "unknown",
            "data_source": self.data_source,
            "relevance_level": self.relevance_level,
            "open_access_status": self.open_access_status,
            "notes": " | ".join(self.notes),
        }
        row["metadata_status"] = self.metadata_status_override or status_for(
            row, bool(self.pdf_paths), bool(self.source_manifests and not self.pdf_paths)
        )
        return row


def manifest_record(row: dict[str, str], source_name: str, source_row: int) -> Record:
    title = first_present(row, "title", "Title")
    language = normalize_language(first_present(row, "lang", "language"), title)
    doi = normalize_doi(first_present(row, "doi", "DOI"))
    url = first_present(row, "url", "article_url", "pdf_url", "official_pdf_url")
    journal = first_present(row, "journal", "venue", "source", "category")
    methods = first_present(row, "methods", "method")
    topic = first_present(row, "topic")
    data = first_present(row, "data", "data_source")
    relevance = normalize_relevance(first_present(row, "relevance"))
    notes = [first_present(row, "notes", "reason") or ""]
    verify = first_present(row, "verify_in")
    if verify:
        notes.append(f"verify_in: {verify}")
    source_status = first_present(row, "status")
    if source_status:
        notes.append(f"manifest_status: {source_status}")
    status_text = " ".join([source_name, title, source_status, first_present(row, "reason")]).lower()
    metadata_status_override = ""
    if "candidate" in status_text or "to verify" in status_text or "query bucket" in status_text:
        metadata_status_override = "needs_manual_check"
    open_access_status = source_status if "open" in source_status.lower() else ""
    text_for_classification = " ".join([title, topic, methods, data])
    return Record(
        title=title,
        language=language,
        year=first_present(row, "year"),
        authors=first_present(row, "authors"),
        journal_or_source=journal,
        doi=doi,
        url=url,
        source_manifests=[source_name],
        topic_group=classify_topic(text_for_classification),
        method_group=classify_methods(text_for_classification),
        data_source=data,
        relevance_level=relevance,
        open_access_status=open_access_status,
        metadata_status_override=metadata_status_override,
        notes=[note for note in notes if note],
        raw_sources=[f"{source_name}:{source_row}"],
    )


def pdf_record(row: dict[str, str]) -> Record:
    candidate = first_present(row, "possible_title_from_filename")
    notes = []
    if candidate:
        notes.append(f"filename_title_candidate: {candidate}")
    return Record(
        pdf_paths=[first_present(row, "relative_path")],
        sha256_values=[first_present(row, "sha256")],
        source_collections=[first_present(row, "source_collection")],
        topic_group=classify_topic(candidate),
        method_group=classify_methods(candidate),
        notes=notes,
        raw_sources=[first_present(row, "relative_path")],
    )


def add_or_merge(records: list[Record], incoming: Record) -> tuple[int, str, float]:
    incoming_doi = normalize_doi(incoming.doi)
    if incoming_doi:
        for idx, record in enumerate(records):
            if normalize_doi(record.doi) == incoming_doi:
                record.merge_from(incoming)
                return idx, "doi", 1.0

    if incoming.title:
        best_idx = -1
        best_score = 0.0
        for idx, record in enumerate(records):
            score = title_similarity(record.title, incoming.title)
            if score > best_score:
                best_idx, best_score = idx, score
        if best_idx >= 0 and best_score >= 0.90:
            records[best_idx].merge_from(incoming)
            return best_idx, "title_similarity", best_score

    records.append(incoming)
    return len(records) - 1, "new", 0.0


def attach_pdf(records: list[Record], incoming: Record) -> tuple[int, str, float]:
    sha = incoming.sha256_values[0] if incoming.sha256_values else ""
    for idx, record in enumerate(records):
        if sha and sha in record.sha256_values:
            record.merge_from(incoming)
            return idx, "sha256", 1.0

    candidate = ""
    for note in incoming.notes:
        if note.startswith("filename_title_candidate: "):
            candidate = note.replace("filename_title_candidate: ", "", 1)
            break

    best_idx = -1
    best_score = 0.0
    for idx, record in enumerate(records):
        score = title_similarity(record.title, candidate)
        if score > best_score:
            best_idx, best_score = idx, score

    if best_idx >= 0 and best_score >= 0.76:
        records[best_idx].merge_from(incoming)
        records[best_idx].notes.append(f"pdf_matched_by_filename_similarity={best_score:.3f}")
        return best_idx, "pdf_filename_title_similarity", best_score

    records.append(incoming)
    return len(records) - 1, "pdf_only_new", 0.0


def attach_note_mentions(records: list[Record]) -> None:
    markdown_files = sorted([*SYNTHESIS_DIR.glob("*.md"), *SYNTHESIS_DIR.glob("*.markdown")])
    note_texts = []
    for path in markdown_files:
        try:
            note_texts.append((path.name, path.read_text(encoding="utf-8", errors="ignore").lower()))
        except OSError:
            continue

    for record in records:
        norm_title = normalize_title(record.title)
        if not norm_title or len(norm_title) < 20:
            continue
        compact_title = norm_title[:80]
        mentions = []
        for name, text in note_texts:
            if compact_title in normalize_title(text):
                mentions.append(name)
        if mentions:
            record.notes.append("mentioned_in_notes: " + "; ".join(mentions))


def duplicate_rows(cleaned_rows: list[dict[str, str]]) -> list[dict[str, str]]:
    dupes: list[dict[str, str]] = []
    by_doi: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in cleaned_rows:
        doi = normalize_doi(row["doi"])
        if doi:
            by_doi[doi].append(row)
    for doi, rows in sorted(by_doi.items()):
        if len(rows) > 1:
            for row in rows:
                dupes.append({"duplicate_reason": "doi", "duplicate_key": doi, **row})

    seen_pairs = set()
    for i, left in enumerate(cleaned_rows):
        for right in cleaned_rows[i + 1 :]:
            score = title_similarity(left["title"], right["title"])
            if score >= 0.92:
                key = tuple(sorted([left["paper_id"], right["paper_id"]]))
                if key not in seen_pairs:
                    seen_pairs.add(key)
                    dupes.append({"duplicate_reason": f"title_similarity={score:.3f}", "duplicate_key": left["title"], **left})
                    dupes.append({"duplicate_reason": f"title_similarity={score:.3f}", "duplicate_key": left["title"], **right})
    return dupes


def missing_metadata_rows(cleaned_rows: list[dict[str, str]]) -> list[dict[str, str]]:
    rows = []
    for row in cleaned_rows:
        missing = [key for key in ["title", "year", "doi", "authors", "journal_or_source"] if not row.get(key)]
        if row["metadata_status"] in {"needs_manual_check", "partial", "pdf_only", "manifest_only"} or missing:
            rows.append({**row, "missing_fields": ";".join(missing)})
    return rows


def priority_score(row: dict[str, str]) -> tuple[int, str]:
    text = " ".join([row.get("title", ""), row.get("topic_group", ""), row.get("method_group", ""), row.get("notes", "")]).lower()
    score = 0
    for keyword, weight in [
        ("bare_rock_fraction_fbr", 5),
        ("lsmm_mesma_sma", 5),
        ("mesma", 5),
        ("lsmm", 5),
        ("deeplabv3+", 4),
        ("deep_learning_segmentation", 4),
        ("machine_learning", 3),
        ("dem_topography", 3),
        ("gee_time_series", 2),
        ("very_high", 3),
        ("high", 2),
    ]:
        if keyword in text:
            score += weight
    if row.get("pdf_path"):
        score += 2
    if row.get("doi"):
        score += 1
    return (-score, row.get("year", "9999"))


def write_overview(cleaned_rows: list[dict[str, str]]) -> None:
    total = len(cleaned_rows)
    with_pdf = [row for row in cleaned_rows if row["pdf_path"]]
    metadata_only = [row for row in cleaned_rows if row["source_manifest"] and not row["pdf_path"]]
    chinese = [row for row in cleaned_rows if row["language"] == "Chinese" or has_cjk(row["title"])]
    english = [row for row in cleaned_rows if row["language"] == "English"]
    by_year = Counter(row["year"] or "missing" for row in cleaned_rows)
    by_topic = Counter(row["topic_group"] or "other" for row in cleaned_rows)
    by_method = Counter(method for row in cleaned_rows for method in (row["method_group"] or "unknown").split(";"))
    missing_doi = [row for row in cleaned_rows if not row["doi"]]
    missing_year = [row for row in cleaned_rows if not row["year"]]
    missing_title = [row for row in cleaned_rows if not row["title"]]
    needs_check = [row for row in cleaned_rows if row["metadata_status"] == "needs_manual_check" or "manual" in row["metadata_status"]]
    priority = sorted(cleaned_rows, key=priority_score)[:20]

    def counter_lines(counter: Counter[str]) -> list[str]:
        return [f"- {key}: {value}" for key, value in sorted(counter.items(), key=lambda item: (str(item[0]) == "missing", str(item[0])))]

    def record_lines(rows: list[dict[str, str]], limit: int | None = None) -> list[str]:
        selected = rows if limit is None else rows[:limit]
        if not selected:
            return ["- None"]
        lines = []
        for row in selected:
            label = row["title"] or row["notes"][:120] or row["paper_id"]
            year = row["year"] or "year missing"
            lines.append(f"- {row['paper_id']} ({year}): {label}")
        return lines

    lines = [
        "# Literature Database Overview",
        "",
        f"Generated: {datetime.now().isoformat(timespec='seconds')}",
        "",
        "## Summary",
        "",
        f"- Total literature records: {total}",
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
        "## Missing year",
        "",
        *record_lines(missing_year),
        "",
        "## Missing title",
        "",
        *record_lines(missing_title),
        "",
        "## Needs manual check",
        "",
        *record_lines(needs_check),
        "",
        "## Priority reading list",
        "",
        *record_lines(priority, 20),
        "",
    ]
    (SYNTHESIS_DIR / "literature_database_overview.md").write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    records: list[Record] = []
    raw_rows: list[dict[str, str]] = []
    match_events: list[str] = []

    pdf_rows = read_csv(PDF_INVENTORY)
    manifest_paths = sorted(MANIFEST_DIR.glob("*.csv"))

    for manifest_path in manifest_paths:
        for source_row, row in enumerate(read_csv(manifest_path), start=2):
            record = manifest_record(row, manifest_path.name, source_row)
            idx, reason, score = add_or_merge(records, record)
            match_events.append(f"manifest {manifest_path.name}:{source_row} -> record_index={idx} reason={reason} score={score:.3f}")
            raw_rows.append(
                {
                    "raw_record_id": f"RAW{len(raw_rows)+1:05d}",
                    "raw_source_type": "manifest",
                    "source_file": manifest_path.name,
                    "source_row": str(source_row),
                    "match_key": reason,
                    **record.clean_row(""),
                }
            )

    for row in pdf_rows:
        record = pdf_record(row)
        idx, reason, score = attach_pdf(records, record)
        match_events.append(f"pdf {row.get('relative_path','')} -> record_index={idx} reason={reason} score={score:.3f}")
        raw_rows.append(
            {
                "raw_record_id": f"RAW{len(raw_rows)+1:05d}",
                "raw_source_type": "pdf_inventory",
                "source_file": "database/pdf_inventory.csv",
                "source_row": "",
                "match_key": reason,
                **record.clean_row(""),
            }
        )

    attach_note_mentions(records)

    cleaned_rows = [record.clean_row(f"KRD{idx:04d}") for idx, record in enumerate(records, start=1)]
    cleaned_rows.sort(key=lambda row: (row["year"] or "9999", normalize_title(row["title"]) or row["paper_id"]))

    for idx, row in enumerate(cleaned_rows, start=1):
        row["paper_id"] = f"KRD{idx:04d}"

    dupes = duplicate_rows(cleaned_rows)
    missing = missing_metadata_rows(cleaned_rows)

    write_csv(DATABASE_DIR / "literature_database_raw.csv", raw_rows, RAW_FIELDS)
    write_csv(DATABASE_DIR / "literature_database_cleaned.csv", cleaned_rows, CLEAN_FIELDS)
    write_csv(DATABASE_DIR / "missing_metadata.csv", missing, [*CLEAN_FIELDS, "missing_fields"])
    write_csv(DATABASE_DIR / "duplicate_literature_records.csv", dupes, ["duplicate_reason", "duplicate_key", *CLEAN_FIELDS])
    write_overview(cleaned_rows)

    LOG_DIR.mkdir(parents=True, exist_ok=True)
    log_lines = [
        "# Literature Database Build Log",
        "",
        f"Generated: {datetime.now().isoformat(timespec='seconds')}",
        f"PDF inventory rows read: {len(pdf_rows)}",
        f"Manifest CSV files read: {len(manifest_paths)}",
        f"Raw input rows written: {len(raw_rows)}",
        f"Cleaned records written: {len(cleaned_rows)}",
        f"Missing metadata rows written: {len(missing)}",
        f"Potential duplicate rows written: {len(dupes)}",
        "",
        "## Manifest files",
        "",
        *[f"- {path.name}: {len(read_csv(path))} rows" for path in manifest_paths],
        "",
        "## Matching events",
        "",
        *[f"- {event}" for event in match_events],
        "",
    ]
    (LOG_DIR / "literature_database_build_log.md").write_text("\n".join(log_lines), encoding="utf-8")

    print(f"Read {len(pdf_rows)} pdf_inventory rows.")
    print(f"Read {len(manifest_paths)} manifest CSV files.")
    print(f"Wrote {len(raw_rows)} raw rows.")
    print(f"Wrote {len(cleaned_rows)} cleaned records.")
    print(f"Wrote {len(missing)} missing metadata rows.")
    print(f"Wrote {len(dupes)} duplicate candidate rows.")


if __name__ == "__main__":
    main()
