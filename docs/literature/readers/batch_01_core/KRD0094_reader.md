# Full-Paper Reader: EN007 KRD MESMA SVM

## 1. Bibliographic Information

- Paper ID: KRD0094
- Title: EN007 KRD MESMA SVM
- Translated title if applicable: unknown
- Authors: unknown
- Year: unknown
- Journal / Source: unknown
- DOI: unknown
- URL: unknown
- PDF path: `docs/literature/pdfs/package_2000_2026/EN007_KRD_MESMA_SVM.pdf`
- Language: unknown
- Readability status: usable_with_caution
- Metadata status: metadata_incomplete

## 2. Reading Scope and Source Anchors

This reader was generated from the full selectable text layer of the PDF. It preserves page-level anchors and section/figure/table signals. It does not reproduce large original-text passages and does not fabricate missing metadata.

- Abstract: p.1
- Introduction: p.1
- Study Area: p.1, p.2, p.3, p.5, p.11
- Data: p.2, p.3, p.6, p.9, p.11, p.12, p.13
- Methods: p.1, p.2, p.3, p.4, p.5, p.6, p.7, p.8, p.9, p.10, p.11, p.12
- Experiments: p.5, p.11
- Results: p.1, p.2, p.3, p.4, p.5, p.6, p.7, p.8, p.9, p.10, p.11
- Discussion: p.9
- Conclusions: p.3, p.11
- References: p.11
- Figures/Tables captions: 12 located
  - p.2: Table 1. Classification of exposed bedrock rate (EBR) in different KRD studies
  - p.3: Figure 1. The location of research area and distribution
  - p.3: Table 2. Landsat 8 OLI images used in the study
  - p.4: Figure 2. A view from sampling with a 100cm auger to
  - p.5: Figure 3. The views from different environments in study area of KRD in the research area; a) Severe KRD b) Moderate
  - p.6: Table 3. The criteria used in the classification of KRD in this study
  - p.7: Figure 5. The results of methods used to assess KRD: a) Karst Bare Rock Index (KBRI), b) Normalized Difference Rock
  - p.8: Figure 4. The Linear relationships between exposed bedrock rate and methods which used to assess KRD in this study

## 3. Abstract-Level Understanding

Source anchors: p.1, p.2, p.3

基于可抽取的摘要文本，本研究逻辑可按以下方式理解。以下内容只依据摘要和题录可确认的信息，不补造缺失结论。

- 研究背景: 论文主题与 `lsmm_mesma_sma` 相关，关键词信号包括 `MESMA;SMA;SVM`。
- 研究目标: EN007 KRD MESMA SVM
- 数据: 见下方 Data Sources 中从全文定位到的证据信号。
- 方法: 见下方 Method Workflow 中从全文定位到的证据信号。
- 主要结果: 仅在 Results Reading Notes 中记录可定位的结果/指标信号；未在此处编造具体数值。
- 意义: 其价值主要体现在对 KRD/FBR/分类/遥感制图/验证框架的支撑，具体等级见第 13 节。

Abstract evidence snippet:

> Remote sensing Karst Rocky Desertification Spectral Indices Spectral Mixture Analysis Machine Learning Karst Rocky Desertification (KRD) is the reduction of vegetative productivity of this land with the release of bedrock as a result of the full or partial transportation of the fertile soil through natural processes and human activities in karst landscapes. The purpose of this study is to reveal the effectiveness of Remote Sensing methods in monitoring, mapping and evaluating KRD. Landsat 8 OLI images were used to carry out these procedures. In monitoring this process, Karst Bare Rock Index (KBRI), Normalized Difference Rock Index (NDRI), Carbonate Rock Index 2 (CRI2), Normalized Difference Build -Up Index (NDBI), Normalized Diffe rence Vegetation Index (NDVI), Dimidiate Pixel Model (DPM), Multi Endmember Spectral Mixture Analysis (MESMA) and Support Vector Machine (SVM) were used from the spectral indices. In order to determine KRD with spectral indexes, a strong linear relationship was tested between some indices such as DPM (R 2=0,79), KBRI (R 2=0,66), and NDBI (R 2=0,64) and field measurements. In order to evaluate the results obtained, KRD was divided into 4 basic classes such

