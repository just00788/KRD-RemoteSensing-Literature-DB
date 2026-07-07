from __future__ import annotations

import csv
import re
from collections import Counter, defaultdict
from difflib import SequenceMatcher
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DB = ROOT / "database"
SYN = ROOT / "docs" / "literature" / "synthesis"
READERS = ROOT / "docs" / "literature" / "readers"
CARDS = ROOT / "docs" / "literature" / "paper_cards"


DUP_FIELDS = [
    "duplicate_group_id",
    "canonical_paper_id",
    "duplicate_paper_id",
    "duplicate_title",
    "duplicate_year",
    "duplicate_doi",
    "duplicate_source",
    "duplicate_reason",
    "merge_confidence",
    "keep_or_merge",
    "notes",
]

CANON_FIELDS = [
    "canonical_paper_id",
    "all_source_paper_ids",
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
    "relevance_level",
    "metadata_status",
    "source_manifests",
    "duplicate_group_id",
    "deduplication_confidence",
    "needs_manual_confirmation",
    "notes",
]

MAP_FIELDS = [
    "canonical_paper_id",
    "title",
    "year",
    "language",
    "journal_or_source",
    "doi",
    "mapped_pdf_path",
    "mapped_pdf_sha256",
    "pdf_mapping_status",
    "pdf_mapping_confidence",
    "pdf_match_method",
    "has_reader",
    "has_paper_card",
    "read_status",
    "suggested_for_batch_03",
    "notes",
]


class DSU:
    def __init__(self, ids: list[str]) -> None:
        self.parent = {x: x for x in ids}

    def find(self, x: str) -> str:
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, a: str, b: str) -> None:
        ra, rb = self.find(a), self.find(b)
        if ra == rb:
            return
        self.parent[max(ra, rb)] = min(ra, rb)


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


def norm_title(text: str) -> str:
    text = (text or "").lower()
    text = re.sub(r"cnki query bucket:|google scholar query bucket:", " ", text)
    text = re.sub(r"^\s*\d{4}\s*remotesens\s*\d+\s*\d+\s*", " ", text)
    text = re.sub(r"\b(pdf|main|remote\s*sens|remotesens)\b", " ", text)
    text = re.sub(r"[^0-9a-z\u4e00-\u9fff]+", "", text)
    return text


def norm_doi(text: str) -> str:
    text = (text or "").strip().lower()
    text = text.replace("https://doi.org/", "").replace("http://doi.org/", "")
    return text


def is_placeholder(row: dict[str, str]) -> bool:
    title = (row.get("title") or "").lower()
    return "query bucket" in title or row.get("year") == "2000-2026"


def useful_title(row: dict[str, str]) -> str:
    for key in ("title", "translated_title"):
        val = row.get(key, "")
        if val and not is_placeholder(row):
            return val
    return row.get("title", "")


def title_candidates(row: dict[str, str], pdf_by_path: dict[str, dict[str, str]]) -> list[tuple[str, str]]:
    candidates: list[tuple[str, str]] = []
    if row.get("title") and not is_placeholder(row):
        candidates.append(("metadata_title", norm_title(row.get("title", ""))))
    if row.get("translated_title"):
        candidates.append(("translated_title", norm_title(row.get("translated_title", ""))))
    pdf_path = row.get("pdf_path", "")
    if pdf_path and pdf_path in pdf_by_path:
        pdf = pdf_by_path[pdf_path]
        candidates.append(("pdf_possible_title", norm_title(pdf.get("possible_title_from_filename", ""))))
        candidates.append(("pdf_file_name", norm_title(Path(pdf.get("file_name", "")).stem)))
    return [(source, value) for source, value in candidates if len(value) >= 16]


def collect_ids(folder: Path, suffix: str) -> set[str]:
    ids: set[str] = set()
    if not folder.exists():
        return ids
    regex = re.compile(r"(KRD\d+)_" + re.escape(suffix) + r"\.md$")
    for path in folder.rglob("*.md"):
        match = regex.search(path.name)
        if match:
            ids.add(match.group(1))
    return ids


def score_title(a: str, b: str) -> float:
    if not a or not b:
        return 0.0
    shorter, longer = sorted((a, b), key=len)
    if len(shorter) >= 24 and shorter in longer:
        coverage = len(shorter) / max(len(longer), 1)
        if coverage >= 0.45:
            return 0.95
    return SequenceMatcher(None, a, b).ratio()


