# Paper Card: A Rocky Desertification Land Extraction Method Based on Spectral Texture Scattering Terrain Feature Set and Multiscale Segmentation

## 1. Bibliographic Information

- Paper ID: KRD0051
- Title: A Rocky Desertification Land Extraction Method Based on Spectral Texture Scattering Terrain Feature Set and Multiscale Segmentation
- Chinese title if applicable: unknown
- Authors: unknown
- Year: 2024
- Journal: IEEE
- DOI: unknown
- URL: https://ieeexplore.ieee.org/document/11023630
- PDF path: `docs/literature/pdfs/package_2000_2026/A_Rocky_Desertification_Land_Extraction_Method_Based_on_Spectral-Texture-Scattering-Terrain_Multisource_Features_With_Time_Series.pdf`
- Language: English

## 2. Research Objective

Use the full reader and Abstract/Introduction anchors to confirm exact objectives. Current grounded objective signal: A Rocky Desertification Land Extraction Method Based on Spectral Texture Scattering Terrain Feature Set and Multiscale Segmentation

## 3. Study Area

Study area anchors: p.3, p.5, p.9, p.14. Exact place names require manual confirmation from the PDF.

## 4. Data Sources

- Satellite data: located
- DEM/topographic data: located
- Field/UAV/reference data: not reported by parser
- Temporal coverage: needs manual extraction from data section.
- Spatial resolution: needs manual extraction from data section.

## 5. Target Variable / Classification System

Topic group: deep_learning_segmentation. Target evidence pages: p.1, p.1, p.1, p.1, p.1, p.1, p.1, p.2.

## 6. Methods

- Preprocessing: located
- Features: located
- Main model: DEM_ablation
- Comparison models: inspect Methods/Results anchors.
- DEM/topographic variables: located
- FBR/LSMM/MESMA: located
- Deep learning / semantic segmentation: located
- Experimental design: inspect training/split/validation evidence in reader.

## 7. Validation Strategy

- Reference data: inspect validation/metric excerpts.
- Sample split: located
- Independent validation: not reported by parser
- Cross-region validation: not reported by parser
- Metrics: F1, IoU, Kappa, OA, PA, Precision, R2, UA, accuracy, bias, confusion matrix, overall accuracy, slope

## 8. Main Findings

Only include findings explicitly supported by the paper. This automated card does not record numerical findings unless manually verified in the reader/PDF. See result evidence pages: p.1, p.1, p.1, p.1, p.1, p.1, p.1, p.1.

## 9. Limitations

Located limitation/future-work evidence pages: p.2, p.11, p.14, p.14, p.15. Manual confirmation needed.

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
- Relevant target/method signals: deep_learning_segmentation; DEM_ablation.
- Located target evidence pages: p.1, p.1, p.1, p.1, p.1, p.1.
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

- DOI missing in database
- DOI needs manual verification
- metadata incomplete
