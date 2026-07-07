# Full-Paper Reader: A Rocky Desertification Land Extraction Method Based on Spectral Texture Scattering Terrain Feature Set and Multiscale Segmentation

## 1. Bibliographic Information

- Paper ID: KRD0051
- Title: A Rocky Desertification Land Extraction Method Based on Spectral Texture Scattering Terrain Feature Set and Multiscale Segmentation
- Translated title if applicable: unknown
- Authors: unknown
- Year: 2024
- Journal / Source: IEEE
- DOI: unknown
- URL: https://ieeexplore.ieee.org/document/11023630
- PDF path: `docs/literature/pdfs/package_2000_2026/A_Rocky_Desertification_Land_Extraction_Method_Based_on_Spectral-Texture-Scattering-Terrain_Multisource_Features_With_Time_Series.pdf`
- Language: English
- Readability status: ready
- Metadata status: metadata_incomplete

## 2. Reading Scope and Source Anchors

This reader was generated from the full selectable text layer of the PDF. It preserves page-level anchors and section/figure/table signals. It does not reproduce large original-text passages and does not fabricate missing metadata.

- Abstract: p.1
- Introduction: not located
- Study Area: p.3, p.5, p.9, p.14
- Data: p.1, p.2, p.3, p.4, p.5, p.6, p.7, p.8, p.11, p.13, p.14, p.15, ...
- Methods: p.1, p.2, p.3, p.5, p.6, p.7, p.8, p.9, p.10, p.11, p.12, p.13, ...
- Experiments: p.1, p.4, p.5, p.6, p.9, p.10, p.13
- Results: p.1, p.2, p.3, p.4, p.6, p.7, p.8, p.9, p.10, p.11, p.12, p.13, ...
- Discussion: not located
- Conclusions: not located
- References: p.10, p.15
- Figures/Tables captions: 13 located
  - p.3: Fig. 1. Map of study area.
  - p.4: Fig. 2. Flowchart presenting proposed framework for Roc extraction in the study.
  - p.6: Fig. 3. Schematic of the overall architecture of MDNA-1DCNN.
  - p.7: Fig. 4. Specific architecture of GLFA.
  - p.8: Fig. 5. Specific architecture of MHA.
  - p.8: Fig. 6. Specific architecture of MDACB.
  - p.9: Fig. 7. Recognition result map of Roc in the study area. (a) Map of Roc
  - p.9: Fig. 7 presents the Roc extraction results based on MDNA1DCNN. It is evident that the Roc in Ziyun County is mainly

## 3. Abstract-Level Understanding

Source anchors: p.1

基于可抽取的摘要文本，本研究逻辑可按以下方式理解。以下内容只依据摘要和题录可确认的信息，不补造缺失结论。

- 研究背景: 论文主题与 `deep_learning_segmentation` 相关，关键词信号包括 `DEM_ablation`。
- 研究目标: A Rocky Desertification Land Extraction Method Based on Spectral Texture Scattering Terrain Feature Set and Multiscale Segmentation
- 数据: 见下方 Data Sources 中从全文定位到的证据信号。
- 方法: 见下方 Method Workflow 中从全文定位到的证据信号。
- 主要结果: 仅在 Results Reading Notes 中记录可定位的结果/指标信号；未在此处编造具体数值。
- 意义: 其价值主要体现在对 KRD/FBR/分类/遥感制图/验证框架的支撑，具体等级见第 13 节。

Abstract evidence snippet:

> IEEE TRANSACTIONS ON GEOSCIENCE AND REMOTE SENSING, VOL. 63, 2025 4411616 A Rocky Desertification Land Extraction Method Based on Spectral-Texture-Scattering-Terrain Multisource Features With Time Series Chaokang He , Qinjun Wang , Wentao Xu , Boqi Yuan , and Wenyue Xie Abstract— In karst regions, rocky desertification (RD) represents an extreme form of land degradation, posing significant threats to both the ecological environment and socioeconomic development. Extracting the spatial distribution of rocky desertification land (Roc) is crucial for RD management, resource allocation, and sustainable development. However, current research primarily focuses on RD degree classification, with lack of studies distinguishing Roc from bare soil land (Bar) and other land types, neglecting the dynamic degradation characteristics of Roc in single-temporal data, and facing challenges in effectively integrating high-dimensional nonlinear features with machine learning (ML) methods, leading to confusion between Roc and Bar and inaccurate Roc identification. To address these challenges, this study first constructs a timeseries-based spectral-texture-scattering-terrain (STST) feature set and a

