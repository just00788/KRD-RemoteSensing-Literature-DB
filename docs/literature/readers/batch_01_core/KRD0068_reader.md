# Full-Paper Reader: RAP-Net: A Region Affinity Propagation-Guided Semantic Segmentation Network for Plateau Karst Landform Delineation

## 1. Bibliographic Information

- Paper ID: KRD0068
- Title: RAP-Net: A Region Affinity Propagation-Guided Semantic Segmentation Network for Plateau Karst Landform Delineation
- Translated title if applicable: unknown
- Authors: Remote Sensing authors
- Year: 2025
- Journal / Source: Remote Sensing
- DOI: 10.3390/rs17173082
- URL: https://www.mdpi.com/2072-4292/17/17/3082
- PDF path: `docs/literature/pdfs/package_2021_2026/EN17_RAP-Net_A_Region_Affinity_Propagation-Guided_Semantic_Segmentation_Network_for_Plateau_Kar.pdf`
- Language: English
- Readability status: ready
- Metadata status: complete

## 2. Reading Scope and Source Anchors

This reader was generated from the full selectable text layer of the PDF. It preserves page-level anchors and section/figure/table signals. It does not reproduce large original-text passages and does not fabricate missing metadata.

- Abstract: p.1
- Introduction: p.1
- Study Area: p.5, p.7
- Data: p.1, p.2, p.3, p.5, p.6, p.7, p.8, p.13, p.15, p.20, p.21, p.22
- Methods: p.1, p.2, p.3, p.4, p.5, p.6, p.8, p.9, p.10, p.11, p.12, p.13, ...
- Experiments: p.1, p.6, p.8, p.13, p.14, p.16, p.17, p.20
- Results: p.2, p.4, p.6, p.8, p.10, p.13, p.14, p.15, p.16, p.17, p.19, p.20
- Discussion: p.17
- Conclusions: p.19, p.20
- References: p.21
- Figures/Tables captions: 19 located
  - p.5: Figure 1. Study area location and typical plateau karst landforms: ( a) Location of the study area.
  - p.6: Figure 2. Interpretation results of plateau karst landforms.
  - p.7: Figure 3. Process of PKLD production.
  - p.7: Figure 4. On-site fieldwork and validation in the study area. (a) On-site verification of a sample point
  - p.9: Figure 5. Region Affinity Propagation Guided Semantic Segmentation Network.
  - p.9: Figure 6. Region Affinity Propagation Block.
  - p.10: Figure 7. High-Frequency Multi-Scale Attention Block.
  - p.11: Figure 1 convolution is applied to each downsampled feature map to unify the channel

## 3. Abstract-Level Understanding

Source anchors: p.1, p.2, p.3

基于可抽取的摘要文本，本研究逻辑可按以下方式理解。以下内容只依据摘要和题录可确认的信息，不补造缺失结论。

- 研究背景: 论文主题与 `deep_learning_segmentation` 相关，关键词信号包括 `unknown`。
- 研究目标: RAP-Net: A Region Affinity Propagation-Guided Semantic Segmentation Network for Plateau Karst Landform Delineation
- 数据: 见下方 Data Sources 中从全文定位到的证据信号。
- 方法: 见下方 Method Workflow 中从全文定位到的证据信号。
- 主要结果: 仅在 Results Reading Notes 中记录可定位的结果/指标信号；未在此处编造具体数值。
- 意义: 其价值主要体现在对 KRD/FBR/分类/遥感制图/验证框架的支撑，具体等级见第 13 节。

Abstract evidence snippet:

