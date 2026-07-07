# Full-Paper Reader: Dynamic monitoring of rocky desertification utilizing a novel model based on Sentinel-2 images and KNDVI

## 1. Bibliographic Information

- Paper ID: KRD0054
- Title: Dynamic monitoring of rocky desertification utilizing a novel model based on Sentinel-2 images and KNDVI
- Translated title if applicable: unknown
- Authors: Taylor & Francis / DOAJ listing
- Year: 2024
- Journal / Source: Geocarto International or related
- DOI: 10.1080/19475705.2024.2399659
- URL: https://doaj.org/article/78f3c665c35e4a309cb200d18f8ad001
- PDF path: `docs/literature/pdfs/package_2000_2026/Dynamic monitoring of rocky desertification utilizing a novel model based on Sentinel-2 images and KNDVI.pdf`
- Language: English
- Readability status: ready
- Metadata status: complete

## 2. Reading Scope and Source Anchors

This reader was generated from the full selectable text layer of the PDF. It preserves page-level anchors and section/figure/table signals. It does not reproduce large original-text passages and does not fabricate missing metadata.

- Abstract: p.2
- Introduction: p.2
- Study Area: p.2, p.5, p.6, p.14, p.17
- Data: p.1, p.4, p.5, p.6, p.7, p.12, p.17, p.18
- Methods: p.1, p.2, p.3, p.4, p.5, p.6, p.8, p.9, p.10, p.11, p.12, p.13, ...
- Experiments: p.2
- Results: p.2, p.3, p.4, p.11, p.12, p.15, p.16, p.17, p.18
- Discussion: p.15
- Conclusions: p.16
- References: p.17
- Figures/Tables captions: 16 located
  - p.5: Figure 1. Location of the study area.
  - p.6: Table 1. Band information of Sentinel-2 images.
  - p.7: Figure 2. Principle of feature space.
  - p.8: Table 2. Formulas of typical surface parameter.
  - p.9: Figure 3. Point-point model feature space (a) EVI-BLI; (b) KNDVI-BLI; (c) NDVI-BLI; (d) MSAVI-BLI.
  - p.10: Figure 4. Spatial distribution of different levesl of rocky desertification. (a) No rocky desertification;
  - p.10: Figure 5. Establishment of rocky desertification monitoring model.
  - p.11: Table 3. The classification standard of monitoring index.

## 3. Abstract-Level Understanding

Source anchors: p.1, p.2, p.3

基于可抽取的摘要文本，本研究逻辑可按以下方式理解。以下内容只依据摘要和题录可确认的信息，不补造缺失结论。

- 研究背景: 论文主题与 `rocky_desertification_classification` 相关，关键词信号包括 `feature_space;vegetation_index`。
- 研究目标: Dynamic monitoring of rocky desertification utilizing a novel model based on Sentinel-2 images and KNDVI
- 数据: 见下方 Data Sources 中从全文定位到的证据信号。
- 方法: 见下方 Method Workflow 中从全文定位到的证据信号。
- 主要结果: 仅在 Results Reading Notes 中记录可定位的结果/指标信号；未在此处编造具体数值。
- 意义: 其价值主要体现在对 KRD/FBR/分类/遥感制图/验证框架的支撑，具体等级见第 13 节。

Abstract evidence snippet:

> As a new vegetation index, kernel normalized difference vegeta - tion index (KNDVI) has great advantages in monitoring regional land degradation and vegetation status. However, the research on the spatial monitoring of rocky desertification based on KNDVI and feature space model has not been reported. In this study, the KNDVI, MSAVI, NDVI, EVI and BLI were introduced to establish four feature space monitoring index. After accuracy validation and comparisons, the optimal rocky desertification monitoring model was proposed and the spatio-temporal changes of rocky desertifi - cation had been analyzed. The time scale of this study was from 2018 to 2022, and the study area was about 3412 km 2 . The results showed that: (1) The rocky desertification monitoring model of KNDVI-BLI had the highest accuracy with R 2 ¼0.909 and RMSE of 0.392. (2) The rocky desertification in the western, northern and southeastern parts of Qixingguan District was more severe than other parts. (3) During 2018–2022, the rocky desertification showed an exacerbating trend in Qixingguan District. The area of extremely severe rocky desertification increased by 8.24 km 2 , while that of severe rocky desertification i

## 4. Introduction Reading Notes

