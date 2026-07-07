# Full-Paper Reader: Fine-Grained Land Use Remote Sensing Mapping in Karst Mountain Areas Using Very High Resolution Images

## 1. Bibliographic Information

- Paper ID: KRD0064
- Title: Fine-Grained Land Use Remote Sensing Mapping in Karst Mountain Areas Using Very High Resolution Images
- Translated title if applicable: unknown
- Authors: Remote Sensing authors
- Year: 2025
- Journal / Source: Remote Sensing
- DOI: 10.3390/rs17142368
- URL: https://www.mdpi.com/2072-4292/17/14/2368
- PDF path: `docs/literature/pdfs/package_2021_2026/EN18_Fine-Grained_Land_Use_Remote_Sensing_Mapping_in_Karst_Mountain_Areas_Using_Very_High_Resol.pdf`
- Language: English
- Readability status: ready
- Metadata status: complete

## 2. Reading Scope and Source Anchors

This reader was generated from the full selectable text layer of the PDF. It preserves page-level anchors and section/figure/table signals. It does not reproduce large original-text passages and does not fabricate missing metadata.

- Abstract: p.1
- Introduction: p.1, p.2
- Study Area: p.3, p.4, p.6, p.7, p.11, p.12, p.13, p.17
- Data: p.1, p.2, p.3, p.4, p.5, p.7, p.8, p.10, p.11, p.16, p.18, p.19, ...
- Methods: p.1, p.2, p.3, p.4, p.5, p.7, p.9, p.10, p.11, p.12, p.14, p.15, ...
- Experiments: p.1, p.4, p.5, p.7, p.10, p.11, p.17, p.18, p.20
- Results: p.1, p.2, p.3, p.4, p.5, p.7, p.10, p.11, p.12, p.13, p.14, p.15, ...
- Discussion: not located
- Conclusions: p.17
- References: p.19
- Figures/Tables captions: 13 located
  - p.4: Figure 1. The location and digital elevation model (DEM) of the study area: (a) Location of Guizhou
  - p.6: Figure 2. The process of land use mapping in karst mountain areas guided by geographical zoning
  - p.7: Figure 3. Geographical zoning results: (a) natural zoning; (b) functional zoning.
  - p.8: Table 1. Description of stratified objects extraction for land use mapping.
  - p.9: Table 1. Cont.
  - p.10: Figure 4. Architecture of the HBGNet (Ref. [11]).
  - p.11: Table 2). Among them, water achieves the highest recognition performance, primarily due
  - p.12: Table 2. Accuracy of the extracted land use objects.

## 3. Abstract-Level Understanding

Source anchors: p.1, p.2, p.3

基于可抽取的摘要文本，本研究逻辑可按以下方式理解。以下内容只依据摘要和题录可确认的信息，不补造缺失结论。

- 研究背景: 论文主题与 `machine_learning` 相关，关键词信号包括 `unknown`。
- 研究目标: Fine-Grained Land Use Remote Sensing Mapping in Karst Mountain Areas Using Very High Resolution Images
- 数据: 见下方 Data Sources 中从全文定位到的证据信号。
- 方法: 见下方 Method Workflow 中从全文定位到的证据信号。
- 主要结果: 仅在 Results Reading Notes 中记录可定位的结果/指标信号；未在此处编造具体数值。
- 意义: 其价值主要体现在对 KRD/FBR/分类/遥感制图/验证框架的支撑，具体等级见第 13 节。

Abstract evidence snippet:

> Karst mountain areas, as complex geological systems formed by carbonate rock development, possess unique three-dimensional spatial structures and hydrogeological processes that fundamentally influence regional ecosystem evolution, land resource assessment, and sustainable development strategy formulation. In recent years, through the implementation of systematic ecological restoration projects, the ecological degradation of karst mountain areas in Southwest China has been significantly curbed. However, the research on the fine-grained land use mapping and quantitative characterization of spatial heterogeneity in karst mountain areas is still insufficient. This knowledge gap impedes scientific decisionmaking and precise policy formulation for regional ecological environment management. Hence, this paper proposes a novel methodology for land use mapping in karst mountain areas using very high resolution (VHR) remote sensing (RS) images. The innovation of this method lies in the

