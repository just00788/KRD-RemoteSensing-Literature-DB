# Full-Paper Reader: 顾及Vis-NIR光谱指数时序统计特征的红层荒漠化场景分类

## 1. Bibliographic Information

- Paper ID: KRD0076
- Title: 顾及Vis-NIR光谱指数时序统计特征的红层荒漠化场景分类
- Translated title if applicable: unknown
- Authors: 陈震等
- Year: 2025
- Journal / Source: 农业工程学报
- DOI: 10.11975/j.issn.1002-6819.202411052
- URL: https://www.aeeisp.com/nygcxb/cn/article/pdf/preview/10.11975/j.issn.1002-6819.202411052.pdf
- PDF path: `docs/literature/pdfs/package_2000_2026/顾及Vis-NIR光谱指数时序统计特征的红层荒漠化场景分类_陈震.pdf`
- Language: Chinese
- Readability status: ready
- Metadata status: complete

## 2. Reading Scope and Source Anchors

This reader was generated from the full selectable text layer of the PDF. It preserves page-level anchors and section/figure/table signals. It does not reproduce large original-text passages and does not fabricate missing metadata.

- Abstract: p.1, p.7, p.8, p.9, p.10
- Introduction: p.1
- Study Area: p.1, p.2, p.3, p.4, p.5, p.6, p.7
- Data: p.1, p.2, p.3, p.4, p.6, p.7, p.8, p.9, p.10
- Methods: p.1, p.2, p.3, p.4, p.5, p.6, p.7, p.8, p.9, p.10
- Experiments: p.1, p.4
- Results: p.1, p.2, p.3, p.4, p.5, p.6, p.7, p.10
- Discussion: p.6
- Conclusions: p.7
- References: not located
- Figures/Tables captions: 25 located
  - p.2: 图1 研究区地理位置示意图
  - p.2: Fig.1 Geographical location map of the study area
  - p.2: 表 1 Sentinel-2 L2A Vis-NIR部分波段信息
  - p.2: Table 1 Sentinel-2 L2A Vis-NIR (visible and near-infrared) bands
  - p.3: 图2 研究区典型地表覆盖场景真彩色合成影像
  - p.3: Fig.2 True color composite image of typical land cover scenes in
  - p.3: 图3 红层荒漠化场景分类技术路线
  - p.3: Fig.3 Technical route of classification of red-bed desertification scenes

## 3. Abstract-Level Understanding

Source anchors: p.1, p.2, p.3

基于可抽取的摘要文本，本研究逻辑可按以下方式理解。以下内容只依据摘要和题录可确认的信息，不补造缺失结论。

- 研究背景: 论文主题与 `machine_learning` 相关，关键词信号包括 `RF;SVM;vegetation_index`。
- 研究目标: 顾及Vis-NIR光谱指数时序统计特征的红层荒漠化场景分类
- 数据: 见下方 Data Sources 中从全文定位到的证据信号。
- 方法: 见下方 Method Workflow 中从全文定位到的证据信号。
- 主要结果: 仅在 Results Reading Notes 中记录可定位的结果/指标信号；未在此处编造具体数值。
- 意义: 其价值主要体现在对 KRD/FBR/分类/遥感制图/验证框架的支撑，具体等级见第 13 节。

Abstract evidence snippet:

> 荒漠化调查是区域土地修复、植被恢复与水土保持等农业整治工程的基础工作。而在东南丘陵区红层荒漠化的 多光谱遥感监测中，仅依靠单一时相影像有限的光谱特征，难以表征和区分红层区复杂地表覆盖类型。针对该问题，该 研究以湘赣北部交界的红层出露带为研究区，提出一种顾及Vis-NIR光谱指数时序统计特征的红层荒漠化场景多尺度分 层分类方法。研究首先在典型地表覆盖敏感指数基础上，基于时序统计分析方法，增强红层目标与其他地物覆盖的可分 性；然后结合面向对象影像分析技术和决策树分类方法，先后从像元尺度和对象尺度完成红层区纯净地物覆盖和荒漠化 混合场景覆盖分类;最后与随机森林（random forest，RF）和支持向量机（support vector machine，SVM）分类模型进行 对比分析。结果表明：敏感光谱指数的时序统计分析能够有效增强红层区典型覆盖场景的可分性；结合时序统计增强与 面向对象空间优化的分层决策模型相较于RF和SVM两类分类模型总体分类精度提高了3.04%、3.52%；其中对裸岩的 提取精确率为86.15%，召回率为89.31%，F1分数为0.88， F1分数相较于RF和SVM分别提高了4.76%和6.02%，有 效地减少了裸岩错分漏分，提高了红层荒漠化场景分类精度。该研究为荒漠化遥感调查提供了一种简单有效的技术方案， 也为赣西北红层荒漠化区域的土地修复等相关农业整治工作提供可靠的空间数据支持。

## 4. Introduction Reading Notes

- Source anchors: p.1
- Background unfolding: extracted introduction pages should be read around the anchors above; the parser located target/method signals listed below.
- Why the problem matters: only infer from located KRD/desertification/remote-sensing problem statements; do not add unsupported claims.
- Remote sensing role: see satellite/data excerpts in Section 5.
- Existing research categories: classification, FBR/LSMM/MESMA, ML, semantic segmentation, DEM/topography when signaled below.
- Existing research insufficiency / gap / objectives / contributions: inspect Introduction anchors manually for exact wording before using in manuscript.
- Borrowable point for our Introduction: build a clear progression from KRD importance -> remote-sensing monitoring -> method/data limitation -> our FBR/classification/DEM/cross-region contribution.

Located target/method evidence:
- p.1: 顾及Vis-NIR光谱指数时序统计特征的红层荒漠化场景分类
- p.1: 摘 要：荒漠化调查是区域土地修复、植被恢复与水土保持等农业整治工程的基础工作。而在东南丘陵区红层荒漠化的
- p.1: 研究以湘赣北部交界的红层出露带为研究区，提出一种顾及Vis-NIR光谱指数时序统计特征的红层荒漠化场景多尺度分
- p.1: 性；然后结合面向对象影像分析技术和决策树分类方法，先后从像元尺度和对象尺度完成红层区纯净地物覆盖和荒漠化
- p.1: 面向对象空间优化的分层决策模型相较于RF和SVM两类分类模型总体分类精度提高了3.04%、3.52%；其中对裸岩的
- p.1: 效地减少了裸岩错分漏分，提高了红层荒漠化场景分类精度。该研究为荒漠化遥感调查提供了一种简单有效的技术方案，
- p.1: 也为赣西北红层荒漠化区域的土地修复等相关农业整治工作提供可靠的空间数据支持。
- p.1: 关键词：遥感；决策树；特征优选；红层荒漠化；Vis-NIR光谱指数；时序统计；空间优化
- p.1: 顾及Vis-NIR光谱指数时序统计特征的红层荒漠化场景分类[J].
- p.1: 红层石漠化[2]。红层荒漠化引起的严重水土流失造成土
- p.1: 混合场景覆盖分类;最后与随机森林（random forest，RF）和支持向量机（support vector machine，SVM）分类模型进行
- p.1: 面向对象空间优化的分层决策模型相较于RF和SVM两类分类模型总体分类精度提高了3.04%、3.52%；其中对裸岩的
- p.1: 提取精确率为86.15%，召回率为89.31%，F1分数为0.88， F1分数相较于RF和SVM分别提高了4.76%和6.02%，有
- p.2: 球引擎（google earth engine, GEE）提供已完成大气校正


## 5. Study Area and Data Sources

