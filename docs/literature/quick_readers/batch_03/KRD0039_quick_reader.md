# Batch 03 Quick Reader: 遥感植被指数增强石漠化信息研究

## 1. Bibliographic Information

- Canonical paper ID: KRD0039
- Title: 遥感植被指数增强石漠化信息研究
- Authors: Unknown from OPAJ listing
- Year: 2021
- Journal / Source: 中文期刊（开放检索页）
- DOI: needs verification
- Language: Chinese
- PDF path: docs/literature/pdfs/package_2000_2026/遥感植被指数增强石漠化信息研究_叶杰.pdf
- PDF mapping confidence: 1.00
- Why selected: Chinese vegetation-index enhancement paper; useful for index and KRD information extraction rules.

## 2. Reading Scope

- Abstract: located
- Introduction: not clearly located
- Methods: located
- Results: located
- Discussion: located
- Figures/Tables: 8 caption signals located
- References: located
- PDF text layer: extractable text found
- Page count: 6

## 3. Core Scientific Contribution

本 quick reading 仅基于 PDF text layer 抽取，定位到该文与 vegetation index / Chinese method literature / KRD extraction 相关。 其可用于补强 Skill 的方法、术语或验证设计规则；具体数值结论未在本阶段强行复述，需回到原文核验。

## 4. Relevance to Skill Gaps

- FBR/fBR: medium
- LSMM/SMA/MESMA/FCLS: low
- ML classification: high
- Deep learning / semantic segmentation: not applicable
- DEM/topography: high
- GF/Gaofen imagery: high
- validation metrics: high
- Chinese literature coverage: high
- Remote Sensing style: high

## 5. Method Notes

- data source: Landsat; DEM
- preprocessing: 校正、几何校正、裁剪等预处 理。影像数据无云层遮盖，图像结构清晰，数据质量 较好。 1.3 石漠化分级 本文以裸岩基岩占总面积的比例 （或植被覆盖面 积占比） 、植被种类等作为石漠化遥感评价的主要指 标，结合研究区植被覆盖特征，在 DZ/T 0190-2015 《区域环境地质勘查遥感技术规定 （1∶50 000 ） 》中石 漠化程度分级标准的基础上，增加了潜在石漠化类型， 将石漠化程度由弱到强依次划分为潜在石漠化 （PR）、 轻度石漠化 （LR） 、中度石漠化 （MR） 和重度石漠化 （SR）4 个等级。 1.4 评价方法 地表植被的覆盖和基岩裸露 （裸岩） 的状况呈负 相关，碳酸
- target variable: 裸岩基岩占总面积的比例 （或植被覆盖面 积占比） 、植被种类等作为石漠化遥感评价的主要指 标，结合研究区植被覆盖特征，在 DZ/T 0190-2015 《区域环境地质勘查遥感技术规定 （1∶50 000 ） 》中石 漠化程度分级标准的基础上，增加了潜在石漠化类型， 将石漠化程度由弱到强依次划分为潜在石漠化 （PR）、 轻度石漠化 （LR） 、中度石漠化 （MR） 和重度石漠化 （SR）4 个等级。 1.4 评价方法 地表植被的覆盖和基岩裸露 （裸岩） 的状况呈负 相关，碳酸盐岩地区裸岩的裸露率与石漠化程度呈正 相关，因此地表植被的覆盖度能较好地反映岩溶石漠 化的分布情况，可利用植被指数来提
- model or algorithm: RF; SVM; vegetation index; object-oriented classification; time series
- features: Index ( Vol.19,No.9)GEOSPATIAL INFORMATION ·IV· Multi-temporal Remote Sensing Images of Natural Resources Intelligent Matching Method by SHI Dichao Abstract Remote sensing image is one of the basic data for natural resource assets inspection. And time series image matching is the key for multi-temporal remote sensing data to evaluate natural resource ass
- DEM/topographic variables: demonstrate advantages to some degree. The “vegetation index characteristics + Euclidean distance + confusion matrix” method can screen the optimal vegetation index, which can significantly enhance the effect of stony desertification extraction. This method is not only suitable for Karst areas, but also has reference significance in desertification area
- sample construction: training and optimization for the ship recognition mission with cloud occlusion. The maximum F1-Score of the processing results is up to 0.725 3. The trained network model has the capacity of ship target recognition, and the experimental results can prove the validity and accuracy of this method. Key words remote sensing image processing, deep learning, c
- validation design: accuracy is low. In this paper, we proposed CNN-SIFT descriptor based on visual field perception. We used the siamese network that was sensitive to visual differences to extract the visual field difference characteristics of the same name points, and adjusted the visual field adaptively according to the degree of flatness, which could enhance the matchin
- metrics: OA, Kappa, Precision, F1, IoU

## 6. Important Figures and Tables