## 4. Introduction Reading Notes

- Source anchors: p.1, p.2
- Background unfolding: extracted introduction pages should be read around the anchors above; the parser located target/method signals listed below.
- Why the problem matters: only infer from located KRD/desertification/remote-sensing problem statements; do not add unsupported claims.
- Remote sensing role: see satellite/data excerpts in Section 5.
- Existing research categories: classification, FBR/LSMM/MESMA, ML, semantic segmentation, DEM/topography when signaled below.
- Existing research insufficiency / gap / objectives / contributions: inspect Introduction anchors manually for exact wording before using in manuscript.
- Borrowable point for our Introduction: build a clear progression from KRD importance -> remote-sensing monitoring -> method/data limitation -> our FBR/classification/DEM/cross-region contribution.

Located target/method evidence:
- p.3: study area is dominated by moderate to severe rocky desertification, and human activities
- p.3: in managing rocky desertification have led to extensive land reclamation, creating an urgent
- p.9: Compared to traditional semantic segmentation networks, it offers
- p.11: spectral-textural variability of typical karst landforms (e.g., bare rocks, crevice vegetation).
- p.17: within karst rocky desertification control areas, early-stage vegetation recovery zones, and
- p.19: Karst Rocky Desertification Progress: Soil Calcium as a Possible Driving Force.Sci.
- p.19: Semantic Segmentation of Urban Buildings from VHR Remote Sensing
- p.20: Rocky Desertification Analysis by Sentinel-1 Data.
- p.20: Rocky Desertification in a Peak-Cluster Depression Basin in Southwest Guangxi, China.
- p.1: Comparative analysis demonstrated the superior performance
- p.2: As data technologies advance and geographical information analysis demands deepen, segmentation
- p.2: using segmentation objects significantly reduces spatial data volume while increasing
- p.2: in both space and time for fine-grained object segmentation.


## 5. Study Area and Data Sources

- Study area: locate from Study Area anchors: p.3, p.4, p.6, p.7, p.11, p.12, p.13, p.17
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
- p.1: Academic Editor: Junmin Liu
- p.1: Chinese Academy of Sciences, Beijing 100101, China; luojc@aircas.ac.cn
- p.1: 4 University of Chinese Academy of Sciences, Beijing 100049, China
- p.1: Comparative analysis demonstrated the superior performance
- p.1: academic research, governmental analysis, and related applications.
- p.2: As data technologies advance and geographical information analysis demands deepen, segmentation
- p.3: activation layers) but also demonstrate superior segmentation performance and potential
- p.3: remote sensing image segmentation, demonstrating significant effectiveness [29–31].
- p.3: adapted to complex terrain conditions and implementing hierarchical strategies in stratified
- p.4: Situated in the transitional slope zone between the


## 6. Target Variable or Classification System

- Target variable / object: derived from located evidence only.
- KRD/rocky desertification signal: yes
- FBR/fBR/bare-rock fraction signal: no
- Semantic segmentation class signal: yes
- If FBR/fBR is involved, treat it as a continuous/proportional variable unless the paper explicitly thresholds it into classes.
- If rocky desertification levels are involved, inspect the paper for the exact grade system before reuse.

Target evidence:
- p.3: study area is dominated by moderate to severe rocky desertification, and human activities
- p.3: in managing rocky desertification have led to extensive land reclamation, creating an urgent
- p.9: Compared to traditional semantic segmentation networks, it offers
- p.11: spectral-textural variability of typical karst landforms (e.g., bare rocks, crevice vegetation).
- p.17: within karst rocky desertification control areas, early-stage vegetation recovery zones, and
- p.19: Karst Rocky Desertification Progress: Soil Calcium as a Possible Driving Force.Sci.
- p.19: Semantic Segmentation of Urban Buildings from VHR Remote Sensing
- p.20: Rocky Desertification Analysis by Sentinel-1 Data.
- p.20: Rocky Desertification in a Peak-Cluster Depression Basin in Southwest Guangxi, China.


## 7. Method Workflow