> Karst rocky desertification on the Qinghai–Tibet Plateau poses a severe threat to the region’s fragile ecosystem. Accordingly, the rapid and accurate delineation of plateau karst landforms is essential for monitoring ecological degradation and guiding restoration strategies. However, automatic recognition of these landforms in remote sensing imagery is hindered by challenges such as blurred boundaries, fragmented targets, and poor intraregion consistency. To address these issues, we propose the Region Affinity Propagation Network (RAP-Net). This framework enhances intra-region consistency, edge sensitivity, and multi-scale context fusion through its core modules: Region Affinity Propagation (RAP), High-Frequency Multi-Scale Attention (HFMSA), and Global–Local Cross Attention (GLCA). In addition, we constructed the Plateau Karst Landform Dataset (PKLD), a high-resolution remote sensing dataset specifically tailored for this task, which provides a standardized benchmark for future studies. On the PKLD, RAP-Net surpasses eight state-of-the-art methods, achieving 3.69–10.31% higher IoU and 3.88–14.28% higher Recall, thereby demonstrating significant improvements in boundary delineation

## 4. Introduction Reading Notes

- Source anchors: p.1
- Background unfolding: extracted introduction pages should be read around the anchors above; the parser located target/method signals listed below.
- Why the problem matters: only infer from located KRD/desertification/remote-sensing problem statements; do not add unsupported claims.
- Remote sensing role: see satellite/data excerpts in Section 5.
- Existing research categories: classification, FBR/LSMM/MESMA, ML, semantic segmentation, DEM/topography when signaled below.
- Existing research insufficiency / gap / objectives / contributions: inspect Introduction anchors manually for exact wording before using in manuscript.
- Borrowable point for our Introduction: build a clear progression from KRD importance -> remote-sensing monitoring -> method/data limitation -> our FBR/classification/DEM/cross-region contribution.

Located target/method evidence:
- p.1: Karst rocky desertification on the Qinghai–Tibet Plateau poses a severe threat to the region’s fragile ecosystem.
- p.1: Keywords: karst landforms; Qinghai–Tibet Plateau; semantic segmentation; affinity propagation
- p.1: Karst rocky desertification poses a severe and often irreversible threat to the fragile
- p.1: widespread exposure of carbonate bedrock, and the formation of distinctive karst landforms
- p.2: networks (CNNs) and graph neural networks (GNNs) to classify rocky desertification
- p.3: bare rocks, alpine grassland, gravel surfaces, and terrain shadows.
- p.3: We propose RAP-Net, an end-to-end semantic segmentation network tailored for
- p.3: In remote sensing semantic segmentation tasks, objects frequently exhibit complex
- p.4: sensing semantic segmentation, particularly in extracting structured objects such as urban
- p.8: To address the challenges of low regional consistency and limited cross-region generalization in plateau karst segmentation, we propose a structure-aware semantic segmentation
- p.1: Segmentation Network for Plateau
- p.1: Segmentation Network for Plateau Karst Landform Remote
- p.1: Keywords: karst landforms; Qinghai–Tibet Plateau; semantic segmentation; affinity propagation
- p.2: used K-means clustering and random forest classifiers to


## 5. Study Area and Data Sources

- Study area: locate from Study Area anchors: p.5, p.7
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
- p.1: Academic Editor: Hubert Hasenauer
- p.1: 1 Department of Surveying & Mapping Engineering, College of Earth and Planetary Sciences, Chengdu
- p.1: 2 Sichuan Coalfield 141 Construction Investment Co., Ltd., Deyang 618029, China
- p.1: thereby demonstrating significant improvements in boundary delineation and structural
- p.2: Compared to field-based surveys, visual interpretation
- p.2: provides a cost-effective and efficient means of mapping large and topographically complex
- p.2: diverse regions and complex terrains [ 10].
- p.2: with UAV imagery to map wetland vegetation in karst environments, demonstrating the
- p.2: a DeepLabV3+-based approach integrating optical imagery and digital elevation model
- p.2: (DEM) data to map cone karst landscapes in Libo, China [12].


## 6. Target Variable or Classification System

- Target variable / object: derived from located evidence only.
- KRD/rocky desertification signal: yes
- FBR/fBR/bare-rock fraction signal: yes
- Semantic segmentation class signal: yes
- If FBR/fBR is involved, treat it as a continuous/proportional variable unless the paper explicitly thresholds it into classes.
- If rocky desertification levels are involved, inspect the paper for the exact grade system before reuse.

