# Full-Paper Reader: EN009 Classification of Karst Rocky Desertification Levels in Jins

## 1. Bibliographic Information

- Paper ID: KRD0095
- Title: EN009 Classification of Karst Rocky Desertification Levels in Jins
- Translated title if applicable: unknown
- Authors: unknown
- Year: unknown
- Journal / Source: unknown
- DOI: unknown
- URL: unknown
- PDF path: `docs/literature/pdfs/package_2000_2026/EN009_Classification_of_Karst_Rocky_Desertification_Levels_in_Jins.pdf`
- Language: unknown
- Readability status: usable_with_caution
- Metadata status: metadata_incomplete

## 2. Reading Scope and Source Anchors

This reader was generated from the full selectable text layer of the PDF. It preserves page-level anchors and section/figure/table signals. It does not reproduce large original-text passages and does not fabricate missing metadata.

- Abstract: p.1
- Introduction: p.2
- Study Area: p.3, p.4, p.5, p.16
- Data: p.1, p.2, p.3, p.4, p.5, p.7, p.8, p.9, p.10, p.16, p.18, p.19, ...
- Methods: p.1, p.2, p.3, p.4, p.5, p.6, p.8, p.10, p.11, p.12, p.13, p.14, ...
- Experiments: p.3, p.17
- Results: p.1, p.3, p.6, p.7, p.12, p.13, p.14, p.15, p.16, p.17, p.18
- Discussion: p.3, p.16, p.20
- Conclusions: p.9, p.18
- References: p.19
- Figures/Tables captions: 20 located
  - p.4: Figure 1. Overview map of the study area : (a) location of Jinsha County; and (b) digital elevation
  - p.4: Table 1 presents all the data used in this study. The SDGSAT-1 MSI data used in this
  - p.4: Table 1. Data used in this study.
  - p.5: Table 2. Absolute radiometric calibration correction factors.
  - p.6: Figure 2.
  - p.6: Figure 2. Overall workflow of this study. MSI: multispectral imager; UAV: unmanned aerial vehicle;
  - p.7: Figure 3. Reflectance spectral curves of carbonate rocks and vegetation ascertained from SDGSAT1 MSI data.
  - p.9: Figure 4. Principles of feature space [24–26]. Points A and B represent areas exhibiting low levels of

## 3. Abstract-Level Understanding

Source anchors: p.1, p.2, p.3

基于可抽取的摘要文本，本研究逻辑可按以下方式理解。以下内容只依据摘要和题录可确认的信息，不补造缺失结论。

- 研究背景: 论文主题与 `machine_learning` 相关，关键词信号包括 `unknown`。
- 研究目标: EN009 Classification of Karst Rocky Desertification Levels in Jins
- 数据: 见下方 Data Sources 中从全文定位到的证据信号。
- 方法: 见下方 Method Workflow 中从全文定位到的证据信号。
- 主要结果: 仅在 Results Reading Notes 中记录可定位的结果/指标信号；未在此处编造具体数值。
- 意义: 其价值主要体现在对 KRD/FBR/分类/遥感制图/验证框架的支撑，具体等级见第 13 节。

Abstract evidence snippet:

> Karst rocky desertification (KRD) is a significant issue that affects the ecological and economic sustainability of southwest China. Obtaining the accurate distribution of different levels of KRD can provide decision -making support for the effective management of KRD. The Sustainable Development Goals Science Satellite 1 (SDGSAT -1) is the world’s first scientific satellite serving the 2030 Agenda for Sustainable Development of the United Nations, and is dedicated to develop ing high-resolution, multi-scale, global public datasets to support policy and decision -making support systems for sustainable development. SDGSAT-1 multispectral data provide detailed ground information with a spatial resolution of 10 m and a rich spectral resolution. In this study, we combined the red-modified carbonate rock index (RCRI, an index t hat characterizes the degree of carbonate rock exposure) and the normalized difference red edge index (NDRE, an index that characterizes the degree of vegetation coverage) to propose a novel feature space method based on SDGSAT-1 multispectral data to classify the different levels of KRD in the Jinsha County of Guizhou Province, a representative region with signi