- Source anchors: p.2
- Background unfolding: extracted introduction pages should be read around the anchors above; the parser located target/method signals listed below.
- Why the problem matters: only infer from located KRD/desertification/remote-sensing problem statements; do not add unsupported claims.
- Remote sensing role: see satellite/data excerpts in Section 5.
- Existing research categories: classification, FBR/LSMM/MESMA, ML, semantic segmentation, DEM/topography when signaled below.
- Existing research insufficiency / gap / objectives / contributions: inspect Introduction anchors manually for exact wording before using in manuscript.
- Borrowable point for our Introduction: build a clear progression from KRD importance -> remote-sensing monitoring -> method/data limitation -> our FBR/classification/DEM/cross-region contribution.

Located target/method evidence:
- p.2: Dynamic monitoring of rocky desertification utilizing a
- p.2: land degradation and vegetation status.
- p.2: the spatial monitoring of rocky desertification based on KNDVI
- p.2: comparisons, the optimal rocky desertification monitoring model
- p.2: showed that: (1) The rocky desertification monitoring model of
- p.2: (2) The rocky desertification in the western, northern and
- p.2: (3) During 2018–2022, the rocky desertification
- p.2: extremely severe rocky desertification increased by 8.24 km
- p.2: that of severe rocky desertification increased by 20.46 km
- p.2: method for the control of rocky desertification.
- p.1: desertiﬁcation utilizing a novel model based on Sentinel-2 images and KNDVI, Geomatics,
- p.2: novel model based on Sentinel-2 images and KNDVI
- p.2: As a new vegetation index, kernel normalized difference vegeta -
- p.2: tion index (KNDVI) has great advantages in monitoring regional


## 5. Study Area and Data Sources

- Study area: locate from Study Area anchors: p.2, p.5, p.6, p.14, p.17
- Geographic/environmental background: extract from Study Area anchors; manual confirmation needed for exact place names and environmental facts.
- Satellite data: see evidence below.
- DEM/topographic data: see evidence below.
- Field data: see evidence below if `field/sample/reference` appears.
- UAV data: see evidence below if `UAV` appears.
- Reference data: see validation evidence in Section 8.
- Temporal coverage: record only when explicitly visible in evidence excerpts.
- Spatial resolution: record only when explicitly visible in evidence excerpts.
- Preprocessing steps: see Method Workflow.

Data evidence:
- p.1: utilizing a novel model based on Sentinel-2
- p.1: desertiﬁcation utilizing a novel model based on Sentinel-2 images and KNDVI, Geomatics,
- p.2: novel model based on Sentinel-2 images and KNDVI
- p.2: Research Station, Northwest Institute of Eco-Environment and Resources, Chinese Academy of
- p.2: and Rural Affairs/Institute of Agricultural Resources and Regional Planning, Chinese Academy of
- p.2: southeastern parts of Qixingguan District was more severe than
- p.2: disasters that endanger human safety and affect ecology.
- p.2: These changes do not impact the academic content of the article.
- p.3: terrain or wind, and in this area, the perennial precipitation is more concentrated,
- p.3: and the terrain is more complicated, resulting in more loss of water and soil, making


## 6. Target Variable or Classification System

- Target variable / object: derived from located evidence only.
- KRD/rocky desertification signal: yes
- FBR/fBR/bare-rock fraction signal: yes
- Semantic segmentation class signal: no
- If FBR/fBR is involved, treat it as a continuous/proportional variable unless the paper explicitly thresholds it into classes.
- If rocky desertification levels are involved, inspect the paper for the exact grade system before reuse.

Target evidence:
- p.2: Dynamic monitoring of rocky desertification utilizing a
- p.2: land degradation and vegetation status.
- p.2: the spatial monitoring of rocky desertification based on KNDVI
- p.2: comparisons, the optimal rocky desertification monitoring model
- p.2: showed that: (1) The rocky desertification monitoring model of
- p.2: (2) The rocky desertification in the western, northern and
- p.2: (3) During 2018–2022, the rocky desertification
- p.2: extremely severe rocky desertification increased by 8.24 km
- p.2: that of severe rocky desertification increased by 20.46 km
- p.2: method for the control of rocky desertification.


## 7. Method Workflow

The workflow below is derived from located method/data signals. Missing items are explicitly marked.
- preprocessing: located
- feature construction: located
- spectral indices: located
- DEM/topographic variables: located
- LSMM/SMA/MESMA/FCLS: located
- machine learning models: located
- deep learning models: not reported
- semantic segmentation architecture: not reported
- training strategy: located
- sample split: located
- cross-validation: not reported
- cross-region validation: located
- ablation design: not reported
- comparison methods: located

