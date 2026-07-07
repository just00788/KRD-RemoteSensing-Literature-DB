# Paper Card: 基于无人机影像与Sentinel-2影像的基岩裸露率反演与石漠化程度评价

## 1. Bibliographic Information

- Paper ID: KRD0062
- Title: 基于无人机影像与Sentinel-2影像的基岩裸露率反演与石漠化程度评价
- Chinese title if applicable: unknown
- Authors: unknown
- Year: 2024
- Journal: 百度学术条目/学位论文
- DOI: unknown
- URL: https://xueshu.baidu.com/usercenter/paper/show?paperid=1g7704h0692f0090v50t08c0nt344512
- PDF path: `docs/literature/pdfs/package_2000_2026/基于无人机影像与Sentinel-2影像的基岩裸露率反演与石漠化程度评价_赵喆.pdf`
- Language: Chinese

## 2. Research Objective

Use the full reader and Abstract/Introduction anchors to confirm exact objectives. Current grounded objective signal: 基于无人机影像与Sentinel-2影像的基岩裸露率反演与石漠化程度评价

## 3. Study Area

Study area anchors: p.6, p.9, p.10, p.12, p.13, p.15, p.16, p.17, p.18, p.19, p.20, p.22, .... Exact place names require manual confirmation from the PDF.

## 4. Data Sources

- Satellite data: located
- DEM/topographic data: located
- Field/UAV/reference data: located
- Temporal coverage: needs manual extraction from data section.
- Spatial resolution: needs manual extraction from data section.

## 5. Target Variable / Classification System

Topic group: bare_rock_fraction_fbr. Target evidence pages: p.1, p.2, p.2, p.2, p.2, p.2, p.2, p.2.

## 6. Methods

- Preprocessing: located
- Features: located
- Main model: DEM_ablation
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
- Metrics: F1, IoU, Kappa, OA, PA, Precision, R2, RMSE, Recall, UA, accuracy, confusion matrix, overall accuracy, slope

## 8. Main Findings

Only include findings explicitly supported by the paper. This automated card does not record numerical findings unless manually verified in the reader/PDF. See result evidence pages: p.1, p.1, p.1, p.1, p.2, p.3, p.3, p.3.

## 9. Limitations

Located limitation/future-work evidence pages: p.7, p.7, p.10, p.12, p.16, p.17, p.31, p.32. Manual confirmation needed.

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
- Relevant target/method signals: bare_rock_fraction_fbr; DEM_ablation.
- Located target evidence pages: p.1, p.2, p.2, p.2, p.2, p.2.
- Located metric evidence pages: p.1, p.2, p.2, p.2, p.4, p.4.

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