## 4. Introduction Reading Notes

- Source anchors: p.2
- Background unfolding: extracted introduction pages should be read around the anchors above; the parser located target/method signals listed below.
- Why the problem matters: only infer from located KRD/desertification/remote-sensing problem statements; do not add unsupported claims.
- Remote sensing role: see satellite/data excerpts in Section 5.
- Existing research categories: classification, FBR/LSMM/MESMA, ML, semantic segmentation, DEM/topography when signaled below.
- Existing research insufficiency / gap / objectives / contributions: inspect Introduction anchors manually for exact wording before using in manuscript.
- Borrowable point for our Introduction: build a clear progression from KRD importance -> remote-sensing monitoring -> method/data limitation -> our FBR/classification/DEM/cross-region contribution.

Located target/method evidence:
- p.1: Classification of Karst Rocky Desertification Levels in Jinsha
- p.1: Abstract: Karst rocky desertification (KRD) is a significant issue that affects the ecological
- p.1: Keywords: SDGSAT-1; feature space; karst rocky desertification; classification of KRD
- p.1: Karst Rocky Desertification Levels in
- p.2: Karst rocky desertification (KRD) is a form of land degradation that refers to the degradation process caused by severe soil erosion and inappropriate human activities in the
- p.2: The use of remote-sensing data is of significant value in the monitoring of land degradation, offering a rapid method with which to study surface features and phenomena
- p.2: bedrock fractions, fractional vegetation cover, and slope s, to construct a decision tree to
- p.6: DEM: digital elevation model; KRDI: karst rocky desertification monitoring index; KRD: karst rocky
- p.6: The exposed bedrock fraction (EBF) and fractional vegetation cover (FVC) are two
- p.8: bedrocks, resulting in higher vegetation indices and lower rock indices.
- p.1: County Using a Feature Space Method Based on SDGSAT-1
- p.1: that characterizes the degree of vegetation coverage) to propose a novel feature space
- p.1: Keywords: SDGSAT-1; feature space; karst rocky desertification; classification of KRD
- p.1: Jinsha County Using a Feature Space


## 5. Study Area and Data Sources

- Study area: locate from Study Area anchors: p.3, p.4, p.5, p.16
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
- p.1: 7 Key Laboratory of Digital Earth Sciences, Aerospace Information Research Institute, Chinese Academy of
- p.1: Academic Editor: Sandra Eckert
- p.2: Those with mild KRD demonstrate emerging rock exposure, noticeable soil erosion, and sparse vegetation.
- p.2: Field investigation s and remote-sensing technology are both
- p.2: Field investigations often demand substantial
- p.2: bedrock fractions, fractional vegetation cover, and slope s, to construct a decision tree to
- p.2: The thresholds of the KRDI for each level of KRD are then customized based on the sample
- p.3: been applied to various research fields.
- p.3: SDGSAT-1 data have also been used for desertification monitoring, demonstrating the
- p.3: The study area was Jinsha County, which is located in the eastern part of Bijie City,


## 6. Target Variable or Classification System

- Target variable / object: derived from located evidence only.
- KRD/rocky desertification signal: yes
- FBR/fBR/bare-rock fraction signal: no
- Semantic segmentation class signal: no
- If FBR/fBR is involved, treat it as a continuous/proportional variable unless the paper explicitly thresholds it into classes.
- If rocky desertification levels are involved, inspect the paper for the exact grade system before reuse.

Target evidence:
- p.1: Classification of Karst Rocky Desertification Levels in Jinsha
- p.1: Abstract: Karst rocky desertification (KRD) is a significant issue that affects the ecological
- p.1: Keywords: SDGSAT-1; feature space; karst rocky desertification; classification of KRD
- p.1: Karst Rocky Desertification Levels in
- p.2: Karst rocky desertification (KRD) is a form of land degradation that refers to the degradation process caused by severe soil erosion and inappropriate human activities in the
- p.2: The use of remote-sensing data is of significant value in the monitoring of land degradation, offering a rapid method with which to study surface features and phenomena
- p.2: bedrock fractions, fractional vegetation cover, and slope s, to construct a decision tree to
- p.6: DEM: digital elevation model; KRDI: karst rocky desertification monitoring index; KRD: karst rocky
- p.6: The exposed bedrock fraction (EBF) and fractional vegetation cover (FVC) are two
- p.8: bedrocks, resulting in higher vegetation indices and lower rock indices.


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
- training strategy: not reported
- sample split: located
- cross-validation: not reported
- cross-region validation: not reported
- ablation design: not reported
- comparison methods: located

