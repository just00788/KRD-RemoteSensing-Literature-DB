# Full-Paper Reader: Extracting Information on Rocky Desertification from Satellite Images: A Comparative Study

## 1. Bibliographic Information

- Paper ID: KRD0033
- Title: Extracting Information on Rocky Desertification from Satellite Images: A Comparative Study
- Translated title if applicable: unknown
- Authors: Pu J.; Zhao X.; Dong P.; Wang Q.; Yue Q.
- Year: 2021
- Journal / Source: core
- DOI: 10.3390/rs13132497
- URL: https://www.mdpi.com/2072-4292/13/13/2497
- PDF path: `docs/literature/pdfs/package_2000_2026/EN001_Extracting_Information_on_Rocky_Desertification_from_Satelli.pdf`
- Language: English
- Readability status: ready
- Metadata status: complete

## 2. Reading Scope and Source Anchors

This reader was generated from the full selectable text layer of the PDF. It preserves page-level anchors and section/figure/table signals. It does not reproduce large original-text passages and does not fabricate missing metadata.

- Abstract: p.1
- Introduction: p.1
- Study Area: p.1, p.2, p.3, p.4, p.5, p.7, p.8, p.9, p.16, p.17, p.18, p.19
- Data: p.1, p.2, p.3, p.4, p.5, p.6, p.7, p.8, p.9, p.10, p.12, p.13, ...
- Methods: p.1, p.2, p.3, p.5, p.6, p.7, p.8, p.9, p.11, p.12, p.13, p.17, ...
- Experiments: p.3, p.4, p.8, p.9, p.11, p.12, p.18
- Results: p.1, p.2, p.3, p.8, p.9, p.10, p.11, p.12, p.13, p.14, p.15, p.16, ...
- Discussion: p.3, p.16
- Conclusions: p.18
- References: p.19
- Figures/Tables captions: 20 located
  - p.4: Figure 1. Location of study area and sample pictures: most of the exposed rocks in the karst region show characteristics of
  - p.4: Figure 1. Location of study area and sample pictures: most of the exposed rocks in the karst region show characteristics of
  - p.5: Table 1. Data sources and descriptions.
  - p.6: Table 2. Major parameters of three open-access satellite images.
  - p.7: Figure 2. Methodology flowchart of the comparative study.
  - p.7: Figure 2. Methodology ﬂowchart of the comparative study.
  - p.8: Table 3. Samples and descriptions of rocky desertiﬁcation levels.
  - p.10: Table 4. Comparison of important bands on information extraction of rocky desertiﬁcation.

## 3. Abstract-Level Understanding

Source anchors: p.1, p.2, p.3

基于可抽取的摘要文本，本研究逻辑可按以下方式理解。以下内容只依据摘要和题录可确认的信息，不补造缺失结论。

- 研究背景: 论文主题与 `rocky_desertification_classification` 相关，关键词信号包括 `unknown`。
- 研究目标: Extracting Information on Rocky Desertification from Satellite Images: A Comparative Study
- 数据: 见下方 Data Sources 中从全文定位到的证据信号。
- 方法: 见下方 Method Workflow 中从全文定位到的证据信号。
- 主要结果: 仅在 Results Reading Notes 中记录可定位的结果/指标信号；未在此处编造具体数值。
- 意义: 其价值主要体现在对 KRD/FBR/分类/遥感制图/验证框架的支撑，具体等级见第 13 节。

Abstract evidence snippet:

> Rocky desertiﬁcation occurs in many karst terrains of the world and poses major challenges for regional sustainable development. Remotely sensed data can provide important information on rocky desertiﬁcation. In this study, three common open-access satellite image datasets (Sentinel2B, Landsat-8, and Gaofen-6) were used for extracting information on rocky desertiﬁcation in a typical karst region (Guangnan County, Yunnan) of southwest China, using three machine-learning algorithms implemented in the Python programming language: random forest (RF), bagged decision tree (BDT), and extremely randomized trees (ERT). Comparative analyses of the three data sources and three algorithms show that: (1) The Sentinel-2B image has the best capability for extracting rocky desertiﬁcation information, with an overall accuracy (OA) of 85.21% using the ERT method. This can be attributed to the higher spatial resolution of the Sentinel-2B image than that of Landsat-8 and Gaofen-6 images and Gaofen-6’s lack of the shortwave infrared (SWIR) bands suitable for mapping carbonate rocks. (2) The ERT method has the best classiﬁcation results of rocky desertiﬁcation. Compared with the RF and BDT methods, the

