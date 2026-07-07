# Full-Paper Reader: Optimization of Rocky Desertification Classification Model Based on Vegetation Type and Seasonal Characteristic

## 1. Bibliographic Information

- Paper ID: KRD0035
- Title: Optimization of Rocky Desertification Classification Model Based on Vegetation Type and Seasonal Characteristic
- Translated title if applicable: unknown
- Authors: Qian C.; Qiang H.; Wang F.; Li M.
- Year: 2021
- Journal / Source: core
- DOI: 10.3390/rs13152935
- URL: https://www.mdpi.com/2072-4292/13/15/2935
- PDF path: `docs/literature/pdfs/package_2021_2026/EN02_Optimization_of_Rocky_Desertification_Classification_Model_Based_on_Vegetation_Type_and_Se.pdf`
- Language: English
- Readability status: ready
- Metadata status: complete

## 2. Reading Scope and Source Anchors

This reader was generated from the full selectable text layer of the PDF. It preserves page-level anchors and section/figure/table signals. It does not reproduce large original-text passages and does not fabricate missing metadata.

- Abstract: p.1
- Introduction: p.1
- Study Area: p.3
- Data: p.1, p.2, p.3, p.4, p.5, p.6, p.7, p.8, p.12, p.13, p.14, p.15, ...
- Methods: p.1, p.2, p.3, p.4, p.5, p.6, p.7, p.8, p.9, p.10, p.11, p.12, ...
- Experiments: p.8, p.15, p.20
- Results: p.1, p.2, p.3, p.9, p.10, p.11, p.12, p.13, p.14, p.15, p.16, p.17, ...
- Discussion: p.17
- Conclusions: p.1, p.20
- References: p.21
- Figures/Tables captions: 25 located
  - p.5: Figure 1. Research area and typical samples.
  - p.5: Figure 1. Research area and typical samples.
  - p.6: Figure 2. Workflow of the processing steps in this study. (RE: rock exposure; FVC: fractional vegetation cover; EL: elevation; AD: albedo; NDBI: normalized difference building index; HD: humidity; ET: evapotranspiration; LSTD: land surface
  - p.6: Figure 2. Workﬂow of the processing steps in this study. (RE: rock exposure; FVC: fractional vegetation cover; EL: elevation;
  - p.7: Figure 3. Cloud recognition. (a) Original image (b) Cloudy identification.
  - p.7: Table 1. Rocky desertification factors.
  - p.7: Figure 3. Cloud recognition. (a) Original image (b) Cloudy identiﬁcation.
  - p.7: Table 1. Rocky desertiﬁcation factors.

## 3. Abstract-Level Understanding

Source anchors: p.1, p.2, p.3

基于可抽取的摘要文本，本研究逻辑可按以下方式理解。以下内容只依据摘要和题录可确认的信息，不补造缺失结论。

- 研究背景: 论文主题与 `machine_learning` 相关，关键词信号包括 `unknown`。
- 研究目标: Optimization of Rocky Desertification Classification Model Based on Vegetation Type and Seasonal Characteristic
- 数据: 见下方 Data Sources 中从全文定位到的证据信号。
- 方法: 见下方 Method Workflow 中从全文定位到的证据信号。
- 主要结果: 仅在 Results Reading Notes 中记录可定位的结果/指标信号；未在此处编造具体数值。
- 意义: 其价值主要体现在对 KRD/FBR/分类/遥感制图/验证框架的支撑，具体等级见第 13 节。

Abstract evidence snippet:

> Building a high-precision, stable, and universal automatic extraction model of the rocky desertiﬁcation information is the premise for exploring the spatiotemporal evolution of rocky desertiﬁcation. Taking Guizhou province as the research area and based on MODIS and continuous forest inventory data in China, we used a machine learning algorithm to build a rocky desertiﬁcation model with bedrock exposure rate, temperature difference, humidity, and other characteristic factors and considered improving the model accuracy from the spatial and temporal dimensions. The results showed the following: (1) The supervised classiﬁcation method was used to build a rocky desertiﬁcation model, and the logical model, RF model, and SVM model were constructed separately. The accuracies of the models were 73.8%, 78.2%, and 80.6%, respectively, and the kappa coefﬁcients were 0.61, 0.672, and 0.707, respectively. SVM performed the best. (2) Vegetation types and vegetation seasonal phases are closely related to rocky desertiﬁcation. After combining them, the model accuracy and kappa coefﬁcient improved to 91.1% and 0.861. (3) The spatial distribution characteristics of rocky desertiﬁcation in Guizhou ar

## 4. Introduction Reading Notes

- Source anchors: p.1
- Background unfolding: extracted introduction pages should be read around the anchors above; the parser located target/method signals listed below.
- Why the problem matters: only infer from located KRD/desertification/remote-sensing problem statements; do not add unsupported claims.
- Remote sensing role: see satellite/data excerpts in Section 5.
- Existing research categories: classification, FBR/LSMM/MESMA, ML, semantic segmentation, DEM/topography when signaled below.
- Existing research insufficiency / gap / objectives / contributions: inspect Introduction anchors manually for exact wording before using in manuscript.
- Borrowable point for our Introduction: build a clear progression from KRD importance -> remote-sensing monitoring -> method/data limitation -> our FBR/classification/DEM/cross-region contribution.

Located target/method evidence:
- p.1: model with bedrock exposure rate, temperature difference, humidity, and other characteristic factors
- p.1: It is a process of land degradation under the background of fragile karst geology and a humid or semihumid climate in
- p.2: used to improve the bedrock exposure index of a system to determine the types and spatial
- p.3: method for weight analysis and accumulation to enable quantitative remote sensing monitoring of rocky desertiﬁcation by extracting the vegetation coverage, bedrock bare rate,
- p.4: Eventually, it causes severe soil erosion, large areas of exposed bedrock,
- p.4: The phenomena of land degradation and soil disappearance of
- p.5: (b) No rocky desertification.
- p.5: ( c) Potential rocky desertification.
- p.5: ( d) Light rocky desertification.
- p.5: (e) Middle rocky desertification.
- p.1: 2 School of Smart Agricultural, Suzhou Polytechnic Institute of Agriculture, Suzhou 215008, China;
- p.1: showed the following: (1) The supervised classiﬁcation method was used to build a rocky desertiﬁcation model, and the logical model, RF model, and SVM model were constructed separately.
- p.1: desertiﬁcation, and the SVM model has the highest rocky desertiﬁcation classiﬁcation accuracy.
- p.2: [ 19] used Landsat 8 to construct a feature space model of albedo and


## 5. Study Area and Data Sources

- Study area: locate from Study Area anchors: p.3
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
- p.1: Academic Editors: Maria Lanfredi,
- p.1: Taking Guizhou province as the research area and based on MODIS and continuous
- p.1: Keywords: rocky desertiﬁcation; supervised classiﬁcation method; MODIS data; feature extraction;
- p.1: The karst area in Southwest China is located in the center of the karst area in Eastern
- p.2: [ 19] used Landsat 8 to construct a feature space model of albedo and
- p.2: karst mountain area using Landsat 8 and discussed the relationship between LST and the
- p.2: primarily associated with the land use, gravel content, and slope gradient in a typical
- p.2: coefﬁcient between the KRD index and slope in the karst area, especially where the slope
- p.2: between the rocky desertiﬁcation grade and the factor set of the samples to ﬁnd the most
- p.2: [27] established the calculation model of vegetation coverage in Guangxi with MODIS


## 6. Target Variable or Classification System

- Target variable / object: derived from located evidence only.
- KRD/rocky desertification signal: yes
- FBR/fBR/bare-rock fraction signal: yes
- Semantic segmentation class signal: no
- If FBR/fBR is involved, treat it as a continuous/proportional variable unless the paper explicitly thresholds it into classes.
- If rocky desertification levels are involved, inspect the paper for the exact grade system before reuse.

Target evidence:
- p.1: model with bedrock exposure rate, temperature difference, humidity, and other characteristic factors
- p.1: It is a process of land degradation under the background of fragile karst geology and a humid or semihumid climate in
- p.2: used to improve the bedrock exposure index of a system to determine the types and spatial
- p.3: method for weight analysis and accumulation to enable quantitative remote sensing monitoring of rocky desertiﬁcation by extracting the vegetation coverage, bedrock bare rate,
- p.4: Eventually, it causes severe soil erosion, large areas of exposed bedrock,
- p.4: The phenomena of land degradation and soil disappearance of
- p.5: (b) No rocky desertification.
- p.5: ( c) Potential rocky desertification.
- p.5: ( d) Light rocky desertification.
- p.5: (e) Middle rocky desertification.


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
- p.1: 2 School of Smart Agricultural, Suzhou Polytechnic Institute of Agriculture, Suzhou 215008, China;
- p.1: showed the following: (1) The supervised classiﬁcation method was used to build a rocky desertiﬁcation model, and the logical model, RF model, and SVM model were constructed separately.
- p.1: desertiﬁcation, and the SVM model has the highest rocky desertiﬁcation classiﬁcation accuracy.
- p.2: [ 19] used Landsat 8 to construct a feature space model of albedo and
- p.2: NDVI, MSAVI, and TGSI and compared their extraction accuracies.
- p.2: indicated that the three feature space models are feasible for extracting desertiﬁcation
- p.2: between evapotranspiration index and NDVI and the evapotranspiration index can reﬂect
- p.2: [22] retrieved the land surface temperature (LST) of a
- p.2: LUCC and NDVI of different land use types.
- p.2: of NDVI and LST showed an opposite pattern.
- p.2: relationship between the NDVI value and vegetation coverage in Guangxi using a binary
- p.2: analysis (SMA) methods to improve the accuracy of rocky desertiﬁcation estimation in
- p.1: Academic Editors: Maria Lanfredi,
- p.1: Taking Guizhou province as the research area and based on MODIS and continuous
- p.1: Keywords: rocky desertiﬁcation; supervised classiﬁcation method; MODIS data; feature extraction;
- p.1: The karst area in Southwest China is located in the center of the karst area in Eastern
- p.2: [ 19] used Landsat 8 to construct a feature space model of albedo and
- p.2: karst mountain area using Landsat 8 and discussed the relationship between LST and the
- p.2: primarily associated with the land use, gravel content, and slope gradient in a typical
- p.2: coefﬁcient between the KRD index and slope in the karst area, especially where the slope
- p.2: between the rocky desertiﬁcation grade and the factor set of the samples to ﬁnd the most
- p.2: [27] established the calculation model of vegetation coverage in Guangxi with MODIS


## 8. Validation Strategy and Metrics

- Reference sample source: locate from excerpts below; manual confirmation recommended.
- Sample size: record only if explicitly visible in source excerpts; otherwise unknown.
- Train/test split: see located split/training evidence; otherwise not reported.
- Spatial split: located only if terms such as spatial/block split appear; otherwise not reported.
- Independent validation: located only if explicit evidence appears; otherwise not reported.
- Cross-region validation: located only if explicit evidence appears; otherwise not reported.

- Continuous-variable metrics located: slope
- Classification metrics located: OA, overall accuracy, Kappa, Precision, IoU, confusion matrix

Metric evidence:
- p.1: Abstract: Building a high-precision, stable, and universal automatic extraction model of the rocky
- p.1: desertiﬁcation information is the premise for exploring the spatiotemporal evolution of rocky desertiﬁcation.
- p.1: and considered improving the model accuracy from the spatial and temporal dimensions.
- p.1: showed the following: (1) The supervised classiﬁcation method was used to build a rocky desertiﬁcation model, and the logical model, RF model, and SVM model were constructed separately.
- p.1: accuracies of the models were 73.8%, 78.2%, and 80.6%, respectively, and the kappa coefﬁcients were
- p.1: After combining them, the model accuracy
- p.1: and kappa coefﬁcient improved to 91.1% and 0.861.
- p.1: (3) The spatial distribution characteristics of
- p.1: rocky desertiﬁcation in Guizhou are obvious, showing a pattern of being heavy in the west, light in
- p.1: In conclusion, combining the vertical spatial structure of vegetation and the
- p.1: differences in seasonal phase is an effective method to improve the modeling accuracy of rocky
- p.1: desertiﬁcation, and the SVM model has the highest rocky desertiﬁcation classiﬁcation accuracy.


Important distinction enforced for our manuscript: continuous FBR inversion metrics (R2/RMSE/MAE/bias/slope) must not be mixed with classification metrics (OA/Kappa/Precision/Recall/F1/IoU/mF1/mIoU).

## 9. Figures and Tables

### Located Figure/Table 1
- Source anchor: p.5
- Caption: Figure 1. Research area and typical samples.
- What it shows: inferred only from caption wording; inspect the PDF image before reuse.
- Why it matters: potentially relevant; requires manual inspection
- Useful for our manuscript: maybe
- Similar figure/table for our paper: manual review first

### Located Figure/Table 2
- Source anchor: p.5
- Caption: Figure 1. Research area and typical samples.
- What it shows: inferred only from caption wording; inspect the PDF image before reuse.
- Why it matters: potentially relevant; requires manual inspection
- Useful for our manuscript: maybe
- Similar figure/table for our paper: manual review first

### Located Figure/Table 3
- Source anchor: p.6
- Caption: Figure 2. Workflow of the processing steps in this study. (RE: rock exposure; FVC: fractional vegetation cover; EL: elevation; AD: albedo; NDBI: normalized difference building index; HD: humidity; ET: evapotranspiration; LSTD: land surface
- What it shows: inferred only from caption wording; inspect the PDF image before reuse.
- Why it matters: directly relevant to study design/results visualization
- Useful for our manuscript: yes
- Similar figure/table for our paper: consider

### Located Figure/Table 4
- Source anchor: p.6
- Caption: Figure 2. Workﬂow of the processing steps in this study. (RE: rock exposure; FVC: fractional vegetation cover; EL: elevation;
- What it shows: inferred only from caption wording; inspect the PDF image before reuse.
- Why it matters: potentially relevant; requires manual inspection
- Useful for our manuscript: maybe
- Similar figure/table for our paper: manual review first

### Located Figure/Table 5
- Source anchor: p.7
- Caption: Figure 3. Cloud recognition. (a) Original image (b) Cloudy identification.
- What it shows: inferred only from caption wording; inspect the PDF image before reuse.
- Why it matters: potentially relevant; requires manual inspection
- Useful for our manuscript: maybe
- Similar figure/table for our paper: manual review first

### Located Figure/Table 6
- Source anchor: p.7
- Caption: Table 1. Rocky desertification factors.
- What it shows: inferred only from caption wording; inspect the PDF image before reuse.
- Why it matters: potentially relevant; requires manual inspection
- Useful for our manuscript: maybe
- Similar figure/table for our paper: manual review first

### Located Figure/Table 7
- Source anchor: p.7
- Caption: Figure 3. Cloud recognition. (a) Original image (b) Cloudy identiﬁcation.
- What it shows: inferred only from caption wording; inspect the PDF image before reuse.
- Why it matters: potentially relevant; requires manual inspection
- Useful for our manuscript: maybe
- Similar figure/table for our paper: manual review first

### Located Figure/Table 8
- Source anchor: p.7
- Caption: Table 1. Rocky desertiﬁcation factors.
- What it shows: inferred only from caption wording; inspect the PDF image before reuse.
- Why it matters: potentially relevant; requires manual inspection
- Useful for our manuscript: maybe
- Similar figure/table for our paper: manual review first

### Located Figure/Table 9
- Source anchor: p.11
- Caption: Figure 4. FVC index. (a) Maximum value combination. (b) Mean value combination. (c) Minimum value combination.
- What it shows: inferred only from caption wording; inspect the PDF image before reuse.
- Why it matters: potentially relevant; requires manual inspection
- Useful for our manuscript: maybe
- Similar figure/table for our paper: manual review first

### Located Figure/Table 10
- Source anchor: p.11
- Caption: Figure 5. The standard deviation of the RE index images based on the three synthesis
- What it shows: inferred only from caption wording; inspect the PDF image before reuse.
- Why it matters: potentially relevant; requires manual inspection
- Useful for our manuscript: maybe
- Similar figure/table for our paper: manual review first

### Located Figure/Table 11
- Source anchor: p.11
- Caption: Figure 5. RE index. (a) Maximum value combination. (b) Mean value combination. (c) Minimum value combination.
- What it shows: inferred only from caption wording; inspect the PDF image before reuse.
- Why it matters: potentially relevant; requires manual inspection
- Useful for our manuscript: maybe
- Similar figure/table for our paper: manual review first

### Located Figure/Table 12
- Source anchor: p.11
- Caption: Figure 4. FVC index. (a) Maximum value combination. (b) Mean value combination. (c) Minimum value combination.
- What it shows: inferred only from caption wording; inspect the PDF image before reuse.
- Why it matters: potentially relevant; requires manual inspection
- Useful for our manuscript: maybe
- Similar figure/table for our paper: manual review first

### Located Figure/Table 13
- Source anchor: p.11
- Caption: Figure 4. FVC index. (a) Maximum value combination. (b) Mean value combination. (c) Minimum value combination.
- What it shows: inferred only from caption wording; inspect the PDF image before reuse.
- Why it matters: potentially relevant; requires manual inspection
- Useful for our manuscript: maybe
- Similar figure/table for our paper: manual review first

### Located Figure/Table 14
- Source anchor: p.11
- Caption: Figure 5. The standard deviation of the RE index images based on the three synthesis
- What it shows: inferred only from caption wording; inspect the PDF image before reuse.
- Why it matters: potentially relevant; requires manual inspection
- Useful for our manuscript: maybe
- Similar figure/table for our paper: manual review first

### Located Figure/Table 15
- Source anchor: p.11
- Caption: Figure 5. RE index. (a) Maximum value combination. (b) Mean value combination. (c) Minimum value combination.
- What it shows: inferred only from caption wording; inspect the PDF image before reuse.
- Why it matters: potentially relevant; requires manual inspection
- Useful for our manuscript: maybe
- Similar figure/table for our paper: manual review first

### Located Figure/Table 16
- Source anchor: p.11
- Caption: Figure 5. RE index. (a) Maximum value combination. (b) Mean value combination. (c) Minimum value combination.
- What it shows: inferred only from caption wording; inspect the PDF image before reuse.
- Why it matters: potentially relevant; requires manual inspection
- Useful for our manuscript: maybe
- Similar figure/table for our paper: manual review first

### Located Figure/Table 17
- Source anchor: p.11
- Caption: Figure 6. Other KRD factors. (a) LSTD. (b) ET. (c) AD. (d) HD. (e) NDBI. (f) EL.
- What it shows: inferred only from caption wording; inspect the PDF image before reuse.
- Why it matters: potentially relevant; requires manual inspection
- Useful for our manuscript: maybe
- Similar figure/table for our paper: manual review first

### Located Figure/Table 18
- Source anchor: p.11
- Caption: Figure 7. Factor correlation. (a) Correlation coefficient. (b) p-value.
- What it shows: inferred only from caption wording; inspect the PDF image before reuse.
- Why it matters: potentially relevant; requires manual inspection
- Useful for our manuscript: maybe
- Similar figure/table for our paper: manual review first

### Located Figure/Table 19
- Source anchor: p.11
- Caption: Figure 6. Other KRD factors. (a) LSTD. (b) ET. (c) AD. (d) HD. (e) NDBI. (f) EL.
- What it shows: inferred only from caption wording; inspect the PDF image before reuse.
- Why it matters: potentially relevant; requires manual inspection
- Useful for our manuscript: maybe
- Similar figure/table for our paper: manual review first

### Located Figure/Table 20
- Source anchor: p.12
- Caption: Figure 6. Other KRD factors. (a) LSTD. (b) ET. (c) AD. (d) HD. (e) NDBI. (f) EL.
- What it shows: inferred only from caption wording; inspect the PDF image before reuse.
- Why it matters: potentially relevant; requires manual inspection
- Useful for our manuscript: maybe
- Similar figure/table for our paper: manual review first

### Located Figure/Table 21
- Source anchor: p.12
- Caption: Figure 7. Factor correlation. (a) Correlation coefficient. (b) p-value.
- What it shows: inferred only from caption wording; inspect the PDF image before reuse.
- Why it matters: potentially relevant; requires manual inspection
- Useful for our manuscript: maybe
- Similar figure/table for our paper: manual review first

### Located Figure/Table 22
- Source anchor: p.12
- Caption: Figure 7. Factor correlation. (a) Correlation coefﬁcient. (b) p-value.
- What it shows: inferred only from caption wording; inspect the PDF image before reuse.
- Why it matters: potentially relevant; requires manual inspection
- Useful for our manuscript: maybe
- Similar figure/table for our paper: manual review first

### Located Figure/Table 23
- Source anchor: p.13
- Caption: Table 2. Rocky desertiﬁcation model comparation.
- What it shows: inferred only from caption wording; inspect the PDF image before reuse.
- Why it matters: potentially relevant; requires manual inspection
- Useful for our manuscript: maybe
- Similar figure/table for our paper: manual review first

### Located Figure/Table 24
- Source anchor: p.13
- Caption: Table 3. Rocky desertiﬁcation classiﬁcation accuracy comparation.
- What it shows: inferred only from caption wording; inspect the PDF image before reuse.
- Why it matters: directly relevant to study design/results visualization
- Useful for our manuscript: yes
- Similar figure/table for our paper: consider

### Located Figure/Table 25
- Source anchor: p.13
- Caption: Table 3. Rocky desertification classification accuracy comparation.
- What it shows: inferred only from caption wording; inspect the PDF image before reuse.
- Why it matters: directly relevant to study design/results visualization
- Useful for our manuscript: yes
- Similar figure/table for our paper: consider


## 10. Results Reading Notes

- Source anchors: p.1, p.2, p.3, p.9, p.10, p.11, p.12, p.13, p.14, p.15, p.16, p.17, ...
- Main experimental results: use only values and claims visible in the excerpts/PDF tables.
- Model comparison results: inspect metric/table captions before using exact rankings.
- Data source comparison results: record only where Sentinel/Landsat/GF/DEM evidence is explicit.
- FBR/bare-rock inversion results: separate continuous metrics from class metrics.
- Classification accuracy: report OA/Kappa/Precision/Recall/F1/IoU/mF1/mIoU only if explicitly found.
- DEM/topographic factor contribution: note only when DEM/topographic excerpts are explicit.
- Spatial distribution / uncertainty / significance: inspect maps and captions manually.

Located result/metric evidence:
- p.1: and considered improving the model accuracy from the spatial and temporal dimensions.
- p.1: accuracies of the models were 73.8%, 78.2%, and 80.6%, respectively, and the kappa coefﬁcients were
- p.1: After combining them, the model accuracy
- p.1: and kappa coefﬁcient improved to 91.1% and 0.861.
- p.1: differences in seasonal phase is an effective method to improve the modeling accuracy of rocky
- p.1: desertiﬁcation, and the SVM model has the highest rocky desertiﬁcation classiﬁcation accuracy.
- p.1: research results provide data support for exploring the spatiotemporal evolution pattern of rocky
- p.1: occur, land productivity decreases, and soil erosion is severe, resulting in large exposed
- p.2: that the overall classiﬁcation accuracy of the three models was more than 80%, which
- p.2: The results showed that there were significant differences in the LST of different land use types, with the highest being recorded
- p.1: Abstract: Building a high-precision, stable, and universal automatic extraction model of the rocky
- p.1: desertiﬁcation information is the premise for exploring the spatiotemporal evolution of rocky desertiﬁcation.
- p.1: and considered improving the model accuracy from the spatial and temporal dimensions.
- p.1: showed the following: (1) The supervised classiﬁcation method was used to build a rocky desertiﬁcation model, and the logical model, RF model, and SVM model were constructed separately.
- p.1: accuracies of the models were 73.8%, 78.2%, and 80.6%, respectively, and the kappa coefﬁcients were
- p.1: After combining them, the model accuracy


## 11. Discussion Reading Notes

- Source anchors: p.17
- Mechanism explanations, data-source performance, terrain effects, comparison to previous studies, limitations, and future work should be extracted from these anchors only.
- Borrowable Discussion writing pattern: explain why a data/model/factor improves mapping, then tie the explanation to spatial patterns and validation evidence.

Located discussion/limitation evidence:
- not located


## 12. Conclusion Reading Notes

- Source anchors: p.1, p.20
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
- cross-region transfer support: high. Reason: grounded signals were located in the text layer.
- accuracy assessment support: high. Reason: grounded signals were located in the text layer.
- Discussion comparison support: not applicable. Reason: grounded signals were not located in the text layer.
- limitations support: not applicable. Reason: grounded signals were not located in the text layer.
- figure/table design support: high. Reason: grounded signals were located in the text layer.
- terminology support: high. Reason: grounded signals were located in the text layer.
- Remote Sensing writing style support: not applicable. Reason: grounded signals were not located in the text layer.

## 14. Reusable Knowledge for Future Skill

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


## 15. Items Needing Manual Review

- none
