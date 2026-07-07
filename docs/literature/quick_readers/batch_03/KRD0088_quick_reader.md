# Batch 03 Quick Reader: Extraction of Bare Rock Information in Rocky Desertification Area Based on Improved DeepLabV3+ WU Yongjun1 WANG Hong2,

## 1. Bibliographic Information

- Canonical paper ID: KRD0088
- Title: Extraction of Bare Rock Information in Rocky Desertification Area Based on Improved DeepLabV3+ WU Yongjun1 WANG Hong2,
- Authors: needs verification
- Year: needs verification
- Journal / Source: needs verification
- DOI: needs verification
- Language: needs verification
- PDF path: docs/literature/pdfs/package_2000_2026/CN003_DeepLabV3.pdf
- PDF mapping confidence: 1.00
- Why selected: Only PDF-backed DeepLabV3+ Chinese candidate not previously read; fills semantic segmentation gap.

## 2. Reading Scope

- Abstract: located
- Introduction: located
- Methods: located
- Results: located
- Discussion: not clearly located
- Figures/Tables: 8 caption signals located
- References: located
- PDF text layer: extractable text found
- Page count: 13

## 3. Core Scientific Contribution

本 quick reading 仅基于 PDF text layer 抽取，定位到该文与 DeepLabV3+ / semantic segmentation / Chinese literature 相关。 其可用于补强 Skill 的方法、术语或验证设计规则；具体数值结论未在本阶段强行复述，需回到原文核验。

## 4. Relevance to Skill Gaps

- FBR/fBR: high
- LSMM/SMA/MESMA/FCLS: medium
- ML classification: medium
- Deep learning / semantic segmentation: high
- DEM/topography: not applicable
- GF/Gaofen imagery: medium
- validation metrics: high
- Chinese literature coverage: not applicable
- Remote Sensing style: not applicable

## 5. Method Notes

- data source: Landsat
- preprocessing: 预处理的影像，通过ArcGIS进行人工标注制作标签。将制作好的标签 与原始影像进行同步处理，通过滑动窗口裁剪为512像素×512像素的影像，使用水平翻转、旋转、镜像 操作进行数据增广，最后得到2 000张影像，按照9∶1的比例随机划分训练集和验证集。 实验采用的操作系统为Ubuntu18.04，深度学习框架为PyTorch，使用的GPU为NVIDIA RTX 2080 Ti。训练超参数设置如下：迭代轮次（Epoch）为80，批大小（Batch Size）为4，动量为0.9，使用 Adam（Adaptive Moment Estimation）优化器，初始学习率为0.000 5，并通过余弦退火下
- target variable: Rocky Desertification Area Based on Improved DeepLabV3+ WU Yongjun1 WANG Hong2,* YANG Chen2 （ 1 Qianxi’nan Prefecture Natural Resource Management Service Center, Xingyi 562400, China ） （ 2 College of Mining, Guizhou University, Guiyang 550025, China ） Abstract Aiming at the problems of h
- model or algorithm: DeepLabV3+; RF
- features: feature extraction, which greatly reduces the amount of model parameters. Secondly, the features extracted by the encoder are enhanced through the feature pyramid network and the coordinate attention mechanism to obtain more small target information and reduce the loss of image details. Finally, in the atrous spatial pyramid pooling module, the
- DEM/topographic variables: not clearly extracted
- sample construction: 训练集和验证集。 实验采用的操作系统为Ubuntu18.04，深度学习框架为PyTorch，使用的GPU为NVIDIA RTX 2080 Ti。训练超参数设置如下：迭代轮次（Epoch）为80，批大小（Batch Size）为4，动量为0.9，使用 Adam（Adaptive Moment Estimation）优化器，初始学习率为0.000 5，并通过余弦退火下降调整策略自适 应调整学习率。 2.2 评价指标 选择交并比IOU（Intersection Over Union）、F1分数（F1-Score）、模型参数量作为本文的评价指标。 IOU表示真实值和预测值两个集合交集和并集之比，表示预测结果与标签像素的交叠率，是衡量图像分 割精度的重要指标，具体见公式（7）。F1是精确率P（Percision）和召回
- validation design: accuracy of bare rock extraction. Keywords bare rock extraction; deep learning; semantic segmentation; coordinate attention mechanism 0 引言 石漠化是我国西南地区最严重的生态环境问题之一，与沙漠化、水土流失并称为我国的三大生态灾 害[1-2]。石漠化是指在喀斯特地区，不合理的人类活动，自然植被遭到破坏，造成土壤流失、基岩裸露等 类似荒漠景观的土地退化过程。喀斯特石漠化严重的影响着区域生态环境，会导致水土流失、自然灾害 频发、生物多样性下降等生态危害[3]；其带来的危害已成为制约我国西南地区可持续发展的重要因素。 因此，石漠化的治理对我国西南地区改善生态环境、保障经济社会可持
- metrics: OA, Precision, Recall, F1, IoU