## 4. Introduction Reading Notes

- Source anchors: p.1
- Background unfolding: extracted introduction pages should be read around the anchors above; the parser located target/method signals listed below.
- Why the problem matters: only infer from located KRD/desertification/remote-sensing problem statements; do not add unsupported claims.
- Remote sensing role: see satellite/data excerpts in Section 5.
- Existing research categories: classification, FBR/LSMM/MESMA, ML, semantic segmentation, DEM/topography when signaled below.
- Existing research insufficiency / gap / objectives / contributions: inspect Introduction anchors manually for exact wording before using in manuscript.
- Borrowable point for our Introduction: build a clear progression from KRD importance -> remote-sensing monitoring -> method/data limitation -> our FBR/classification/DEM/cross-region contribution.

Located target/method evidence:
- p.1: Monitoring and classification of karst rocky desertification with Landsat 8 OLI images using
- p.1: Karst Rocky Desertification
- p.1: Karst Rocky Desertification (KRD) is the reduction of vegetative productivity of this land with
- p.1: the release of bedrock as a result of the full or partial transportation of the fertile soil through
- p.1: process, Karst Bare Rock Index (KBRI), Normalized Difference Rock Index (NDRI), Carbonate
- p.2: bedrock after the soil cover has been removed due to the
- p.2: actually refers to land degradation in karst landscapes in
- p.2: Vegetation cover, exposed bedrock and soil depth
- p.2: Moreover, areas with an Exposed Bedrock Rate
- p.2: Classification of exposed bedrock rate (EBR) in different KRD studies
- p.1: Vegetation Index (NDVI), Dimidiate Pixel Model (DPM), Multi Endmember Spectral Mixture
- p.1: Analysis (MESMA) and Support Vector Machine (SVM) were used from the spectral indices.
- p.1: determined that the SVM method had the highest accuracy (Kappa=0.88).
- p.1: through surface streams [2].


## 5. Study Area and Data Sources

