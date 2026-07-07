# Batch 02 Remote Sensing Full Reading

This is a task draft for the next Codex run. Do not execute it from this file.

## Objective

Read a small supplementary set of confirmed or strongly indicated Remote Sensing papers to strengthen target-journal writing-style coverage before journal profile analysis.

## Inputs

- `docs/literature/synthesis/need_for_batch_02_remote_sensing_reading.md`
- `docs/literature/synthesis/batch_02_remote_sensing_recommendation.md`
- `database/literature_database_cleaned.csv`
- `database/literature_database_enriched_batch_01.csv`
- local PDFs under `docs/literature/pdfs/remote_sensing_only/` and related duplicate paths

## Recommended Papers

1. KRD0025: Analysis of Landsat-8 OLI Imagery for Estimating Exposed Bedrock Fractions in Typical Karst Regions of Southwest China
2. KRD0046: Extraction of Rocky Desertification Information in the Karst Area Based on the Red-NIR-SWIR Spectral Feature Space
3. KRD0023: Quantitative Estimation of Carbonate Rock Fraction in Karst Regions Based on Spectral Feature Analysis
4. KRD0045: The Changes of Spatiotemporal Pattern of Rocky Desertification and Its Dominant Driving Factors in Typical Karst Mountainous Areas under the Background of Global Change
5. KRD0070: Spatiotemporal Evolution and Driving Factors of Karst Rocky Desertification in Guangxi, China, Under Climate Change and Human Activities
6. KRD0016: Is Forest Restoration in the Southwest China Karst Promoted Mainly by Climate Change or Human-Induced Factors?
7. KRD0044: Spatiotemporal Evolution Analysis and Future Scenario Prediction of Rocky Desertification in a Subtropical Karst Region

## Required Outputs

- `docs/literature/readers/batch_02_remote_sensing/`
- `docs/literature/paper_cards/batch_02_remote_sensing/`
- `docs/literature/synthesis/batch_02_remote_sensing/batch_02_remote_sensing_synthesis.md`
- `docs/literature/synthesis/remote_sensing_journal_style_input_matrix.md`
- updated enriched database without overwriting batch_01 fields

## Constraints

- Follow `AGENTS.md`.
- Do not mix continuous FBR metrics with classification metrics.
- Do not claim GF-7 stereo DEM improves Area 1 to Area 2 transfer.
- Preserve page/section/figure/table anchors.
- Flag metadata uncertainty instead of guessing.