Target evidence:
- p.1: Karst rocky desertification on the Qinghai–Tibet Plateau poses a severe threat to the region’s fragile ecosystem.
- p.1: Keywords: karst landforms; Qinghai–Tibet Plateau; semantic segmentation; affinity propagation
- p.1: Karst rocky desertification poses a severe and often irreversible threat to the fragile
- p.1: widespread exposure of carbonate bedrock, and the formation of distinctive karst landforms
- p.2: networks (CNNs) and graph neural networks (GNNs) to classify rocky desertification
- p.3: bare rocks, alpine grassland, gravel surfaces, and terrain shadows.
- p.3: We propose RAP-Net, an end-to-end semantic segmentation network tailored for
- p.3: In remote sensing semantic segmentation tasks, objects frequently exhibit complex
- p.4: sensing semantic segmentation, particularly in extracting structured objects such as urban
- p.8: To address the challenges of low regional consistency and limited cross-region generalization in plateau karst segmentation, we propose a structure-aware semantic segmentation


## 7. Method Workflow

The workflow below is derived from located method/data signals. Missing items are explicitly marked.
- preprocessing: located
- feature construction: located
- spectral indices: not reported
- DEM/topographic variables: located
- LSMM/SMA/MESMA/FCLS: located
- machine learning models: located
- deep learning models: located
- semantic segmentation architecture: located
- training strategy: located
- sample split: located
- cross-validation: not reported
- cross-region validation: located
- ablation design: located
- comparison methods: located

Located method/data evidence:
- p.1: Segmentation Network for Plateau
- p.1: Segmentation Network for Plateau Karst Landform Remote
- p.1: Keywords: karst landforms; Qinghai–Tibet Plateau; semantic segmentation; affinity propagation
- p.2: used K-means clustering and random forest classifiers to
- p.2: However, their detection performance still largely depends
- p.2: learning has emerged as a powerful tool for improving both the efficiency and accuracy of
- p.2: karst landform segmentation.
- p.2: a DeepLabV3+-based approach integrating optical imagery and digital elevation model
- p.2: developed a deep learning-based segmentation model by combining convolutional neural
- p.2: networks (CNNs) and graph neural networks (GNNs) to classify rocky desertification
- p.2: Enclosed karst depressions are relatively rare, and the surface patterns tend
- p.2: recognition primarily rely on CNN architectures and their variants [16–18].
- p.1: Academic Editor: Hubert Hasenauer
- p.1: 1 Department of Surveying & Mapping Engineering, College of Earth and Planetary Sciences, Chengdu
- p.1: 2 Sichuan Coalfield 141 Construction Investment Co., Ltd., Deyang 618029, China
- p.1: thereby demonstrating significant improvements in boundary delineation and structural
- p.2: Compared to field-based surveys, visual interpretation
- p.2: provides a cost-effective and efficient means of mapping large and topographically complex
- p.2: diverse regions and complex terrains [ 10].
- p.2: with UAV imagery to map wetland vegetation in karst environments, demonstrating the
- p.2: a DeepLabV3+-based approach integrating optical imagery and digital elevation model
- p.2: (DEM) data to map cone karst landscapes in Libo, China [12].


## 8. Validation Strategy and Metrics

- Reference sample source: locate from excerpts below; manual confirmation recommended.
- Sample size: record only if explicitly visible in source excerpts; otherwise unknown.
- Train/test split: see located split/training evidence; otherwise not reported.
- Spatial split: located only if terms such as spatial/block split appear; otherwise not reported.
- Independent validation: located only if explicit evidence appears; otherwise not reported.
- Cross-region validation: located only if explicit evidence appears; otherwise not reported.

- Continuous-variable metrics located: bias, slope
- Classification metrics located: OA, Precision, Recall, F1, IoU, confusion matrix