## 4. Introduction Reading Notes

- Source anchors: p.1
- Background unfolding: extracted introduction pages should be read around the anchors above; the parser located target/method signals listed below.
- Why the problem matters: only infer from located KRD/desertification/remote-sensing problem statements; do not add unsupported claims.
- Remote sensing role: see satellite/data excerpts in Section 5.
- Existing research categories: classification, FBR/LSMM/MESMA, ML, semantic segmentation, DEM/topography when signaled below.
- Existing research insufficiency / gap / objectives / contributions: inspect Introduction anchors manually for exact wording before using in manuscript.
- Borrowable point for our Introduction: build a clear progression from KRD importance -> remote-sensing monitoring -> method/data limitation -> our FBR/classification/DEM/cross-region contribution.

Located target/method evidence:
- p.1: Karst areas are ecologically fragile and susceptible to land degradation [3].
- p.1: manifestation of land degradation in karst areas that results in vegetation deterioration,
- p.1: soil erosion, and bedrock exposure, under the dual action of natural processes and human
- p.1: land degradation in karst areas.
- p.2: contains mixed spectral information of vegetation, bedrock, and bare soil [20].
- p.4: been in a vicious cycle of “fragile ecology → extensive development → rocky desertification → enhanced poverty” [47].
- p.4: Due to the wide distribution of rocky desertification,
- p.4: rocky desertification in 2008.
- p.4: Thus, the overall situation of rocky desertification in the study area has not
- p.6: we compared the separability of the fractional vegetation cover (FVC) and exposed bedrock
- p.1: algorithms implemented in the Python programming language: random forest (RF), bagged decision
- p.1: Compared with the RF and BDT methods, the ERT method has stronger randomness in modeling and
- p.1: surface system, accounting for 15% of the Earth’s land area [1,2].
- p.2: Satellite remote sensing provides a synoptic view for studying Earth surface features and


## 5. Study Area and Data Sources

- Study area: locate from Study Area anchors: p.1, p.2, p.3, p.4, p.5, p.7, p.8, p.9, p.16, p.17, p.18, p.19
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
- p.1: Academic Editor: Lenio Soares
- p.1: Abstract: Rocky desertiﬁcation occurs in many karst terrains of the world and poses major challenges
- p.1: In this study, three common open-access satellite image datasets (Sentinel2B, Landsat-8, and Gaofen-6) were used for extracting information on rocky desertiﬁcation in a
- p.1: and three algorithms show that: (1) The Sentinel-2B image has the best capability for extracting rocky
- p.1: can be attributed to the higher spatial resolution of the Sentinel-2B image than that of Landsat-8 and
- p.1: Gaofen-6 images and Gaofen-6’s lack of the shortwave infrared (SWIR) bands suitable for mapping
- p.1: (3) The combination of the Sentinel-2B images and the ERT method provides an effective, efﬁcient,
- p.2: Geological Survey (USGS) have been providing open access to Landsat series data [ 16],
- p.2: desertiﬁcation, including unmanned aerial vehicles (UAV) [18], SPOT satellites [19], ALOS
- p.2: However, UAV images, as well as most commercial high-resolution satellite images,


## 6. Target Variable or Classification System

- Target variable / object: derived from located evidence only.
- KRD/rocky desertification signal: yes
- FBR/fBR/bare-rock fraction signal: yes
- Semantic segmentation class signal: no
- If FBR/fBR is involved, treat it as a continuous/proportional variable unless the paper explicitly thresholds it into classes.
- If rocky desertification levels are involved, inspect the paper for the exact grade system before reuse.

