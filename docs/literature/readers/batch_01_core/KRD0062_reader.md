# Full-Paper Reader: 基于无人机影像与Sentinel-2影像的基岩裸露率反演与石漠化程度评价

## 1. Bibliographic Information

- Paper ID: KRD0062
- Title: 基于无人机影像与Sentinel-2影像的基岩裸露率反演与石漠化程度评价
- Translated title if applicable: unknown
- Authors: unknown
- Year: 2024
- Journal / Source: 百度学术条目/学位论文
- DOI: unknown
- URL: https://xueshu.baidu.com/usercenter/paper/show?paperid=1g7704h0692f0090v50t08c0nt344512
- PDF path: `docs/literature/pdfs/package_2000_2026/基于无人机影像与Sentinel-2影像的基岩裸露率反演与石漠化程度评价_赵喆.pdf`
- Language: Chinese
- Readability status: ready
- Metadata status: metadata_incomplete

## 2. Reading Scope and Source Anchors

This reader was generated from the full selectable text layer of the PDF. It preserves page-level anchors and section/figure/table signals. It does not reproduce large original-text passages and does not fabricate missing metadata.

- Abstract: p.2, p.3, p.4, p.5
- Introduction: p.6, p.8, p.9, p.10, p.11, p.12, p.13, p.14, p.15, p.16, p.17
- Study Area: p.6, p.9, p.10, p.12, p.13, p.15, p.16, p.17, p.18, p.19, p.20, p.22, ...
- Data: p.2, p.4, p.5, p.6, p.7, p.9, p.10, p.11, p.12, p.13, p.15, p.16, ...
- Methods: p.2, p.4, p.5, p.6, p.7, p.9, p.10, p.11, p.12, p.13, p.14, p.15, ...
- Experiments: p.2, p.4, p.5, p.6, p.7, p.16, p.17, p.18, p.19, p.20, p.21, p.22, ...
- Results: p.2, p.3, p.5, p.6, p.7, p.8, p.9, p.10, p.11, p.12, p.13, p.14, ...
- Discussion: not located
- Conclusions: p.2, p.4, p.7, p.17, p.56, p.70, p.71
- References: p.7, p.72, p.73, p.74, p.75, p.76, p.77
- Figures/Tables captions: 25 located
  - p.16: 图 1.1 技术路线图
  - p.18: 图 2.1 研究区概况
  - p.19: 表 2.1 无人机数据采集指标
  - p.20: 图 2.2 无人机影像获取流程
  - p.21: 图 2.3 无人机拼接影像
  - p.22: 表 2.2 Sentinel-2A 波段参数
  - p.22: 图 2.4 去云方法效果对比
  - p.23: 图 2.5 WHU 建筑数据集

## 3. Abstract-Level Understanding

Source anchors: p.1, p.2, p.3

基于可抽取的摘要文本，本研究逻辑可按以下方式理解。以下内容只依据摘要和题录可确认的信息，不补造缺失结论。

- 研究背景: 论文主题与 `bare_rock_fraction_fbr` 相关，关键词信号包括 `DEM_ablation`。
- 研究目标: 基于无人机影像与Sentinel-2影像的基岩裸露率反演与石漠化程度评价
- 数据: 见下方 Data Sources 中从全文定位到的证据信号。
- 方法: 见下方 Method Workflow 中从全文定位到的证据信号。
- 主要结果: 仅在 Results Reading Notes 中记录可定位的结果/指标信号；未在此处编造具体数值。
- 意义: 其价值主要体现在对 KRD/FBR/分类/遥感制图/验证框架的支撑，具体等级见第 13 节。

Abstract evidence snippet:

> I 摘 要 喀斯特岩溶石漠化是亚热带岩溶地区的自然演化和人类过度活动所导致的 生态退化现象。该现象对于当地的生态环境以及全球生态平衡都造成了不可忽 视的威胁。基岩裸露率作为判断石漠化程度的核心指标，是石漠化程度分级的 主要依据。已有研究所采用的数据 以中低分辨率的遥感影像提取石漠化信息为 主，但提取效果往往不够理想。 提取方法以目视解译选择样本训练分类为主， 存在很大的主观性。随 着机器视觉技术的快速发展，以深度学习为代表的图像 处理技术给石漠化的准确分析带来了可能。Google Earth Engine云平台具有海量 遥感数据存储、处理和可视化的能力。Sentinel-2 遥感影像具有数据免费且分辨 率较高的优势。为此，本文依托 Google Earth Engine 云平台，以滇东喀斯特高 原为例，提出了一种基于无人机影像和 Sentinel-2 遥感影像的基岩裸露率深度学 习反演方法，对滇东喀斯特高原石漠化 程度进行评估 。主要研究内容和结论如 下： （1）基于 迁移学习 的无人机影像 裸岩信息提取。首先 ，将获取的无人机 影像集划分训练集、测试集和验证集，并制作裸岩信息的标签；其次，采用迁 移学习的方法，利用卷积神经网络在大规模遥感建筑分类数据集上预训练，再 将预训练的模型迁移到裸岩信息提取的模型中 ，通过微调参数再次训练，实现 裸岩信息的精确提取，解决了训练样本较少、训练时间长等问题。 结果表明： 通过预训练模型，使得在少量样本数据的情况下， 实验结果有着较高的精度。 经过迁移学习 ResNet50 模型，其总体精度达到了 0.9727、交并比为 0.8552、F

## 4. Introduction Reading Notes

- Source anchors: p.6, p.8, p.9, p.10, p.11, p.12, p.13, p.14, p.15, p.16, p.17
- Background unfolding: extracted introduction pages should be read around the anchors above; the parser located target/method signals listed below.
- Why the problem matters: only infer from located KRD/desertification/remote-sensing problem statements; do not add unsupported claims.
- Remote sensing role: see satellite/data excerpts in Section 5.
- Existing research categories: classification, FBR/LSMM/MESMA, ML, semantic segmentation, DEM/topography when signaled below.
- Existing research insufficiency / gap / objectives / contributions: inspect Introduction anchors manually for exact wording before using in manuscript.
- Borrowable point for our Introduction: build a clear progression from KRD importance -> remote-sensing monitoring -> method/data limitation -> our FBR/classification/DEM/cross-region contribution.

Located target/method evidence:
- p.1: 英文题目： Study of bedrock exposure rate inversion
- p.2: 喀斯特岩溶石漠化是亚热带岩溶地区的自然演化和人类过度活动所导致的
- p.2: 视的威胁。基岩裸露率作为判断石漠化程度的核心指标，是石漠化程度分级的
- p.2: 主要依据。已有研究所采用的数据 以中低分辨率的遥感影像提取石漠化信息为
- p.2: 处理技术给石漠化的准确分析带来了可能。Google Earth Engine云平台具有海量
- p.2: 原为例，提出了一种基于无人机影像和 Sentinel-2 遥感影像的基岩裸露率深度学
- p.2: 习反演方法，对滇东喀斯特高原石漠化 程度进行评估 。主要研究内容和结论如
- p.2: （1）基于 迁移学习 的无人机影像 裸岩信息提取。首先 ，将获取的无人机
- p.2: 影像集划分训练集、测试集和验证集，并制作裸岩信息的标签；其次，采用迁
- p.2: 将预训练的模型迁移到裸岩信息提取的模型中 ，通过微调参数再次训练，实现
- p.5: have high accuracy in the case of a small amount of sample data.
- p.5: set as the independent variable; finally, the performance evaluation and a ccuracy
- p.11: 与其他土地覆盖类型的不同光谱响应，使用不同输入波段（Landsat TM 波段 35、NDVI 和 NDRI 来自 TM 图像）的监督最大似然分类试验评估了中国西南部
- p.11: 一个卷积神经网络（CNN），基于 USDA 的 0.6 m 国家航空库存计划（NAIP）


## 5. Study Area and Data Sources