The workflow below is derived from located method/data signals. Missing items are explicitly marked.
- preprocessing: located
- feature construction: located
- spectral indices: located
- DEM/topographic variables: located
- LSMM/SMA/MESMA/FCLS: located
- machine learning models: located
- deep learning models: located
- semantic segmentation architecture: located
- training strategy: located
- sample split: located
- cross-validation: not reported
- cross-region validation: located
- ablation design: not reported
- comparison methods: located

Located method/data evidence:
- p.1: Comparative analysis demonstrated the superior performance
- p.2: As data technologies advance and geographical information analysis demands deepen, segmentation
- p.2: using segmentation objects significantly reduces spatial data volume while increasing
- p.2: in both space and time for fine-grained object segmentation.
- p.2: region-based [17], supervised and unsupervised [ 18], traditional and deep learning approaches [19], as well as single-scale and multi-scale methods based on segmentation
- p.2: constitute an important component of traditional segmentation approaches.
- p.2: false, missing, shifted, and broken boundaries, affecting segmentation accuracy.
- p.2: classic category of traditional segmentation methods is region-based image segmentation, represented by K-means, Multi-Resolution Segmentation, and Mean-Shift algorithms.
- p.3: texture, etc.), achieving segmentation through iterative merging or splitting of adjacent
- p.3: single-scale segmentation struggles to accommodate the non-uniform segmentation requirements across different geographical objects.
- p.3: Currently, segmentation methods are
- p.3: segmentation techniques can not only eliminate tedious manual processes through carefully
- p.1: Academic Editor: Junmin Liu
- p.1: Chinese Academy of Sciences, Beijing 100101, China; luojc@aircas.ac.cn
- p.1: 4 University of Chinese Academy of Sciences, Beijing 100049, China
- p.1: Comparative analysis demonstrated the superior performance
- p.1: academic research, governmental analysis, and related applications.
- p.2: As data technologies advance and geographical information analysis demands deepen, segmentation
- p.3: activation layers) but also demonstrate superior segmentation performance and potential
- p.3: remote sensing image segmentation, demonstrating significant effectiveness [29–31].
- p.3: adapted to complex terrain conditions and implementing hierarchical strategies in stratified
- p.4: Situated in the transitional slope zone between the


## 8. Validation Strategy and Metrics

- Reference sample source: locate from excerpts below; manual confirmation recommended.
- Sample size: record only if explicitly visible in source excerpts; otherwise unknown.
- Train/test split: see located split/training evidence; otherwise not reported.
- Spatial split: located only if terms such as spatial/block split appear; otherwise not reported.
- Independent validation: located only if explicit evidence appears; otherwise not reported.
- Cross-region validation: located only if explicit evidence appears; otherwise not reported.

- Continuous-variable metrics located: slope
- Classification metrics located: OA, overall accuracy, Kappa, Precision, Recall, F1, IoU, mIoU

Metric evidence:
- p.1: Guiyang 550025, China; pandapo8341@163.com
- p.1: 3 State Key Laboratory of Remote Sensing and Digital Earth, Aerospace Information Research Institute,
- p.1: Karst mountain areas, as complex geological systems formed by carbonate rock development, possess unique three-dimensional spatial structures and hydrogeological processes
- p.1: fine-grained land use mapping and quantitative characterization of spatial heterogeneity
- p.1: Hence, this paper proposes a novel methodology for land use mapping in karst mountain
- p.1: Guanling and Zhenfeng counties in the Huajiang section of the Beipanjiang River Basin,
- p.1: notable accuracy metrics with an overall accuracy (OA) of 0.815 and a mean intersection
- p.1: over union (mIoU) of 0.688.
- p.1: Comparative analysis demonstrated the superior performance
- p.1: The approach provides a robust mapping framework for
- p.2: carbonate rock distribution, karst landforms are well-developed and diverse, spanning a
- p.2: scarcity of acidic insoluble substances from parent rock weathering, soil formation is slow


Important distinction enforced for our manuscript: continuous FBR inversion metrics (R2/RMSE/MAE/bias/slope) must not be mixed with classification metrics (OA/Kappa/Precision/Recall/F1/IoU/mF1/mIoU).

## 9. Figures and Tables