def add_reason(reasons: dict[tuple[str, str], list[tuple[str, float, bool]]], a: str, b: str, reason: str, conf: float, manual: bool = False) -> None:
    key = tuple(sorted((a, b)))
    reasons[key].append((reason, conf, manual))


def choose_value(rows: list[dict[str, str]], key: str) -> str:
    vals = [r.get(key, "").strip() for r in rows if r.get(key, "").strip()]
    if not vals:
        return ""
    vals.sort(key=lambda v: (len(v), v), reverse=True)
    return vals[0]


def choose_title(rows: list[dict[str, str]]) -> str:
    titles = [r.get("title", "").strip() for r in rows if r.get("title", "").strip() and not is_placeholder(r)]
    if not titles:
        titles = [r.get("title", "").strip() for r in rows if r.get("title", "").strip()]
    if not titles:
        return ""
    return sorted(titles, key=lambda v: (len(v), v), reverse=True)[0]


def split_multi(text: str) -> list[str]:
    if not text:
        return []
    parts = re.split(r";|\|", text)
    return [p.strip() for p in parts if p.strip()]


def merge_multi(rows: list[dict[str, str]], key: str) -> str:
    seen: list[str] = []
    for row in rows:
        for part in split_multi(row.get(key, "")):
            if part not in seen:
                seen.append(part)
    return "; ".join(seen)


def best_pdf_for_group(rows: list[dict[str, str]], pdf_rows: list[dict[str, str]]) -> tuple[str, str, str, str, str]:
    direct = []
    for row in rows:
        pdf_path = row.get("pdf_path", "").strip()
        if pdf_path:
            inv = next((p for p in pdf_rows if p.get("relative_path") == pdf_path), None)
            direct.append((pdf_path, row.get("sha256") or (inv or {}).get("sha256", ""), "mapped", "1.00", "database_pdf_path"))
    if direct:
        direct.sort(key=lambda x: (0 if x[1] else 1, x[0]))
        return direct[0]

    row_titles = [norm_title(r.get("title", "")) for r in rows if not is_placeholder(r)]
    row_titles += [norm_title(r.get("translated_title", "")) for r in rows if r.get("translated_title")]
    row_titles = [t for t in row_titles if len(t) >= 12]
    best: tuple[float, dict[str, str] | None] = (0.0, None)
    for pdf in pdf_rows:
        possible = norm_title(pdf.get("possible_title_from_filename", ""))
        if len(possible) < 8:
            continue
        score = max((score_title(t, possible) for t in row_titles), default=0.0)
        if score > best[0]:
            best = (score, pdf)
    if best[1] and best[0] >= 0.88:
        return (
            best[1].get("relative_path", ""),
            best[1].get("sha256", ""),
            "mapped",
            f"{best[0]:.2f}",
            "pdf_filename_title_similarity",
        )
    if best[1] and best[0] >= 0.72:
        return (
            best[1].get("relative_path", ""),
            best[1].get("sha256", ""),
            "needs_manual_check",
            f"{best[0]:.2f}",
            "low_confidence_pdf_filename_similarity",
        )
    return "", "", "pdf_missing", "0.00", "no_pdf_match"