- Study area: locate from Study Area anchors: p.6, p.9, p.10, p.12, p.13, p.15, p.16, p.17, p.18, p.19, p.20, p.22, ...
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
- p.1: 论文题目：基于无人机影像与 Sentinel-2 影像的
- p.1: UA V and Sentinel-2 images
- p.2: 处理技术给石漠化的准确分析带来了可能。Google Earth Engine云平台具有海量
- p.2: 遥感数据存储、处理和可视化的能力。Sentinel-2 遥感影像具有数据免费且分辨
- p.2: 率较高的优势。为此，本文依托 Google Earth Engine 云平台，以滇东喀斯特高
- p.2: 原为例，提出了一种基于无人机影像和 Sentinel-2 遥感影像的基岩裸露率深度学
- p.2: （2）基于 Sentinel-2 影像和回归模型的基岩裸露率反演。根据 Sentinel-2 影
- p.3: 关键词：迁移学习；无人机影像；Sentinel-2 反演；回归模型；滇东喀斯特
- p.4: training classification of s elected samples, which is very subjective.
- p.4: Google Earth Engin e cloud platform has the ability to store, process


## 6. Target Variable or Classification System

- Target variable / object: derived from located evidence only.
- KRD/rocky desertification signal: yes
- FBR/fBR/bare-rock fraction signal: yes
- Semantic segmentation class signal: no
- If FBR/fBR is involved, treat it as a continuous/proportional variable unless the paper explicitly thresholds it into classes.
- If rocky desertification levels are involved, inspect the paper for the exact grade system before reuse.

Target evidence:
- p.1: 英文题目： Study of bedrock exposure rate inversion
- p.2: 喀斯特岩溶石漠化是亚热带岩溶地区的自然演化和人类过度活动所导致的
- p.2: 视的威胁。基岩裸露率作为判断石漠化程度的核心指标，是石漠化程度分级的
- p.2: 主要依据。已有研究所采用的数据 以中低分辨率的遥感影像提取石漠化信息为
- p.2: 处理技术给石漠化的准确分析带来了可能。Google Earth Engine云平台具有海量
- p.2: 原为例，提出了一种基于无人机影像和 Sentinel-2 遥感影像的基岩裸露率深度学
- p.2: 习反演方法，对滇东喀斯特高原石漠化 程度进行评估 。主要研究内容和结论如
- p.2: （1）基于 迁移学习 的无人机影像 裸岩信息提取。首先 ，将获取的无人机
- p.2: 影像集划分训练集、测试集和验证集，并制作裸岩信息的标签；其次，采用迁
- p.2: 将预训练的模型迁移到裸岩信息提取的模型中 ，通过微调参数再次训练，实现


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
- cross-validation: located
- cross-region validation: located
- ablation design: not reported
- comparison methods: located

Located method/data evidence:
- p.5: have high accuracy in the case of a small amount of sample data.
- p.5: set as the independent variable; finally, the performance evaluation and a ccuracy
- p.11: 与其他土地覆盖类型的不同光谱响应，使用不同输入波段（Landsat TM 波段 35、NDVI 和 NDRI 来自 TM 图像）的监督最大似然分类试验评估了中国西南部
- p.11: 一个卷积神经网络（CNN），基于 USDA 的 0.6 m 国家航空库存计划（NAIP）
- p.13: 型，并考虑改进模型的空间和时间维度的准确性。结果表明 SVM 表现最好，模
- p.13: 85.21%。与随机森林（ RF） 和袋 装决 策 树（BDT） 方 法 相 比，极 端 随机 数
- p.22: （2）Sentinel-2 数据预处理。本文通过 Google Earth Engine（GEE）获取与
- p.24: 本文提取裸岩信息使用的开发语言是 Python 以及 TensorFlow 深度学习开源
- p.24: 与原型的开发[40]。TensorFlow 是谷歌 2015 年发布的一款深度学习框架，其具有
- p.24: 境；其次安装与 TensorFlow 版本号对应 的并行计算架构 （Cuda10.1），再安装
- p.24: TensorFlow_gpu-2.3.0； 最后需要安装 python 相 关 的 依 赖 库 ， 如 ：NumPy、
- p.24: 深度学习框架 TensorFlow_gpu-2.3.0
- p.1: 论文题目：基于无人机影像与 Sentinel-2 影像的
- p.1: UA V and Sentinel-2 images
- p.2: 处理技术给石漠化的准确分析带来了可能。Google Earth Engine云平台具有海量
- p.2: 遥感数据存储、处理和可视化的能力。Sentinel-2 遥感影像具有数据免费且分辨
- p.2: 率较高的优势。为此，本文依托 Google Earth Engine 云平台，以滇东喀斯特高
- p.2: 原为例，提出了一种基于无人机影像和 Sentinel-2 遥感影像的基岩裸露率深度学
- p.2: （2）基于 Sentinel-2 影像和回归模型的基岩裸露率反演。根据 Sentinel-2 影
- p.3: 关键词：迁移学习；无人机影像；Sentinel-2 反演；回归模型；滇东喀斯特
- p.4: training classification of s elected samples, which is very subjective.
- p.4: Google Earth Engin e cloud platform has the ability to store, process


