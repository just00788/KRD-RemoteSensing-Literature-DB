# Full-Paper Reader: EN003 Machine learning algorithm for estimating karst rocky desert

## 1. Bibliographic Information

- Paper ID: KRD0091
- Title: EN003 Machine learning algorithm for estimating karst rocky desert
- Translated title if applicable: unknown
- Authors: unknown
- Year: unknown
- Journal / Source: unknown
- DOI: unknown
- URL: unknown
- PDF path: `docs/literature/pdfs/package_2000_2026/EN003_Machine_learning_algorithm_for_estimating_karst_rocky_desert.pdf`
- Language: unknown
- Readability status: usable_with_caution
- Metadata status: metadata_incomplete

## 2. Reading Scope and Source Anchors

This reader was generated from the full selectable text layer of the PDF. It preserves page-level anchors and section/figure/table signals. It does not reproduce large original-text passages and does not fabricate missing metadata.

- Abstract: not located
- Introduction: p.15
- Study Area: p.1, p.2, p.4, p.7, p.8, p.9, p.10, p.11
- Data: p.1, p.2, p.3, p.7, p.8, p.9, p.10, p.11, p.12, p.14, p.15, p.16
- Methods: p.1, p.2, p.3, p.7, p.8, p.9, p.10, p.11, p.12, p.14, p.15
- Experiments: p.8, p.9, p.15
- Results: p.1, p.2, p.3, p.4, p.5, p.7, p.8, p.10, p.12
- Discussion: p.7
- Conclusions: p.8
- References: p.10, p.14
- Figures/Tables captions: 15 located
  - p.3: Table 1. MIC and correlation coefficients on the factors influencing of KRD. RE rock exposure, FVC
  - p.3: Figure 1. Feature factors of KRD in 2020 selected based on MIC. Abbreviations: NKRD—No karst rocky
  - p.4: Figure 2. Feature factors of KRD selected based on correlation coefficient. *Significant correlation at the 0.05
  - p.5: Figure 3. Feature factors of KRD in 2020 selected based on MIC and R in the peak-cluster depression basin in
  - p.5: Table 2. Accuracy of the RF , including the kappa, OA, UA, and PA.
  - p.5: Figure 4. The importance of feature factors of KRD in the peak-cluster depression basin in southwest Guangxi,
  - p.6: Figure 5. Spatial distribution of the karst rocky desertification. Maps were generated using QGIS 3.26.2
  - p.7: Table 3. Change in the karst rocky desertification areas of different levels.

## 3. Abstract-Level Understanding

Source anchors: p.1

基于可抽取的摘要文本，本研究逻辑可按以下方式理解。以下内容只依据摘要和题录可确认的信息，不补造缺失结论。

- 研究背景: 论文主题与 `machine_learning` 相关，关键词信号包括 `unknown`。
- 研究目标: EN003 Machine learning algorithm for estimating karst rocky desert
- 数据: 见下方 Data Sources 中从全文定位到的证据信号。
- 方法: 见下方 Method Workflow 中从全文定位到的证据信号。
- 主要结果: 仅在 Results Reading Notes 中记录可定位的结果/指标信号；未在此处编造具体数值。
- 意义: 其价值主要体现在对 KRD/FBR/分类/遥感制图/验证框架的支撑，具体等级见第 13 节。

Abstract evidence snippet:

> 1 Vol.:(0123456789)Scientific Reports | (2022) 12:19121 | https://doi.org/10.1038/s41598-022-21684-5 www.nature.com/scientificreports Machine learning algorithm for estimating karst rocky desertification in a peak‑cluster depression basin in southwest Guangxi, China Yali Zhang1, Yichao Tian1,2*, Ying Li3, Donghua Wang4, Jin Tao1, Yongwei Yang1, Junliang Lin1, Qiang Zhang1 & Luhua Wu5 Karst rocky desertification (KRD) has become one of the most serious ecological and environmental problems in karst areas. At present, mapping KRD with a high accuracy and on a large scale is still a difficult problem in the control of KRD. In this study, a random forest (RF) based on maximum information coefficient and correlation coefficient feature selection is proposed to predict KRD. Nine predictors stood out as feature factors to estimate KRD. Rock exposure was the most important predictor, followed by fractional vegetation cover for the prediction of KRD processes. The kappa and classification accuracy indexes were to evaluate the performance of the model. We recorded overall accuracy rate and kappa index values of 94.7% and 0.92 for the testing datasets respectively. The RF model w