- Figure/Table number: item 1
  - caption: 图 1 所示。 研究区属北亚热带向暖温带过渡的季风性气候区，雨 量充沛，年降雨量为 391.3 ～ 1 423.7 mm，多年平均降 雨量为 804.3 mm；地域分布不均匀，具有西北多、东 南少的特点。水源区属长江流域汉江水系，丹江自西 北向东南纵贯全境；主要支流包括淇河、老鹳河等， 分别在寺湾、马蹬汇入丹江干流，控制流域面积均在 1 000 km 2 以上。研究区形态呈西北—东南分布，区内 地形地貌由西北向东南依次为侵蚀中山、侵蚀低山向 丘陵与岗地、冲击平原等过渡；区内石炭系、奥陶系、 寒武系、震旦系地层均有分
  - what it supports: figure/table evidence signal for methods or results.
  - whether useful for our manuscript: useful if manually verified.
- Figure/Table number: item 2
  - caption: 图 1 研究区遥感影像
  - what it supports: figure/table evidence signal for methods or results.
  - whether useful for our manuscript: useful if manually verified.
- Figure/Table number: item 3
  - caption: 图 1.2 影像数据源 本文选取1996-10-18、2006-10-14、2016-11-10 三期 月份相近的 30 m 分辨率 Landsat TM/OLI 多光谱数据 作为石漠化程度信息增强与提取的数据源。所有数据 均经过辐射定标、大气校正、几何校正、裁剪等预处 理。影像数据无云层遮盖，图像结构清晰，数据质量 较好。 1.3 石漠化分级 本文以裸岩基岩占总面积的比例 （或植被覆盖面 积占比） 、植被种类等作为石漠化遥感评价的主要指 标，结合研究区植被覆盖特征，在 DZ/T 0190-2015 《区域环境地质
  - what it supports: figure/table evidence signal for methods or results.
  - whether useful for our manuscript: useful if manually verified.
- Figure/Table number: item 4
  - caption: 表 1）对研究区石漠化信息增强的效果；并利用 “植被指数特征 + 欧氏距离 + 混淆矩阵” 的方法对上述 6 种植被指数增强石漠化的可分性与识别能力进行了定 量评价。
  - what it supports: figure/table evidence signal for methods or results.
  - whether useful for our manuscript: useful if manually verified.
- Figure/Table number: item 5
  - caption: 表 1 植被指数模型 植被指数 模型 备注 RVI RVI = ρ ρ NIR R ERVI ERVI = C CSWIR1 NIR NIR SWIR1ρ ρ CNIR、CSWIR1 分别为 NIR、 SWIR1 波段的 亮度平均值 NDVI NDVI = ρρ ρρ NIR R NIR R + − PNDVI PNDVI = ρ ρρρ ρ ρρρ NIR B G R NIR B G R + ++ − ++() () EVI EVI = ρρ ρNIR R B 2.5( ) +− +6 7.5 1 ρρNIR R
  - what it supports: figure/table evidence signal for methods or results.
  - whether useful for our manuscript: useful if manually verified.

## 7. Key Findings Relevant to Our Manuscript

- e are few correct matching points obtained by traditional image matching method, and the matching accuracy is low. In this paper, we proposed CNN-SIFT descriptor based on visual field perception. We used the siamese network that was sensitive to visual differences to extract the visual field difference characteristics of the same nam (needs verification before using numerical claims)
- ding to the degree of flatness, which could enhance the matching ability and improve the matching accuracy. Experimental results show that comparing with SIFT descriptor with a neighborhood of 128×128, the matching points of CNN-SIFT descriptor increase more than 41.32%, the correct matching rate improves 18.64%, and the matching rat (needs verification before using numerical claims)
- 19.20%. This approach has been successfully applied to natural resource precision monitoring. The accuracy can meet the requirement of the actual work in the natural resource assets inspection, and this method can provide a reference for the large-scale orthophoto images production of other satellite images. Key words image matching, (needs verification before using numerical claims)
- s the capacity of ship target recognition, and the experimental results can prove the validity and accuracy of this method. Key words remote sensing image processing, deep learning, convolution neural network, target recognition (Page: 7) Object-oriented High-resolution Remote Sensing Image Information Extraction Method by HU Jinmei Ab (needs verification before using numerical claims)
- information to realize land use classification. Experimental result shows that the classification accuracy of this method is higher than that of traditional object-oriented classification method. Key words object-oriented, image classification, high-resolution image, SVM, random forest algorithm (Page: 10) Research on the Enhancement (needs verification before using numerical claims)

## 8. What Should Be Added to Skill Source

- scientific rule: Treat this paper as supporting metadata for vegetation index / Chinese method literature / KRD extraction; do not generalize beyond extracted method signals.
- terminology: Add or confirm terms linked to rocky_desertification_classification and vegetation_index.
- warning: Numerical results and DOI/author metadata marked `needs verification` must not be reused without checking the original paper.
- experiment design implication: Use the paper to refine variables, feature construction, or validation checklist, not to replace project-specific experiments.
- writing implication: Mention this cluster as background support only after citation metadata is verified.

## 9. Manual Review Needed

- metadata uncertainty: yes
- PDF extraction issue: no major text-layer issue detected
- DOI needs check: yes
- figures/tables unclear: captions extracted but visual content still needs manual check
- result values need verification: yes