## 4. Introduction Reading Notes

- Source anchors: not located
- Background unfolding: extracted introduction pages should be read around the anchors above; the parser located target/method signals listed below.
- Why the problem matters: only infer from located KRD/desertification/remote-sensing problem statements; do not add unsupported claims.
- Remote sensing role: see satellite/data excerpts in Section 5.
- Existing research categories: classification, FBR/LSMM/MESMA, ML, semantic segmentation, DEM/topography when signaled below.
- Existing research insufficiency / gap / objectives / contributions: inspect Introduction anchors manually for exact wording before using in manuscript.
- Borrowable point for our Introduction: build a clear progression from KRD importance -> remote-sensing monitoring -> method/data limitation -> our FBR/classification/DEM/cross-region contribution.

Located target/method evidence:
- p.1: A Rocky Desertification Land Extraction Method
- p.1: Abstract— In karst regions, rocky desertification (RD) represents an extreme form of land degradation, posing significant
- p.1: rocky desertification (RD) land extraction, time series.
- p.1: issue of rocky desertification (RD) in the southwestern region
- p.1: RD is a special type of land degradation,
- p.1: to thinning soil layers and exposure of the bedrock, which
- p.1: information on rocky desertification land (Roc) can aid in the
- p.2: is a dynamic land degradation process [15].
- p.3: HE et al.: ROCKY DESERTIFICATION LAND EXTRACTION METHOD 4411616
- p.5: HE et al.: ROCKY DESERTIFICATION LAND EXTRACTION METHOD 4411616
- p.1: Multisource Features With Time Series
- p.1: set and applies multiscale segmentation (MS) processing.
- p.1: network (MDNA-1DCNN) is designed for object-oriented classification (OOC) in Ziyun County, Guizhou Province, and Longlin
- p.1: cutting the images into small patches for network input, enabling


## 5. Study Area and Data Sources

- Study area: locate from Study Area anchors: p.3, p.5, p.9, p.14
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
- p.1: Based on Spectral-Texture-Scattering-Terrain
- p.1: To address these challenges, this study first constructs a timeseries-based spectral-texture-scattering-terrain (STST) feature
- p.1: Institute, Chinese Academy of Sciences, Beijing 100094, China, also with
- p.1: and Environment, Yanqi Lake Campus, University of Chinese Academy of
- p.1: Aerospace Information Research Institute, Chinese Academy of Sciences,
- p.1: of Chinese Academy of Sciences, Beijing 101408, China, also with the
- p.1: the self-repairing capacity and stability of the regional ecosystem, increasing the frequency of natural disasters [3].
- p.1: It has demonstrated extensive potential in
- p.2: a NIR-SWIR spectral feature space index based on Landsat 8, while Chen et al.
- p.2: in complex terrains, and interference from clouds and fog,


## 6. Target Variable or Classification System

- Target variable / object: derived from located evidence only.
- KRD/rocky desertification signal: yes
- FBR/fBR/bare-rock fraction signal: yes
- Semantic segmentation class signal: yes
- If FBR/fBR is involved, treat it as a continuous/proportional variable unless the paper explicitly thresholds it into classes.
- If rocky desertification levels are involved, inspect the paper for the exact grade system before reuse.

Target evidence:
- p.1: A Rocky Desertification Land Extraction Method
- p.1: Abstract— In karst regions, rocky desertification (RD) represents an extreme form of land degradation, posing significant
- p.1: rocky desertification (RD) land extraction, time series.
- p.1: issue of rocky desertification (RD) in the southwestern region
- p.1: RD is a special type of land degradation,
- p.1: to thinning soil layers and exposure of the bedrock, which
- p.1: information on rocky desertification land (Roc) can aid in the
- p.2: is a dynamic land degradation process [15].
- p.3: HE et al.: ROCKY DESERTIFICATION LAND EXTRACTION METHOD 4411616
- p.5: HE et al.: ROCKY DESERTIFICATION LAND EXTRACTION METHOD 4411616


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
- cross-region validation: not reported
- ablation design: located
- comparison methods: located

