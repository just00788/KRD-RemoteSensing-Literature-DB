# Full-Paper Reader: 基于改进DeepLabV3+的石漠化地区裸岩信息提取

## 1. Bibliographic Information

- Paper ID: KRD0116
- Title: 基于改进DeepLabV3+的石漠化地区裸岩信息提取
- Translated title if applicable: unknown
- Authors: 吴永俊
- Year: unknown
- Journal / Source: unknown
- DOI: unknown
- URL: unknown
- PDF path: `docs/literature/pdfs/package_2000_2026/基于改进DeepLabV3+的石漠化地区裸岩信息提取_吴永俊.pdf`
- Language: Chinese
- Readability status: ready
- Metadata status: metadata_incomplete

## 2. Reading Scope and Source Anchors

This reader was generated from the full selectable text layer of the PDF. It preserves page-level anchors and section/figure/table signals. It does not reproduce large original-text passages and does not fabricate missing metadata.

- Abstract: p.1
- Introduction: p.2
- Study Area: not located
- Data: p.2, p.4, p.8, p.12
- Methods: p.1, p.2, p.3, p.7, p.8, p.9, p.10, p.11, p.12, p.13
- Experiments: p.8, p.9, p.10
- Results: p.1, p.2, p.3, p.5, p.6, p.7, p.8, p.9, p.10, p.11, p.12
- Discussion: not located
- Conclusions: not located
- References: p.12
- Figures/Tables captions: 19 located
  - p.3: 图 1 DeepLabV3+模型结构
  - p.3: Fig.1 DeepLabV3+ model structure
  - p.4: 图 2 坐标注意力机制
  - p.4: Fig.2 Coordinate attention mechanism
  - p.5: 图 3 MobileNetV3基本单元
  - p.5: Fig.3 MobileNetV3 block
  - p.5: 表 1 MobileNetV3网络结构
  - p.6: 表 2 CA-DC-MobileNetV3网络结构

## 3. Abstract-Level Understanding

Source anchors: p.1, p.2, p.3

基于可抽取的摘要文本，本研究逻辑可按以下方式理解。以下内容只依据摘要和题录可确认的信息，不补造缺失结论。

- 研究背景: 论文主题与 `deep_learning_segmentation` 相关，关键词信号包括 `DeepLabV3+`。
- 研究目标: 基于改进DeepLabV3+的石漠化地区裸岩信息提取
- 数据: 见下方 Data Sources 中从全文定位到的证据信号。
- 方法: 见下方 Method Workflow 中从全文定位到的证据信号。
- 主要结果: 仅在 Results Reading Notes 中记录可定位的结果/指标信号；未在此处编造具体数值。
- 意义: 其价值主要体现在对 KRD/FBR/分类/遥感制图/验证框架的支撑，具体等级见第 13 节。

Abstract evidence snippet:

> Aiming at the problems of high cost and low precision of traditional bare rock extraction methods in karst areas, this paper constructs a bare rock extraction method based on improved DeepLabV3+. This method first uses CA-DC-MobileNetV3 to replace DeepLabV3+ backbone network Xception in the encoder for feature extraction, which greatly reduces the amount of model parameters. Secondly, the features extracted by the encoder are enhanced through the feature pyramid network and the coordinate attention mechanism to obtain more small target information and reduce the loss of image details. Finally, in the atrous spatial pyramid pooling module, the features of the convolutional layers with different dilation rates are fused to improve the utilization of information. The results show that the method in this paper performs best in the bare rock extraction tasks in 收稿日期：2023-03-20 基金项目：国家自然科学基金（41901225） 引用格式：吴永俊, 汪泓, 杨晨. 基于改进DeepLabV3+的石漠化地区裸岩信息提取[J]. 航天返回与遥感, 2024, 45(1): 123-135. WU Yongjun, WANG Hong, YANG Chen. Extraction of Bare Rock Information in Rocky Desertification Area Based on Improved DeepLabV3+[J]. Spacecraft Recovery & Remote Sensing, 2024, 45(1): 123-135. (in Chinese) 第 45 

## 4. Introduction Reading Notes