## 4. Introduction Reading Notes

- Source anchors: p.15
- Background unfolding: extracted introduction pages should be read around the anchors above; the parser located target/method signals listed below.
- Why the problem matters: only infer from located KRD/desertification/remote-sensing problem statements; do not add unsupported claims.
- Remote sensing role: see satellite/data excerpts in Section 5.
- Existing research categories: classification, FBR/LSMM/MESMA, ML, semantic segmentation, DEM/topography when signaled below.
- Existing research insufficiency / gap / objectives / contributions: inspect Introduction anchors manually for exact wording before using in manuscript.
- Borrowable point for our Introduction: build a clear progression from KRD importance -> remote-sensing monitoring -> method/data limitation -> our FBR/classification/DEM/cross-region contribution.

Located target/method evidence:
- p.1: Karst rocky desertification (KRD) has become one of the most serious ecological and environmental
- p.1: predictor, followed by fractional vegetation cover for the prediction of KRD processes.
- p.1: Karst rocky desertification, similar to desertification, is a landscape characterized by a large area of exposed bedrock due to vegetation destruction and soil erosion in karst areas1,2.
- p.1: It is not only a process of land degradation but
- p.1: also the result of land degradation.
- p.1: Typically, karst rocky desertification areas are characterized by thin surface
- p.1: The ecological environmental security problems caused by karst rocky desertification
- p.1: advancement of remote sensing techniques, karst rocky desertification assessment based on remote sensing
- p.1: the degree of karst rocky desertification by setting the brightness temperature threshold in Pingguo County,
- p.1: the abundances of vegetation and exposed rock were extracted to monitor and evaluate the karst rocky desertification using the retrieved annual vegetation coverage from medium-resolution Moderate Resolution Imaging
- p.1: In this study, a random forest (RF) based on maximum
- p.1: classification accuracy indexes were to evaluate the performance of the model.
- p.1: remote sensing data combined with the RF model can obtain better prediction results of KRD, thereby
- p.1: Typically, karst rocky desertification areas are characterized by thin surface


## 5. Study Area and Data Sources

- Study area: locate from Study Area anchors: p.1, p.2, p.4, p.7, p.8, p.9, p.10, p.11
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
- p.1: intensive interest in the field of global environmental change8.
- p.1: using a multispectral remote sensing Landsat 8 image to calculate the brightness temperature and determining
- p.1: Spectroradiometer (MODIS) data.
- p.1: GF-1 wide field of view (WFV) satellite data for the Nandong underground river basin.
- p.2: it demands considerable professional knowledge and is always time-consuming, which strongly hinders its efficiency.
- p.2: When the vegetation fraction, bedrock exposure, and slope factor were added to the
- p.2: However, high-quality expert-annotated samples
- p.2: to a certain extent, avoids the subjectivity of the artificial selection of samples, but has difficulty distinguishing
- p.2: have been extensively used in the fields of hydrology, meteorology, and ecology, and they have also provided a
- p.2: vegetation coverage, rock exposure rate, and slope are usually used as grading factors for the degree of karst


## 6. Target Variable or Classification System

- Target variable / object: derived from located evidence only.
- KRD/rocky desertification signal: yes
- FBR/fBR/bare-rock fraction signal: yes
- Semantic segmentation class signal: no
- If FBR/fBR is involved, treat it as a continuous/proportional variable unless the paper explicitly thresholds it into classes.
- If rocky desertification levels are involved, inspect the paper for the exact grade system before reuse.