Located method/data evidence:
- p.1: County Using a Feature Space Method Based on SDGSAT-1
- p.1: that characterizes the degree of vegetation coverage) to propose a novel feature space
- p.1: Keywords: SDGSAT-1; feature space; karst rocky desertification; classification of KRD
- p.1: Jinsha County Using a Feature Space
- p.2: The use of remote-sensing data is of significant value in the monitoring of land degradation, offering a rapid method with which to study surface features and phenomena
- p.2: Different remote-sensing indices can reflect different surface features and can obtain
- p.2: Grading index [20–22] and feature space [23–25]
- p.2: The feature space method constructs a two-dimensional surface based on two KRD characterization indices ; a KRD monitoring index
- p.2: method, the feature space method can effectively reflect the interactions between different
- p.3: macroscopic observations of the earth’s surface as well as provide coordinated multi-payload day-and-night detection.
- p.3: In this study, we created a feature space method based on the red-modified carbonate
- p.3: that the RCRI –NDRE feature space method is an efficacious approach to assessing the
- p.1: 7 Key Laboratory of Digital Earth Sciences, Aerospace Information Research Institute, Chinese Academy of
- p.1: Academic Editor: Sandra Eckert
- p.2: Those with mild KRD demonstrate emerging rock exposure, noticeable soil erosion, and sparse vegetation.
- p.2: Field investigation s and remote-sensing technology are both
- p.2: Field investigations often demand substantial
- p.2: bedrock fractions, fractional vegetation cover, and slope s, to construct a decision tree to
- p.2: The thresholds of the KRDI for each level of KRD are then customized based on the sample
- p.3: been applied to various research fields.
- p.3: SDGSAT-1 data have also been used for desertification monitoring, demonstrating the
- p.3: The study area was Jinsha County, which is located in the eastern part of Bijie City,


## 8. Validation Strategy and Metrics

- Reference sample source: locate from excerpts below; manual confirmation recommended.
- Sample size: record only if explicitly visible in source excerpts; otherwise unknown.
- Train/test split: see located split/training evidence; otherwise not reported.
- Spatial split: located only if terms such as spatial/block split appear; otherwise not reported.
- Independent validation: located only if explicit evidence appears; otherwise not reported.
- Cross-region validation: located only if explicit evidence appears; otherwise not reported.

- Continuous-variable metrics located: bias, slope
- Classification metrics located: OA, overall accuracy, Kappa, Precision, F1, IoU, confusion matrix

Metric evidence:
- p.1: County Using a Feature Space Method Based on SDGSAT-1
- p.1: Qi Chen 1,2, Han Fu 3,4,*, Xiaoming Li 2,3,5, Xiaochuan Qin 6 and Lin Yan 2,7
- p.1: 2 International Research Center of Big Data for Sustainable Development Goals, Beijing 100094, China;
- p.1: 3 Hainan Aerospace Technology Innovation Center, Wenchang 571399, China
- p.1: 4 State Key Laboratory of Space-Earth Integrated Information Technology, Beijing Institute of Satellite
- p.1: 5 Key Laboratory of Earth Observation of Hainan Province, Hainan Aerospace Information Research
- p.1: 6 Beijing Tsinghua Tongheng Planning and Design Institute Co., Ltd., Beijing 100094, China;
- p.1: 7 Key Laboratory of Digital Earth Sciences, Aerospace Information Research Institute, Chinese Academy of
- p.1: The Sustainable Development Goals Science Satellite 1 (SDGSAT -1) is the
- p.1: spatial resolution of 10 m and a rich spectral resolution.
- p.1: that characterizes the degree of vegetation coverage) to propose a novel feature space
- p.1: This method effectively identified different levels of KRD with an overall classification accuracy of 87% .