- Source anchors: p.2
- Background unfolding: extracted introduction pages should be read around the anchors above; the parser located target/method signals listed below.
- Why the problem matters: only infer from located KRD/desertification/remote-sensing problem statements; do not add unsupported claims.
- Remote sensing role: see satellite/data excerpts in Section 5.
- Existing research categories: classification, FBR/LSMM/MESMA, ML, semantic segmentation, DEM/topography when signaled below.
- Existing research insufficiency / gap / objectives / contributions: inspect Introduction anchors manually for exact wording before using in manuscript.
- Borrowable point for our Introduction: build a clear progression from KRD importance -> remote-sensing monitoring -> method/data limitation -> our FBR/classification/DEM/cross-region contribution.

Located target/method evidence:
- p.1: 摘 要 针对传统喀斯特地区裸岩提取方法成本高、精度低的问题，文章构建了一种基于改进
- p.1: DeepLabV3+的裸岩提取方法。该方法首先在编码器中 用 CA-DC-MobileNetV3替 换 DeepLabV3+骨干网
- p.1: 法在不同场景裸岩提取任务中表现最好，模型参数量约为 DeepLabV3+的 1/13，交并比、 F1分数分别为
- p.1: 关键词 裸岩提取 深度学习 语义分割 坐标注意力机制
- p.1: Extraction of Bare Rock Information in Rocky Desertification Area
- p.1: Abstract Aiming at the problems of high cost and low precision of traditional bare rock extraction
- p.1: methods in karst areas, this paper constructs a bare rock extraction method based on improved DeepLabV3+.
- p.1: The results show that the method in this paper performs best in the bare rock extraction tasks in
- p.1: 基于改进DeepLabV3+的石漠化地区裸岩信息提取[J].
- p.1: Extraction of Bare Rock Information in Rocky Desertification Area Based
- p.1: DeepLabV3+的裸岩提取方法。该方法首先在编码器中 用 CA-DC-MobileNetV3替 换 DeepLabV3+骨干网
- p.1: 法在不同场景裸岩提取任务中表现最好，模型参数量约为 DeepLabV3+的 1/13，交并比、 F1分数分别为
- p.1: 72.46%、84.03%，上述 2个指标相比 于 DeepLabV3+模型分别提高了 4.62和 3.19个百分点，并优于其余
- p.1: Based on Improved DeepLabV3+


## 5. Study Area and Data Sources

- Study area: locate from Study Area anchors: not located
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
- p.2: Landsat8裸岩和其他土地覆盖类型的光谱特征，通过蓝光、近红外波段差和比，构建归一化裸岩指数
- p.2: 区Landsat8影像，通过指数法获取的裸岩率， 使 Landsat8影像提取裸岩的精度得到提高，但该方法工作
- p.12: 基于无人机影像与Landsat8影像关联的重庆市石漠化信息提取与现状评价[D].
- p.12: of Unmanned Aerial Vehicle Photo and Landsat8 Image[D].


## 6. Target Variable or Classification System

- Target variable / object: derived from located evidence only.
- KRD/rocky desertification signal: yes
- FBR/fBR/bare-rock fraction signal: yes
- Semantic segmentation class signal: yes
- If FBR/fBR is involved, treat it as a continuous/proportional variable unless the paper explicitly thresholds it into classes.
- If rocky desertification levels are involved, inspect the paper for the exact grade system before reuse.

Target evidence:
- p.1: 摘 要 针对传统喀斯特地区裸岩提取方法成本高、精度低的问题，文章构建了一种基于改进
- p.1: DeepLabV3+的裸岩提取方法。该方法首先在编码器中 用 CA-DC-MobileNetV3替 换 DeepLabV3+骨干网
- p.1: 法在不同场景裸岩提取任务中表现最好，模型参数量约为 DeepLabV3+的 1/13，交并比、 F1分数分别为
- p.1: 关键词 裸岩提取 深度学习 语义分割 坐标注意力机制
- p.1: Extraction of Bare Rock Information in Rocky Desertification Area
- p.1: Abstract Aiming at the problems of high cost and low precision of traditional bare rock extraction
- p.1: methods in karst areas, this paper constructs a bare rock extraction method based on improved DeepLabV3+.
- p.1: The results show that the method in this paper performs best in the bare rock extraction tasks in
- p.1: 基于改进DeepLabV3+的石漠化地区裸岩信息提取[J].
- p.1: Extraction of Bare Rock Information in Rocky Desertification Area Based


## 7. Method Workflow

