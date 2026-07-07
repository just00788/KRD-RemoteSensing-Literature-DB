# Deduplication and PDF Mapping Report

## Summary

- Original literature records: 116
- Canonical independent paper records after conservative deduplication: 111
- Duplicate records merged into canonical groups: 5
- DOI duplicate record count: 0
- Title duplicate record count: 5
- PDF SHA256 duplicate file count: 33
- Metadata-only and PDF-backed record merges: 4
- Records with PDF mapping before deduplication: 39
- Canonical records with PDF mapping after deduplication: 63
- High-relevance canonical records still without PDF: 31
- Duplicate groups needing manual confirmation: 3

## Manual Confirmation Groups

DUP0001, DUP0002, DUP0005

## Batch 03 Impact

Use `literature_database_canonical_with_pdf_mapping.csv` rather than the raw 116-record table for future coverage audit and batch_03 decisions. The canonical database suggests 29 PDF-mapped, not-yet-read canonical records as possible batch_03 candidates. Because this pass is conservative, low-confidence title/translation relationships are not force-merged and should be checked manually before final paper counts are reported.

## Rules Applied

- DOI exact matches were merged first.
- Exact SHA256 matches in literature records were merged.
- Exact and very high normalized title similarity were merged.
- Possible but lower-confidence title similarity was recorded as needing manual confirmation, not force-merged.
- Original records and PDF files were not deleted or modified.
- `literature_database_cleaned.csv` was not overwritten.
