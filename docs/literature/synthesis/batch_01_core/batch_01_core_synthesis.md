# Batch 01 Core Paper Synthesis

Generated: 2026-07-07T16:29:16

## 1. Papers Read

| paper_id | title | year | journal | readability_status | reader generated | card generated | manual review needed |
|---|---|---:|---|---|---|---|---|
| KRD0013 | 石漠化遥感评价因子提取研究 / Remote sensing of indicators for evaluating karst rocky desertification | 2011 | 生态学相关期刊/中国生态系统研究网络存档 | ready | yes | yes | yes |
| KRD0033 | Extracting Information on Rocky Desertification from Satellite Images: A Comparative Study | 2021 | core | ready | yes | yes | no |
| KRD0035 | Optimization of Rocky Desertification Classification Model Based on Vegetation Type and Seasonal Characteristic | 2021 | core | ready | yes | yes | no |
| KRD0051 | A Rocky Desertification Land Extraction Method Based on Spectral Texture Scattering Terrain Feature Set and Multiscale Segmentation | 2024 | IEEE | ready | yes | yes | yes |
| KRD0054 | Dynamic monitoring of rocky desertification utilizing a novel model based on Sentinel-2 images and KNDVI | 2024 | Geocarto International or related | ready | yes | yes | no |
| KRD0057 | Spatio-Temporal Evolution Characteristics and Driving Factors of Karst Rocky Desertification in Qujing City Based on GEE | 2024 | Sustainability | ready | yes | yes | no |
| KRD0058 | 基于多源数据的石漠化地区裸岩信息提取和景观格局分析 | 2024 | 万方学位论文 | ready | yes | yes | yes |
| KRD0062 | 基于无人机影像与Sentinel-2影像的基岩裸露率反演与石漠化程度评价 | 2024 | 百度学术条目/学位论文 | ready | yes | yes | yes |
| KRD0064 | Fine-Grained Land Use Remote Sensing Mapping in Karst Mountain Areas Using Very High Resolution Images | 2025 | Remote Sensing | ready | yes | yes | no |
| KRD0068 | RAP-Net: A Region Affinity Propagation-Guided Semantic Segmentation Network for Plateau Karst Landform Delineation | 2025 | Remote Sensing | ready | yes | yes | no |
| KRD0076 | 顾及Vis-NIR光谱指数时序统计特征的红层荒漠化场景分类 | 2025 | 农业工程学报 | ready | yes | yes | no |
| KRD0116 | 基于改进DeepLabV3+的石漠化地区裸岩信息提取 | unknown | unknown | ready | yes | yes | yes |
| KRD0091 | EN003 Machine learning algorithm for estimating karst rocky desert | unknown | unknown | usable_with_caution | yes | yes | yes |
| KRD0092 | EN004 Comparing Remote Sensing Methods for Monitoring Karst Rocky | unknown | unknown | usable_with_caution | yes | yes | yes |
| KRD0094 | EN007 KRD MESMA SVM | unknown | unknown | usable_with_caution | yes | yes | yes |
| KRD0095 | EN009 Classification of Karst Rocky Desertification Levels in Jins | unknown | unknown | usable_with_caution | yes | yes | yes |

## 2. Main Research Themes

- rocky desertification classification: 11 papers (KRD0013, KRD0033, KRD0035, KRD0051, KRD0054, KRD0057, KRD0058, KRD0062, KRD0116, KRD0092, KRD0095).
- FBR/fBR/bare-rock fraction: 13 papers (KRD0013, KRD0033, KRD0035, KRD0051, KRD0054, KRD0058, KRD0062, KRD0068, KRD0076, KRD0116, KRD0091, KRD0092, KRD0094).
- LSMM/SMA/MESMA: 9 papers (KRD0035, KRD0051, KRD0054, KRD0058, KRD0062, KRD0116, KRD0091, KRD0092, KRD0094).
- machine learning: 16 papers (KRD0013, KRD0033, KRD0035, KRD0051, KRD0054, KRD0057, KRD0058, KRD0062, KRD0064, KRD0068, KRD0076, KRD0116, KRD0091, KRD0092, KRD0094, KRD0095).
- semantic segmentation: 4 papers (KRD0051, KRD0064, KRD0068, KRD0116).
- DEM/topographic factors: 14 papers (KRD0013, KRD0033, KRD0035, KRD0051, KRD0054, KRD0057, KRD0062, KRD0064, KRD0068, KRD0076, KRD0091, KRD0092, KRD0094, KRD0095).
- multi-source remote sensing: 15 papers (KRD0033, KRD0035, KRD0051, KRD0054, KRD0057, KRD0058, KRD0062, KRD0064, KRD0068, KRD0076, KRD0116, KRD0091, KRD0092, KRD0094, KRD0095).
- cross-region validation: 8 papers (KRD0035, KRD0054, KRD0057, KRD0062, KRD0064, KRD0068, KRD0091, KRD0094).
- Remote Sensing writing style: 11 papers (KRD0013, KRD0033, KRD0051, KRD0054, KRD0062, KRD0064, KRD0068, KRD0116, KRD0092, KRD0094, KRD0095).