Target evidence:
- p.1: Karst rocky desertification (KRD) has become one of the most serious ecological and environmental
- p.1: predictor, followed by fractional vegetation cover for the prediction of KRD processes.
- p.1: Karst rocky desertification, similar to desertification, is a landscape characterized by a large area of exposed bedrock due to vegetation destruction and soil erosion in karst areas1,2.
- p.1: It is not only a process of land degradation but
- p.1: also the result of land degradation.
- p.1: Typically, karst rocky desertification areas are characterized by thin surface
- p.1: The ecological environmental security problems caused by karst rocky desertification
- p.1: advancement of remote sensing techniques, karst rocky desertification assessment based on remote sensing
- p.1: the degree of karst rocky desertification by setting the brightness temperature threshold in Pingguo County,
- p.1: the abundances of vegetation and exposed rock were extracted to monitor and evaluate the karst rocky desertification using the retrieved annual vegetation coverage from medium-resolution Moderate Resolution Imaging


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
- p.1: In this study, a random forest (RF) based on maximum
- p.1: classification accuracy indexes were to evaluate the performance of the model.
- p.1: remote sensing data combined with the RF model can obtain better prediction results of KRD, thereby
- p.1: Typically, karst rocky desertification areas are characterized by thin surface
- p.2: Therefore, it can only be used for the assessment of the degree of karst rocky desertification on a small
- p.2: vegetation index (NDVI) data participation decision classification to classify the KRD, which effectively avoided
- p.2: Qi et al.22 assessed the feasibility of using the dimidiate pixel model (DPM) and spectral mixture analysis (SMA)
- p.2: Alternatively, a combination of spectral analysis and the vegetation index can
- p.2: between types of ground objects with small spectral characteristic differences.
- p.2: era, machine learning methods such as support vector machines, random forest models, and neural networks
- p.3: the RF models is presented in Table 2, which indicates that the overall accuracy rate of the random forest model
- p.3: So, the random forest model is more reliable in mapping the karst
- p.1: intensive interest in the field of global environmental change8.
- p.1: using a multispectral remote sensing Landsat 8 image to calculate the brightness temperature and determining
- p.1: Spectroradiometer (MODIS) data.
- p.1: GF-1 wide field of view (WFV) satellite data for the Nandong underground river basin.
- p.2: it demands considerable professional knowledge and is always time-consuming, which strongly hinders its efficiency.
- p.2: When the vegetation fraction, bedrock exposure, and slope factor were added to the
- p.2: However, high-quality expert-annotated samples
- p.2: to a certain extent, avoids the subjectivity of the artificial selection of samples, but has difficulty distinguishing
- p.2: have been extensively used in the fields of hydrology, meteorology, and ecology, and they have also provided a
- p.2: vegetation coverage, rock exposure rate, and slope are usually used as grading factors for the degree of karst


## 8. Validation Strategy and Metrics

- Reference sample source: locate from excerpts below; manual confirmation recommended.
- Sample size: record only if explicitly visible in source excerpts; otherwise unknown.
- Train/test split: see located split/training evidence; otherwise not reported.
- Spatial split: located only if terms such as spatial/block split appear; otherwise not reported.
- Independent validation: located only if explicit evidence appears; otherwise not reported.
- Cross-region validation: located only if explicit evidence appears; otherwise not reported.

- Continuous-variable metrics located: slope
- Classification metrics located: OA, overall accuracy, Kappa, Precision, IoU

Metric evidence:
- p.1: Yali Zhang1, Yichao Tian1,2*, Ying Li3, Donghua Wang4, Jin Tao1, Yongwei Yang1,
- p.1: Junliang Lin1, Qiang Zhang1 & Luhua Wu5
- p.1: Karst rocky desertification (KRD) has become one of the most serious ecological and environmental
- p.1: At present, mapping KRD with a high accuracy and on a large scale is still
- p.1: classification accuracy indexes were to evaluate the performance of the model.
- p.1: accuracy rate and kappa index values of 94.7% and 0.92 for the testing datasets respectively.
- p.1: have seriously affected people’s living environment and sustainable development7, and thus, KRD has drawn
- p.1: the abundances of vegetation and exposed rock were extracted to monitor and evaluate the karst rocky desertification using the retrieved annual vegetation coverage from medium-resolution Moderate Resolution Imaging
- p.1: The information on karst rocky desertification was extracted using high spatial resolution
- p.2: relied on visual interpretation or human–computer interactive interpretation 18.
- p.2: Huang and Cai19, in which the human–computer interaction interpretation method was used to interpret remote
- p.2: sensing images acquired in 1974, 1993, and 2001, and then, the spatial pattern and changes in the karst rocky


Important distinction enforced for our manuscript: continuous FBR inversion metrics (R2/RMSE/MAE/bias/slope) must not be mixed with classification metrics (OA/Kappa/Precision/Recall/F1/IoU/mF1/mIoU).

## 9. Figures and Tables

### Located Figure/Table 1
- Source anchor: p.3
- Caption: Table 1. MIC and correlation coefficients on the factors influencing of KRD. RE rock exposure, FVC
- What it shows: inferred only from caption wording; inspect the PDF image before reuse.
- Why it matters: potentially relevant; requires manual inspection
- Useful for our manuscript: maybe
- Similar figure/table for our paper: manual review first