The workflow below is derived from located method/data signals. Missing items are explicitly marked.
- preprocessing: located
- feature construction: located
- spectral indices: not reported
- DEM/topographic variables: not reported
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
- p.1: DeepLabV3+的裸岩提取方法。该方法首先在编码器中 用 CA-DC-MobileNetV3替 换 DeepLabV3+骨干网
- p.1: 法在不同场景裸岩提取任务中表现最好，模型参数量约为 DeepLabV3+的 1/13，交并比、 F1分数分别为
- p.1: 72.46%、84.03%，上述 2个指标相比 于 DeepLabV3+模型分别提高了 4.62和 3.19个百分点，并优于其余
- p.1: Based on Improved DeepLabV3+
- p.1: methods in karst areas, this paper constructs a bare rock extraction method based on improved DeepLabV3+.
- p.1: method first uses CA-DC-MobileNetV3 to replace DeepLabV3+ backbone network Xception in the encoder for
- p.1: more small target information and reduce the loss of image details.
- p.1: The results show that the method in this paper performs best in the bare rock extraction tasks in
- p.1: 基于改进DeepLabV3+的石漠化地区裸岩信息提取[J].
- p.1: on Improved DeepLabV3+[J].
- p.2: different scenarios, the number of model parameters is about 1/13 of that of DeepLabV3+, and the intersection
- p.2: Compared with the DeepLabV3+ model, the above two
- p.2: Landsat8裸岩和其他土地覆盖类型的光谱特征，通过蓝光、近红外波段差和比，构建归一化裸岩指数
- p.2: 区Landsat8影像，通过指数法获取的裸岩率， 使 Landsat8影像提取裸岩的精度得到提高，但该方法工作
- p.12: 基于无人机影像与Landsat8影像关联的重庆市石漠化信息提取与现状评价[D].
- p.12: of Unmanned Aerial Vehicle Photo and Landsat8 Image[D].


## 8. Validation Strategy and Metrics

- Reference sample source: locate from excerpts below; manual confirmation recommended.
- Sample size: record only if explicitly visible in source excerpts; otherwise unknown.
- Train/test split: see located split/training evidence; otherwise not reported.
- Spatial split: located only if terms such as spatial/block split appear; otherwise not reported.
- Independent validation: located only if explicit evidence appears; otherwise not reported.
- Cross-region validation: located only if explicit evidence appears; otherwise not reported.

- Continuous-variable metrics located: not located
- Classification metrics located: OA, Precision, Recall, F1, IoU

Metric evidence:
- p.1: 法在不同场景裸岩提取任务中表现最好，模型参数量约为 DeepLabV3+的 1/13，交并比、 F1分数分别为
- p.1: Abstract Aiming at the problems of high cost and low precision of traditional bare rock extraction
- p.1: methods in karst areas, this paper constructs a bare rock extraction method based on improved DeepLabV3+.
- p.1: feature extraction, which greatly reduces the amount of model parameters.
- p.1: Finally, in the atrous spatial pyramid pooling
- p.1: The results show that the method in this paper performs best in the bare rock extraction tasks in
- p.1: Spacecraft Recovery & Remote Sensing, 2024, 45(1): 123-135.
- p.1: 2024 年 2 月 SPACECRAFT RECOVERY & REMOTE SENSING 123
- p.2: different scenarios, the number of model parameters is about 1/13 of that of DeepLabV3+, and the intersection
- p.2: ratio and F1-Score are 72.46% and 84.04% respectively.
- p.2: Compared with the DeepLabV3+ model, the above two
- p.2: used semantic segmentation models, improving the accuracy of bare rock extraction.


Important distinction enforced for our manuscript: continuous FBR inversion metrics (R2/RMSE/MAE/bias/slope) must not be mixed with classification metrics (OA/Kappa/Precision/Recall/F1/IoU/mF1/mIoU).

## 9. Figures and Tables

### Located Figure/Table 1
- Source anchor: p.3
- Caption: 图 1 DeepLabV3+模型结构
- What it shows: inferred only from caption wording; inspect the PDF image before reuse.
- Why it matters: potentially relevant; requires manual inspection
- Useful for our manuscript: maybe
- Similar figure/table for our paper: manual review first

### Located Figure/Table 2
- Source anchor: p.3
- Caption: Fig.1 DeepLabV3+ model structure
- What it shows: inferred only from caption wording; inspect the PDF image before reuse.
- Why it matters: potentially relevant; requires manual inspection
- Useful for our manuscript: maybe
- Similar figure/table for our paper: manual review first

