# Paper Card: 基于改进DeepLabV3+的石漠化地区裸岩信息提取

## 1. Bibliographic Information

- Paper ID: KRD0116
- Title: 基于改进DeepLabV3+的石漠化地区裸岩信息提取
- Chinese title if applicable: unknown
- Authors: 吴永俊
- Year: unknown
- Journal: unknown
- DOI: unknown
- URL: unknown
- PDF path: `docs/literature/pdfs/package_2000_2026/基于改进DeepLabV3+的石漠化地区裸岩信息提取_吴永俊.pdf`
- Language: Chinese

## 2. Research Objective

Use the full reader and Abstract/Introduction anchors to confirm exact objectives. Current grounded objective signal: 基于改进DeepLabV3+的石漠化地区裸岩信息提取

## 3. Study Area

Study area anchors: not located. Exact place names require manual confirmation from the PDF.

## 4. Data Sources

- Satellite data: located
- DEM/topographic data: not reported by parser
- Field/UAV/reference data: not reported by parser
- Temporal coverage: needs manual extraction from data section.
- Spatial resolution: needs manual extraction from data section.

## 5. Target Variable / Classification System

Topic group: deep_learning_segmentation. Target evidence pages: p.1, p.1, p.1, p.1, p.1, p.1, p.1, p.1.

## 6. Methods

- Preprocessing: located
- Features: located
- Main model: DeepLabV3+
- Comparison models: inspect Methods/Results anchors.
- DEM/topographic variables: not applicable or not reported
- FBR/LSMM/MESMA: located
- Deep learning / semantic segmentation: located
- Experimental design: inspect training/split/validation evidence in reader.

## 7. Validation Strategy

- Reference data: inspect validation/metric excerpts.
- Sample split: located
- Independent validation: not reported by parser
- Cross-region validation: not reported by parser
- Metrics: F1, IoU, OA, PA, Precision, Recall, UA, accuracy

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
- Relevant target/method signals: deep_learning_segmentation; DeepLabV3+.
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


## 12. Manual Review Needed

- year missing in database
- DOI missing in database
- DOI needs manual verification
- metadata incomplete