### Located Figure/Table 2
- Source anchor: p.3
- Caption: Figure 1. Feature factors of KRD in 2020 selected based on MIC. Abbreviations: NKRD—No karst rocky
- What it shows: inferred only from caption wording; inspect the PDF image before reuse.
- Why it matters: directly relevant to study design/results visualization
- Useful for our manuscript: yes
- Similar figure/table for our paper: consider

### Located Figure/Table 3
- Source anchor: p.4
- Caption: Figure 2. Feature factors of KRD selected based on correlation coefficient. *Significant correlation at the 0.05
- What it shows: inferred only from caption wording; inspect the PDF image before reuse.
- Why it matters: directly relevant to study design/results visualization
- Useful for our manuscript: yes
- Similar figure/table for our paper: consider

### Located Figure/Table 4
- Source anchor: p.5
- Caption: Figure 3. Feature factors of KRD in 2020 selected based on MIC and R in the peak-cluster depression basin in
- What it shows: inferred only from caption wording; inspect the PDF image before reuse.
- Why it matters: directly relevant to study design/results visualization
- Useful for our manuscript: yes
- Similar figure/table for our paper: consider

### Located Figure/Table 5
- Source anchor: p.5
- Caption: Table 2. Accuracy of the RF , including the kappa, OA, UA, and PA.
- What it shows: inferred only from caption wording; inspect the PDF image before reuse.
- Why it matters: directly relevant to study design/results visualization
- Useful for our manuscript: yes
- Similar figure/table for our paper: consider

### Located Figure/Table 6
- Source anchor: p.5
- Caption: Figure 4. The importance of feature factors of KRD in the peak-cluster depression basin in southwest Guangxi,
- What it shows: inferred only from caption wording; inspect the PDF image before reuse.
- Why it matters: directly relevant to study design/results visualization
- Useful for our manuscript: yes
- Similar figure/table for our paper: consider

### Located Figure/Table 7
- Source anchor: p.6
- Caption: Figure 5. Spatial distribution of the karst rocky desertification. Maps were generated using QGIS 3.26.2
- What it shows: inferred only from caption wording; inspect the PDF image before reuse.
- Why it matters: directly relevant to study design/results visualization
- Useful for our manuscript: yes
- Similar figure/table for our paper: consider

### Located Figure/Table 8
- Source anchor: p.7
- Caption: Table 3. Change in the karst rocky desertification areas of different levels.
- What it shows: inferred only from caption wording; inspect the PDF image before reuse.
- Why it matters: potentially relevant; requires manual inspection
- Useful for our manuscript: maybe
- Similar figure/table for our paper: manual review first