Metric evidence:
- p.1: Propagation-Guided Semantic
- p.1: RAP-Net: A Region Affinity Propagation-Guided Semantic
- p.1: 1 Department of Surveying & Mapping Engineering, College of Earth and Planetary Sciences, Chengdu
- p.1: 2 Sichuan Coalfield 141 Construction Investment Co., Ltd., Deyang 618029, China
- p.1: To address these issues, we propose the Region Affinity Propagation
- p.1: and multi-scale context fusion through its core modules: Region Affinity Propagation
- p.1: On the PKLD, RAP-Net surpasses eight
- p.1: state-of-the-art methods, achieving 3.69–10.31% higher IoU and 3.88–14.28% higher Recall,
- p.1: IoU and F1-scores, respectively, than the Swin Transformer, confirming its robustness and
- p.1: Keywords: karst landforms; Qinghai–Tibet Plateau; semantic segmentation; affinity propagation
- p.2: Currently, karst landform mapping primarily relies on visual interpretation techniques,
- p.2: including manual analysis of remote sensing imagery, along with machine learning and


Important distinction enforced for our manuscript: continuous FBR inversion metrics (R2/RMSE/MAE/bias/slope) must not be mixed with classification metrics (OA/Kappa/Precision/Recall/F1/IoU/mF1/mIoU).

## 9. Figures and Tables

### Located Figure/Table 1
- Source anchor: p.5
- Caption: Figure 1. Study area location and typical plateau karst landforms: ( a) Location of the study area.
- What it shows: inferred only from caption wording; inspect the PDF image before reuse.
- Why it matters: directly relevant to study design/results visualization
- Useful for our manuscript: yes
- Similar figure/table for our paper: consider

### Located Figure/Table 2
- Source anchor: p.6
- Caption: Figure 2. Interpretation results of plateau karst landforms.
- What it shows: inferred only from caption wording; inspect the PDF image before reuse.
- Why it matters: potentially relevant; requires manual inspection
- Useful for our manuscript: maybe
- Similar figure/table for our paper: manual review first

### Located Figure/Table 3
- Source anchor: p.7
- Caption: Figure 3. Process of PKLD production.
- What it shows: inferred only from caption wording; inspect the PDF image before reuse.
- Why it matters: potentially relevant; requires manual inspection
- Useful for our manuscript: maybe
- Similar figure/table for our paper: manual review first

### Located Figure/Table 4
- Source anchor: p.7
- Caption: Figure 4. On-site fieldwork and validation in the study area. (a) On-site verification of a sample point
- What it shows: inferred only from caption wording; inspect the PDF image before reuse.
- Why it matters: directly relevant to study design/results visualization
- Useful for our manuscript: yes
- Similar figure/table for our paper: consider

### Located Figure/Table 5
- Source anchor: p.9
- Caption: Figure 5. Region Affinity Propagation Guided Semantic Segmentation Network.
- What it shows: inferred only from caption wording; inspect the PDF image before reuse.
- Why it matters: potentially relevant; requires manual inspection
- Useful for our manuscript: maybe
- Similar figure/table for our paper: manual review first

### Located Figure/Table 6
- Source anchor: p.9
- Caption: Figure 6. Region Affinity Propagation Block.
- What it shows: inferred only from caption wording; inspect the PDF image before reuse.
- Why it matters: potentially relevant; requires manual inspection
- Useful for our manuscript: maybe
- Similar figure/table for our paper: manual review first

### Located Figure/Table 7
- Source anchor: p.10
- Caption: Figure 7. High-Frequency Multi-Scale Attention Block.
- What it shows: inferred only from caption wording; inspect the PDF image before reuse.
- Why it matters: potentially relevant; requires manual inspection
- Useful for our manuscript: maybe
- Similar figure/table for our paper: manual review first

### Located Figure/Table 8
- Source anchor: p.11
- Caption: Figure 1 convolution is applied to each downsampled feature map to unify the channel
- What it shows: inferred only from caption wording; inspect the PDF image before reuse.
- Why it matters: directly relevant to study design/results visualization
- Useful for our manuscript: yes
- Similar figure/table for our paper: consider

### Located Figure/Table 9
- Source anchor: p.12
- Caption: Figure 8. Global-Local Cross Attention Block.
- What it shows: inferred only from caption wording; inspect the PDF image before reuse.
- Why it matters: potentially relevant; requires manual inspection
- Useful for our manuscript: maybe
- Similar figure/table for our paper: manual review first