Located method/data evidence:
- p.1: Multisource Features With Time Series
- p.1: set and applies multiscale segmentation (MS) processing.
- p.1: network (MDNA-1DCNN) is designed for object-oriented classification (OOC) in Ziyun County, Guizhou Province, and Longlin
- p.1: cutting the images into small patches for network input, enabling
- p.1: show that MDNA-1DCNN achieves an overall accuracy (OA)
- p.1: outperforming other advanced deep learning (DL) networks and
- p.1: Index Terms— 1-D convolutional neural network (1DCNN),
- p.1: rocky desertification (RD) land extraction, time series.
- p.1: models to differentiate RD surface features.
- p.2: a NIR-SWIR spectral feature space index based on Landsat 8, while Chen et al.
- p.2: [14] constructed a feature space
- p.2: Taking seasonal phenology into account, a timespectrum feature space was constructed using the karst RD
- p.1: Based on Spectral-Texture-Scattering-Terrain
- p.1: To address these challenges, this study first constructs a timeseries-based spectral-texture-scattering-terrain (STST) feature
- p.1: Institute, Chinese Academy of Sciences, Beijing 100094, China, also with
- p.1: and Environment, Yanqi Lake Campus, University of Chinese Academy of
- p.1: Aerospace Information Research Institute, Chinese Academy of Sciences,
- p.1: of Chinese Academy of Sciences, Beijing 101408, China, also with the
- p.1: the self-repairing capacity and stability of the regional ecosystem, increasing the frequency of natural disasters [3].
- p.1: It has demonstrated extensive potential in
- p.2: a NIR-SWIR spectral feature space index based on Landsat 8, while Chen et al.
- p.2: in complex terrains, and interference from clouds and fog,


## 8. Validation Strategy and Metrics

- Reference sample source: locate from excerpts below; manual confirmation recommended.
- Sample size: record only if explicitly visible in source excerpts; otherwise unknown.
- Train/test split: see located split/training evidence; otherwise not reported.
- Spatial split: located only if terms such as spatial/block split appear; otherwise not reported.
- Independent validation: located only if explicit evidence appears; otherwise not reported.
- Cross-region validation: located only if explicit evidence appears; otherwise not reported.

- Continuous-variable metrics located: R2, bias, slope
- Classification metrics located: OA, overall accuracy, Kappa, Precision, F1, IoU, confusion matrix

Metric evidence:
- p.1: Extracting the spatial distribution of rocky
- p.1: Subsequently, by incorporating an improved spatial-channel attention
- p.1: County, Guangxi Province, China.
- p.1: cutting the images into small patches for network input, enabling
- p.1: show that MDNA-1DCNN achieves an overall accuracy (OA)
- p.1: of 97.67% and a Kappa coefficient of 97.07% in multiclass
- p.1: tasks, with F1-score (F1) and Intersection Over Union (IoU)
- p.1: Moreover, the STST feature set, which encompasses
- p.1: multiple attribute features from various perspectives, is more
- p.1: Chaokang He, Wentao Xu, Boqi Yuan, and Wenyue Xie are with the
- p.1: Key Laboratory of Digital Earth Science, Aerospace Information Research
- p.1: Goals, Beijing 100094, China, and also with the College of Resources


Important distinction enforced for our manuscript: continuous FBR inversion metrics (R2/RMSE/MAE/bias/slope) must not be mixed with classification metrics (OA/Kappa/Precision/Recall/F1/IoU/mF1/mIoU).

## 9. Figures and Tables

### Located Figure/Table 1
- Source anchor: p.3
- Caption: Fig. 1. Map of study area.
- What it shows: inferred only from caption wording; inspect the PDF image before reuse.
- Why it matters: directly relevant to study design/results visualization
- Useful for our manuscript: yes
- Similar figure/table for our paper: consider