- Study area: locate from Study Area anchors: p.1, p.2, p.3, p.4, p.5, p.6, p.7
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
- p.1: 以Landsat-8 OLI影像为基础建立二维SWIR-NIR、RedNIR和SWIR-Red反射率光谱特征空间，并以此构建三
- p.1: TAN等[17]利用Landsat-8 OLI影像，在像元尺度上基于
- p.2: 选取桂、滇和贵三地Landsat遥感影像和实地测量数据
- p.2: 球引擎（google earth engine, GEE）提供已完成大气校正
- p.2: 的Sentinel-2 L2A级影像作为数据源，该影像具有较高
- p.2: 的空间分辨率和时间分辨率。Sentinel-2的两颗卫星重访
- p.2: 为60 m[22]。表1列出了本文所使用的该卫星数据中VisNIR波段参数信息。GEE中设定该数据集云覆盖量20%
- p.2: 以下，并借助Sentinel-2 L2A衍生场景分类图层（scene
- p.2: 表 1 Sentinel-2 L2A Vis-NIR部分波段信息
- p.2: Table 1 Sentinel-2 L2A Vis-NIR (visible and near-infrared) bands


## 6. Target Variable or Classification System

- Target variable / object: derived from located evidence only.
- KRD/rocky desertification signal: yes
- FBR/fBR/bare-rock fraction signal: yes
- Semantic segmentation class signal: no
- If FBR/fBR is involved, treat it as a continuous/proportional variable unless the paper explicitly thresholds it into classes.
- If rocky desertification levels are involved, inspect the paper for the exact grade system before reuse.

Target evidence:
- p.1: 顾及Vis-NIR光谱指数时序统计特征的红层荒漠化场景分类
- p.1: 摘 要：荒漠化调查是区域土地修复、植被恢复与水土保持等农业整治工程的基础工作。而在东南丘陵区红层荒漠化的
- p.1: 研究以湘赣北部交界的红层出露带为研究区，提出一种顾及Vis-NIR光谱指数时序统计特征的红层荒漠化场景多尺度分
- p.1: 性；然后结合面向对象影像分析技术和决策树分类方法，先后从像元尺度和对象尺度完成红层区纯净地物覆盖和荒漠化
- p.1: 面向对象空间优化的分层决策模型相较于RF和SVM两类分类模型总体分类精度提高了3.04%、3.52%；其中对裸岩的
- p.1: 效地减少了裸岩错分漏分，提高了红层荒漠化场景分类精度。该研究为荒漠化遥感调查提供了一种简单有效的技术方案，
- p.1: 也为赣西北红层荒漠化区域的土地修复等相关农业整治工作提供可靠的空间数据支持。
- p.1: 关键词：遥感；决策树；特征优选；红层荒漠化；Vis-NIR光谱指数；时序统计；空间优化
- p.1: 顾及Vis-NIR光谱指数时序统计特征的红层荒漠化场景分类[J].
- p.1: 红层石漠化[2]。红层荒漠化引起的严重水土流失造成土


## 7. Method Workflow

The workflow below is derived from located method/data signals. Missing items are explicitly marked.
- preprocessing: located
- feature construction: located
- spectral indices: located
- DEM/topographic variables: located
- LSMM/SMA/MESMA/FCLS: not reported
- machine learning models: located
- deep learning models: not reported
- semantic segmentation architecture: located
- training strategy: located
- sample split: located
- cross-validation: not reported
- cross-region validation: not reported
- ablation design: not reported
- comparison methods: located