Target evidence:
- p.1: Karst areas are ecologically fragile and susceptible to land degradation [3].
- p.1: manifestation of land degradation in karst areas that results in vegetation deterioration,
- p.1: soil erosion, and bedrock exposure, under the dual action of natural processes and human
- p.1: land degradation in karst areas.
- p.2: contains mixed spectral information of vegetation, bedrock, and bare soil [20].
- p.4: been in a vicious cycle of “fragile ecology → extensive development → rocky desertification → enhanced poverty” [47].
- p.4: Due to the wide distribution of rocky desertification,
- p.4: rocky desertification in 2008.
- p.4: Thus, the overall situation of rocky desertification in the study area has not
- p.6: we compared the separability of the fractional vegetation cover (FVC) and exposed bedrock


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
- cross-region validation: not reported
- ablation design: not reported
- comparison methods: located

Located method/data evidence:
- p.1: algorithms implemented in the Python programming language: random forest (RF), bagged decision
- p.1: Compared with the RF and BDT methods, the ERT method has stronger randomness in modeling and
- p.1: surface system, accounting for 15% of the Earth’s land area [1,2].
- p.2: Satellite remote sensing provides a synoptic view for studying Earth surface features and
- p.2: desertiﬁcation, it is worthwhile to compare the performance of different information extraction methods applied to the image data.
- p.2: employed, such as spectral mixture analysis (SMA) [21], dimidiate pixel model (DPM) [20],
- p.2: using the SMA and DPM alone, because the surface color of rocks may vary depending
- p.2: performance and widespread application [17,32].
- p.2: Random forest (RF) and bagged
- p.3: However, both the RF and BDT algorithms use the bagging
- p.3: and random way, with smaller variance and more stable prediction results [38].
- p.3: It has the advantages of RF and BDT and
- p.1: Academic Editor: Lenio Soares
- p.1: Abstract: Rocky desertiﬁcation occurs in many karst terrains of the world and poses major challenges
- p.1: In this study, three common open-access satellite image datasets (Sentinel2B, Landsat-8, and Gaofen-6) were used for extracting information on rocky desertiﬁcation in a
- p.1: and three algorithms show that: (1) The Sentinel-2B image has the best capability for extracting rocky
- p.1: can be attributed to the higher spatial resolution of the Sentinel-2B image than that of Landsat-8 and
- p.1: Gaofen-6 images and Gaofen-6’s lack of the shortwave infrared (SWIR) bands suitable for mapping
- p.1: (3) The combination of the Sentinel-2B images and the ERT method provides an effective, efﬁcient,
- p.2: Geological Survey (USGS) have been providing open access to Landsat series data [ 16],
- p.2: desertiﬁcation, including unmanned aerial vehicles (UAV) [18], SPOT satellites [19], ALOS
- p.2: However, UAV images, as well as most commercial high-resolution satellite images,


## 8. Validation Strategy and Metrics

- Reference sample source: locate from excerpts below; manual confirmation recommended.
- Sample size: record only if explicitly visible in source excerpts; otherwise unknown.
- Train/test split: see located split/training evidence; otherwise not reported.
- Spatial split: located only if terms such as spatial/block split appear; otherwise not reported.
- Independent validation: located only if explicit evidence appears; otherwise not reported.
- Cross-region validation: located only if explicit evidence appears; otherwise not reported.

- Continuous-variable metrics located: slope
- Classification metrics located: OA, overall accuracy, Precision, IoU

Metric evidence:
- p.1: Images: A Comparative Study
- p.1: from Satellite Images: A Comparative
- p.1: Academic Editor: Lenio Soares
- p.1: 3 Department of Geography and the Environment, University of North Texas, Denton, TX 76203, USA;
- p.1: typical karst region (Guangnan County, Yunnan) of southwest China, using three machine-learning
- p.1: algorithms implemented in the Python programming language: random forest (RF), bagged decision
- p.1: Comparative analyses of the three data sources
- p.1: and three algorithms show that: (1) The Sentinel-2B image has the best capability for extracting rocky
- p.1: desertiﬁcation information, with an overall accuracy (OA) of 85.21% using the ERT method.
- p.1: can be attributed to the higher spatial resolution of the Sentinel-2B image than that of Landsat-8 and
- p.1: Compared with the RF and BDT methods, the ERT method has stronger randomness in modeling and
- p.1: and free approach to information extraction for mapping rocky desertiﬁcation.


Important distinction enforced for our manuscript: continuous FBR inversion metrics (R2/RMSE/MAE/bias/slope) must not be mixed with classification metrics (OA/Kappa/Precision/Recall/F1/IoU/mF1/mIoU).