### Located Figure/Table 2
- Source anchor: p.4
- Caption: Fig. 2. Flowchart presenting proposed framework for Roc extraction in the study.
- What it shows: inferred only from caption wording; inspect the PDF image before reuse.
- Why it matters: potentially relevant; requires manual inspection
- Useful for our manuscript: maybe
- Similar figure/table for our paper: manual review first

### Located Figure/Table 3
- Source anchor: p.6
- Caption: Fig. 3. Schematic of the overall architecture of MDNA-1DCNN.
- What it shows: inferred only from caption wording; inspect the PDF image before reuse.
- Why it matters: potentially relevant; requires manual inspection
- Useful for our manuscript: maybe
- Similar figure/table for our paper: manual review first

### Located Figure/Table 4
- Source anchor: p.7
- Caption: Fig. 4. Specific architecture of GLFA.
- What it shows: inferred only from caption wording; inspect the PDF image before reuse.
- Why it matters: potentially relevant; requires manual inspection
- Useful for our manuscript: maybe
- Similar figure/table for our paper: manual review first

### Located Figure/Table 5
- Source anchor: p.8
- Caption: Fig. 5. Specific architecture of MHA.
- What it shows: inferred only from caption wording; inspect the PDF image before reuse.
- Why it matters: potentially relevant; requires manual inspection
- Useful for our manuscript: maybe
- Similar figure/table for our paper: manual review first

### Located Figure/Table 6
- Source anchor: p.8
- Caption: Fig. 6. Specific architecture of MDACB.
- What it shows: inferred only from caption wording; inspect the PDF image before reuse.
- Why it matters: potentially relevant; requires manual inspection
- Useful for our manuscript: maybe
- Similar figure/table for our paper: manual review first

### Located Figure/Table 7
- Source anchor: p.9
- Caption: Fig. 7. Recognition result map of Roc in the study area. (a) Map of Roc
- What it shows: inferred only from caption wording; inspect the PDF image before reuse.
- Why it matters: directly relevant to study design/results visualization
- Useful for our manuscript: yes
- Similar figure/table for our paper: consider

### Located Figure/Table 8
- Source anchor: p.9
- Caption: Fig. 7 presents the Roc extraction results based on MDNA1DCNN. It is evident that the Roc in Ziyun County is mainly
- What it shows: inferred only from caption wording; inspect the PDF image before reuse.
- Why it matters: potentially relevant; requires manual inspection
- Useful for our manuscript: maybe
- Similar figure/table for our paper: manual review first

### Located Figure/Table 9
- Source anchor: p.10
- Caption: Fig. 8. Heatmap of the confusion matrix of classification probabilities using multiple models in Ziyun. (a) SVM. (b) RF. (c) XGB. (d) LGBM. (e) M-1DCNN.
- What it shows: inferred only from caption wording; inspect the PDF image before reuse.
- Why it matters: directly relevant to study design/results visualization
- Useful for our manuscript: yes
- Similar figure/table for our paper: consider

### Located Figure/Table 10
- Source anchor: p.11
- Caption: Fig. 9. Heatmap of the confusion matrix of classification probabilities using multiple models in Longlin. (a) SVM. (b) RF. (c) XGB. (d) LGBM. (e) M-1DCNN.
- What it shows: inferred only from caption wording; inspect the PDF image before reuse.
- Why it matters: directly relevant to study design/results visualization
- Useful for our manuscript: yes
- Similar figure/table for our paper: consider

### Located Figure/Table 11
- Source anchor: p.12
- Caption: Fig. 10. Detailed comparison map of Roc extraction results under multiple models. (a)–(e) Represent the visualization of the separability between Roc and
- What it shows: inferred only from caption wording; inspect the PDF image before reuse.
- Why it matters: directly relevant to study design/results visualization
- Useful for our manuscript: yes
- Similar figure/table for our paper: consider

### Located Figure/Table 12
- Source anchor: p.13
- Caption: Fig. 11. Heatmap of the confusion matrix for classification using multiple feature combinations. (a) Spe+Tex+Sca. (b) Spe+Tex+Ter. (c) Spe+Sca+Ter.
- What it shows: inferred only from caption wording; inspect the PDF image before reuse.
- Why it matters: directly relevant to study design/results visualization
- Useful for our manuscript: yes
- Similar figure/table for our paper: consider

