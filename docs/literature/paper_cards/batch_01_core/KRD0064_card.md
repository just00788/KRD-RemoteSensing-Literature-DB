# Paper Card: Fine-Grained Land Use Remote Sensing Mapping in Karst Mountain Areas Using Very High Resolution Images

## 1. Bibliographic Information

- Paper ID: KRD0064
- Title: Fine-Grained Land Use Remote Sensing Mapping in Karst Mountain Areas Using Very High Resolution Images
- Chinese title if applicable: unknown
- Authors: Remote Sensing authors
- Year: 2025
- Journal: Remote Sensing
- DOI: 10.3390/rs17142368
- URL: https://www.mdpi.com/2072-4292/17/14/2368
- PDF path: `docs/literature/pdfs/package_2021_2026/EN18_Fine-Grained_Land_Use_Remote_Sensing_Mapping_in_Karst_Mountain_Areas_Using_Very_High_Resol.pdf`
- Language: English

## 2. Research Objective

Use the full reader and Abstract/Introduction anchors to confirm exact objectives. Current grounded objective signal: Fine-Grained Land Use Remote Sensing Mapping in Karst Mountain Areas Using Very High Resolution Images

## 3. Study Area

Study area anchors: p.3, p.4, p.6, p.7, p.11, p.12, p.13, p.17. Exact place names require manual confirmation from the PDF.

## 4. Data Sources

- Satellite data: not reported by parser
- DEM/topographic data: located
- Field/UAV/reference data: not reported by parser
- Temporal coverage: needs manual extraction from data section.
- Spatial resolution: needs manual extraction from data section.

## 5. Target Variable / Classification System

Topic group: machine_learning. Target evidence pages: p.3, p.3, p.9, p.11, p.17, p.19, p.19, p.20.

## 6. Methods

- Preprocessing: located
- Features: located
- Main model: unknown
- Comparison models: inspect Methods/Results anchors.
- DEM/topographic variables: located
- FBR/LSMM/MESMA: not applicable or not reported
- Deep learning / semantic segmentation: located
- Experimental design: inspect training/split/validation evidence in reader.

## 7. Validation Strategy

- Reference data: inspect validation/metric excerpts.
- Sample split: located
- Independent validation: not reported by parser
- Cross-region validation: located
- Metrics: F1, IoU, Kappa, OA, PA, Precision, Recall, UA, accuracy, mIoU, overall accuracy, slope

## 8. Main Findings

Only include findings explicitly supported by the paper. This automated card does not record numerical findings unless manually verified in the reader/PDF. See result evidence pages: p.1, p.1, p.2, p.2, p.2, p.2, p.3, p.3.

## 9. Limitations

Located limitation/future-work evidence pages: p.5, p.11, p.18, p.18. Manual confirmation needed.

## 10. Relevance to Our Manuscript

- Introduction: not applicable
- Methods: high
- Results: high
- Discussion: high
- Figure/table design: high
- Terminology: high
- Remote Sensing style: high

## 11. Reusable Skill Knowledge

### Scientific rules
- Relevant target/method signals: machine_learning; unknown.
- Located target evidence pages: p.3, p.3, p.9, p.11, p.17, p.19.
- Located metric evidence pages: p.1, p.1, p.1, p.1, p.1, p.1.

### Writing patterns
- Use source-anchored Introduction gap statements and Methods reproducibility language; inspect the located Introduction/Methods pages before adopting exact wording.
- Pair map/accuracy figures with class-level metric tables when classification is involved.

### Terminology
- Canonical terms to preserve: karst rocky desertification; fractional bedrock/bare-rock fraction when explicitly used; LSMM/SMA/MESMA; OA/Kappa/F1/IoU for classification; R2/RMSE/MAE for continuous inversion.

### Warnings
- Do not treat LSMM continuous FBR output as a classification map.
- Do not compare R2/RMSE directly with OA/Kappa/F1/IoU as if they were the same metric type.
- Use spatially independent validation where possible; flag random patch split as a limitation.
- Separate open-source DEM cross-area use from GF-7 stereo-derived DEM local enhancement claims.


## 12. Manual Review Needed

- none
