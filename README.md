# KRD Remote Sensing Literature Database

This repository stores and organizes literature assets for karst rocky desertification (KRD) remote sensing research. It is intended to support paper reading, evidence management, method comparison, and preparation of a future `krd-remote-sensing` ChatGPT Skill.

## Research Topic

The project focuses on remote sensing methods for karst rocky desertification monitoring, especially fractional bedrock exposure, LSMM/MESMA, machine learning, semantic segmentation, DEM/topographic enhancement, Google Earth Engine workflows, and cross-region transfer between study areas.

## Repository Structure

- `docs/literature/pdfs/`: PDF collections grouped by source package.
- `docs/literature/manifests/`: CSV, RIS, BibTeX, and related literature manifest files.
- `docs/literature/paper_cards/`: Future structured paper extraction cards.
- `docs/literature/synthesis/`: Markdown notes and synthesis documents.
- `docs/literature/skill_source/`: Future source material for the ChatGPT Skill.
- `database/`: Generated machine-readable inventories.
- `logs/`: Copy and inventory logs.
- `outputs/`: Future derived outputs.
- `scripts/`: Repository maintenance and database scripts.

## PDF Source Collections

- `package_2000_2026`: copied from `D:\7.1\RS\KRD_desertification_literature_package_2000_2026_v2\pdfs_downloaded`.
- `package_2021_2026`: copied from `D:\7.1\RS\KRD_desertification_literature_package_2021_2026\pdfs_downloaded`.
- `remote_sensing_only`: copied from `D:\7.1\RS\RemoteSensing_rocky_desertification_package\pdfs_downloaded`.

## Inventory

Run:

```bash
python scripts/build_pdf_inventory.py
```

The script scans `docs/literature/pdfs/`, calculates SHA256 hashes, detects duplicate PDFs, and writes:

- `database/pdf_inventory.csv`
- `database/pdf_duplicates.csv`
- `logs/pdf_inventory_log.md`

## Copyright Notice

PDF files in this repository are for private research and literature management only. They should not be publicly redistributed unless open access status and redistribution permission have been confirmed.

## Next Goal

The next major goal is to convert this literature database into a structured source base for a `krd-remote-sensing` ChatGPT Skill.