## 8. Validation Strategy and Metrics

- Reference sample source: locate from excerpts below; manual confirmation recommended.
- Sample size: record only if explicitly visible in source excerpts; otherwise unknown.
- Train/test split: see located split/training evidence; otherwise not reported.
- Spatial split: located only if terms such as spatial/block split appear; otherwise not reported.
- Independent validation: located only if explicit evidence appears; otherwise not reported.
- Cross-region validation: located only if explicit evidence appears; otherwise not reported.

- Continuous-variable metrics located: R2, RMSE, slope
- Classification metrics located: OA, overall accuracy, Kappa, Precision, Recall, F1, IoU, confusion matrix

Metric evidence:
- p.1: UA V and Sentinel-2 images
- p.2: 经过迁移学习 ResNet50 模型，其总体精度达到了 0.9727、交并比为 0.8552、F1
- p.2: 行性能评估和精度验证。结果表明：对比不同回归模型的 R2 和 RMSE，最终得
- p.2: 到反演结果较好的梯度提升树回归模型，其 R2 为 0.725、RMSE 为 7.37%。
- p.4: judging the degree of rock desertification, is the principal index for grading the degree
- p.4: Methods Visual interpretation is the main
- p.4: and visualize massive remote sensing data.
- p.4: depth learning inversion method of bedrock exposed rate based on UA V images and
- p.4: Sentinel-2 remote sensing images is proposed to evaluate the degree of rocky
- p.4: (1) Extracting naked rock information from UA V images based on migration
- p.4: Firstly, divide the acquired UA V image set into training sets and test sets, and
- p.4: for extracting naked rock i nformation, fine -tuning the parameter training idea for


Important distinction enforced for our manuscript: continuous FBR inversion metrics (R2/RMSE/MAE/bias/slope) must not be mixed with classification metrics (OA/Kappa/Precision/Recall/F1/IoU/mF1/mIoU).

## 9. Figures and Tables

### Located Figure/Table 1
- Source anchor: p.16
- Caption: 图 1.1 技术路线图
- What it shows: inferred only from caption wording; inspect the PDF image before reuse.
- Why it matters: potentially relevant; requires manual inspection
- Useful for our manuscript: maybe
- Similar figure/table for our paper: manual review first

### Located Figure/Table 2
- Source anchor: p.18
- Caption: 图 2.1 研究区概况
- What it shows: inferred only from caption wording; inspect the PDF image before reuse.
- Why it matters: directly relevant to study design/results visualization
- Useful for our manuscript: yes
- Similar figure/table for our paper: consider

### Located Figure/Table 3
- Source anchor: p.19
- Caption: 表 2.1 无人机数据采集指标
- What it shows: inferred only from caption wording; inspect the PDF image before reuse.
- Why it matters: potentially relevant; requires manual inspection
- Useful for our manuscript: maybe
- Similar figure/table for our paper: manual review first

