# Batch 03 Quick Reader: 面向对象的喀斯特地区石漠化遥感信息提取研究——以贵州省……为例

## 1. Bibliographic Information

- Canonical paper ID: KRD0027
- Title: 面向对象的喀斯特地区石漠化遥感信息提取研究——以贵州省……为例
- Authors: needs verification
- Year: 2018
- Journal / Source: 地质力学学报
- DOI: 10.12090/j.issn.1006-6616.2018.24.02.028
- Language: Chinese
- PDF path: docs/literature/pdfs/package_2000_2026/面向对象的喀斯特地区石漠化遥感信息提取研究——以贵州省大方地区为例_周迪.pdf
- PDF mapping confidence: 1.00
- Why selected: Verified Chinese object-oriented KRD information extraction paper with terrain/texture signals.

## 2. Reading Scope

- Abstract: located
- Introduction: not clearly located
- Methods: located
- Results: located
- Discussion: not clearly located
- Figures/Tables: 8 caption signals located
- References: located
- PDF text layer: extractable text found
- Page count: 11

## 3. Core Scientific Contribution

本 quick reading 仅基于 PDF text layer 抽取，定位到该文与 Chinese method literature / DEM-topography / object-oriented classification 相关。 其可用于补强 Skill 的方法、术语或验证设计规则；具体数值结论未在本阶段强行复述，需回到原文核验。

## 4. Relevance to Skill Gaps

- FBR/fBR: medium
- LSMM/SMA/MESMA/FCLS: low
- ML classification: not applicable
- Deep learning / semantic segmentation: not applicable
- DEM/topography: high
- GF/Gaofen imagery: high
- validation metrics: high
- Chinese literature coverage: high
- Remote Sensing style: high

## 5. Method Notes

- data source: Landsat; DEM
- preprocessing: 预处理 鉴 于中等分辨率的 Landsat影像选择的分割尺 度可以得到较高精度的分类结果 ，而高分数据由 于发射时间的原因 ，不利于开展时序方面的研究 ， 且不能将建立在 Landsat影像的分类规则直接应用 于高分数据 ，会产生分类精度误差 。因此 ，采用 美国地质调查局网站提供的免费 、易获取 、覆盖 范围广的三景 LandsatTM / ETM +影像，时间分别为 1988- 9- 15、2002- 8- 29和 2016- 9- 21， 分 辨 率 为 30 m ，轨道号为 128 /41，影像的预处理主要包括 辐射 校 正、几 何 校 正、影像裁剪和坐标转换等 。 此外，由于岩溶石漠
- target variable: rocky desertification information extraction accuracy in karst rocky desertification area under the circumstances of complicated geological environment，large topographic relief and obvious shadows． In order to improve the accuracy of remote sensing image information extraction，texture feature data a
- model or algorithm: vegetation index; time series
- features: feature data and topographic data are used to assist the object oriented method in the rocky desertification information extraction in karst rocky desertification area． Firstly，based on the characteristics of rocky 地 质 力 学 学 报 2018 desertification with uneven image sizes in TM / ETM +， the optimal segmentation parameters are calculated using texture and terr
- DEM/topographic variables: DEM 数据，运用 Arcgis软件平台提取坡度 、高程作 为重要辅助因子参与多尺度影像分割 (见图 4)。 图 4 坡 度和 NDVI 信息提取结果 Fig. 4 Ｒesults of gradient and NDVI information extraction 3 石漠化遥感影像信息提取 3. 1 最优分割尺度的确定 为 获取分割的最佳尺度 ，起始分割阀值设为 5 ，并以 5 为单位依次递增进行分割 ，当分割阈值 增加到 105 时，会出现较严重的 “过分割 ” 现象， 因此不再提高分割尺度 。通过计算各个分割阈值 所得多边形面积的均值方差 ，可得到均值方差曲 线图 (见图 5 ) ，不同地物类别的最佳分割尺 度就 是每个峰值对应的分割尺度 。结果表明 ，该曲线 一共有 3 处峰值 (方差曲线极大值 )
- sample construction: 样本质量较好的基础上完 成的，并且分类规则较单一 。而大方县石漠化分 布极不均匀 ，具有不同尺度的斑块效应 ，采用单 一尺度的分类规则不能满足石漠化信息提取的精 度需求，因此需考虑多尺度分割的分类规则 。 鉴于此，在之前学者的研究基础上 ，针 对 石 漠化区域的地质背景复杂的情况 ，采用基于纹理 特征数据和地形辅助的面向对象分类方法 ，通过 纹理和地形因子计算最优分割参数对遥感影像进 行多尺度分割 ;然后依据不同石漠化程度在植被 覆盖度、纹理、亮度等方面的差异建立分类规则 ， 快速地提取石漠化信息 ，避免石漠化信息提取中 只依靠光谱特征带来的限制 ，减少基于像素的监 督分类和非监督分类产生的 “椒盐现象 ”，分类精 度明显提高 。同时结合多时相遥感监测结果 ，较 好地反映出大方地区石漠化分布范围的变化情况 ，
- validation design: accuracy in karst rocky desertification area under the circumstances of complicated geological environment，large topographic relief and obvious shadows． In order to improve the accuracy of remote sensing image information extraction，texture feature data and topographic data are used to assist the object oriented method in the rocky desertification informatio
- metrics: OA, Kappa, IoU

## 6. Important Figures and Tables