### Located Figure/Table 1
- Source anchor: p.4
- Caption: Figure 1. The location and digital elevation model (DEM) of the study area: (a) Location of Guizhou
- What it shows: inferred only from caption wording; inspect the PDF image before reuse.
- Why it matters: directly relevant to study design/results visualization
- Useful for our manuscript: yes
- Similar figure/table for our paper: consider

### Located Figure/Table 2
- Source anchor: p.6
- Caption: Figure 2. The process of land use mapping in karst mountain areas guided by geographical zoning
- What it shows: inferred only from caption wording; inspect the PDF image before reuse.
- Why it matters: directly relevant to study design/results visualization
- Useful for our manuscript: yes
- Similar figure/table for our paper: consider

### Located Figure/Table 3
- Source anchor: p.7
- Caption: Figure 3. Geographical zoning results: (a) natural zoning; (b) functional zoning.
- What it shows: inferred only from caption wording; inspect the PDF image before reuse.
- Why it matters: potentially relevant; requires manual inspection
- Useful for our manuscript: maybe
- Similar figure/table for our paper: manual review first

### Located Figure/Table 4
- Source anchor: p.8
- Caption: Table 1. Description of stratified objects extraction for land use mapping.
- What it shows: inferred only from caption wording; inspect the PDF image before reuse.
- Why it matters: directly relevant to study design/results visualization
- Useful for our manuscript: yes
- Similar figure/table for our paper: consider

### Located Figure/Table 5
- Source anchor: p.9
- Caption: Table 1. Cont.
- What it shows: inferred only from caption wording; inspect the PDF image before reuse.
- Why it matters: potentially relevant; requires manual inspection
- Useful for our manuscript: maybe
- Similar figure/table for our paper: manual review first

### Located Figure/Table 6
- Source anchor: p.10
- Caption: Figure 4. Architecture of the HBGNet (Ref. [11]).
- What it shows: inferred only from caption wording; inspect the PDF image before reuse.
- Why it matters: potentially relevant; requires manual inspection
- Useful for our manuscript: maybe
- Similar figure/table for our paper: manual review first

### Located Figure/Table 7
- Source anchor: p.11
- Caption: Table 2). Among them, water achieves the highest recognition performance, primarily due
- What it shows: inferred only from caption wording; inspect the PDF image before reuse.
- Why it matters: potentially relevant; requires manual inspection
- Useful for our manuscript: maybe
- Similar figure/table for our paper: manual review first

### Located Figure/Table 8
- Source anchor: p.12
- Caption: Table 2. Accuracy of the extracted land use objects.
- What it shows: inferred only from caption wording; inspect the PDF image before reuse.
- Why it matters: directly relevant to study design/results visualization
- Useful for our manuscript: yes
- Similar figure/table for our paper: consider

### Located Figure/Table 9
- Source anchor: p.13
- Caption: Figure 5. Land use mapping results of the study area.
- What it shows: inferred only from caption wording; inspect the PDF image before reuse.
- Why it matters: directly relevant to study design/results visualization
- Useful for our manuscript: yes
- Similar figure/table for our paper: consider

### Located Figure/Table 10
- Source anchor: p.14
- Caption: Table 3. Landscape pattern indices for multi-patch land use types.
- What it shows: inferred only from caption wording; inspect the PDF image before reuse.
- Why it matters: potentially relevant; requires manual inspection
- Useful for our manuscript: maybe
- Similar figure/table for our paper: manual review first

### Located Figure/Table 11
- Source anchor: p.15
- Caption: Figure 6. Comparative visualization of geospatial object extraction results across distinct model
- What it shows: inferred only from caption wording; inspect the PDF image before reuse.
- Why it matters: potentially relevant; requires manual inspection
- Useful for our manuscript: maybe
- Similar figure/table for our paper: manual review first

### Located Figure/Table 12
- Source anchor: p.16
- Caption: Table 4. Comparative accuracy comparison of unified and stratified frameworks.
- What it shows: inferred only from caption wording; inspect the PDF image before reuse.
- Why it matters: directly relevant to study design/results visualization
- Useful for our manuscript: yes
- Similar figure/table for our paper: consider