- Study area: locate from Study Area anchors: p.1, p.2, p.3, p.5, p.11
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
- p.1: desertification with Landsat 8 OLI images using spectral indices, multi -endmember
- p.1: Monitoring and classification of karst rocky desertification with Landsat 8 OLI images using
- p.1: 1Süleyman Demirel University, Geography Department, Türkiye
- p.1: Landsat 8 OLI images were used to carry out these procedures.
- p.1: some indices such as DPM (R 2=0,79), KBRI (R 2=0,66), and NDBI (R 2=0,64) and field
- p.2: rocky desertification and field measureme nts (In -Situ
- p.3: Landsat 8 OLI images presented by the United States
- p.3: Landsat 8 satellite was launched by the
- p.3: Landsat 8 OLI images used in the study
- p.3: Forestry with the help of fieldwork from sampling points


## 6. Target Variable or Classification System

- Target variable / object: derived from located evidence only.
- KRD/rocky desertification signal: yes
- FBR/fBR/bare-rock fraction signal: yes
- Semantic segmentation class signal: no
- If FBR/fBR is involved, treat it as a continuous/proportional variable unless the paper explicitly thresholds it into classes.
- If rocky desertification levels are involved, inspect the paper for the exact grade system before reuse.

Target evidence:
- p.1: Monitoring and classification of karst rocky desertification with Landsat 8 OLI images using
- p.1: Karst Rocky Desertification
- p.1: Karst Rocky Desertification (KRD) is the reduction of vegetative productivity of this land with
- p.1: the release of bedrock as a result of the full or partial transportation of the fertile soil through
- p.1: process, Karst Bare Rock Index (KBRI), Normalized Difference Rock Index (NDRI), Carbonate
- p.2: bedrock after the soil cover has been removed due to the
- p.2: actually refers to land degradation in karst landscapes in
- p.2: Vegetation cover, exposed bedrock and soil depth
- p.2: Moreover, areas with an Exposed Bedrock Rate
- p.2: Classification of exposed bedrock rate (EBR) in different KRD studies


## 7. Method Workflow

The workflow below is derived from located method/data signals. Missing items are explicitly marked.
- preprocessing: located
- feature construction: located
- spectral indices: located
- DEM/topographic variables: located
- LSMM/SMA/MESMA/FCLS: located
- machine learning models: located
- deep learning models: not reported
- semantic segmentation architecture: located
- training strategy: located
- sample split: located
- cross-validation: not reported
- cross-region validation: located
- ablation design: not reported
- comparison methods: located

Located method/data evidence:
- p.1: Vegetation Index (NDVI), Dimidiate Pixel Model (DPM), Multi Endmember Spectral Mixture
- p.1: Analysis (MESMA) and Support Vector Machine (SVM) were used from the spectral indices.
- p.1: determined that the SVM method had the highest accuracy (Kappa=0.88).
- p.1: through surface streams [2].
- p.1: are among the different types of surfaces that make up
- p.2: classification of surfaces on which this problem is
- p.2: [13], the regions where the open rock surface
- p.2: hand, the same surfaces were marked as areas with
- p.2: Use/Land Cover Change and Land Surface Temperature
- p.2: the best perf orming indices that gave good results for
- p.2: Forest) were also used to distinguish bare karst surfaces
- p.4: sub-pixel segmentation are in monitoring KRD, the linear
- p.1: desertification with Landsat 8 OLI images using spectral indices, multi -endmember
- p.1: Monitoring and classification of karst rocky desertification with Landsat 8 OLI images using
- p.1: 1Süleyman Demirel University, Geography Department, Türkiye
- p.1: Landsat 8 OLI images were used to carry out these procedures.
- p.1: some indices such as DPM (R 2=0,79), KBRI (R 2=0,66), and NDBI (R 2=0,64) and field
- p.2: rocky desertification and field measureme nts (In -Situ
- p.3: Landsat 8 OLI images presented by the United States
- p.3: Landsat 8 satellite was launched by the
- p.3: Landsat 8 OLI images used in the study
- p.3: Forestry with the help of fieldwork from sampling points


## 8. Validation Strategy and Metrics

- Reference sample source: locate from excerpts below; manual confirmation recommended.
- Sample size: record only if explicitly visible in source excerpts; otherwise unknown.
- Train/test split: see located split/training evidence; otherwise not reported.
- Spatial split: located only if terms such as spatial/block split appear; otherwise not reported.
- Independent validation: located only if explicit evidence appears; otherwise not reported.
- Cross-region validation: located only if explicit evidence appears; otherwise not reported.

- Continuous-variable metrics located: R2, slope
- Classification metrics located: OA, overall accuracy, Kappa, IoU

Metric evidence:
- p.1: https://dergipark.org.tr/en/pub/ijeg
- p.1: 1Süleyman Demirel University, Geography Department, Türkiye
- p.1: 2Mehmet Akif Ersoy University, Department of Turkish and Social Sciences Education , Türkiye
- p.1: the release of bedrock as a result of the full or partial transportation of the fertile soil through
- p.1: reveal the effectiveness of Remote Sensing methods in monitoring, mapping and evaluating
- p.1: In order to evaluate the results obtained, KRD was divided into 4 basic classes
- p.1: determined that the SVM method had the highest accuracy (Kappa=0.88).
- p.1: classification results, which have the highest accuracy in the study area, the rate of areas
- p.1: melting of soluble rocks and passing underground
- p.1: several parts of the world.
- p.2: actually refers to land degradation in karst landscapes in
- p.2: However, there is n o standard approach to the


Important distinction enforced for our manuscript: continuous FBR inversion metrics (R2/RMSE/MAE/bias/slope) must not be mixed with classification metrics (OA/Kappa/Precision/Recall/F1/IoU/mF1/mIoU).

## 9. Figures and Tables

### Located Figure/Table 1
- Source anchor: p.2
- Caption: Table 1. Classification of exposed bedrock rate (EBR) in different KRD studies
- What it shows: inferred only from caption wording; inspect the PDF image before reuse.
- Why it matters: directly relevant to study design/results visualization
- Useful for our manuscript: yes
- Similar figure/table for our paper: consider

### Located Figure/Table 2
- Source anchor: p.3
- Caption: Figure 1. The location of research area and distribution
- What it shows: inferred only from caption wording; inspect the PDF image before reuse.
- Why it matters: potentially relevant; requires manual inspection
- Useful for our manuscript: maybe
- Similar figure/table for our paper: manual review first

### Located Figure/Table 3
- Source anchor: p.3
- Caption: Table 2. Landsat 8 OLI images used in the study
- What it shows: inferred only from caption wording; inspect the PDF image before reuse.
- Why it matters: potentially relevant; requires manual inspection
- Useful for our manuscript: maybe
- Similar figure/table for our paper: manual review first

### Located Figure/Table 4
- Source anchor: p.4
- Caption: Figure 2. A view from sampling with a 100cm auger to
- What it shows: inferred only from caption wording; inspect the PDF image before reuse.
- Why it matters: potentially relevant; requires manual inspection
- Useful for our manuscript: maybe
- Similar figure/table for our paper: manual review first

### Located Figure/Table 5
- Source anchor: p.5
- Caption: Figure 3. The views from different environments in study area of KRD in the research area; a) Severe KRD b) Moderate
- What it shows: inferred only from caption wording; inspect the PDF image before reuse.
- Why it matters: directly relevant to study design/results visualization
- Useful for our manuscript: yes
- Similar figure/table for our paper: consider