- Figure/Table number: item 1
  - caption: 图 1) ，总 面积为 2746 km 2 。大 方县位于低纬度高 海拔地区，属亚热带湿润季风气候 ，年平均气温 11. 8 ℃ ，年平均降雨量 1155 mm ，降水多集中在 4 ～ 9 月。山脉多呈东北西南走向 ，地势西南高东北 低。研究区碳酸盐岩分布广泛 ，岩溶地形较为发 育，地 表 的松散土层以及碎屑物质的堆积较少 ， 露头较好;砂、泥岩分布 ，常形成构造侵蚀地形 。 石漠化发育地区 ，主要位于乌蒙山脉南麓的黔西 高原向黔中山原丘陵过渡的斜坡地带 ，属中山地 貌类型。根据地貌的成因 ，研究区地貌可分成岩 溶
  - what it supports: figure/table evidence signal for methods or results.
  - whether useful for our manuscript: useful if manually verified.
- Figure/Table number: item 2
  - caption: 图 1 研 究区位置图
  - what it supports: figure/table evidence signal for methods or results.
  - whether useful for our manuscript: useful if manually verified.
- Figure/Table number: item 3
  - caption: Fig. 1 Location map of the study area 2 研究方法与数据来源 2. 1 原理与技术流程 面 向对象分类方法主要包括四个部分 :遥感 影像的分割 、定义类层次结构 、建立分类规则以 及信息提取 ，具体通过多尺度技术分割划分成大 小不同的对象 ，提取出符合实际目标的地物信息 。 技术流程见
  - what it supports: figure/table evidence signal for methods or results.
  - whether useful for our manuscript: useful if manually verified.
- Figure/Table number: item 4
  - caption: 图 2，首先基于纹理特征与地形数据进 行影像多尺度分割 ，再利用对象的空间特征和光 谱特征等定义类层次结构 ，并在隶属度函数分类 的过程中结合 NDVI 、地形数据 、纹理特征数据等 多源信息，对提取出的石漠化信息进行精度评价 。
  - what it supports: figure/table evidence signal for methods or results.
  - whether useful for our manuscript: useful if manually verified.
- Figure/Table number: item 5
  - caption: 图 2 石漠化遥感影像信息提取流程图
  - what it supports: figure/table evidence signal for methods or results.
  - whether useful for our manuscript: useful if manually verified.

## 7. Key Findings Relevant to Our Manuscript

- classification methods can' t meet the requirements of rocky desertification information extraction accuracy in karst rocky desertification area under the circumstances of complicated geological environment，large topographic relief and obvious shadows． In order to improve the accuracy of remote sensing image information extraction，texture (needs verification before using numerical claims)
- icated geological environment，large topographic relief and obvious shadows． In order to improve the accuracy of remote sensing image information extraction，texture feature data and topographic data are used to assist the object oriented method in the rocky desertification information extraction in karst rocky desertification area． Firstly (needs verification before using numerical claims)
- fectively reduce the“salt and pepper phenomenon”caused by complicated topography，and the extraction accuracy is much better． Key words : karst rocky desertification; object- oriented classification; supervised classification; unsupervised classification;information extraction;Dafang County 0 引 言 贵 州省大方地区石漠化分布面积广 ，类型多 样，在人类活动的影响下 ，石漠化的程度加剧 (needs verification before using numerical claims)
- 方 9 6 2 地 质 力 学 学 报 2018 法，地 物内部存在较多 “椒盐 ” 点，不能准确对 地物进行分类 。 表 5 分类方法精度对比表 Table 5 Comparison of the accuracy of each method 方 法 监督分类 非监督分类 面向对象分类 年份 1988 年 2002年 2016年 1988 年 2002年 2016年 1988 年 2002年 2016年 总 体精度 72. 15% 78. 81% 76. 43% 62. 50% 63. 25% 72. 90% 91. 45% 93. 56% 95. 31% Kappa 系 数 0. 65 0. 71 0. 68 0. 54 0. 55 0. 58 0. 9 0. 92 (needs verification before using numerical claims)
- 样本点 ，其 中喀斯特地区样点 246个，非喀斯特地区样点 154 个。通过混淆矩阵计算得到生产者精度为 94. 56% ， 用 户 精 度 95. 43% ， 总 体 精 度 为 95. 31% ，Kappa 系数为 0. 94。由表 5 可知，三个 年份信息提取的精度 ，面向对象分类方法的精度 最高，分类效果较好 ，证明了这种方法在石漠化 信息提取方面具有一定的优势 。而基于像素的监 督分类得到的分类效果一般 ，分类过程略显繁琐 ， 分类精度最高为 78. 81% 。对于基于像素的非监督 分类， 过 程 简 单， 操 作 快 捷， 分类精度最高为 72. 9% ，Kappa 系数为 0. 58 ，分类的后处理过程较 麻烦，结果误差较大 ，分类精度远不如前两种方 9 6 (needs verification before using numerical claims)

## 8. What Should Be Added to Skill Source

- scientific rule: Treat this paper as supporting metadata for Chinese method literature / DEM-topography / object-oriented classification; do not generalize beyond extracted method signals.
- terminology: Add or confirm terms linked to deep_learning_segmentation and DEM_ablation.
- warning: Numerical results and DOI/author metadata marked `needs verification` must not be reused without checking the original paper.
- experiment design implication: Use the paper to refine variables, feature construction, or validation checklist, not to replace project-specific experiments.
- writing implication: Mention this cluster as background support only after citation metadata is verified.

## 9. Manual Review Needed

- metadata uncertainty: yes
- PDF extraction issue: no major text-layer issue detected
- DOI needs check: no
- figures/tables unclear: captions extracted but visual content still needs manual check
- result values need verification: yes