### Located Figure/Table 4
- Source anchor: p.20
- Caption: 图 2.2 无人机影像获取流程
- What it shows: inferred only from caption wording; inspect the PDF image before reuse.
- Why it matters: directly relevant to study design/results visualization
- Useful for our manuscript: yes
- Similar figure/table for our paper: consider

### Located Figure/Table 5
- Source anchor: p.21
- Caption: 图 2.3 无人机拼接影像
- What it shows: inferred only from caption wording; inspect the PDF image before reuse.
- Why it matters: potentially relevant; requires manual inspection
- Useful for our manuscript: maybe
- Similar figure/table for our paper: manual review first

### Located Figure/Table 6
- Source anchor: p.22
- Caption: 表 2.2 Sentinel-2A 波段参数
- What it shows: inferred only from caption wording; inspect the PDF image before reuse.
- Why it matters: potentially relevant; requires manual inspection
- Useful for our manuscript: maybe
- Similar figure/table for our paper: manual review first

### Located Figure/Table 7
- Source anchor: p.22
- Caption: 图 2.4 去云方法效果对比
- What it shows: inferred only from caption wording; inspect the PDF image before reuse.
- Why it matters: potentially relevant; requires manual inspection
- Useful for our manuscript: maybe
- Similar figure/table for our paper: manual review first

### Located Figure/Table 8
- Source anchor: p.23
- Caption: 图 2.5 WHU 建筑数据集
- What it shows: inferred only from caption wording; inspect the PDF image before reuse.
- Why it matters: potentially relevant; requires manual inspection
- Useful for our manuscript: maybe
- Similar figure/table for our paper: manual review first

### Located Figure/Table 9
- Source anchor: p.24
- Caption: 表 2.3 实验软硬件环境
- What it shows: inferred only from caption wording; inspect the PDF image before reuse.
- Why it matters: potentially relevant; requires manual inspection
- Useful for our manuscript: maybe
- Similar figure/table for our paper: manual review first

### Located Figure/Table 10
- Source anchor: p.25
- Caption: 图 2.6 Google Earth Engine 云平台
- What it shows: inferred only from caption wording; inspect the PDF image before reuse.
- Why it matters: potentially relevant; requires manual inspection
- Useful for our manuscript: maybe
- Similar figure/table for our paper: manual review first

### Located Figure/Table 11
- Source anchor: p.25
- Caption: 图 2.6 展示了 GEE 云平台计算文山州的 NDVI 的操作界面。该界面主要分
- What it shows: inferred only from caption wording; inspect the PDF image before reuse.
- Why it matters: potentially relevant; requires manual inspection
- Useful for our manuscript: maybe
- Similar figure/table for our paper: manual review first

### Located Figure/Table 12
- Source anchor: p.26
- Caption: 图 3.1：首先采用 Canny 算法制作无人机影像标签，对数据集和标签进行裁剪，
- What it shows: inferred only from caption wording; inspect the PDF image before reuse.
- Why it matters: potentially relevant; requires manual inspection
- Useful for our manuscript: maybe
- Similar figure/table for our paper: manual review first

### Located Figure/Table 13
- Source anchor: p.26
- Caption: 图 3.1 基于迁移学习的无人机影像裸岩提取流程
- What it shows: inferred only from caption wording; inspect the PDF image before reuse.
- Why it matters: directly relevant to study design/results visualization
- Useful for our manuscript: yes
- Similar figure/table for our paper: consider

### Located Figure/Table 14
- Source anchor: p.27
- Caption: 图 3.2 影像标签制作流程
- What it shows: inferred only from caption wording; inspect the PDF image before reuse.
- Why it matters: directly relevant to study design/results visualization
- Useful for our manuscript: yes
- Similar figure/table for our paper: consider

### Located Figure/Table 15
- Source anchor: p.28
- Caption: 图 3.3 最佳分割阈值选择
- What it shows: inferred only from caption wording; inspect the PDF image before reuse.
- Why it matters: potentially relevant; requires manual inspection
- Useful for our manuscript: maybe
- Similar figure/table for our paper: manual review first

