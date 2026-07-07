# Paper Card: Optimization of Rocky Desertification Classification Model Based on Vegetation Type and Seasonal Characteristic

## 1. Bibliographic Information

- Paper ID: KRD0035
- Title: Optimization of Rocky Desertification Classification Model Based on Vegetation Type and Seasonal Characteristic
- Chinese title if applicable: unknown
- Authors: Qian C.; Qiang H.; Wang F.; Li M.
- Year: 2021
- Journal: core
- DOI: 10.3390/rs13152935
- URL: https://www.mdpi.com/2072-4292/13/15/2935
- PDF path: `docs/literature/pdfs/package_2021_2026/EN02_Optimization_of_Rocky_Desertification_Classification_Model_Based_on_Vegetation_Type_and_Se.pdf`
- Language: English

## 2. Research Objective

Use the full reader and Abstract/Introduction anchors to confirm exact objectives. Current grounded objective signal: Optimization of Rocky Desertification Classification Model Based on Vegetation Type and Seasonal Characteristic

## 3. Study Area

Study area anchors: p.3. Exact place names require manual confirmation from the PDF.

## 4. Data Sources

- Satellite data: located
- DEM/topographic data: located
- Field/UAV/reference data: located
- Temporal coverage: needs manual extraction from data section.
- Spatial resolution: needs manual extraction from data section.

## 5. Target Variable / Classification System

Topic group: machine_learning. Target evidence pages: p.1, p.1, p.2, p.3, p.4, p.4, p.5, p.5.

## 6. Methods

- Preprocessing: located
- Features: located
- Main model: unknown
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
- Metrics: IoU, Kappa, OA, PA, Precision, UA, accuracy, confusion matrix, overall accuracy, slope

## 8. Main Findings

Only include findings explicitly supported by the paper. This automated card does not record numerical findings unless manually verified in the reader/PDF. See result evidence pages: p.1, p.1, p.1, p.1, p.1, p.1, p.1, p.1.

## 9. Limitations

Located limitation/future-work evidence pages: not located. Manual confirmation needed.

## 10. Relevance to Our Manuscript

- Introduction: not applicable
- Methods: high
- Results: high
- Discussion: not applicable
- Figure/table design: high
- Terminology: high
- Remote Sensing style: not applicable

## 11. Reusable Skill Knowledge

### Scientific rules
- Relevant target/method signals: machine_learning; unknown.
- Located target evidence pages: p.1, p.1, p.2, p.3, p.4, p.4.
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
