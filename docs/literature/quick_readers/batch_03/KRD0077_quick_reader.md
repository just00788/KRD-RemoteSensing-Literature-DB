# Batch 03 Quick Reader: Classification of rocky desertification degrees and spatiotemporal distribution patterns using a feature-space RDI framework

## 1. Bibliographic Information

- Canonical paper ID: KRD0077
- Title: Classification of rocky desertification degrees and spatiotemporal distribution patterns using a feature-space RDI framework
- Authors: Frontiers authors
- Year: 2026
- Journal / Source: Frontiers in Environmental Science
- DOI: 10.3389/fenvs.2026.1772333
- Language: English
- PDF path: docs/literature/pdfs/package_2021_2026/EN15_Classification_of_rocky_desertification_degrees_and_spatiotemporal_distribution_patterns_u.pdf
- PDF mapping confidence: 0.83
- Why selected: Recent feature-space RDI framework candidate with spatiotemporal distribution and class-level framing.

## 2. Reading Scope

- Abstract: not clearly located
- Introduction: located
- Methods: located
- Results: located
- Discussion: located
- Figures/Tables: 8 caption signals located
- References: located
- PDF text layer: extractable text found
- Page count: 17

## 3. Core Scientific Contribution

本 quick reading 仅基于 PDF text layer 抽取，定位到该文与 feature space / class-level metrics / validation and time-series 相关。 其可用于补强 Skill 的方法、术语或验证设计规则；具体数值结论未在本阶段强行复述，需回到原文核验。

## 4. Relevance to Skill Gaps

- FBR/fBR: low
- LSMM/SMA/MESMA/FCLS: medium
- ML classification: high
- Deep learning / semantic segmentation: not applicable
- DEM/topography: high
- GF/Gaofen imagery: not applicable
- validation metrics: high
- Chinese literature coverage: not applicable
- Remote Sensing style: high

## 5. Method Notes

- data source: Sentinel-2; Landsat; DEM
- preprocessing: preprocessing The Landsat imagery used in this study, including Landsat five and Landsat seven scenes from 1985 to 2024, was obtained from the Google Earth Engine (GEE) platform. Images were selected with a cloud cover of less than 10%. All acquisitions were concentrated between July and Septemb
- target variable: Rocky desertification is a major ecological problem in karst regions, driven by the combined effects of natural conditions and human activities. To investigate its spatiotemporal evolution and driving mechanisms, this study constructed a two- dimensional Rocky Desertification Index (RDI) based on
- model or algorithm: RF; feature space; vegetation index
- features: features; (2) Spatiotemporal analysis was employed to reveal the dynamic evolution patterns of rocky desertification; (3) A combined approach integrating Geodetector and PLS-SEM was introduced to simultaneously quantify the spatial explanatory power of driving factors and elucidate their interaction pathways. This integrated analytical framework provid
- DEM/topographic variables: demy of Environmental Sciences, Beijing, China, 2 State Environmental Protection Key Laboratory of Regional Eco- Process and Function Assessment, Chinese Research Academy of Environmental Sciences, Beijing, China Rocky desertification is a major ecological problem in karst regions, driven by the combined effects of natural conditions and human activities
- sample construction: samples covering various landscape types for the year 2020, with sample selection comprehensively referring to Sentinel-2 satellite imagery, and high- resolution Google Earth base maps. Based on these samples, a confusion matrix was constructed to achieve a quantitative assessment of the model’s performance, which was also employed to validate the inve
- validation design: accuracy reached 88.16%, and rocky desertification exhibited an overall alleviation trend, with non-desertified areas expanding continuously and moderate and intensive rocky desertification decreasing significantly. Optimal Parameter-based Geographical Detector (OPGD) analysis identified land use as the dominant driving factor, with q-values ranging from
- metrics: OA, IoU

## 6. Important Figures and Tables

- Figure/Table number: item 1
  - caption: Figure1a ). The climate is classified as subtropical monsoon humid, characterized by mild temperatures throughout the year and abundant precipitation. Situated in the core zone of karst landforms, the study area is characterized by severe soil erosion and a hi
  - what it supports: figure/table evidence signal for methods or results.
  - whether useful for our manuscript: useful if manually verified.