## 9. Figures and Tables

### Located Figure/Table 1
- Source anchor: p.4
- Caption: Figure 1. Location of study area and sample pictures: most of the exposed rocks in the karst region show characteristics of
- What it shows: inferred only from caption wording; inspect the PDF image before reuse.
- Why it matters: directly relevant to study design/results visualization
- Useful for our manuscript: yes
- Similar figure/table for our paper: consider

### Located Figure/Table 2
- Source anchor: p.4
- Caption: Figure 1. Location of study area and sample pictures: most of the exposed rocks in the karst region show characteristics of
- What it shows: inferred only from caption wording; inspect the PDF image before reuse.
- Why it matters: directly relevant to study design/results visualization
- Useful for our manuscript: yes
- Similar figure/table for our paper: consider

### Located Figure/Table 3
- Source anchor: p.5
- Caption: Table 1. Data sources and descriptions.
- What it shows: inferred only from caption wording; inspect the PDF image before reuse.
- Why it matters: potentially relevant; requires manual inspection
- Useful for our manuscript: maybe
- Similar figure/table for our paper: manual review first

### Located Figure/Table 4
- Source anchor: p.6
- Caption: Table 2. Major parameters of three open-access satellite images.
- What it shows: inferred only from caption wording; inspect the PDF image before reuse.
- Why it matters: potentially relevant; requires manual inspection
- Useful for our manuscript: maybe
- Similar figure/table for our paper: manual review first

### Located Figure/Table 5
- Source anchor: p.7
- Caption: Figure 2. Methodology flowchart of the comparative study.
- What it shows: inferred only from caption wording; inspect the PDF image before reuse.
- Why it matters: potentially relevant; requires manual inspection
- Useful for our manuscript: maybe
- Similar figure/table for our paper: manual review first

### Located Figure/Table 6
- Source anchor: p.7
- Caption: Figure 2. Methodology ﬂowchart of the comparative study.
- What it shows: inferred only from caption wording; inspect the PDF image before reuse.
- Why it matters: potentially relevant; requires manual inspection
- Useful for our manuscript: maybe
- Similar figure/table for our paper: manual review first

### Located Figure/Table 7
- Source anchor: p.8
- Caption: Table 3. Samples and descriptions of rocky desertiﬁcation levels.
- What it shows: inferred only from caption wording; inspect the PDF image before reuse.
- Why it matters: potentially relevant; requires manual inspection
- Useful for our manuscript: maybe
- Similar figure/table for our paper: manual review first

### Located Figure/Table 8
- Source anchor: p.10
- Caption: Table 4. Comparison of important bands on information extraction of rocky desertiﬁcation.
- What it shows: inferred only from caption wording; inspect the PDF image before reuse.
- Why it matters: potentially relevant; requires manual inspection
- Useful for our manuscript: maybe
- Similar figure/table for our paper: manual review first