Located method/data evidence:
- p.1: 混合场景覆盖分类;最后与随机森林（random forest，RF）和支持向量机（support vector machine，SVM）分类模型进行
- p.1: 面向对象空间优化的分层决策模型相较于RF和SVM两类分类模型总体分类精度提高了3.04%、3.52%；其中对裸岩的
- p.1: 提取精确率为86.15%，召回率为89.31%，F1分数为0.88， F1分数相较于RF和SVM分别提高了4.76%和6.02%，有
- p.2: 球引擎（google earth engine, GEE）提供已完成大气校正
- p.2: 为60 m[22]。表1列出了本文所使用的该卫星数据中VisNIR波段参数信息。GEE中设定该数据集云覆盖量20%
- p.3: 注：R、G、B、NIR分别代表红、绿、蓝、近红外波段；NDWI为归一化水体指数；NDVI为归一化植被指数；NDRI归一化极差指数；NDIOI为归一化氧
- p.3: 化铁指数；DT为决策树算法；RF为随机森林算法；SVM为支持向量机算法；MHCM为多尺度分层分类方法。
- p.3: Note: R, G, B, and NIR represent red, green, blue, and near-infrared spectral bands, respectively; NDWI represents the normalized difference water index; NDVI
- p.3: represents the normalized difference vegetation index; NDRI represents the normalized difference range index; NDIOI represents the normalized difference iron oxide
- p.3: index; DT represents the decision tree algorithm; RF represents the random forest algorithm; SVM represents the support vector machine algorithm; MHCM represents
- p.3: NDVI增强植被及其动态变化信息[26]。建筑的平均反射
- p.3: 其他覆盖物，且生长植被的混合像元NDVI值往往高于
- p.1: 以Landsat-8 OLI影像为基础建立二维SWIR-NIR、RedNIR和SWIR-Red反射率光谱特征空间，并以此构建三
- p.1: TAN等[17]利用Landsat-8 OLI影像，在像元尺度上基于
- p.2: 选取桂、滇和贵三地Landsat遥感影像和实地测量数据
- p.2: 球引擎（google earth engine, GEE）提供已完成大气校正
- p.2: 的Sentinel-2 L2A级影像作为数据源，该影像具有较高
- p.2: 的空间分辨率和时间分辨率。Sentinel-2的两颗卫星重访
- p.2: 为60 m[22]。表1列出了本文所使用的该卫星数据中VisNIR波段参数信息。GEE中设定该数据集云覆盖量20%
- p.2: 以下，并借助Sentinel-2 L2A衍生场景分类图层（scene
- p.2: 表 1 Sentinel-2 L2A Vis-NIR部分波段信息
- p.2: Table 1 Sentinel-2 L2A Vis-NIR (visible and near-infrared) bands


## 8. Validation Strategy and Metrics

- Reference sample source: locate from excerpts below; manual confirmation recommended.
- Sample size: record only if explicitly visible in source excerpts; otherwise unknown.
- Train/test split: see located split/training evidence; otherwise not reported.
- Spatial split: located only if terms such as spatial/block split appear; otherwise not reported.
- Independent validation: located only if explicit evidence appears; otherwise not reported.
- Cross-region validation: located only if explicit evidence appears; otherwise not reported.

- Continuous-variable metrics located: not located
- Classification metrics located: OA, Kappa, Precision, Recall, F1, IoU

Metric evidence:
- p.1: 提取精确率为86.15%，召回率为89.31%，F1分数为0.88， F1分数相较于RF和SVM分别提高了4.76%和6.02%，有
- p.4: 过计算混淆矩阵，得到总体精度（overall accuracy, OA）、
- p.4: Kappa系数、精确率（Precision）、召回率（Recall）和F1
- p.4: Table 2 J-M(Jeffries-Matusita) distance between different samples in the preferred indies feature space
- p.5: Fig.7 Pixel-base misclassification comparison map of decision
- p.6: Table 3 Spatial optimization rules
- p.6: 提高3.04%、3.52%和2.87%； Kappa系数分别比RF 、
- p.6: 分类，其中MHCM在裸岩分类上，F1分数为0.88，精
- p.6: 确率为86.15%，召回率为89.31%，F1分数相较于RF
- p.6: Table 4 Comparison of the accuracy of each classification model
- p.7: Fig.8 Partial comparison of classification results from different classification models
- p.7: Kappa系数为0.92，其中裸岩的提取精确率为86.15%，


Important distinction enforced for our manuscript: continuous FBR inversion metrics (R2/RMSE/MAE/bias/slope) must not be mixed with classification metrics (OA/Kappa/Precision/Recall/F1/IoU/mF1/mIoU).

## 9. Figures and Tables