Important distinction enforced for our manuscript: continuous FBR inversion metrics (R2/RMSE/MAE/bias/slope) must not be mixed with classification metrics (OA/Kappa/Precision/Recall/F1/IoU/mF1/mIoU).

## 9. Figures and Tables

### Located Figure/Table 1
- Source anchor: p.4
- Caption: Figure 1. Overview map of the study area : (a) location of Jinsha County; and (b) digital elevation
- What it shows: inferred only from caption wording; inspect the PDF image before reuse.
- Why it matters: directly relevant to study design/results visualization
- Useful for our manuscript: yes
- Similar figure/table for our paper: consider

### Located Figure/Table 2
- Source anchor: p.4
- Caption: Table 1 presents all the data used in this study. The SDGSAT-1 MSI data used in this
- What it shows: inferred only from caption wording; inspect the PDF image before reuse.
- Why it matters: potentially relevant; requires manual inspection
- Useful for our manuscript: maybe
- Similar figure/table for our paper: manual review first

### Located Figure/Table 3
- Source anchor: p.4
- Caption: Table 1. Data used in this study.
- What it shows: inferred only from caption wording; inspect the PDF image before reuse.
- Why it matters: potentially relevant; requires manual inspection
- Useful for our manuscript: maybe
- Similar figure/table for our paper: manual review first

### Located Figure/Table 4
- Source anchor: p.5
- Caption: Table 2. Absolute radiometric calibration correction factors.
- What it shows: inferred only from caption wording; inspect the PDF image before reuse.
- Why it matters: potentially relevant; requires manual inspection
- Useful for our manuscript: maybe
- Similar figure/table for our paper: manual review first

### Located Figure/Table 5
- Source anchor: p.6
- Caption: Figure 2.
- What it shows: inferred only from caption wording; inspect the PDF image before reuse.
- Why it matters: potentially relevant; requires manual inspection
- Useful for our manuscript: maybe
- Similar figure/table for our paper: manual review first

### Located Figure/Table 6
- Source anchor: p.6
- Caption: Figure 2. Overall workflow of this study. MSI: multispectral imager; UAV: unmanned aerial vehicle;
- What it shows: inferred only from caption wording; inspect the PDF image before reuse.
- Why it matters: directly relevant to study design/results visualization
- Useful for our manuscript: yes
- Similar figure/table for our paper: consider

### Located Figure/Table 7
- Source anchor: p.7
- Caption: Figure 3. Reflectance spectral curves of carbonate rocks and vegetation ascertained from SDGSAT1 MSI data.
- What it shows: inferred only from caption wording; inspect the PDF image before reuse.
- Why it matters: potentially relevant; requires manual inspection
- Useful for our manuscript: maybe
- Similar figure/table for our paper: manual review first

### Located Figure/Table 8
- Source anchor: p.9
- Caption: Figure 4. Principles of feature space [24–26]. Points A and B represent areas exhibiting low levels of
- What it shows: inferred only from caption wording; inspect the PDF image before reuse.
- Why it matters: directly relevant to study design/results visualization
- Useful for our manuscript: yes
- Similar figure/table for our paper: consider

### Located Figure/Table 9
- Source anchor: p.9
- Caption: Figure 5 is a schematic diagram of the feature space identified from SDGSAT-1 MSI
- What it shows: inferred only from caption wording; inspect the PDF image before reuse.
- Why it matters: directly relevant to study design/results visualization
- Useful for our manuscript: yes
- Similar figure/table for our paper: consider

### Located Figure/Table 10
- Source anchor: p.10
- Caption: Figure 5. Feature space f rom SDGSAT-1 MSI data. The straight line (y) represents the baseline,
- What it shows: inferred only from caption wording; inspect the PDF image before reuse.
- Why it matters: directly relevant to study design/results visualization
- Useful for our manuscript: yes
- Similar figure/table for our paper: consider