### Located Figure/Table 6
- Source anchor: p.6
- Caption: Table 3. The criteria used in the classification of KRD in this study
- What it shows: inferred only from caption wording; inspect the PDF image before reuse.
- Why it matters: directly relevant to study design/results visualization
- Useful for our manuscript: yes
- Similar figure/table for our paper: consider

### Located Figure/Table 7
- Source anchor: p.7
- Caption: Figure 5. The results of methods used to assess KRD: a) Karst Bare Rock Index (KBRI), b) Normalized Difference Rock
- What it shows: inferred only from caption wording; inspect the PDF image before reuse.
- Why it matters: potentially relevant; requires manual inspection
- Useful for our manuscript: maybe
- Similar figure/table for our paper: manual review first

### Located Figure/Table 8
- Source anchor: p.8
- Caption: Figure 4. The Linear relationships between exposed bedrock rate and methods which used to assess KRD in this study
- What it shows: inferred only from caption wording; inspect the PDF image before reuse.
- Why it matters: potentially relevant; requires manual inspection
- Useful for our manuscript: maybe
- Similar figure/table for our paper: manual review first

### Located Figure/Table 9
- Source anchor: p.8
- Caption: Table 4. Kappa coefficient of classification results
- What it shows: inferred only from caption wording; inspect the PDF image before reuse.
- Why it matters: directly relevant to study design/results visualization
- Useful for our manuscript: yes
- Similar figure/table for our paper: consider

### Located Figure/Table 10
- Source anchor: p.8
- Caption: Figure 6. A view of the uninterrupted garrigue
- What it shows: inferred only from caption wording; inspect the PDF image before reuse.
- Why it matters: potentially relevant; requires manual inspection
- Useful for our manuscript: maybe
- Similar figure/table for our paper: manual review first

### Located Figure/Table 11
- Source anchor: p.9
- Caption: Figure 7. Classification ranges which of KRD results created
- What it shows: inferred only from caption wording; inspect the PDF image before reuse.
- Why it matters: directly relevant to study design/results visualization
- Useful for our manuscript: yes
- Similar figure/table for our paper: consider

### Located Figure/Table 12
- Source anchor: p.10
- Caption: Figure 8. The views from areas where previously cultivated but not now used for agriculture due to desertification
- What it shows: inferred only from caption wording; inspect the PDF image before reuse.
- Why it matters: potentially relevant; requires manual inspection
- Useful for our manuscript: maybe
- Similar figure/table for our paper: manual review first