### Located Figure/Table 16
- Source anchor: p.29
- Caption: 图 3.4 中值滤波去除噪声
- What it shows: inferred only from caption wording; inspect the PDF image before reuse.
- Why it matters: potentially relevant; requires manual inspection
- Useful for our manuscript: maybe
- Similar figure/table for our paper: manual review first

### Located Figure/Table 17
- Source anchor: p.30
- Caption: 图 3.5 展现了影像矢量化的结果。通过 Canny 算法得到了裸岩的边缘信息，
- What it shows: inferred only from caption wording; inspect the PDF image before reuse.
- Why it matters: potentially relevant; requires manual inspection
- Useful for our manuscript: maybe
- Similar figure/table for our paper: manual review first

### Located Figure/Table 18
- Source anchor: p.30
- Caption: 图 3.5 数据集样例图
- What it shows: inferred only from caption wording; inspect the PDF image before reuse.
- Why it matters: potentially relevant; requires manual inspection
- Useful for our manuscript: maybe
- Similar figure/table for our paper: manual review first

### Located Figure/Table 19
- Source anchor: p.31
- Caption: 图 3.6 数据增强
- What it shows: inferred only from caption wording; inspect the PDF image before reuse.
- Why it matters: potentially relevant; requires manual inspection
- Useful for our manuscript: maybe
- Similar figure/table for our paper: manual review first

### Located Figure/Table 20
- Source anchor: p.32
- Caption: 图 3.7 传统机器学习与迁移学习对比
- What it shows: inferred only from caption wording; inspect the PDF image before reuse.
- Why it matters: potentially relevant; requires manual inspection
- Useful for our manuscript: maybe
- Similar figure/table for our paper: manual review first

### Located Figure/Table 21
- Source anchor: p.34
- Caption: 表 3.1 高分建筑影像与无人机裸岩影像相似性对比
- What it shows: inferred only from caption wording; inspect the PDF image before reuse.
- Why it matters: potentially relevant; requires manual inspection
- Useful for our manuscript: maybe
- Similar figure/table for our paper: manual review first

### Located Figure/Table 22
- Source anchor: p.34
- Caption: 图 3.8 VGG16 原始网络模型
- What it shows: inferred only from caption wording; inspect the PDF image before reuse.
- Why it matters: potentially relevant; requires manual inspection
- Useful for our manuscript: maybe
- Similar figure/table for our paper: manual review first

### Located Figure/Table 23
- Source anchor: p.35
- Caption: 图 3.9 残差结构示意图
- What it shows: inferred only from caption wording; inspect the PDF image before reuse.
- Why it matters: potentially relevant; requires manual inspection
- Useful for our manuscript: maybe
- Similar figure/table for our paper: manual review first

### Located Figure/Table 24
- Source anchor: p.37
- Caption: 图 3.10 预训练模型改进示意图
- What it shows: inferred only from caption wording; inspect the PDF image before reuse.
- Why it matters: potentially relevant; requires manual inspection
- Useful for our manuscript: maybe
- Similar figure/table for our paper: manual review first

### Located Figure/Table 25
- Source anchor: p.37
- Caption: 图 3.11 基于一次迁移学习遥感建筑提取结果
- What it shows: inferred only from caption wording; inspect the PDF image before reuse.
- Why it matters: potentially relevant; requires manual inspection
- Useful for our manuscript: maybe
- Similar figure/table for our paper: manual review first


## 10. Results Reading Notes

- Source anchors: p.2, p.3, p.5, p.6, p.7, p.8, p.9, p.10, p.11, p.12, p.13, p.14, ...
- Main experimental results: use only values and claims visible in the excerpts/PDF tables.
- Model comparison results: inspect metric/table captions before using exact rankings.
- Data source comparison results: record only where Sentinel/Landsat/GF/DEM evidence is explicit.
- FBR/bare-rock inversion results: separate continuous metrics from class metrics.
- Classification accuracy: report OA/Kappa/Precision/Recall/F1/IoU/mF1/mIoU only if explicitly found.
- DEM/topographic factor contribution: note only when DEM/topographic excerpts are explicit.
- Spatial distribution / uncertainty / significance: inspect maps and captions manually.