def main() -> None:
    rows = read_csv(DB / "literature_database_cleaned.csv")
    pdf_rows = read_csv(DB / "pdf_inventory.csv")
    pdf_by_path = {r.get("relative_path", ""): r for r in pdf_rows}
    ids = [r["paper_id"] for r in rows]
    by_id = {r["paper_id"]: r for r in rows}
    dsu = DSU(ids)
    reasons: dict[tuple[str, str], list[tuple[str, float, bool]]] = defaultdict(list)

    doi_groups: dict[str, list[str]] = defaultdict(list)
    title_groups: dict[str, list[str]] = defaultdict(list)
    sha_groups: dict[str, list[str]] = defaultdict(list)

    for row in rows:
        pid = row["paper_id"]
        doi = norm_doi(row.get("doi", ""))
        if doi:
            doi_groups[doi].append(pid)
        title = norm_title(row.get("title", ""))
        if title and len(title) >= 16 and not is_placeholder(row):
            title_groups[title].append(pid)
        sha = row.get("sha256", "").strip()
        if sha:
            sha_groups[sha].append(pid)

    for group in doi_groups.values():
        if len(group) > 1:
            for pid in group[1:]:
                dsu.union(group[0], pid)
                add_reason(reasons, group[0], pid, "doi_exact", 0.99)

    for group in title_groups.values():
        if len(group) > 1:
            for pid in group[1:]:
                dsu.union(group[0], pid)
                add_reason(reasons, group[0], pid, "normalized_title_exact", 0.96)

    for group in sha_groups.values():
        if len(group) > 1:
            for pid in group[1:]:
                dsu.union(group[0], pid)
                add_reason(reasons, group[0], pid, "record_sha256_exact", 0.99)

    # High-confidence title, translated-title, and PDF filename matching. Low-confidence pairs are reported but not merged.
    for i, a in enumerate(rows):
        if is_placeholder(a):
            continue
        a_titles = title_candidates(a, pdf_by_path)
        if not a_titles:
            continue
        for b in rows[i + 1 :]:
            if is_placeholder(b):
                continue
            b_titles = title_candidates(b, pdf_by_path)
            if not b_titles:
                continue
            scored = [
                (score_title(x[1], y[1]), x[0], y[0])
                for x in a_titles
                for y in b_titles
            ]
            score, a_source, b_source = max(scored, key=lambda item: item[0])
            pdf_based = "pdf_" in a_source or "pdf_" in b_source
            if score >= 0.94:
                dsu.union(a["paper_id"], b["paper_id"])
                reason = "pdf_filename_title_high_similarity" if pdf_based else "normalized_title_high_similarity"
                add_reason(reasons, a["paper_id"], b["paper_id"], reason, score, manual=pdf_based)
            elif pdf_based and score >= 0.88:
                dsu.union(a["paper_id"], b["paper_id"])
                add_reason(reasons, a["paper_id"], b["paper_id"], "pdf_filename_title_probable_match", score, manual=True)
            elif score >= 0.88:
                add_reason(reasons, a["paper_id"], b["paper_id"], "possible_title_similarity_not_merged", score, True)

    groups: dict[str, list[str]] = defaultdict(list)
    for pid in ids:
        groups[dsu.find(pid)].append(pid)

    duplicate_group_ids: dict[str, str] = {}
    dup_index = 1
    for root, members in sorted(groups.items()):
        if len(members) > 1:
            gid = f"DUP{dup_index:04d}"
            dup_index += 1
            for pid in members:
                duplicate_group_ids[pid] = gid

    duplicate_rows: list[dict[str, str]] = []
    metadata_pdf_merges = 0
    for root, members in sorted(groups.items()):
        if len(members) == 1:
            continue
        member_rows = [by_id[m] for m in sorted(members)]
        canonical = sorted(members)[0]
        has_pdf = [m for m in member_rows if m.get("pdf_path")]
        no_pdf = [m for m in member_rows if not m.get("pdf_path")]
        if has_pdf and no_pdf:
            metadata_pdf_merges += len(no_pdf)
        for pid in sorted(members):
            row = by_id[pid]
            pair_reasons = []
            for other in members:
                if other == pid:
                    continue
                pair_reasons.extend(reasons.get(tuple(sorted((pid, other))), []))
            if pid == canonical:
                reason = "canonical_record"
                conf = "1.00"
                manual = False
                keep = "keep"
            elif pair_reasons:
                best = sorted(pair_reasons, key=lambda x: x[1], reverse=True)[0]
                reason = "; ".join(sorted(set(r[0] for r in pair_reasons if not r[0].startswith("possible_")))) or best[0]
                conf = f"{best[1]:.2f}"
                manual = any(r[2] for r in pair_reasons)
                keep = "merge" if float(conf) >= 0.94 and not manual else "needs_manual_confirmation"
            else:
                reason = "same_duplicate_component"
                conf = "0.90"
                manual = True
                keep = "needs_manual_confirmation"
            duplicate_rows.append(
                {
                    "duplicate_group_id": duplicate_group_ids[pid],
                    "canonical_paper_id": canonical,
                    "duplicate_paper_id": pid,
                    "duplicate_title": row.get("title", ""),
                    "duplicate_year": row.get("year", ""),
                    "duplicate_doi": row.get("doi", ""),
                    "duplicate_source": row.get("journal_or_source", "") or row.get("source_collection", ""),
                    "duplicate_reason": reason,
                    "merge_confidence": conf,
                    "keep_or_merge": keep,
                    "notes": "Original record retained in literature_database_cleaned.csv; canonical view only.",
                }
            )

    canonical_rows: list[dict[str, str]] = []
    reader_ids = collect_ids(READERS, "reader")
    card_ids = collect_ids(CARDS, "card")
    mapping_rows: list[dict[str, str]] = []

    for root, members in sorted(groups.items()):
        member_rows = [by_id[m] for m in sorted(members)]
        canonical = sorted(members)[0]
        gid = duplicate_group_ids.get(canonical, "")
        pair_conf = [
            conf
            for (a, b), vals in reasons.items()
            if a in members and b in members
            for _, conf, manual in vals
            if not manual
        ]
        manual_needed = False
        if len(members) > 1:
            manual_needed = any(
                manual for (a, b), vals in reasons.items() if a in members and b in members for _, _, manual in vals
            )
        confidence = max(pair_conf) if pair_conf else (1.00 if len(members) == 1 else 0.90)
        metadata_statuses = "; ".join(sorted(set(r.get("metadata_status", "") for r in member_rows if r.get("metadata_status"))))
        notes = "; ".join([r.get("notes", "") for r in member_rows if r.get("notes")][:3])
        canonical_rows.append(
            {
                "canonical_paper_id": canonical,
                "all_source_paper_ids": "; ".join(sorted(members)),
                "title": choose_title(member_rows),
                "translated_title": choose_value(member_rows, "translated_title"),
                "language": choose_value(member_rows, "language"),
                "year": choose_value(member_rows, "year"),
                "authors": choose_value(member_rows, "authors"),
                "journal_or_source": choose_value(member_rows, "journal_or_source"),
                "doi": choose_value(member_rows, "doi"),
                "url": choose_value(member_rows, "url"),
                "topic_group": merge_multi(member_rows, "topic_group"),
                "method_group": merge_multi(member_rows, "method_group"),
                "relevance_level": choose_value(member_rows, "relevance_level"),
                "metadata_status": metadata_statuses or "partial",
                "source_manifests": merge_multi(member_rows, "source_manifest"),
                "duplicate_group_id": gid,
                "deduplication_confidence": f"{confidence:.2f}",
                "needs_manual_confirmation": "yes" if manual_needed else "no",
                "notes": notes,
            }
        )

    for c in canonical_rows:
        member_ids = c["all_source_paper_ids"].split("; ")
        member_rows = [by_id[m] for m in member_ids if m in by_id]
        pdf_path, sha, status, conf, method = best_pdf_for_group(member_rows, pdf_rows)
        has_reader = any(m in reader_ids for m in member_ids)
        has_card = any(m in card_ids for m in member_ids)
        if has_reader:
            read_status = "full_reader"
        elif has_card:
            read_status = "paper_card_only"
        elif status == "mapped":
            read_status = "unread_pdf_mapped"
        else:
            read_status = "unread_no_pdf"
        high_topic = any(
            token in f"{c['title']} {c['topic_group']} {c['method_group']}".lower()
            for token in ["rocky", "desertification", "fbr", "bare", "lsmm", "sma", "mesma", "deeplab", "u-net", "dem", "gee"]
        )
        suggested = "yes" if status in {"mapped", "needs_manual_check"} and not has_reader and high_topic else "no"
        mapping_rows.append(
            {
                "canonical_paper_id": c["canonical_paper_id"],
                "title": c["title"],
                "year": c["year"],
                "language": c["language"],
                "journal_or_source": c["journal_or_source"],
                "doi": c["doi"],
                "mapped_pdf_path": pdf_path,
                "mapped_pdf_sha256": sha,
                "pdf_mapping_status": status,
                "pdf_mapping_confidence": conf,
                "pdf_match_method": method,
                "has_reader": "yes" if has_reader else "no",
                "has_paper_card": "yes" if has_card else "no",
                "read_status": read_status,
                "suggested_for_batch_03": suggested,
                "notes": "Canonical PDF mapping; original records and PDFs were not modified.",
            }
        )

    write_csv(DB / "literature_duplicate_groups.csv", duplicate_rows, DUP_FIELDS)
    write_csv(DB / "literature_database_canonical.csv", canonical_rows, CANON_FIELDS)
    write_csv(DB / "literature_database_canonical_with_pdf_mapping.csv", mapping_rows, MAP_FIELDS)

    doi_duplicate_record_count = sum(len(v) for v in doi_groups.values() if len(v) > 1)
    title_duplicate_record_count = sum(
        1
        for r in duplicate_rows
        if r["keep_or_merge"] != "keep" and "title" in r["duplicate_reason"]
    )
    pdf_sha_duplicate_count = sum(len(v) for v in defaultdict(list, {}).values())
    pdf_sha_groups: dict[str, list[str]] = defaultdict(list)
    for p in pdf_rows:
        if p.get("sha256"):
            pdf_sha_groups[p["sha256"]].append(p.get("relative_path", ""))
    pdf_sha_duplicate_count = sum(len(v) for v in pdf_sha_groups.values() if len(v) > 1)

    inventory_paths = {p.get("relative_path", "") for p in pdf_rows}
    pre_pdf = sum(
        1
        for r in rows
        if r.get("pdf_path") and (r.get("pdf_path") in inventory_paths or (ROOT / r.get("pdf_path", "")).exists())
    )
    post_pdf = sum(1 for r in mapping_rows if r["pdf_mapping_status"] in {"mapped", "needs_manual_check"})
    high_no_pdf = sum(
        1
        for r in mapping_rows
        if r["pdf_mapping_status"] == "pdf_missing"
        and any(t in f"{r['title']} {r['journal_or_source']}".lower() for t in ["rocky", "desertification", "karst", "bare", "bedrock"])
    )
    manual_groups = sorted({r["duplicate_group_id"] for r in duplicate_rows if r["keep_or_merge"] == "needs_manual_confirmation"})
    batch03_count = sum(1 for r in mapping_rows if r["suggested_for_batch_03"] == "yes")

    report = f"""# Deduplication and PDF Mapping Report

## Summary

- Original literature records: {len(rows)}
- Canonical independent paper records after conservative deduplication: {len(canonical_rows)}
- Duplicate records merged into canonical groups: {len(rows) - len(canonical_rows)}
- DOI duplicate record count: {doi_duplicate_record_count}
- Title duplicate record count: {title_duplicate_record_count}
- PDF SHA256 duplicate file count: {pdf_sha_duplicate_count}
- Metadata-only and PDF-backed record merges: {metadata_pdf_merges}
- Records with PDF mapping before deduplication: {pre_pdf}
- Canonical records with PDF mapping after deduplication: {post_pdf}
- High-relevance canonical records still without PDF: {high_no_pdf}
- Duplicate groups needing manual confirmation: {len(manual_groups)}

## Manual Confirmation Groups

{", ".join(manual_groups) if manual_groups else "None detected by the conservative merge rules."}

## Batch 03 Impact

Use `literature_database_canonical_with_pdf_mapping.csv` rather than the raw 116-record table for future coverage audit and batch_03 decisions. The canonical database suggests {batch03_count} PDF-mapped, not-yet-read canonical records as possible batch_03 candidates. Because this pass is conservative, low-confidence title/translation relationships are not force-merged and should be checked manually before final paper counts are reported.

## Rules Applied

- DOI exact matches were merged first.
- Exact SHA256 matches in literature records were merged.
- Exact and very high normalized title similarity were merged.
- Possible but lower-confidence title similarity was recorded as needing manual confirmation, not force-merged.
- Original records and PDF files were not deleted or modified.
- `literature_database_cleaned.csv` was not overwritten.
"""
    (SYN / "deduplication_and_pdf_mapping_report.md").write_text(report, encoding="utf-8")

    print(f"original_records={len(rows)}")
    print(f"canonical_records={len(canonical_rows)}")
    print(f"merged_duplicate_records={len(rows) - len(canonical_rows)}")
    print(f"doi_duplicate_record_count={doi_duplicate_record_count}")
    print(f"title_duplicate_record_count={title_duplicate_record_count}")
    print(f"pdf_sha_duplicate_file_count={pdf_sha_duplicate_count}")
    print(f"metadata_pdf_merges={metadata_pdf_merges}")
    print(f"pre_pdf_mapping={pre_pdf}")
    print(f"post_pdf_mapping={post_pdf}")
    print(f"high_relevance_without_pdf={high_no_pdf}")
    print(f"manual_duplicate_groups={len(manual_groups)}")
    print(f"batch03_candidates={batch03_count}")


if __name__ == "__main__":
    main()