### Located Figure/Table 9
- Source anchor: p.9
- Caption: Figure 6. The location of the study area. Maps were generated using QGIS 3.26.2 (https:// www. qgis. org/ en/
- What it shows: inferred only from caption wording; inspect the PDF image before reuse.
- Why it matters: directly relevant to study design/results visualization
- Useful for our manuscript: yes
- Similar figure/table for our paper: consider

### Located Figure/Table 10
- Source anchor: p.10
- Caption: Table 4. Detailed specifications of the remote sensing datasets.
- What it shows: inferred only from caption wording; inspect the PDF image before reuse.
- Why it matters: potentially relevant; requires manual inspection
- Useful for our manuscript: maybe
- Similar figure/table for our paper: manual review first

### Located Figure/Table 11
- Source anchor: p.10
- Caption: Table 5. Relevant parameters and sources of the auxiliary data.
- What it shows: inferred only from caption wording; inspect the PDF image before reuse.
- Why it matters: potentially relevant; requires manual inspection
- Useful for our manuscript: maybe
- Similar figure/table for our paper: manual review first

### Located Figure/Table 12
- Source anchor: p.10
- Caption: Table 6. FVC and RE were extracted using QGIS3.26.2 (https:// www. qgis. org/ en/ site/). NDRI normalized
- What it shows: inferred only from caption wording; inspect the PDF image before reuse.
- Why it matters: potentially relevant; requires manual inspection
- Useful for our manuscript: maybe
- Similar figure/table for our paper: manual review first

### Located Figure/Table 13
- Source anchor: p.11
- Caption: Figure 7. Field data survey map of karst rocky desertification. Map was generated using QGIS 3.26.2 (https://
- What it shows: inferred only from caption wording; inspect the PDF image before reuse.
- Why it matters: directly relevant to study design/results visualization
- Useful for our manuscript: yes
- Similar figure/table for our paper: consider

### Located Figure/Table 14
- Source anchor: p.11
- Caption: Table 7. Field classification standard for karst rocky desertification.
- What it shows: inferred only from caption wording; inspect the PDF image before reuse.
- Why it matters: directly relevant to study design/results visualization
- Useful for our manuscript: yes
- Similar figure/table for our paper: consider

### Located Figure/Table 15
- Source anchor: p.13
- Caption: Figure 8. Flow chart of karst rocky desertification mapping in peak cluster depression in Southwest Guangxi,
- What it shows: inferred only from caption wording; inspect the PDF image before reuse.
- Why it matters: directly relevant to study design/results visualization
- Useful for our manuscript: yes
- Similar figure/table for our paper: consider


## 10. Results Reading Notes

- Source anchors: p.1, p.2, p.3, p.4, p.5, p.7, p.8, p.10, p.12
- Main experimental results: use only values and claims visible in the excerpts/PDF tables.
- Model comparison results: inspect metric/table captions before using exact rankings.
- Data source comparison results: record only where Sentinel/Landsat/GF/DEM evidence is explicit.
- FBR/bare-rock inversion results: separate continuous metrics from class metrics.
- Classification accuracy: report OA/Kappa/Precision/Recall/F1/IoU/mF1/mIoU only if explicitly found.
- DEM/topographic factor contribution: note only when DEM/topographic excerpts are explicit.
- Spatial distribution / uncertainty / significance: inspect maps and captions manually.

Located result/metric evidence:
- p.1: At present, mapping KRD with a high accuracy and on a large scale is still
- p.1: classification accuracy indexes were to evaluate the performance of the model.
- p.1: accuracy rate and kappa index values of 94.7% and 0.92 for the testing datasets respectively.
- p.1: remote sensing data combined with the RF model can obtain better prediction results of KRD, thereby
- p.1: also the result of land degradation.
- p.2: interpretation, and the accuracy of their karst rocky desertification map interpretation reached 93.6%.
- p.2: classifier, the classification accuracy improved from 84.23 to 91.71%.
- p.2: approaches for KRD monitoring.
- p.2: be used to extract karst rocky desertification information with a high accuracy, but this method has difficulty
- p.2: are still a prerequisite for achieving accurate results using intelligent approaches.
- p.1: Yali Zhang1, Yichao Tian1,2*, Ying Li3, Donghua Wang4, Jin Tao1, Yongwei Yang1,
- p.1: Junliang Lin1, Qiang Zhang1 & Luhua Wu5
- p.1: Karst rocky desertification (KRD) has become one of the most serious ecological and environmental
- p.1: At present, mapping KRD with a high accuracy and on a large scale is still
- p.1: classification accuracy indexes were to evaluate the performance of the model.
- p.1: accuracy rate and kappa index values of 94.7% and 0.92 for the testing datasets respectively.


## 11. Discussion Reading Notes

- Source anchors: p.7
- Mechanism explanations, data-source performance, terrain effects, comparison to previous studies, limitations, and future work should be extracted from these anchors only.
- Borrowable Discussion writing pattern: explain why a data/model/factor improves mapping, then tie the explanation to spatial patterns and validation evidence.

Located discussion/limitation evidence:
- p.2: To overcome these limitations, scholars have
- p.8: Owing to the terrain limitations, they can only be carried out in areas with low
- p.8: In addition, another limitation


## 12. Conclusion Reading Notes

- Source anchors: p.8
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
- limitations support: medium. Reason: grounded signals were located in the text layer.
- figure/table design support: medium. Reason: grounded signals were located in the text layer.
- terminology support: medium. Reason: grounded signals were located in the text layer.
- Remote Sensing writing style support: not applicable. Reason: grounded signals were not located in the text layer.

## 14. Reusable Knowledge for Future Skill

### Scientific rules
- Relevant target/method signals: machine_learning; unknown.
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

- title is provisional filename-derived candidate; verify manually
- year missing in database
- DOI missing in database
- readability_status=usable_with_caution
- DOI needs manual verification
- metadata incomplete