## 6. Important Figures and Tables

- Figure/Table number: item 1
  - caption: 图1所示。 深度卷积 神经网络 1×1 卷积 3×3 卷积 空洞率 6 3×3 卷积 空洞率 12 3×3 卷积 空洞率 18 全局平均 池化 1×1 卷积 4 倍 上采样 1×1 卷积 拼接 3×3 卷积 4 倍 上采样 编码器 解码器
  - what it supports: figure/table evidence signal for methods or results.
  - whether useful for our manuscript: useful if manually verified.
- Figure/Table number: item 2
  - caption: 图 1 DeepLabV3+模型结构
  - what it supports: figure/table evidence signal for methods or results.
  - whether useful for our manuscript: useful if manually verified.
- Figure/Table number: item 3
  - caption: Fig.1 DeepLabV3+ model structure 第 1 期 吴永俊 等: 基于改进 DeepLabV3+的石漠化地区裸岩信息提取 125 1.2 坐标注意力机制 注意力机制通过增强网络对目标特征的关注和忽 略无关信息来改善网络性能，可以有效地提升网络特 征提取的能力，被广泛应用于各种深度学习的任务中。 将其引入本文的网络，使得模型提升对裸岩目标的关 注度，忽略地物背景的干扰。CA将位置信息嵌入通 道注意力中，使网络获取更大区域的信息。坐标注意 力机制的实现主要有两个步骤：坐标信息的嵌入和坐 标注意
  - what it supports: figure/table evidence signal for methods or results.
  - whether useful for our manuscript: useful if manually verified.
- Figure/Table number: item 4
  - caption: 图2所示。 X 2 RCHW C H W 首先是坐标信息的嵌入。全局池化通常用于通道 注意力机制中对空间信息进行编码，但其将全局信息 压缩至一个通道内进行描述，会使位置信息难以保留。 因此，该部分将全局池化层分解成两个一维特征编码 操作，对于输入的特征图 ， 为特征图的 通道数， 为特征图的高， 为特征图的宽，使用大 (H; 1) (1; W) 小为 和 的池化核沿水平方向和垂直方向坐标进行通道编码，使模块能获取长范围依赖的信息， 其表达式如式（1）、（2）所示： Zh c(h)= 1 W ∑ 0≤i<W xc
  - what it supports: figure/table evidence signal for methods or results.
  - whether useful for our manuscript: useful if manually verified.
- Figure/Table number: item 5
  - caption: 图 2 坐标注意力机制
  - what it supports: figure/table evidence signal for methods or results.
  - whether useful for our manuscript: useful if manually verified.

## 7. Key Findings Relevant to Our Manuscript