### Located Figure/Table 3
- Source anchor: p.4
- Caption: 图 2 坐标注意力机制
- What it shows: inferred only from caption wording; inspect the PDF image before reuse.
- Why it matters: potentially relevant; requires manual inspection
- Useful for our manuscript: maybe
- Similar figure/table for our paper: manual review first

### Located Figure/Table 4
- Source anchor: p.4
- Caption: Fig.2 Coordinate attention mechanism
- What it shows: inferred only from caption wording; inspect the PDF image before reuse.
- Why it matters: potentially relevant; requires manual inspection
- Useful for our manuscript: maybe
- Similar figure/table for our paper: manual review first

### Located Figure/Table 5
- Source anchor: p.5
- Caption: 图 3 MobileNetV3基本单元
- What it shows: inferred only from caption wording; inspect the PDF image before reuse.
- Why it matters: potentially relevant; requires manual inspection
- Useful for our manuscript: maybe
- Similar figure/table for our paper: manual review first

### Located Figure/Table 6
- Source anchor: p.5
- Caption: Fig.3 MobileNetV3 block
- What it shows: inferred only from caption wording; inspect the PDF image before reuse.
- Why it matters: potentially relevant; requires manual inspection
- Useful for our manuscript: maybe
- Similar figure/table for our paper: manual review first

### Located Figure/Table 7
- Source anchor: p.5
- Caption: 表 1 MobileNetV3网络结构
- What it shows: inferred only from caption wording; inspect the PDF image before reuse.
- Why it matters: potentially relevant; requires manual inspection
- Useful for our manuscript: maybe
- Similar figure/table for our paper: manual review first

### Located Figure/Table 8
- Source anchor: p.6
- Caption: 表 2 CA-DC-MobileNetV3网络结构
- What it shows: inferred only from caption wording; inspect the PDF image before reuse.
- Why it matters: potentially relevant; requires manual inspection
- Useful for our manuscript: maybe
- Similar figure/table for our paper: manual review first

### Located Figure/Table 9
- Source anchor: p.6
- Caption: 图 4 特征金字塔
- What it shows: inferred only from caption wording; inspect the PDF image before reuse.
- Why it matters: potentially relevant; requires manual inspection
- Useful for our manuscript: maybe
- Similar figure/table for our paper: manual review first

### Located Figure/Table 10
- Source anchor: p.6
- Caption: Fig.4 Feature pyramid network structure
- What it shows: inferred only from caption wording; inspect the PDF image before reuse.
- Why it matters: directly relevant to study design/results visualization
- Useful for our manuscript: yes
- Similar figure/table for our paper: consider

### Located Figure/Table 11
- Source anchor: p.7
- Caption: 图5为改进 的 DeepLabV3+模型，使用 CA-DC-MobileNetV3作为骨干网络，以减少模型参数；引入
- What it shows: inferred only from caption wording; inspect the PDF image before reuse.
- Why it matters: potentially relevant; requires manual inspection
- Useful for our manuscript: maybe
- Similar figure/table for our paper: manual review first

### Located Figure/Table 12
- Source anchor: p.7
- Caption: 图 5 改进的DeepLabV3+模型
- What it shows: inferred only from caption wording; inspect the PDF image before reuse.
- Why it matters: potentially relevant; requires manual inspection
- Useful for our manuscript: maybe
- Similar figure/table for our paper: manual review first

### Located Figure/Table 13
- Source anchor: p.7
- Caption: Fig.5 Improved DeepLabV3+ model
- What it shows: inferred only from caption wording; inspect the PDF image before reuse.
- Why it matters: potentially relevant; requires manual inspection
- Useful for our manuscript: maybe
- Similar figure/table for our paper: manual review first

### Located Figure/Table 14
- Source anchor: p.9
- Caption: 表 3 不同改进方案性能指标对比
- What it shows: inferred only from caption wording; inspect the PDF image before reuse.
- Why it matters: potentially relevant; requires manual inspection
- Useful for our manuscript: maybe
- Similar figure/table for our paper: manual review first

### Located Figure/Table 15
- Source anchor: p.9
- Caption: 图 6 可视化的注意力图
- What it shows: inferred only from caption wording; inspect the PDF image before reuse.
- Why it matters: potentially relevant; requires manual inspection
- Useful for our manuscript: maybe
- Similar figure/table for our paper: manual review first