### Located Figure/Table 13
- Source anchor: p.16
- Caption: Figure 7. Corrective efficacy of the geographical zoning strategy on extraction outcomes.
- What it shows: inferred only from caption wording; inspect the PDF image before reuse.
- Why it matters: potentially relevant; requires manual inspection
- Useful for our manuscript: maybe
- Similar figure/table for our paper: manual review first


## 10. Results Reading Notes

- Source anchors: p.1, p.2, p.3, p.4, p.5, p.7, p.10, p.11, p.12, p.13, p.14, p.15, ...
- Main experimental results: use only values and claims visible in the excerpts/PDF tables.
- Model comparison results: inspect metric/table captions before using exact rankings.
- Data source comparison results: record only where Sentinel/Landsat/GF/DEM evidence is explicit.
- FBR/bare-rock inversion results: separate continuous metrics from class metrics.
- Classification accuracy: report OA/Kappa/Precision/Recall/F1/IoU/mF1/mIoU only if explicitly found.
- DEM/topographic factor contribution: note only when DEM/topographic excerpts are explicit.
- Spatial distribution / uncertainty / significance: inspect maps and captions manually.

Located result/metric evidence:
- p.1: notable accuracy metrics with an overall accuracy (OA) of 0.815 and a mean intersection
- p.1: The approach provides a robust mapping framework for
- p.2: fragmented land features, result in a scarcity of high-quality satellite imagery data and
- p.2: region-based [17], supervised and unsupervised [ 18], traditional and deep learning approaches [19], as well as single-scale and multi-scale methods based on segmentation
- p.2: constitute an important component of traditional segmentation approaches.
- p.2: false, missing, shifted, and broken boundaries, affecting segmentation accuracy.
- p.3: Among diverse approaches, the strategy of
- p.3: is expected to achieve a better mapping result with the support of prior knowledge, as
- p.3: resulting in land use objects with diverse morphological characteristics, including variable
- p.4: topography-constrained land use pattern results in highly irregular plot geometries and
- p.1: Guiyang 550025, China; pandapo8341@163.com
- p.1: 3 State Key Laboratory of Remote Sensing and Digital Earth, Aerospace Information Research Institute,
- p.1: Karst mountain areas, as complex geological systems formed by carbonate rock development, possess unique three-dimensional spatial structures and hydrogeological processes
- p.1: fine-grained land use mapping and quantitative characterization of spatial heterogeneity
- p.1: Hence, this paper proposes a novel methodology for land use mapping in karst mountain
- p.1: Guanling and Zhenfeng counties in the Huajiang section of the Beipanjiang River Basin,


## 11. Discussion Reading Notes

- Source anchors: not located
- Mechanism explanations, data-source performance, terrain effects, comparison to previous studies, limitations, and future work should be extracted from these anchors only.
- Borrowable Discussion writing pattern: explain why a data/model/factor improves mapping, then tie the explanation to spatial patterns and validation evidence.

Located discussion/limitation evidence:
- p.11: or roads due to limitations in the spatial resolution of remote sensing imagery and the
- p.18: However, several limitations warrant consideration.
- p.18: Therefore, future work will focus on model adaptability through lightweight
- p.5: This complexity introduces substantial uncertainty
- p.11: or roads due to limitations in the spatial resolution of remote sensing imagery and the
- p.18: However, several limitations warrant consideration.
- p.18: Therefore, future work will focus on model adaptability through lightweight


## 12. Conclusion Reading Notes

- Source anchors: p.17
- Objective summary: inspect Conclusion anchors.
- Method summary: inspect Conclusion anchors.
- Main results: record only exact values visible in Conclusion/Results.
- Contributions/application value: inspect Conclusion anchors.
- Limitations/future work: see limitation evidence above.

## 13. Relevance to Our Remote Sensing Manuscript

- Introduction support: not applicable. Reason: grounded signals were not located in the text layer.
- FBR/LSMM support: not applicable. Reason: grounded signals were not located in the text layer.
- ML baseline support: high. Reason: grounded signals were located in the text layer.
- semantic segmentation support: high. Reason: grounded signals were located in the text layer.
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


## 15. Items Needing Manual Review

- none