### Located Figure/Table 11
- Source anchor: p.11
- Caption: Table 3. Decision tree classification criteria.
- What it shows: inferred only from caption wording; inspect the PDF image before reuse.
- Why it matters: directly relevant to study design/results visualization
- Useful for our manuscript: yes
- Similar figure/table for our paper: consider

### Located Figure/Table 12
- Source anchor: p.11
- Caption: Figure 6. Distribution of sample points: (a) overall distribution of sample sites; and (b,c) local graphs
- What it shows: inferred only from caption wording; inspect the PDF image before reuse.
- Why it matters: potentially relevant; requires manual inspection
- Useful for our manuscript: maybe
- Similar figure/table for our paper: manual review first

### Located Figure/Table 13
- Source anchor: p.12
- Caption: Table 4. Visual interpretation criteria for different levels of KRD.
- What it shows: inferred only from caption wording; inspect the PDF image before reuse.
- Why it matters: potentially relevant; requires manual inspection
- Useful for our manuscript: maybe
- Similar figure/table for our paper: manual review first

### Located Figure/Table 14
- Source anchor: p.13
- Caption: Table 5. Accuracy of KRD classification for different feature spaces.
- What it shows: inferred only from caption wording; inspect the PDF image before reuse.
- Why it matters: directly relevant to study design/results visualization
- Useful for our manuscript: yes
- Similar figure/table for our paper: consider

### Located Figure/Table 15
- Source anchor: p.13
- Caption: Table 6. Confusion matrix for the RCRI–NDRE feature space method.
- What it shows: inferred only from caption wording; inspect the PDF image before reuse.
- Why it matters: directly relevant to study design/results visualization
- Useful for our manuscript: yes
- Similar figure/table for our paper: consider

### Located Figure/Table 16
- Source anchor: p.14
- Caption: Table 7. Confusion matrix for the grading index method.
- What it shows: inferred only from caption wording; inspect the PDF image before reuse.
- Why it matters: directly relevant to study design/results visualization
- Useful for our manuscript: yes
- Similar figure/table for our paper: consider

### Located Figure/Table 17
- Source anchor: p.15
- Caption: Figure 7. KRD classification results: (a) classification result based on the RCRI–NDRE feature space
- What it shows: inferred only from caption wording; inspect the PDF image before reuse.
- Why it matters: directly relevant to study design/results visualization
- Useful for our manuscript: yes
- Similar figure/table for our paper: consider

### Located Figure/Table 18
- Source anchor: p.16
- Caption: Figure 8. Statistical results of areas of different levels of KRD in Jinsha County obtained using the
- What it shows: inferred only from caption wording; inspect the PDF image before reuse.
- Why it matters: potentially relevant; requires manual inspection
- Useful for our manuscript: maybe
- Similar figure/table for our paper: manual review first