### Located Figure/Table 1
- Source anchor: p.2
- Caption: 图1 研究区地理位置示意图
- What it shows: inferred only from caption wording; inspect the PDF image before reuse.
- Why it matters: directly relevant to study design/results visualization
- Useful for our manuscript: yes
- Similar figure/table for our paper: consider

### Located Figure/Table 2
- Source anchor: p.2
- Caption: Fig.1 Geographical location map of the study area
- What it shows: inferred only from caption wording; inspect the PDF image before reuse.
- Why it matters: directly relevant to study design/results visualization
- Useful for our manuscript: yes
- Similar figure/table for our paper: consider

### Located Figure/Table 3
- Source anchor: p.2
- Caption: 表 1 Sentinel-2 L2A Vis-NIR部分波段信息
- What it shows: inferred only from caption wording; inspect the PDF image before reuse.
- Why it matters: potentially relevant; requires manual inspection
- Useful for our manuscript: maybe
- Similar figure/table for our paper: manual review first

### Located Figure/Table 4
- Source anchor: p.2
- Caption: Table 1 Sentinel-2 L2A Vis-NIR (visible and near-infrared) bands
- What it shows: inferred only from caption wording; inspect the PDF image before reuse.
- Why it matters: potentially relevant; requires manual inspection
- Useful for our manuscript: maybe
- Similar figure/table for our paper: manual review first

### Located Figure/Table 5
- Source anchor: p.3
- Caption: 图2 研究区典型地表覆盖场景真彩色合成影像
- What it shows: inferred only from caption wording; inspect the PDF image before reuse.
- Why it matters: directly relevant to study design/results visualization
- Useful for our manuscript: yes
- Similar figure/table for our paper: consider

### Located Figure/Table 6
- Source anchor: p.3
- Caption: Fig.2 True color composite image of typical land cover scenes in
- What it shows: inferred only from caption wording; inspect the PDF image before reuse.
- Why it matters: potentially relevant; requires manual inspection
- Useful for our manuscript: maybe
- Similar figure/table for our paper: manual review first

### Located Figure/Table 7
- Source anchor: p.3
- Caption: 图3 红层荒漠化场景分类技术路线
- What it shows: inferred only from caption wording; inspect the PDF image before reuse.
- Why it matters: directly relevant to study design/results visualization
- Useful for our manuscript: yes
- Similar figure/table for our paper: consider

### Located Figure/Table 8
- Source anchor: p.3
- Caption: Fig.3 Technical route of classification of red-bed desertification scenes
- What it shows: inferred only from caption wording; inspect the PDF image before reuse.
- Why it matters: directly relevant to study design/results visualization
- Useful for our manuscript: yes
- Similar figure/table for our paper: consider

### Located Figure/Table 9
- Source anchor: p.4
- Caption: 表2所示。对每一类地表覆盖类型选择J-M距离均值最
- What it shows: inferred only from caption wording; inspect the PDF image before reuse.
- Why it matters: potentially relevant; requires manual inspection
- Useful for our manuscript: maybe
- Similar figure/table for our paper: manual review first

### Located Figure/Table 10
- Source anchor: p.4
- Caption: 表 2 不同样本在优选特征空间下的J-M距离
- What it shows: inferred only from caption wording; inspect the PDF image before reuse.
- Why it matters: potentially relevant; requires manual inspection
- Useful for our manuscript: maybe
- Similar figure/table for our paper: manual review first

### Located Figure/Table 11
- Source anchor: p.4
- Caption: Table 2 J-M(Jeffries-Matusita) distance between different samples in the preferred indies feature space
- What it shows: inferred only from caption wording; inspect the PDF image before reuse.
- Why it matters: directly relevant to study design/results visualization
- Useful for our manuscript: yes
- Similar figure/table for our paper: consider

### Located Figure/Table 12
- Source anchor: p.5
- Caption: 图4 最优时序统计增强特征灰度图
- What it shows: inferred only from caption wording; inspect the PDF image before reuse.
- Why it matters: potentially relevant; requires manual inspection
- Useful for our manuscript: maybe
- Similar figure/table for our paper: manual review first