## 3. Evidence for Our Scientific Framework

### FBR and LSMM evidence

Batch papers with FBR/LSMM/SMA/MESMA signals support treating FBR/fBR/bare-rock fraction as a continuous or proportional variable unless a paper explicitly thresholds it into classes. Continuous inversion evidence must be evaluated with continuous metrics such as R2/RMSE/MAE/bias/slope when reported.

### Classification and ML evidence

Classification-oriented papers use KRD/rocky desertification classes and commonly require OA/Kappa/class-level accuracy evidence. Machine-learning evidence is concentrated in RF/SVM/classifier and feature-construction papers.

### Deep learning and semantic segmentation evidence

Semantic-segmentation papers in this batch are useful for architecture/baseline framing. FCN and U-Net remain baselines; DeepLabV3+ should be treated as the main semantic segmentation model only in our manuscript design, not retroactively attributed to papers that do not use it.

### DEM/topographic evidence

DEM/topographic signals appear through slope/aspect/elevation/terrain features. For our manuscript, open-source DEM supports Area 1 to Area 2 transfer because it covers both areas; GF-7 stereo-derived DEM should be limited to Study Area 2 local enhancement.

### Validation evidence

The batch reinforces the need to report the validation design and the correct metric family. Spatial block split should be preferred over random patch split for our experiment design.

## 4. Evidence for Our Remote Sensing Manuscript Structure

- Abstract: state target, data, method family, validation, and contribution without mixing FBR and class-map claims.
- Introduction: move from KRD significance to remote-sensing limitations and then to our combined FBR/segmentation/DEM/transfer gap.
- Materials and Methods: make data, preprocessing, feature/model workflow, split strategy, and metrics reproducible.
- Results: separate continuous FBR inversion results from classification/segmentation results.
- Discussion: explain terrain/data/model effects and compare against prior KRD mapping evidence.
- Conclusions: summarize objectives, methods, validated findings, application value, and limitations.
- Figures: prioritize study area, workflow, maps, architecture, ablation, and error/uncertainty figures.
- Tables: prioritize data source, model configuration, metrics, class-level accuracy, and ablation tables.

## 5. Gaps Identified

- Cross-region validation is not consistently located in the batch evidence.
- GF-7 stereo DEM local enhancement is not a common batch theme and should be framed as our local enhancement, not transfer evidence.
- FCN/U-Net/DeepLabV3+ baselines need explicit handling in our design.
- DEM factor ablation should be explicit.
- Continuous FBR and classification levels are easy to conflate; our manuscript must keep them separate.
- Class-level metrics are not always easy to locate; our paper should report OA/Kappa/Precision/Recall/F1/IoU/mF1/mIoU where classification is involved.
- Spatially independent validation should be made explicit.

## 6. Implications for Our Experiment Design

- Use LSMM for continuous FBR inversion and evaluate it with continuous metrics.
- Threshold FBR only when converting it into NRD/LRD/MRD/SRD-style classes for comparison.
- Use DeepLabV3+ as the main semantic segmentation model with FCN and U-Net as baselines.
- Include open-source DEM ablation for Area 1 to Area 2 transfer.
- Use GF-7 stereo-derived DEM only for local high-precision Study Area 2 terrain enhancement.
- Report class-level accuracy assessment and uncertainty/error analysis.

## 7. Implications for Writing

- Introduction gap writing should explicitly state what prior KRD/FBR/classification/DEM work leaves unresolved.
- Methods writing should be reproducible and metric-aware.
- Results writing should pair map interpretation with appropriate metrics.
- Discussion writing should connect spectral/terrain/model mechanisms to spatial patterns.
- Limitations writing should name validation split, spatial transfer, DEM scope, and uncertainty.
- Terminology must consistently distinguish FBR, KRD levels, LSMM, semantic segmentation, and DEM types.

## 8. Recommended Next Batch

Prioritize papers that can fill missing metadata and underrepresented evidence: explicit DeepLabV3+/U-Net/FCN KRD segmentation, DEM ablation, cross-region transfer validation, and high-quality FBR/LSMM/MESMA validation papers with clear continuous metrics.