Located result/metric evidence:
- p.1: 通过预训练模型，使得在少量样本数据的情况下， 实验结果有着较高的精度。
- p.1: 经过迁移学习 ResNet50 模型，其总体精度达到了 0.9727、交并比为 0.8552、F1
- p.1: 行性能评估和精度验证。结果表明：对比不同回归模型的 R2 和 RMSE，最终得
- p.1: 到反演结果较好的梯度提升树回归模型，其 R2 为 0.725、RMSE 为 7.37%。
- p.2: 对比分析近 5 年来石漠化治理成效。结果表明：2016 年以来，滇东喀斯特高原
- p.3: The results show that through pre-training, the experimental results
- p.3: have high accuracy in the case of a small amount of sample data.
- p.3: the overall accuracy of the ResNet50 model reached 0.9727, the intersection to parallel
- p.3: ratio was 0.8552, and the F1 score was 0.9212.
- p.3: The results show that the gradient
- p.1: UA V and Sentinel-2 images
- p.2: 经过迁移学习 ResNet50 模型，其总体精度达到了 0.9727、交并比为 0.8552、F1
- p.2: 行性能评估和精度验证。结果表明：对比不同回归模型的 R2 和 RMSE，最终得
- p.2: 到反演结果较好的梯度提升树回归模型，其 R2 为 0.725、RMSE 为 7.37%。
- p.4: judging the degree of rock desertification, is the principal index for grading the degree
- p.4: Methods Visual interpretation is the main


## 11. Discussion Reading Notes

- Source anchors: not located
- Mechanism explanations, data-source performance, terrain effects, comparison to previous studies, limitations, and future work should be extracted from these anchors only.
- Borrowable Discussion writing pattern: explain why a data/model/factor improves mapping, then tie the explanation to spatial patterns and validation evidence.

Located discussion/limitation evidence:
- p.12: 具有一定的局限性。Jie Pei[13]基于 Landsat8 光谱特征构建了喀斯特岩石裸露指
- p.16: 分析了现阶段研究的局限性，并提出了本文的研究内容及研究方法。
- p.31: 学习能力。迁移学习在面对 数据集规模较小 、高度专业化的局限性时， 往往能
- p.61: 术提取岩性的局限性，本文参考童立强 [73]针对西南地区石漠化遥感调查结果，
- p.7: 第 6 章 结论与展望 ................................................................................
- p.7: 6.2 研究展望 .........................................................................................
- p.10: 不仅解决了训练样本不足、模型训练时间过长等问题，提高了裸岩提取的精度，
- p.12: 具有一定的局限性。Jie Pei[13]基于 Landsat8 光谱特征构建了喀斯特岩石裸露指
- p.16: 分析了现阶段研究的局限性，并提出了本文的研究内容及研究方法。
- p.17: 第 6 章：结论与展望。总结本文各部分研究内容的主要实验结果和结论，
- p.31: 学习能力。迁移学习在面对 数据集规模较小 、高度专业化的局限性时， 往往能
- p.32: 模型的输出变化等任务时， 可能会受到限制， 导致模型的泛化能力不足。


## 12. Conclusion Reading Notes

- Source anchors: p.2, p.4, p.7, p.17, p.56, p.70, p.71
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
- Discussion comparison support: medium. Reason: grounded signals were located in the text layer.
- limitations support: medium. Reason: grounded signals were located in the text layer.
- figure/table design support: medium. Reason: grounded signals were located in the text layer.
- terminology support: medium. Reason: grounded signals were located in the text layer.
- Remote Sensing writing style support: medium. Reason: grounded signals were located in the text layer.

## 14. Reusable Knowledge for Future Skill

### Scientific rules
- Relevant target/method signals: bare_rock_fraction_fbr; DEM_ablation.
- Located target evidence pages: p.1, p.2, p.2, p.2, p.2, p.2.
- Located metric evidence pages: p.1, p.2, p.2, p.2, p.4, p.4.

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
