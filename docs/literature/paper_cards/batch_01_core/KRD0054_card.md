# Paper Card: Dynamic monitoring of rocky desertification utilizing a novel model based on Sentinel-2 images and KNDVI

## 1. Bibliographic Information

- Paper ID: KRD0054
- Title: Dynamic monitoring of rocky desertification utilizing a novel model based on Sentinel-2 images and KNDVI
- Chinese title if applicable: unknown
- Authors: Taylor & Francis / DOAJ listing
- Year: 2024
- Journal: Geocarto International or related
- DOI: 10.1080/19475705.2024.2399659
- URL: https://doaj.org/article/78f3c665c35e4a309cb200d18f8ad001
- PDF path: `docs/literature/pdfs/package_2000_2026/Dynamic monitoring of rocky desertification utilizing a novel model based on Sentinel-2 images and KNDVI.pdf`
- Language: English

## 2. Research Objective

Use the full reader and Abstract/Introduction anchors to confirm exact objectives. Current grounded objective signal: Dynamic monitoring of rocky desertification utilizing a novel model based on Sentinel-2 images and KNDVI

## 3. Study Area

Study area anchors: p.2, p.5, p.6, p.14, p.17. Exact place names require manual confirmation from the PDF.

## 4. Data Sources

- Satellite data: located
- DEM/topographic data: located
- Field/UAV/reference data: not reported by parser
- Temporal coverage: needs manual extraction from data section.
- Spatial resolution: needs manual extraction from data section.

## 5. Target Variable / Classification System

Topic group: rocky_desertification_classification. Target evidence pages: p.2, p.2, p.2, p.2, p.2, p.2, p.2, p.2.

## 6. Methods

- Preprocessing: located
- Features: located
- Main model: feature_space;vegetation_index
- Comparison models: inspect Methods/Results anchors.
- DEM/topographic variables: located
- FBR/LSMM/MESMA: located
- Deep learning / semantic segmentation: not applicable or not reported
- Experimental design: inspect training/split/validation evidence in reader.

## 7. Validation Strategy

- Reference data: inspect validation/metric excerpts.
- Sample split: located
- Independent validation: not reported by parser
- Cross-region validation: located
- Metrics: IoU, OA, PA, Precision, R2, RMSE, UA, accuracy, slope

## 8. Main Findings

Only include findings explicitly supported by the paper. This automated card does not record numerical findings unless manually verified in the reader/PDF. See result evidence pages: p.1, p.1, p.1, p.2, p.2, p.2, p.3, p.4.

## 9. Limitations

Located limitation/future-work evidence pages: p.15, p.15. Manual confirmation needed.

## 10. Relevance to Our Manuscript

- Introduction: high
- Methods: high
- Results: high
- Discussion: high
- Figure/table design: high
- Terminology: high
- Remote Sensing style: high

## 11. Reusable Skill Knowledge

### Scientific rules
- Relevant target/method signals: rocky_desertification_classification; feature_space;vegetation_index.
- Located target evidence pages: p.2, p.2, p.2, p.2, p.2, p.2.
- Located metric evidence pages: p.1, p.2, p.2, p.2, p.2, p.2.

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