### Located Figure/Table 19
- Source anchor: p.17
- Caption: Figure 9. Distribution of KRD in Dafang County with all six levels of KRD (No, Potential, Mild,
- What it shows: inferred only from caption wording; inspect the PDF image before reuse.
- Why it matters: potentially relevant; requires manual inspection
- Useful for our manuscript: maybe
- Similar figure/table for our paper: manual review first

### Located Figure/Table 20
- Source anchor: p.17
- Caption: Table 8. Confusion matrix for the RCRI–NDRE feature space method used for Dafang County.
- What it shows: inferred only from caption wording; inspect the PDF image before reuse.
- Why it matters: directly relevant to study design/results visualization
- Useful for our manuscript: yes
- Similar figure/table for our paper: consider


## 10. Results Reading Notes

- Source anchors: p.1, p.3, p.6, p.7, p.12, p.13, p.14, p.15, p.16, p.17, p.18
- Main experimental results: use only values and claims visible in the excerpts/PDF tables.
- Model comparison results: inspect metric/table captions before using exact rankings.
- Data source comparison results: record only where Sentinel/Landsat/GF/DEM evidence is explicit.
- FBR/bare-rock inversion results: separate continuous metrics from class metrics.
- Classification accuracy: report OA/Kappa/Precision/Recall/F1/IoU/mF1/mIoU only if explicitly found.
- DEM/topographic factor contribution: note only when DEM/topographic excerpts are explicit.
- Spatial distribution / uncertainty / significance: inspect maps and captions manually.

Located result/metric evidence:
- p.1: 2 International Research Center of Big Data for Sustainable Development Goals, Beijing 100094, China;
- p.1: The Sustainable Development Goals Science Satellite 1 (SDGSAT -1) is the
- p.1: This method effectively identified different levels of KRD with an overall classification accuracy of 87% .
- p.2: The Sustainable Development Goals Science Satellite 1 (SDGSAT -1) is the world’s
- p.2: macroscopic observations of the earth’s surface as well as provide coordinated multi-payload day-and-night detection.
- p.2: The MSI payload can acquire images with
- p.2: Its data show distinct advantages for coastal monitoring such as the monitoring of red tides [33] and suspended
- p.2: with a view to broaden ing the application domains of the data.
- p.2: that the RCRI –NDRE feature space method is an efficacious approach to assessing the
- p.2: The accuracy rate is 87%, indicating the potential of SDGSAT-1 MSI data
- p.1: County Using a Feature Space Method Based on SDGSAT-1
- p.1: Qi Chen 1,2, Han Fu 3,4,*, Xiaoming Li 2,3,5, Xiaochuan Qin 6 and Lin Yan 2,7
- p.1: 2 International Research Center of Big Data for Sustainable Development Goals, Beijing 100094, China;
- p.1: 3 Hainan Aerospace Technology Innovation Center, Wenchang 571399, China
- p.1: 4 State Key Laboratory of Space-Earth Integrated Information Technology, Beijing Institute of Satellite
- p.1: 5 Key Laboratory of Earth Observation of Hainan Province, Hainan Aerospace Information Research


## 11. Discussion Reading Notes

- Source anchors: p.3, p.16, p.20
- Mechanism explanations, data-source performance, terrain effects, comparison to previous studies, limitations, and future work should be extracted from these anchors only.
- Borrowable Discussion writing pattern: explain why a data/model/factor improves mapping, then tie the explanation to spatial patterns and validation evidence.

Located discussion/limitation evidence:
- p.1: Sections 4 and 5 comprise analyses of the results and a discussion of the
- p.3: Discussion on the enhancement technology of remote sensing information
- p.19: Uncertainty in remote sensing information extraction of karst rocky


## 12. Conclusion Reading Notes

- Source anchors: p.9, p.18
- Objective summary: inspect Conclusion anchors.
- Method summary: inspect Conclusion anchors.
- Main results: record only exact values visible in Conclusion/Results.
- Contributions/application value: inspect Conclusion anchors.
- Limitations/future work: see limitation evidence above.

## 13. Relevance to Our Remote Sensing Manuscript

- Introduction support: medium. Reason: grounded signals were located in the text layer.
- FBR/LSMM support: not applicable. Reason: grounded signals were not located in the text layer.
- ML baseline support: medium. Reason: grounded signals were located in the text layer.
- semantic segmentation support: not applicable. Reason: grounded signals were not located in the text layer.
- DEM/topography support: medium. Reason: grounded signals were located in the text layer.
- GF/Sentinel/Landsat data comparison support: medium. Reason: grounded signals were located in the text layer.
- cross-region transfer support: not applicable. Reason: grounded signals were not located in the text layer.
- accuracy assessment support: medium. Reason: grounded signals were located in the text layer.
- Discussion comparison support: medium. Reason: grounded signals were located in the text layer.
- limitations support: medium. Reason: grounded signals were located in the text layer.
- figure/table design support: medium. Reason: grounded signals were located in the text layer.
- terminology support: medium. Reason: grounded signals were located in the text layer.
- Remote Sensing writing style support: medium. Reason: grounded signals were located in the text layer.

## 14. Reusable Knowledge for Future Skill

### Scientific rules
- Relevant target/method signals: machine_learning; unknown.
- Located target evidence pages: p.1, p.1, p.1, p.1, p.2, p.2.
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
