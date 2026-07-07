# Paper Card: EN007 KRD MESMA SVM

## 1. Bibliographic Information

- Paper ID: KRD0094
- Title: EN007 KRD MESMA SVM
- Chinese title if applicable: unknown
- Authors: unknown
- Year: unknown
- Journal: unknown
- DOI: unknown
- URL: unknown
- PDF path: `docs/literature/pdfs/package_2000_2026/EN007_KRD_MESMA_SVM.pdf`
- Language: unknown

## 2. Research Objective

Use the full reader and Abstract/Introduction anchors to confirm exact objectives. Current grounded objective signal: EN007 KRD MESMA SVM

## 3. Study Area

Study area anchors: p.1, p.2, p.3, p.5, p.11. Exact place names require manual confirmation from the PDF.

## 4. Data Sources

- Satellite data: located
- DEM/topographic data: located
- Field/UAV/reference data: located
- Temporal coverage: needs manual extraction from data section.
- Spatial resolution: needs manual extraction from data section.

## 5. Target Variable / Classification System

Topic group: lsmm_mesma_sma. Target evidence pages: p.1, p.1, p.1, p.1, p.1, p.2, p.2, p.2.

## 6. Methods

- Preprocessing: not reported
- Features: located
- Main model: MESMA;SMA;SVM
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
- Metrics: IoU, Kappa, OA, PA, R2, UA, accuracy, overall accuracy, slope

## 8. Main Findings

Only include findings explicitly supported by the paper. This automated card does not record numerical findings unless manually verified in the reader/PDF. See result evidence pages: p.1, p.1, p.1, p.1, p.2, p.2, p.2, p.2.

## 9. Limitations

Located limitation/future-work evidence pages: not located. Manual confirmation needed.

## 10. Relevance to Our Manuscript

- Introduction: high
- Methods: high
- Results: high
- Discussion: not applicable
- Figure/table design: high
- Terminology: high
- Remote Sensing style: high

## 11. Reusable Skill Knowledge

### Scientific rules
- Relevant target/method signals: lsmm_mesma_sma; MESMA;SMA;SVM.
- Located target evidence pages: p.1, p.1, p.1, p.1, p.1, p.2.
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

- title is provisional filename-derived candidate; verify manually
- year missing in database
- DOI missing in database
- readability_status=usable_with_caution
- DOI needs manual verification
- metadata incomplete