## 10. Results Reading Notes

- Source anchors: p.1, p.2, p.3, p.4, p.5, p.6, p.7, p.8, p.9, p.10, p.11
- Main experimental results: use only values and claims visible in the excerpts/PDF tables.
- Model comparison results: inspect metric/table captions before using exact rankings.
- Data source comparison results: record only where Sentinel/Landsat/GF/DEM evidence is explicit.
- FBR/bare-rock inversion results: separate continuous metrics from class metrics.
- Classification accuracy: report OA/Kappa/Precision/Recall/F1/IoU/mF1/mIoU only if explicitly found.
- DEM/topographic factor contribution: note only when DEM/topographic excerpts are explicit.
- Spatial distribution / uncertainty / significance: inspect maps and captions manually.

Located result/metric evidence:
- p.1: the release of bedrock as a result of the full or partial transportation of the fertile soil through
- p.1: In order to evaluate the results obtained, KRD was divided into 4 basic classes
- p.1: determined that the SVM method had the highest accuracy (Kappa=0.88).
- p.1: classification results, which have the highest accuracy in the study area, the rate of areas
- p.2: destruction of vegetation as a result of natural processes
- p.2: However, there is n o standard approach to the
- p.2: classification approach was used in this study, in which
- p.2: methods is that they give fast results in monitoring KRD
- p.2: the best perf orming indices that gave good results for
- p.2: obtain more effective results on the image in mapping
- p.1: https://dergipark.org.tr/en/pub/ijeg
- p.1: 1Süleyman Demirel University, Geography Department, Türkiye
- p.1: 2Mehmet Akif Ersoy University, Department of Turkish and Social Sciences Education , Türkiye
- p.1: the release of bedrock as a result of the full or partial transportation of the fertile soil through
- p.1: reveal the effectiveness of Remote Sensing methods in monitoring, mapping and evaluating
- p.1: In order to evaluate the results obtained, KRD was divided into 4 basic classes


## 11. Discussion Reading Notes

- Source anchors: p.9
- Mechanism explanations, data-source performance, terrain effects, comparison to previous studies, limitations, and future work should be extracted from these anchors only.
- Borrowable Discussion writing pattern: explain why a data/model/factor improves mapping, then tie the explanation to spatial patterns and validation evidence.

Located discussion/limitation evidence:
- not located


## 12. Conclusion Reading Notes

- Source anchors: p.3, p.11
- Objective summary: inspect Conclusion anchors.
- Method summary: inspect Conclusion anchors.
- Main results: record only exact values visible in Conclusion/Results.
- Contributions/application value: inspect Conclusion anchors.
- Limitations/future work: see limitation evidence above.

## 13. Relevance to Our Remote Sensing Manuscript

- Introduction support: medium. Reason: grounded signals were located in the text layer.
- FBR/LSMM support: medium. Reason: grounded signals were located in the text layer.
- ML baseline support: medium. Reason: grounded signals were located in the text layer.
- semantic segmentation support: not applicable. Reason: grounded signals were not located in the text layer.
- DEM/topography support: medium. Reason: grounded signals were located in the text layer.
- GF/Sentinel/Landsat data comparison support: medium. Reason: grounded signals were located in the text layer.
- cross-region transfer support: medium. Reason: grounded signals were located in the text layer.
- accuracy assessment support: medium. Reason: grounded signals were located in the text layer.
- Discussion comparison support: not applicable. Reason: grounded signals were not located in the text layer.
- limitations support: not applicable. Reason: grounded signals were not located in the text layer.
- figure/table design support: medium. Reason: grounded signals were located in the text layer.
- terminology support: medium. Reason: grounded signals were located in the text layer.
- Remote Sensing writing style support: medium. Reason: grounded signals were located in the text layer.

## 14. Reusable Knowledge for Future Skill

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


## 15. Items Needing Manual Review

- title is provisional filename-derived candidate; verify manually
- year missing in database
- DOI missing in database
- readability_status=usable_with_caution
- DOI needs manual verification
- metadata incomplete