### Located Figure/Table 13
- Source anchor: p.15
- Caption: Fig. 12. Importance map of different driving factors for RD.
- What it shows: inferred only from caption wording; inspect the PDF image before reuse.
- Why it matters: directly relevant to study design/results visualization
- Useful for our manuscript: yes
- Similar figure/table for our paper: consider


## 10. Results Reading Notes

- Source anchors: p.1, p.2, p.3, p.4, p.6, p.7, p.8, p.9, p.10, p.11, p.12, p.13, ...
- Main experimental results: use only values and claims visible in the excerpts/PDF tables.
- Model comparison results: inspect metric/table captions before using exact rankings.
- Data source comparison results: record only where Sentinel/Landsat/GF/DEM evidence is explicit.
- FBR/bare-rock inversion results: separate continuous metrics from class metrics.
- Classification accuracy: report OA/Kappa/Precision/Recall/F1/IoU/mF1/mIoU only if explicitly found.
- DEM/topographic factor contribution: note only when DEM/topographic excerpts are explicit.
- Spatial distribution / uncertainty / significance: inspect maps and captions manually.

Located result/metric evidence:
- p.1: show that MDNA-1DCNN achieves an overall accuracy (OA)
- p.1: of 97.67% and a Kappa coefficient of 97.07% in multiclass
- p.1: tasks, with F1-score (F1) and Intersection Over Union (IoU)
- p.1: Goals, Beijing 100094, China, and also with the College of Resources
- p.1: Data for Sustainable Development Goals, Beijing 100094, China, also with
- p.1: effective in improving Roc extraction accuracy compared to using
- p.1: has not only resulted in a significant decline in land productivity and biodiversity in the region but also severely weakened
- p.1: Downloaded on July 07,2026 at 07:01:38 UTC from IEEE Xplore.
- p.2: affect decomposition results.
- p.2: effectively improved the classification accuracy of Roc and
- p.1: Extracting the spatial distribution of rocky
- p.1: Subsequently, by incorporating an improved spatial-channel attention
- p.1: County, Guangxi Province, China.
- p.1: cutting the images into small patches for network input, enabling
- p.1: show that MDNA-1DCNN achieves an overall accuracy (OA)
- p.1: of 97.67% and a Kappa coefficient of 97.07% in multiclass


## 11. Discussion Reading Notes

- Source anchors: not located
- Mechanism explanations, data-source performance, terrain effects, comparison to previous studies, limitations, and future work should be extracted from these anchors only.
- Borrowable Discussion writing pattern: explain why a data/model/factor improves mapping, then tie the explanation to spatial patterns and validation evidence.

Located discussion/limitation evidence:
- p.2: However, these methods still face limitations in capturing
- p.11: 68% in Ziyun, with some limitations in distinguishing between
- p.14: Future research could integrate other
- p.14: limitations, and the segmentation quality depends on the
- p.14: Therefore, future work could consider
- p.15: Therefore, in future research, hyperspectral
- p.15: Roc, offering new perspectives and approaches for future
- p.15: In future, considering the complex conditions such
- p.2: However, these methods still face limitations in capturing
- p.11: 68% in Ziyun, with some limitations in distinguishing between
- p.14: limitations, and the segmentation quality depends on the
- p.14: Therefore, future work could consider
- p.15: future work will focus on field surveys and validation


## 12. Conclusion Reading Notes

- Source anchors: not located
- Objective summary: inspect Conclusion anchors.
- Method summary: inspect Conclusion anchors.
- Main results: record only exact values visible in Conclusion/Results.
- Contributions/application value: inspect Conclusion anchors.
- Limitations/future work: see limitation evidence above.

## 13. Relevance to Our Remote Sensing Manuscript

- Introduction support: medium. Reason: grounded signals were located in the text layer.
- FBR/LSMM support: medium. Reason: grounded signals were located in the text layer.
- ML baseline support: medium. Reason: grounded signals were located in the text layer.
- semantic segmentation support: medium. Reason: grounded signals were located in the text layer.
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


## 15. Items Needing Manual Review

- DOI missing in database
- DOI needs manual verification
- metadata incomplete