### Located Figure/Table 10
- Source anchor: p.14
- Caption: Table 1. Quantitative comparison of segmentation performance on the PKLD using different methods.
- What it shows: inferred only from caption wording; inspect the PDF image before reuse.
- Why it matters: potentially relevant; requires manual inspection
- Useful for our manuscript: maybe
- Similar figure/table for our paper: manual review first

### Located Figure/Table 11
- Source anchor: p.15
- Caption: Figure 9. Visual comparison of pixel-level prediction errors among different models on five karst
- What it shows: inferred only from caption wording; inspect the PDF image before reuse.
- Why it matters: potentially relevant; requires manual inspection
- Useful for our manuscript: maybe
- Similar figure/table for our paper: manual review first

### Located Figure/Table 12
- Source anchor: p.16
- Caption: Table 2.
- What it shows: inferred only from caption wording; inspect the PDF image before reuse.
- Why it matters: potentially relevant; requires manual inspection
- Useful for our manuscript: maybe
- Similar figure/table for our paper: manual review first

### Located Figure/Table 13
- Source anchor: p.16
- Caption: Table 2. Ablation results of the proposed modules on the PKLD (Gongjue area), with the best values
- What it shows: inferred only from caption wording; inspect the PDF image before reuse.
- Why it matters: potentially relevant; requires manual inspection
- Useful for our manuscript: maybe
- Similar figure/table for our paper: manual review first

### Located Figure/Table 14
- Source anchor: p.17
- Caption: Table 3. Cross-Regional Generalization Performance of RAP-Net and Swin Transformer on the Mount
- What it shows: inferred only from caption wording; inspect the PDF image before reuse.
- Why it matters: potentially relevant; requires manual inspection
- Useful for our manuscript: maybe
- Similar figure/table for our paper: manual review first

### Located Figure/Table 15
- Source anchor: p.18
- Caption: Figure 10. Visual comparison of pixel-level prediction errors on the Mount Genyen area for
- What it shows: inferred only from caption wording; inspect the PDF image before reuse.
- Why it matters: potentially relevant; requires manual inspection
- Useful for our manuscript: maybe
- Similar figure/table for our paper: manual review first

### Located Figure/Table 16
- Source anchor: p.18
- Caption: Figure 11. Comparison of pixel-wise error composition on the Mount Genyen area for (a) RAP-Net
- What it shows: inferred only from caption wording; inspect the PDF image before reuse.
- Why it matters: potentially relevant; requires manual inspection
- Useful for our manuscript: maybe
- Similar figure/table for our paper: manual review first

### Located Figure/Table 17
- Source anchor: p.19
- Caption: Figure 12. Mount Genyen Validation Routes and Point Map.
- What it shows: inferred only from caption wording; inspect the PDF image before reuse.
- Why it matters: directly relevant to study design/results visualization
- Useful for our manuscript: yes
- Similar figure/table for our paper: consider

### Located Figure/Table 18
- Source anchor: p.19
- Caption: Figure 10 visualization.
- What it shows: inferred only from caption wording; inspect the PDF image before reuse.
- Why it matters: potentially relevant; requires manual inspection
- Useful for our manuscript: maybe
- Similar figure/table for our paper: manual review first

### Located Figure/Table 19
- Source anchor: p.20
- Caption: Table 4. Comparison of FLOPs and Parameters of Different Models.
- What it shows: inferred only from caption wording; inspect the PDF image before reuse.
- Why it matters: potentially relevant; requires manual inspection
- Useful for our manuscript: maybe
- Similar figure/table for our paper: manual review first


## 10. Results Reading Notes