- Figure/Table number: item 2
  - caption: Table 1 , and the spatial distribution of the seven driving factors is illustrated in
  - what it supports: figure/table evidence signal for methods or results.
  - whether useful for our manuscript: useful if manually verified.
- Figure/Table number: item 3
  - caption: Figure 2 . The workflow of this study consists of three main steps. First, the NDVI and BLI indices were calculated to generate raster datasets. Second, the NDVI–BLI feature space was constructed using the feature space method, from which the RDI was derived b
  - what it supports: figure/table evidence signal for methods or results.
  - whether useful for our manuscript: useful if manually verified.
- Figure/Table number: item 4
  - caption: Figure 3 . 2.2.2 Rocky desertification classification based on the feature space method Indices such as NDVI and Rocky index (RI) have been applied to the identification of rocky desertification, either by directly detecting exposed surface rocks or indirectly
  - what it supports: figure/table evidence signal for methods or results.
  - whether useful for our manuscript: useful if manually verified.
- Figure/Table number: item 5
  - caption: Figure 4 , with increasing degrees of rocky desertification, the land use efficiency index tends to increase while the vegetation index tends to decrease. The AB line denotes zones of severe rocky desertification, in contrast to the CD line, which denotes zone
  - what it supports: figure/table evidence signal for methods or results.
  - whether useful for our manuscript: useful if manually verified.

## 7. Key Findings Relevant to Our Manuscript

- ity, Guizhou Province, China, during 1987–2022. The results showed that the overall classification accuracy reached 88.16%, and rocky desertification exhibited an overall alleviation trend, with non-desertified areas expanding continuously and moderate and intensive rocky desertification decreasing significantly. Optimal Parameter-bas (needs verification before using numerical claims)
- ning the RDI thresholds. 2.2.3 Error matrix analysis To systematically evaluate the classification accuracy of the constructed monitoring model, this study integrated multi-source validation data and defined 245 verification samples covering various landscape types for the year 2020, with sample selection comprehensively referring to (needs verification before using numerical claims)
- titative assessment of the model’s performance, which was also employed to validate the inversion accuracy of rocky desertification. The row totals, column totals, user’s accuracy, producer’s accuracy, and overall accuracy were calculated using Equations 3 – 7 , respectively. P i+ � 􏽘 n j�1 P ij (3) P +j � 􏽘 n i�1 P ij (4) P u,i � P (needs verification before using numerical claims)
- to validate the inversion accuracy of rocky desertification. The row totals, column totals, user’s accuracy, producer’s accuracy, and overall accuracy were calculated using Equations 3 – 7 , respectively. P i+ � 􏽘 n j�1 P ij (3) P +j � 􏽘 n i�1 P ij (4) P u,i � P ii P i+ (5) P A,i � P jj P +j (6) P c � 􏽐 n k�1 P kk 􏽐 n i�1 􏽐 n j�1 P ij (needs verification before using numerical claims)
- sion accuracy of rocky desertification. The row totals, column totals, user’s accuracy, producer’s accuracy, and overall accuracy were calculated using Equations 3 – 7 , respectively. P i+ � 􏽘 n j�1 P ij (3) P +j � 􏽘 n i�1 P ij (4) P u,i � P ii P i+ (5) P A,i � P jj P +j (6) P c � 􏽐 n k�1 P kk 􏽐 n i�1 􏽐 n j�1 P ij (7) Where P i+ and P (needs verification before using numerical claims)

## 8. What Should Be Added to Skill Source

- scientific rule: Treat this paper as supporting metadata for feature space / class-level metrics / validation and time-series; do not generalize beyond extracted method signals.
- terminology: Add or confirm terms linked to gee_time_series and feature_space; vegetation_index; time_series.
- warning: Numerical results and DOI/author metadata marked `needs verification` must not be reused without checking the original paper.
- experiment design implication: Use the paper to refine variables, feature construction, or validation checklist, not to replace project-specific experiments.
- writing implication: Mention this cluster as background support only after citation metadata is verified.

## 9. Manual Review Needed

- metadata uncertainty: no obvious metadata gap
- PDF extraction issue: no major text-layer issue detected
- DOI needs check: no
- figures/tables unclear: captions extracted but visual content still needs manual check
- result values need verification: yes