### Located Figure/Table 13
- Source anchor: p.5
- Caption: Fig.4 Grascale image of optimal time-series statistical
- What it shows: inferred only from caption wording; inspect the PDF image before reuse.
- Why it matters: potentially relevant; requires manual inspection
- Useful for our manuscript: maybe
- Similar figure/table for our paper: manual review first

### Located Figure/Table 14
- Source anchor: p.5
- Caption: 图5 样本在优选特征下的灰度图
- What it shows: inferred only from caption wording; inspect the PDF image before reuse.
- Why it matters: potentially relevant; requires manual inspection
- Useful for our manuscript: maybe
- Similar figure/table for our paper: manual review first

### Located Figure/Table 15
- Source anchor: p.5
- Caption: Fig.5 Grayscale image of the sample under optimal features
- What it shows: inferred only from caption wording; inspect the PDF image before reuse.
- Why it matters: directly relevant to study design/results visualization
- Useful for our manuscript: yes
- Similar figure/table for our paper: consider

### Located Figure/Table 16
- Source anchor: p.5
- Caption: 图6 基于时序统计特征的红层场景决策分类模型
- What it shows: inferred only from caption wording; inspect the PDF image before reuse.
- Why it matters: directly relevant to study design/results visualization
- Useful for our manuscript: yes
- Similar figure/table for our paper: consider

### Located Figure/Table 17
- Source anchor: p.5
- Caption: Fig.6 Decision-based classification model for red-bed scenes
- What it shows: inferred only from caption wording; inspect the PDF image before reuse.
- Why it matters: directly relevant to study design/results visualization
- Useful for our manuscript: yes
- Similar figure/table for our paper: consider

### Located Figure/Table 18
- Source anchor: p.5
- Caption: 图7 基于像元的决策分类结果局部错分对比图
- What it shows: inferred only from caption wording; inspect the PDF image before reuse.
- Why it matters: directly relevant to study design/results visualization
- Useful for our manuscript: yes
- Similar figure/table for our paper: consider

### Located Figure/Table 19
- Source anchor: p.5
- Caption: Fig.7 Pixel-base misclassification comparison map of decision
- What it shows: inferred only from caption wording; inspect the PDF image before reuse.
- Why it matters: directly relevant to study design/results visualization
- Useful for our manuscript: yes
- Similar figure/table for our paper: consider

### Located Figure/Table 20
- Source anchor: p.6
- Caption: 表 3 空间优化规则
- What it shows: inferred only from caption wording; inspect the PDF image before reuse.
- Why it matters: potentially relevant; requires manual inspection
- Useful for our manuscript: maybe
- Similar figure/table for our paper: manual review first

### Located Figure/Table 21
- Source anchor: p.6
- Caption: Table 3 Spatial optimization rules
- What it shows: inferred only from caption wording; inspect the PDF image before reuse.
- Why it matters: potentially relevant; requires manual inspection
- Useful for our manuscript: maybe
- Similar figure/table for our paper: manual review first

### Located Figure/Table 22
- Source anchor: p.6
- Caption: 表4所示。MHCM的总体精度分别比RF 、SVM和DT
- What it shows: inferred only from caption wording; inspect the PDF image before reuse.
- Why it matters: directly relevant to study design/results visualization
- Useful for our manuscript: yes
- Similar figure/table for our paper: consider

### Located Figure/Table 23
- Source anchor: p.6
- Caption: 图8为不同分类结果的局部放大图，对比来看，不
- What it shows: inferred only from caption wording; inspect the PDF image before reuse.
- Why it matters: directly relevant to study design/results visualization
- Useful for our manuscript: yes
- Similar figure/table for our paper: consider

### Located Figure/Table 24
- Source anchor: p.6
- Caption: 表 4 各分类模型精度对比
- What it shows: inferred only from caption wording; inspect the PDF image before reuse.
- Why it matters: directly relevant to study design/results visualization
- Useful for our manuscript: yes
- Similar figure/table for our paper: consider

