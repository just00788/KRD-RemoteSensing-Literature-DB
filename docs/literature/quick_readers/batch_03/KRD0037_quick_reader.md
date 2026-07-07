# Batch 03 Quick Reader: 基于多时相Sentinel-2遥感数据的石漠化程度识别方法研究

## 1. Bibliographic Information

- Canonical paper ID: KRD0037
- Title: 基于多时相Sentinel-2遥感数据的石漠化程度识别方法研究
- Authors: Baidu Scholar listing
- Year: 2021
- Journal / Source: 中文学位/期刊检索结果
- DOI: needs verification
- Language: Chinese
- PDF path: docs/literature/pdfs/package_2021_2026/基于多时相Sentinel-2遥感数据的石漠化程度识别方法研究_徐瑞.pdf
- PDF mapping confidence: 1.00
- Why selected: Chinese multi-temporal Sentinel-2 KRD degree identification paper.

## 2. Reading Scope

- Abstract: located
- Introduction: located
- Methods: located
- Results: located
- Discussion: not clearly located
- Figures/Tables: 8 caption signals located
- References: located
- PDF text layer: low text on at least one page; use caution
- Page count: 88

## 3. Core Scientific Contribution

本 quick reading 仅基于 PDF text layer 抽取，定位到该文与 Chinese literature / Sentinel-2 time-series / KRD degree classification 相关。 其可用于补强 Skill 的方法、术语或验证设计规则；具体数值结论未在本阶段强行复述，需回到原文核验。

## 4. Relevance to Skill Gaps

- FBR/fBR: high
- LSMM/SMA/MESMA/FCLS: high
- ML classification: medium
- Deep learning / semantic segmentation: medium
- DEM/topography: high
- GF/Gaofen imagery: high
- validation metrics: high
- Chinese literature coverage: high
- Remote Sensing style: high

## 5. Method Notes

- data source: Sentinel-2; Landsat; DEM
- preprocessing: 预处理 ................................................................................... 14 2.2.1 Sentinel-2 数据 ............................................................................................................. 14 2.2.2 Sentinel-2 L1C 数据预处理 ...............................................
- target variable: Rocky Desertification Degree Based on Multi-temporal Sentinel -2 Remote Sensing Data 学 院 地理学部 专业名称 地图学与地理信息系统 研究方向 遥感技术应用研究 研究生姓名 徐 瑞 学号 1923130063 导 师 姓名 史正涛 职称 教 授 2022 年 5 月 26 日 摘要 I 摘要 石漠化是喀斯特地区在社会因素和自然因素共同作用下 形成的特殊荒漠化 景观，
- model or algorithm: RF; vegetation index; time series
- features: feature vector, Principal Component Analysis(PCA) can predict that the target land cover is a dark pixel or a bright target object in the corresponding PCA image, and the first prin cipal component (PC1) has the highest contribution rate, so choose PC1 as another feature of rocky desertification, and the results show that PC1 is positively correlated wit
- DEM/topographic variables: DEM 数据与预处理 .................................................................................................... 22 2.2.4 样本数据 ..................................................................................................................... 23 2.2.5 岩性分布数据 ..................................................................................................
- sample construction: 样本数据 ..................................................................................................................... 23 2.2.5 岩性分布数据 ............................................................................................................. 25 2.3 本章小结 .................................................................................................
- validation design: accuracy of rocky desertification obtained by the combination of EVI - NDRI2 and PC1 based on the FastTWDTW algorithm is 85.68%, and the Kappa coefficient is 0.81. The classification accuracy is better than other rocky desertification characteristic time series data, CART and comprehensive analysis methods. The comparison methods were divided into two cat
- metrics: OA, Kappa, IoU, R2

## 6. Important Figures and Tables

- Figure/Table number: item 1
  - caption: 图 1.1 技术路线 .................................................................................................... 9
  - what it supports: figure/table evidence signal for methods or results.
  - whether useful for our manuscript: useful if manually verified.
- Figure/Table number: item 2
  - caption: 图 2.1 研究区位置 .............................................................................................. 12
  - what it supports: figure/table evidence signal for methods or results.
  - whether useful for our manuscript: useful if manually verified.
- Figure/Table number: item 3
  - caption: 图 2.2 Fmask 算法流程图.................................................................................... 17
  - what it supports: figure/table evidence signal for methods or results.
  - whether useful for our manuscript: useful if manually verified.
- Figure/Table number: item 4
  - caption: 图 2.3 云、云阴影识别结果 .............................................................................. 19
  - what it supports: figure/table evidence signal for methods or results.
  - whether useful for our manuscript: useful if manually verified.
- Figure/Table number: item 5
  - caption: 图 2.4 有效像元搜索流程 .................................................................................. 21
  - what it supports: figure/table evidence signal for methods or results.
  - whether useful for our manuscript: useful if manually verified.

## 7. Key Findings Relevant to Our Manuscript

- cators such as rocky desertification identification and degree were optimized. The classification accuracy of rocky desertification obtained by the combination of EVI - NDRI2 and PC1 based on the FastTWDTW algorithm is 85.68%, and the Kappa coefficient is 0.81. The classification accuracy is better than other rocky desertification cha (needs verification before using numerical claims)
- based on the FastTWDTW algorithm is 85.68%, and the Kappa coefficient is 0.81. The classification accuracy is better than other rocky desertification characteristic time series data, CART and comprehensive analysis methods. The comparison methods were divided into two categories. One was based on the FastTWDTW algorithm, which compar (needs verification before using numerical claims)
- n information, and the combination of EVI-NDRI2 and PC1, it can effectively improve the extraction accuracy of rocky desertification. The second category was to compare the classification results obtained by the combination of EVI-NDRI2 and PC1 based on the FastTWDTW algorithm with the commonly used rocky desertification extraction me (needs verification before using numerical claims)
- 2 … Pn2 P+2 … … … … … … n P1n P2n … Pnn P+n 分类总和 P1+ P2+ … Pn+ P 由上表可分析得到混淆矩阵的三个统计量：总体精度（Overal accuracy, 第 5 章 基于 FastTWDTW 算法的石漠化程度识别与精度评价 45 OA），用户精度（User’s Accuracy，UA），生产者精度（Productor accuracy， PA），OA，UA和PA的计算公式分别如下所示[24]： 1 n aaa OA pp    （5.1） (needs verification before using numerical claims)
- 由上表可分析得到混淆矩阵的三个统计量：总体精度（Overal accuracy, 第 5 章 基于 FastTWDTW 算法的石漠化程度识别与精度评价 45 OA），用户精度（User’s Accuracy，UA），生产者精度（Productor accuracy， PA），OA，UA和PA的计算公式分别如下所示[24]： 1 n aaa OA pp    （5.1） ii i UA pp   （5.2） (needs verification before using numerical claims)

## 8. What Should Be Added to Skill Source

- scientific rule: Treat this paper as supporting metadata for Chinese literature / Sentinel-2 time-series / KRD degree classification; do not generalize beyond extracted method signals.
- terminology: Add or confirm terms linked to gee_time_series and time_series.
- warning: Numerical results and DOI/author metadata marked `needs verification` must not be reused without checking the original paper.
- experiment design implication: Use the paper to refine variables, feature construction, or validation checklist, not to replace project-specific experiments.
- writing implication: Mention this cluster as background support only after citation metadata is verified.

## 9. Manual Review Needed

- metadata uncertainty: yes
- PDF extraction issue: yes; low-text pages or weak section extraction detected
- DOI needs check: yes
- figures/tables unclear: captions extracted but visual content still needs manual check
- result values need verification: yes