- , respectively, and are superior to other commonly used semantic segmentation models, improving the accuracy of bare rock extraction. Keywords bare rock extraction; deep learning; semantic segmentation; coordinate attention mechanism 0 引言 石漠化是我国西南地区最严重的生态环境问题之一，与沙漠化、水土流失并称为我国的三大生态灾 害[1-2]。石漠化是指在喀斯特地区，不合理的人类活动，自然植被遭到破坏，造成土壤流失、基岩裸露等 类似荒漠景 (needs verification before using numerical claims)
- 吴永俊 1 汪泓 2,* 杨晨 2 （1 黔西南州自然资源管理服务中心，兴义 562400） （2 贵州大学矿业学院，贵阳 550025） 摘 要 针对传统喀斯特地区裸岩提取方法成本高、精度低的问题，文章构建了一种基于改进 DeepLabV3+的裸岩提取方法。该方法首先在编码器中用CA-DC-MobileNetV3替换DeepLabV3+骨干网 络Xception进行特征提取，很大程度上减少了模型的参数量；其次，将编码器提取的特征通过特征金字 塔网络和坐标注意力机制进行加强特征提取，以获取更多小目标信息并减少图像细节损失；最后在空洞 空间金字塔池化模块将不同空洞率的卷积层进行特征融合，提高信息的利用率。研究结果表明：文章方 法在不同场景裸岩提取任务中表现最好 (needs verification before using numerical claims)
- LabV3+的1/13，交并比、F1分数分别为 72.46%、84.03%，上述2个指标相比于DeepLabV3+模型分别提高了4.62和3.19个百分点，并优于其余 常用语义分割模型，提高了裸岩提取精度。 关键词 裸岩提取 深度学习 语义分割 坐标注意力机制 中图分类号：P237 文献标志码：A 文章编号：1009-8518(2024)01-0123-13 DOI：10.3969/j.issn.1009-8518.2024.01.011 Extraction of Bare Rock Information in Rocky Desertification Area Based on Improved DeepLabV3+ WU Yongjun1 (needs verification before using numerical claims)
- 类型的光谱特征，通过蓝光、近红外波段差和比，构建归一化裸岩指数 （Carbonate Rock Indice，CRI）对裸岩信息的提取，但遥感影像易受气候等因素的影响，且受影像空间 分辨率的制约，提取精度往往较低；文献[9]通过人工勾绘获取无人机影像裸岩率，并用其矫正相同研究 区Landsat8影像，通过指数法获取的裸岩率，使Landsat8影像提取裸岩的精度得到提高，但该方法工作 量大，效率低；文献[10]基于无人机影像，通过面向对象的方法对裸岩信息进行提取，提取精度进一步提 高，但喀斯特地区地表覆盖极其不规律，地物通常呈斑块状，破碎度较高，空间分布不均匀，岩石之间 大小形状不尽相同，分割的尺度和参数较难确定，需要反复调整相关阈值参数，人为划定的主观性强。 近年来，深度 (needs verification before using numerical claims)
- 素的影响，且受影像空间 分辨率的制约，提取精度往往较低；文献[9]通过人工勾绘获取无人机影像裸岩率，并用其矫正相同研究 区Landsat8影像，通过指数法获取的裸岩率，使Landsat8影像提取裸岩的精度得到提高，但该方法工作 量大，效率低；文献[10]基于无人机影像，通过面向对象的方法对裸岩信息进行提取，提取精度进一步提 高，但喀斯特地区地表覆盖极其不规律，地物通常呈斑块状，破碎度较高，空间分布不均匀，岩石之间 大小形状不尽相同，分割的尺度和参数较难确定，需要反复调整相关阈值参数，人为划定的主观性强。 近年来，深度学习在图像分割、目标检测等领域得到了广泛的应用。文献[11]基于“简译”软件与 无人机影像实现全卷积神经网络对石漠化地区裸岩信息的提取，提取精度优于传统提取方 (needs verification before using numerical claims)

## 8. What Should Be Added to Skill Source

- scientific rule: Treat this paper as supporting metadata for DeepLabV3+ / semantic segmentation / Chinese literature; do not generalize beyond extracted method signals.
- terminology: Add or confirm terms linked to deep_learning_segmentation and DeepLabV3+.
- warning: Numerical results and DOI/author metadata marked `needs verification` must not be reused without checking the original paper.
- experiment design implication: Use the paper to refine variables, feature construction, or validation checklist, not to replace project-specific experiments.
- writing implication: Mention this cluster as background support only after citation metadata is verified.

## 9. Manual Review Needed

- metadata uncertainty: yes
- PDF extraction issue: no major text-layer issue detected
- DOI needs check: yes
- figures/tables unclear: captions extracted but visual content still needs manual check
- result values need verification: yes