### Located Figure/Table 25
- Source anchor: p.6
- Caption: Table 4 Comparison of the accuracy of each classification model
- What it shows: inferred only from caption wording; inspect the PDF image before reuse.
- Why it matters: directly relevant to study design/results visualization
- Useful for our manuscript: yes
- Similar figure/table for our paper: consider


## 10. Results Reading Notes

- Source anchors: p.1, p.2, p.3, p.4, p.5, p.6, p.7, p.10
- Main experimental results: use only values and claims visible in the excerpts/PDF tables.
- Model comparison results: inspect metric/table captions before using exact rankings.
- Data source comparison results: record only where Sentinel/Landsat/GF/DEM evidence is explicit.
- FBR/bare-rock inversion results: separate continuous metrics from class metrics.
- Classification accuracy: report OA/Kappa/Precision/Recall/F1/IoU/mF1/mIoU only if explicitly found.
- DEM/topographic factor contribution: note only when DEM/topographic excerpts are explicit.
- Spatial distribution / uncertainty / significance: inspect maps and captions manually.

Located result/metric evidence:
- p.1: 对比分析。结果表明：敏感光谱指数的时序统计分析能够有效增强红层区典型覆盖场景的可分性；结合时序统计增强与
- p.1: 面向对象空间优化的分层决策模型相较于RF和SVM两类分类模型总体分类精度提高了3.04%、3.52%；其中对裸岩的
- p.1: 提取精确率为86.15%，召回率为89.31%，F1分数为0.88， F1分数相较于RF和SVM分别提高了4.76%和6.02%，有
- p.1: 效地减少了裸岩错分漏分，提高了红层荒漠化场景分类精度。该研究为荒漠化遥感调查提供了一种简单有效的技术方案，
- p.4: 淆，同时混合像元的存在降低了分类精度[28]。而单一的
- p.4: 分类模型结果进行对比，以评价模型的分类性能。DT是
- p.4: 精度高等优势在遥感信息提取领域取得良好效果[37-38]。
- p.4: 过计算混淆矩阵，得到总体精度（overall accuracy, OA）、
- p.4: Kappa系数、精确率（Precision）、召回率（Recall）和F1
- p.4: 分数等评价指标，进而对分类结果进行定量评价[39]。
- p.1: 提取精确率为86.15%，召回率为89.31%，F1分数为0.88， F1分数相较于RF和SVM分别提高了4.76%和6.02%，有
- p.4: 过计算混淆矩阵，得到总体精度（overall accuracy, OA）、
- p.4: Kappa系数、精确率（Precision）、召回率（Recall）和F1
- p.4: Table 2 J-M(Jeffries-Matusita) distance between different samples in the preferred indies feature space
- p.5: Fig.7 Pixel-base misclassification comparison map of decision
- p.6: Table 3 Spatial optimization rules


## 11. Discussion Reading Notes

- Source anchors: p.6
- Mechanism explanations, data-source performance, terrain effects, comparison to previous studies, limitations, and future work should be extracted from these anchors only.
- Borrowable Discussion writing pattern: explain why a data/model/factor improves mapping, then tie the explanation to spatial patterns and validation evidence.

Located discussion/limitation evidence:
- not located


## 12. Conclusion Reading Notes

- Source anchors: p.7
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
- Discussion comparison support: not applicable. Reason: grounded signals were not located in the text layer.
- limitations support: not applicable. Reason: grounded signals were not located in the text layer.
- figure/table design support: high. Reason: grounded signals were located in the text layer.
- terminology support: high. Reason: grounded signals were located in the text layer.
- Remote Sensing writing style support: not applicable. Reason: grounded signals were not located in the text layer.

## 14. Reusable Knowledge for Future Skill

### Scientific rules
- Relevant target/method signals: machine_learning; RF;SVM;vegetation_index.
- Located target evidence pages: p.1, p.1, p.1, p.1, p.1, p.1.
- Located metric evidence pages: p.1, p.4, p.4, p.4, p.5, p.6.

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

- references section not located by text parser