### Located Figure/Table 16
- Source anchor: p.9
- Caption: Fig.6 Visual attention maps
- What it shows: inferred only from caption wording; inspect the PDF image before reuse.
- Why it matters: directly relevant to study design/results visualization
- Useful for our manuscript: yes
- Similar figure/table for our paper: consider

### Located Figure/Table 17
- Source anchor: p.10
- Caption: 表5更直观地展示了不同语义分割模型在不同场景的预测结果， 表 5中红色线圈为部分漏提区域、
- What it shows: inferred only from caption wording; inspect the PDF image before reuse.
- Why it matters: potentially relevant; requires manual inspection
- Useful for our manuscript: maybe
- Similar figure/table for our paper: manual review first

### Located Figure/Table 18
- Source anchor: p.10
- Caption: 表 4 不同算法性能对比
- What it shows: inferred only from caption wording; inspect the PDF image before reuse.
- Why it matters: potentially relevant; requires manual inspection
- Useful for our manuscript: maybe
- Similar figure/table for our paper: manual review first

### Located Figure/Table 19
- Source anchor: p.10
- Caption: 表 5 实验结果对比
- What it shows: inferred only from caption wording; inspect the PDF image before reuse.
- Why it matters: potentially relevant; requires manual inspection
- Useful for our manuscript: maybe
- Similar figure/table for our paper: manual review first


## 10. Results Reading Notes

- Source anchors: p.1, p.2, p.3, p.5, p.6, p.7, p.8, p.9, p.10, p.11, p.12
- Main experimental results: use only values and claims visible in the excerpts/PDF tables.
- Model comparison results: inspect metric/table captions before using exact rankings.
- Data source comparison results: record only where Sentinel/Landsat/GF/DEM evidence is explicit.
- FBR/bare-rock inversion results: separate continuous metrics from class metrics.
- Classification accuracy: report OA/Kappa/Precision/Recall/F1/IoU/mF1/mIoU only if explicitly found.
- DEM/topographic factor contribution: note only when DEM/topographic excerpts are explicit.
- Spatial distribution / uncertainty / significance: inspect maps and captions manually.

Located result/metric evidence:
- p.1: 摘 要 针对传统喀斯特地区裸岩提取方法成本高、精度低的问题，文章构建了一种基于改进
- p.1: 空间金字塔池化模块将不同空洞率的卷积层进行特征融合，提高信息的利用率。研究结果表明：文章方
- p.1: 法在不同场景裸岩提取任务中表现最好，模型参数量约为 DeepLabV3+的 1/13，交并比、 F1分数分别为
- p.1: The results show that the method in this paper performs best in the bare rock extraction tasks in
- p.2: ratio and F1-Score are 72.46% and 84.04% respectively.
- p.2: used semantic segmentation models, improving the accuracy of bare rock extraction.
- p.2: 分辨率的制约，提取精度往往较低；文献 [9]通过人工勾绘获取无人机影像裸岩率，并用其矫正相同研究
- p.2: 区Landsat8影像，通过指数法获取的裸岩率， 使 Landsat8影像提取裸岩的精度得到提高，但该方法工作
- p.2: 量大，效率低；文献 [10]基于无人机影像，通过面向对象的方法对裸岩信息进行提取，提取精度进一步提
- p.2: 无人机影像实现全卷积神经网络对石漠化地区裸岩信息的提取，提取精度优于传统提取方法，但其方法
- p.1: 法在不同场景裸岩提取任务中表现最好，模型参数量约为 DeepLabV3+的 1/13，交并比、 F1分数分别为
- p.1: Abstract Aiming at the problems of high cost and low precision of traditional bare rock extraction
- p.1: methods in karst areas, this paper constructs a bare rock extraction method based on improved DeepLabV3+.
- p.1: feature extraction, which greatly reduces the amount of model parameters.
- p.1: Finally, in the atrous spatial pyramid pooling
- p.1: The results show that the method in this paper performs best in the bare rock extraction tasks in


## 11. Discussion Reading Notes

- Source anchors: not located
- Mechanism explanations, data-source performance, terrain effects, comparison to previous studies, limitations, and future work should be extracted from these anchors only.
- Borrowable Discussion writing pattern: explain why a data/model/factor improves mapping, then tie the explanation to spatial patterns and validation evidence.

Located discussion/limitation evidence:
- not located


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
- DEM/topography support: not applicable. Reason: grounded signals were not located in the text layer.
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


## 15. Items Needing Manual Review

- year missing in database
- DOI missing in database
- DOI needs manual verification
- metadata incomplete