- Source anchors: p.2, p.4, p.6, p.8, p.10, p.13, p.14, p.15, p.16, p.17, p.19, p.20
- Main experimental results: use only values and claims visible in the excerpts/PDF tables.
- Model comparison results: inspect metric/table captions before using exact rankings.
- Data source comparison results: record only where Sentinel/Landsat/GF/DEM evidence is explicit.
- FBR/bare-rock inversion results: separate continuous metrics from class metrics.
- Classification accuracy: report OA/Kappa/Precision/Recall/F1/IoU/mF1/mIoU only if explicitly found.
- DEM/topographic factor contribution: note only when DEM/topographic excerpts are explicit.
- Spatial distribution / uncertainty / significance: inspect maps and captions manually.

Located result/metric evidence:
- p.1: However, this approach is limited by its dependence on expert knowledge and manual
- p.1: support geological mapping in the Dalmatian karst region of Croatia, thereby improving
- p.1: Compared with traditional manual interpretation, these machine learning approaches have significantly improved mapping efficiency
- p.1: and reduced human workload.
- p.1: learning has emerged as a powerful tool for improving both the efficiency and accuracy of
- p.1: Unlike traditional approaches, deep learning enables automatic feature extraction
- p.1: a DeepLabV3+-based approach integrating optical imagery and digital elevation model
- p.1: achieved improved recognition accuracy, their direct application to the plateau karst regions
- p.2: which combines fine-grained local details with broad contextual cues, thereby improving the representation of multi-scale objects and boosting the accuracy of small-object
- p.2: [ 31] proposed the Orientation Attention Network (OANet),
- p.1: Propagation-Guided Semantic
- p.1: RAP-Net: A Region Affinity Propagation-Guided Semantic
- p.1: 1 Department of Surveying & Mapping Engineering, College of Earth and Planetary Sciences, Chengdu
- p.1: 2 Sichuan Coalfield 141 Construction Investment Co., Ltd., Deyang 618029, China
- p.1: To address these issues, we propose the Region Affinity Propagation
- p.1: and multi-scale context fusion through its core modules: Region Affinity Propagation


## 11. Discussion Reading Notes

- Source anchors: p.17
- Mechanism explanations, data-source performance, terrain effects, comparison to previous studies, limitations, and future work should be extracted from these anchors only.
- Borrowable Discussion writing pattern: explain why a data/model/factor improves mapping, then tie the explanation to spatial patterns and validation evidence.

Located discussion/limitation evidence:
- p.2: To overcome these limitations, researchers have adopted machine learning techniques
- p.4: To address this limitation, we propose an
- p.12: Context Attention Branch by compensating for its limitations in modeling local patterns.
- p.14: CNN-based models demonstrate noticeable limitations in recall performance under the


## 12. Conclusion Reading Notes

- Source anchors: p.19, p.20
- Objective summary: inspect Conclusion anchors.
- Method summary: inspect Conclusion anchors.
- Main results: record only exact values visible in Conclusion/Results.
- Contributions/application value: inspect Conclusion anchors.
- Limitations/future work: see limitation evidence above.

## 13. Relevance to Our Remote Sensing Manuscript

- Introduction support: high. Reason: grounded signals were located in the text layer.
- FBR/LSMM support: high. Reason: grounded signals were located in the text layer.
- ML baseline support: high. Reason: grounded signals were located in the text layer.
- semantic segmentation support: high. Reason: grounded signals were located in the text layer.
- DEM/topography support: high. Reason: grounded signals were located in the text layer.
- GF/Sentinel/Landsat data comparison support: high. Reason: grounded signals were located in the text layer.
- cross-region transfer support: high. Reason: grounded signals were located in the text layer.
- accuracy assessment support: high. Reason: grounded signals were located in the text layer.
- Discussion comparison support: not applicable. Reason: grounded signals were not located in the text layer.
- limitations support: high. Reason: grounded signals were located in the text layer.
- figure/table design support: high. Reason: grounded signals were located in the text layer.
- terminology support: high. Reason: grounded signals were located in the text layer.
- Remote Sensing writing style support: high. Reason: grounded signals were located in the text layer.

## 14. Reusable Knowledge for Future Skill

### Scientific rules
- Relevant target/method signals: deep_learning_segmentation; unknown.
- Located target evidence pages: p.1, p.1, p.1, p.1, p.2, p.3.
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