### Located Figure/Table 9
- Source anchor: p.10
- Caption: Figure 3. FVC and EBF information extracted from three image data (“S”, “L”, and “G” represent the remotely sensed
- What it shows: inferred only from caption wording; inspect the PDF image before reuse.
- Why it matters: potentially relevant; requires manual inspection
- Useful for our manuscript: maybe
- Similar figure/table for our paper: manual review first

### Located Figure/Table 10
- Source anchor: p.10
- Caption: Figure 3. FVC and EBF information extracted from three image data (“S”, “L”, and “G” represent the remotely sensed
- What it shows: inferred only from caption wording; inspect the PDF image before reuse.
- Why it matters: potentially relevant; requires manual inspection
- Useful for our manuscript: maybe
- Similar figure/table for our paper: manual review first

### Located Figure/Table 11
- Source anchor: p.11
- Caption: Figure 4. Euclidean distance accumulation histogram of five indices for classification of rocky desertification (“S”, “L”, and “G” represent three ty pes of images of Sentinel-2B, Landsat-8, and
- What it shows: inferred only from caption wording; inspect the PDF image before reuse.
- Why it matters: directly relevant to study design/results visualization
- Useful for our manuscript: yes
- Similar figure/table for our paper: consider

### Located Figure/Table 12
- Source anchor: p.11
- Caption: Figure 4. Euclidean distance accumulation histogram of ﬁve indices for classiﬁcation of rocky
- What it shows: inferred only from caption wording; inspect the PDF image before reuse.
- Why it matters: potentially relevant; requires manual inspection
- Useful for our manuscript: maybe
- Similar figure/table for our paper: manual review first

### Located Figure/Table 13
- Source anchor: p.12
- Caption: Figure 5. The importance of factor and its relationship with classification accuracy (“S”, “L”, and “G” represent three types
- What it shows: inferred only from caption wording; inspect the PDF image before reuse.
- Why it matters: directly relevant to study design/results visualization
- Useful for our manuscript: yes
- Similar figure/table for our paper: consider

### Located Figure/Table 14
- Source anchor: p.12
- Caption: Figure 5. The importance of factor and its relationship with classiﬁcation accuracy (“S”, “L”, and “G” represent three types
- What it shows: inferred only from caption wording; inspect the PDF image before reuse.
- Why it matters: directly relevant to study design/results visualization
- Useful for our manuscript: yes
- Similar figure/table for our paper: consider

### Located Figure/Table 15
- Source anchor: p.14
- Caption: Figure 6. Producer’s accuracy (PA) and user’s accuracy (UA) for extraction results of different levels of rocky desertification (“S”, “L”, and “G” represent three types of images of Sentinel-2B, Landsat-8, and Gaofen-6.).
- What it shows: inferred only from caption wording; inspect the PDF image before reuse.
- Why it matters: directly relevant to study design/results visualization
- Useful for our manuscript: yes
- Similar figure/table for our paper: consider

### Located Figure/Table 16
- Source anchor: p.14
- Caption: Figure 6. Producer’s accuracy (PA) and user’s accuracy (UA) for extraction results of different levels of rocky desertiﬁcation
- What it shows: inferred only from caption wording; inspect the PDF image before reuse.
- Why it matters: directly relevant to study design/results visualization
- Useful for our manuscript: yes
- Similar figure/table for our paper: consider

### Located Figure/Table 17
- Source anchor: p.15
- Caption: Figure 7. Extraction results of rocky desertification: (a) rocky desertification results extracted from Sentinel-2B images; (b)
- What it shows: inferred only from caption wording; inspect the PDF image before reuse.
- Why it matters: potentially relevant; requires manual inspection
- Useful for our manuscript: maybe
- Similar figure/table for our paper: manual review first

### Located Figure/Table 18
- Source anchor: p.15
- Caption: Figure 7. Extraction results of rocky desertiﬁcation: (a) rocky desertiﬁcation results extracted from Sentinel-2B images;
- What it shows: inferred only from caption wording; inspect the PDF image before reuse.
- Why it matters: potentially relevant; requires manual inspection
- Useful for our manuscript: maybe
- Similar figure/table for our paper: manual review first

### Located Figure/Table 19
- Source anchor: p.16
- Caption: Figure 8. Comparison of classification results of rocky desertification in field sampling sites: ( a) rocky desertification results extracted from Sentinel-2B images; ( b) rocky desertification results extracted from Landsat-8 images; ( c) rocky desertification results extracte d from Gaofen-6 images; ( d) Google Earth images; ( e) field photographs: ( 1) potential rocky
- What it shows: inferred only from caption wording; inspect the PDF image before reuse.
- Why it matters: directly relevant to study design/results visualization
- Useful for our manuscript: yes
- Similar figure/table for our paper: consider

### Located Figure/Table 20
- Source anchor: p.16
- Caption: Figure 8. Comparison of classiﬁcation results of rocky desertiﬁcation in ﬁeld sampling sites: (a) rocky desertiﬁcation results
- What it shows: inferred only from caption wording; inspect the PDF image before reuse.
- Why it matters: potentially relevant; requires manual inspection
- Useful for our manuscript: maybe
- Similar figure/table for our paper: manual review first


## 10. Results Reading Notes

- Source anchors: p.1, p.2, p.3, p.8, p.9, p.10, p.11, p.12, p.13, p.14, p.15, p.16, ...
- Main experimental results: use only values and claims visible in the excerpts/PDF tables.
- Model comparison results: inspect metric/table captions before using exact rankings.
- Data source comparison results: record only where Sentinel/Landsat/GF/DEM evidence is explicit.
- FBR/bare-rock inversion results: separate continuous metrics from class metrics.
- Classification accuracy: report OA/Kappa/Precision/Recall/F1/IoU/mF1/mIoU only if explicitly found.
- DEM/topographic factor contribution: note only when DEM/topographic excerpts are explicit.
- Spatial distribution / uncertainty / significance: inspect maps and captions manually.

Located result/metric evidence:
- p.1: Academic Editor: Lenio Soares
- p.1: desertiﬁcation information, with an overall accuracy (OA) of 85.21% using the ERT method.
- p.1: (2) The ERT method has the best classiﬁcation results of rocky desertiﬁcation.
- p.1: and free approach to information extraction for mapping rocky desertiﬁcation.
- p.1: manifestation of land degradation in karst areas that results in vegetation deterioration,
- p.2: the wide-ﬁeld-of-view (WFV) sensor data on board the Gaofen-1 and Gaofen-6 satellites
- p.2: have demonstrated the capabilities of mapping ground features, such as vegetation, coastal
- p.2: improve the accuracy of information extraction in uneven and rugged terrains.
- p.2: the results on mapping rocky desertiﬁcation are usually of low accuracy in karst areas when
- p.3: randomly, resulting in a large variance [36].
- p.1: Images: A Comparative Study
- p.1: from Satellite Images: A Comparative
- p.1: Academic Editor: Lenio Soares
- p.1: 3 Department of Geography and the Environment, University of North Texas, Denton, TX 76203, USA;
- p.1: typical karst region (Guangnan County, Yunnan) of southwest China, using three machine-learning
- p.1: algorithms implemented in the Python programming language: random forest (RF), bagged decision


## 11. Discussion Reading Notes

- Source anchors: p.3, p.16
- Mechanism explanations, data-source performance, terrain effects, comparison to previous studies, limitations, and future work should be extracted from these anchors only.
- Borrowable Discussion writing pattern: explain why a data/model/factor improves mapping, then tie the explanation to spatial patterns and validation evidence.

Located discussion/limitation evidence:
- p.1: model is worthy of further exploration and discussion for ground object identiﬁcation.
- p.1: rocky desertiﬁcation; (3) discussing the advantages and limitations of the three open-access
- p.3: rocky desertiﬁcation; (3) discussing the advantages and limitations of the three open-access
- p.17: Some limitations of the study are presented below.
- p.17: usually leads to uncertainty in indexes such as EBF and FVC.
- p.18: might be able to reduce the uncertainty caused by landscape heterogeneity [61].


## 12. Conclusion Reading Notes

- Source anchors: p.18
- Objective summary: inspect Conclusion anchors.
- Method summary: inspect Conclusion anchors.
- Main results: record only exact values visible in Conclusion/Results.
- Contributions/application value: inspect Conclusion anchors.
- Limitations/future work: see limitation evidence above.

## 13. Relevance to Our Remote Sensing Manuscript

- Introduction support: not applicable. Reason: grounded signals were not located in the text layer.
- FBR/LSMM support: high. Reason: grounded signals were located in the text layer.
- ML baseline support: high. Reason: grounded signals were located in the text layer.
- semantic segmentation support: not applicable. Reason: grounded signals were not located in the text layer.
- DEM/topography support: high. Reason: grounded signals were located in the text layer.
- GF/Sentinel/Landsat data comparison support: high. Reason: grounded signals were located in the text layer.
- cross-region transfer support: not applicable. Reason: grounded signals were not located in the text layer.
- accuracy assessment support: high. Reason: grounded signals were located in the text layer.
- Discussion comparison support: high. Reason: grounded signals were located in the text layer.
- limitations support: high. Reason: grounded signals were located in the text layer.
- figure/table design support: high. Reason: grounded signals were located in the text layer.
- terminology support: high. Reason: grounded signals were located in the text layer.
- Remote Sensing writing style support: high. Reason: grounded signals were located in the text layer.

## 14. Reusable Knowledge for Future Skill

### Scientific rules
- Relevant target/method signals: rocky_desertification_classification; unknown.
- Located target evidence pages: p.1, p.1, p.1, p.1, p.2, p.4.
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