Located method/data evidence:
- p.1: desertiﬁcation utilizing a novel model based on Sentinel-2 images and KNDVI, Geomatics,
- p.2: novel model based on Sentinel-2 images and KNDVI
- p.2: As a new vegetation index, kernel normalized difference vegeta -
- p.2: tion index (KNDVI) has great advantages in monitoring regional
- p.2: the spatial monitoring of rocky desertification based on KNDVI
- p.2: and feature space model has not been reported.
- p.2: KNDVI, MSAVI, NDVI, EVI and BLI were introduced to establish
- p.2: four feature space monitoring index.
- p.2: KNDVI-BLI had the highest accuracy with R
- p.3: cation based on typical surface parameters.
- p.4: Analysis (VCA) and Fully Constrained Least Squares (FCLS).
- p.4: and found that the typical surface parameter KRDI (Karst Rocky Desertification
- p.1: utilizing a novel model based on Sentinel-2
- p.1: desertiﬁcation utilizing a novel model based on Sentinel-2 images and KNDVI, Geomatics,
- p.2: novel model based on Sentinel-2 images and KNDVI
- p.2: Research Station, Northwest Institute of Eco-Environment and Resources, Chinese Academy of
- p.2: and Rural Affairs/Institute of Agricultural Resources and Regional Planning, Chinese Academy of
- p.2: southeastern parts of Qixingguan District was more severe than
- p.2: disasters that endanger human safety and affect ecology.
- p.2: These changes do not impact the academic content of the article.
- p.3: terrain or wind, and in this area, the perennial precipitation is more concentrated,
- p.3: and the terrain is more complicated, resulting in more loss of water and soil, making


## 8. Validation Strategy and Metrics

- Reference sample source: locate from excerpts below; manual confirmation recommended.
- Sample size: record only if explicitly visible in source excerpts; otherwise unknown.
- Train/test split: see located split/training evidence; otherwise not reported.
- Spatial split: located only if terms such as spatial/block split appear; otherwise not reported.
- Independent validation: located only if explicit evidence appears; otherwise not reported.
- Cross-region validation: located only if explicit evidence appears; otherwise not reported.

- Continuous-variable metrics located: R2, RMSE, slope
- Classification metrics located: OA, Precision, IoU

Metric evidence:
- p.1: ISSN: 1947-5705 (Print) 1947-5713 (Online) Journal homepage: www.tandfonline.com/journals/tgnh20
- p.2: the spatial monitoring of rocky desertification based on KNDVI
- p.2: and feature space model has not been reported.
- p.2: four feature space monitoring index.
- p.2: After accuracy validation and
- p.2: comparisons, the optimal rocky desertification monitoring model
- p.2: was proposed and the spatio-temporal changes of rocky desertifi -
- p.2: KNDVI-BLI had the highest accuracy with R
- p.2: southeastern parts of Qixingguan District was more severe than
- p.2: showed an exacerbating trend in Qixingguan District.
- p.2: These changes do not impact the academic content of the article.
- p.3: serious, which threatens the ecological environment security and the sustainable


Important distinction enforced for our manuscript: continuous FBR inversion metrics (R2/RMSE/MAE/bias/slope) must not be mixed with classification metrics (OA/Kappa/Precision/Recall/F1/IoU/mF1/mIoU).

## 9. Figures and Tables

### Located Figure/Table 1
- Source anchor: p.5
- Caption: Figure 1. Location of the study area.
- What it shows: inferred only from caption wording; inspect the PDF image before reuse.
- Why it matters: directly relevant to study design/results visualization
- Useful for our manuscript: yes
- Similar figure/table for our paper: consider

### Located Figure/Table 2
- Source anchor: p.6
- Caption: Table 1. Band information of Sentinel-2 images.
- What it shows: inferred only from caption wording; inspect the PDF image before reuse.
- Why it matters: potentially relevant; requires manual inspection
- Useful for our manuscript: maybe
- Similar figure/table for our paper: manual review first

### Located Figure/Table 3
- Source anchor: p.7
- Caption: Figure 2. Principle of feature space.
- What it shows: inferred only from caption wording; inspect the PDF image before reuse.
- Why it matters: directly relevant to study design/results visualization
- Useful for our manuscript: yes
- Similar figure/table for our paper: consider

### Located Figure/Table 4
- Source anchor: p.8
- Caption: Table 2. Formulas of typical surface parameter.
- What it shows: inferred only from caption wording; inspect the PDF image before reuse.
- Why it matters: potentially relevant; requires manual inspection
- Useful for our manuscript: maybe
- Similar figure/table for our paper: manual review first

### Located Figure/Table 5
- Source anchor: p.9
- Caption: Figure 3. Point-point model feature space (a) EVI-BLI; (b) KNDVI-BLI; (c) NDVI-BLI; (d) MSAVI-BLI.
- What it shows: inferred only from caption wording; inspect the PDF image before reuse.
- Why it matters: directly relevant to study design/results visualization
- Useful for our manuscript: yes
- Similar figure/table for our paper: consider

### Located Figure/Table 6
- Source anchor: p.10
- Caption: Figure 4. Spatial distribution of different levesl of rocky desertification. (a) No rocky desertification;
- What it shows: inferred only from caption wording; inspect the PDF image before reuse.
- Why it matters: potentially relevant; requires manual inspection
- Useful for our manuscript: maybe
- Similar figure/table for our paper: manual review first

### Located Figure/Table 7
- Source anchor: p.10
- Caption: Figure 5. Establishment of rocky desertification monitoring model.
- What it shows: inferred only from caption wording; inspect the PDF image before reuse.
- Why it matters: potentially relevant; requires manual inspection
- Useful for our manuscript: maybe
- Similar figure/table for our paper: manual review first

### Located Figure/Table 8
- Source anchor: p.11
- Caption: Table 3. The classification standard of monitoring index.
- What it shows: inferred only from caption wording; inspect the PDF image before reuse.
- Why it matters: directly relevant to study design/results visualization
- Useful for our manuscript: yes
- Similar figure/table for our paper: consider

### Located Figure/Table 9
- Source anchor: p.11
- Caption: Figure 6. Spatial distribution of rocky desertification (a) EVI-BLI; (b) MSAVI-BLI; (c) NDVI-BLI; (d)
- What it shows: inferred only from caption wording; inspect the PDF image before reuse.
- Why it matters: potentially relevant; requires manual inspection
- Useful for our manuscript: maybe
- Similar figure/table for our paper: manual review first

### Located Figure/Table 10
- Source anchor: p.12
- Caption: Figure 7. Accuracy validation of different rocky desertification grades in google earth. (a) No rocky
- What it shows: inferred only from caption wording; inspect the PDF image before reuse.
- Why it matters: directly relevant to study design/results visualization
- Useful for our manuscript: yes
- Similar figure/table for our paper: consider

### Located Figure/Table 11
- Source anchor: p.12
- Caption: Table 4. Accuracy verification results of different monitoring models.
- What it shows: inferred only from caption wording; inspect the PDF image before reuse.
- Why it matters: directly relevant to study design/results visualization
- Useful for our manuscript: yes
- Similar figure/table for our paper: consider

### Located Figure/Table 12
- Source anchor: p.13
- Caption: Figure 9 showed that during 2018–2022, the rocky desertification also showed an
- What it shows: inferred only from caption wording; inspect the PDF image before reuse.
- Why it matters: potentially relevant; requires manual inspection
- Useful for our manuscript: maybe
- Similar figure/table for our paper: manual review first

### Located Figure/Table 13
- Source anchor: p.13
- Caption: Figure 8. Spatial distribution of KNDVI-BLI optimal rocky desertification monitoring model. (a)
- What it shows: inferred only from caption wording; inspect the PDF image before reuse.
- Why it matters: potentially relevant; requires manual inspection
- Useful for our manuscript: maybe
- Similar figure/table for our paper: manual review first

### Located Figure/Table 14
- Source anchor: p.13
- Caption: Table 5. Area comparisons of different levels of rocky desertification in
- What it shows: inferred only from caption wording; inspect the PDF image before reuse.
- Why it matters: potentially relevant; requires manual inspection
- Useful for our manuscript: maybe
- Similar figure/table for our paper: manual review first

### Located Figure/Table 15
- Source anchor: p.14
- Caption: Figure 9. Transfer of rocky desertification at different levels from 2018 to 2022 (km
- What it shows: inferred only from caption wording; inspect the PDF image before reuse.
- Why it matters: potentially relevant; requires manual inspection
- Useful for our manuscript: maybe
- Similar figure/table for our paper: manual review first

### Located Figure/Table 16
- Source anchor: p.14
- Caption: Figure 10. Change trend of rocky desertification during 2018–2022.
- What it shows: inferred only from caption wording; inspect the PDF image before reuse.
- Why it matters: potentially relevant; requires manual inspection
- Useful for our manuscript: maybe
- Similar figure/table for our paper: manual review first


## 10. Results Reading Notes

- Source anchors: p.2, p.3, p.4, p.11, p.12, p.15, p.16, p.17, p.18
- Main experimental results: use only values and claims visible in the excerpts/PDF tables.
- Model comparison results: inspect metric/table captions before using exact rankings.
- Data source comparison results: record only where Sentinel/Landsat/GF/DEM evidence is explicit.
- FBR/bare-rock inversion results: separate continuous metrics from class metrics.
- Classification accuracy: report OA/Kappa/Precision/Recall/F1/IoU/mF1/mIoU only if explicitly found.
- DEM/topographic factor contribution: note only when DEM/topographic excerpts are explicit.
- Spatial distribution / uncertainty / significance: inspect maps and captions manually.

Located result/metric evidence:
- p.1: After accuracy validation and
- p.1: KNDVI-BLI had the highest accuracy with R
- p.1: research results could provide a scientific and effective monitoring
- p.2: encountering rain and windy weather, it is easy to cause the wind of the rock, result -
- p.2: and the terrain is more complicated, resulting in more loss of water and soil, making
- p.2: results showed that the soil structure and vegetation restoration ability of cultivated
- p.3: continuity, improve research accuracy, and have great advantages in monitoring
- p.4: Accuracy verification of monitoring model
- p.4: The inversion results of the monitoring model were
- p.5: the inversion accuracy of KNDVI-BLI monitoring model was the highest with
- p.1: ISSN: 1947-5705 (Print) 1947-5713 (Online) Journal homepage: www.tandfonline.com/journals/tgnh20
- p.2: the spatial monitoring of rocky desertification based on KNDVI
- p.2: and feature space model has not been reported.
- p.2: four feature space monitoring index.
- p.2: After accuracy validation and
- p.2: comparisons, the optimal rocky desertification monitoring model


## 11. Discussion Reading Notes

- Source anchors: p.15
- Mechanism explanations, data-source performance, terrain effects, comparison to previous studies, limitations, and future work should be extracted from these anchors only.
- Borrowable Discussion writing pattern: explain why a data/model/factor improves mapping, then tie the explanation to spatial patterns and validation evidence.

Located discussion/limitation evidence:
- p.1: used in monitoring of land degradation, and it also has obvious limitations.
- p.1: As a new vegetation index, KNDVI could solve this limitation well.
- p.15: used in monitoring of land degradation, and it also has obvious limitations.
- p.15: As a new vegetation index, KNDVI could solve this limitation well.


## 12. Conclusion Reading Notes

- Source anchors: p.16
- Objective summary: inspect Conclusion anchors.
- Method summary: inspect Conclusion anchors.
- Main results: record only exact values visible in Conclusion/Results.
- Contributions/application value: inspect Conclusion anchors.
- Limitations/future work: see limitation evidence above.

## 13. Relevance to Our Remote Sensing Manuscript

- Introduction support: high. Reason: grounded signals were located in the text layer.
- FBR/LSMM support: high. Reason: grounded signals were located in the text layer.
- ML baseline support: high. Reason: grounded signals were located in the text layer.
- semantic segmentation support: not applicable. Reason: grounded signals were not located in the text layer.
- DEM/topography support: high. Reason: grounded signals were located in the text layer.
- GF/Sentinel/Landsat data comparison support: high. Reason: grounded signals were located in the text layer.
- cross-region transfer support: high. Reason: grounded signals were located in the text layer.
- accuracy assessment support: high. Reason: grounded signals were located in the text layer.
- Discussion comparison support: high. Reason: grounded signals were located in the text layer.
- limitations support: high. Reason: grounded signals were located in the text layer.
- figure/table design support: high. Reason: grounded signals were located in the text layer.
- terminology support: high. Reason: grounded signals were located in the text layer.
- Remote Sensing writing style support: high. Reason: grounded signals were located in the text layer.

## 14. Reusable Knowledge for Future Skill

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


## 15. Items Needing Manual Review

- none
