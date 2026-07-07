# Semantic Segmentation Evidence Map

Generated: 2026-07-07T16:16:01

## Supporting papers

- KRD0051: A Rocky Desertification Land Extraction Method Based on Spectral Texture Scattering Terrain Feature Set and Multiscale Segmentation (2024); reader: `docs/literature/readers/batch_01_core/KRD0051_reader.md`
- KRD0064: Fine-Grained Land Use Remote Sensing Mapping in Karst Mountain Areas Using Very High Resolution Images (2025); reader: `docs/literature/readers/batch_01_core/KRD0064_reader.md`
- KRD0068: RAP-Net: A Region Affinity Propagation-Guided Semantic Segmentation Network for Plateau Karst Landform Delineation (2025); reader: `docs/literature/readers/batch_01_core/KRD0068_reader.md`

## Data used

### KRD0051
- p.1: Based on Spectral-Texture-Scattering-Terrain
- p.1: To address these challenges, this study first constructs a timeseries-based spectral-texture-scattering-terrain (STST) feature
- p.1: Institute, Chinese Academy of Sciences, Beijing 100094, China, also with
- p.1: and Environment, Yanqi Lake Campus, University of Chinese Academy of

### KRD0064
- p.1: Academic Editor: Junmin Liu
- p.1: Chinese Academy of Sciences, Beijing 100101, China; luojc@aircas.ac.cn
- p.1: 4 University of Chinese Academy of Sciences, Beijing 100049, China
- p.1: Comparative analysis demonstrated the superior performance

### KRD0068
- p.1: Academic Editor: Hubert Hasenauer
- p.1: 1 Department of Surveying & Mapping Engineering, College of Earth and Planetary Sciences, Chengdu
- p.1: 2 Sichuan Coalfield 141 Construction Investment Co., Ltd., Deyang 618029, China
- p.1: thereby demonstrating significant improvements in boundary delineation and structural


## Methods used

### KRD0051
- p.1: Multisource Features With Time Series
- p.1: set and applies multiscale segmentation (MS) processing.
- p.1: network (MDNA-1DCNN) is designed for object-oriented classification (OOC) in Ziyun County, Guizhou Province, and Longlin
- p.1: cutting the images into small patches for network input, enabling

### KRD0064
- p.1: Comparative analysis demonstrated the superior performance
- p.2: As data technologies advance and geographical information analysis demands deepen, segmentation
- p.2: using segmentation objects significantly reduces spatial data volume while increasing
- p.2: in both space and time for fine-grained object segmentation.

### KRD0068
- p.1: Segmentation Network for Plateau
- p.1: Segmentation Network for Plateau Karst Landform Remote
- p.1: Keywords: karst landforms; Qinghai–Tibet Plateau; semantic segmentation; affinity propagation
- p.2: used K-means clustering and random forest classifiers to


## Metrics

### KRD0051
- p.1: Extracting the spatial distribution of rocky
- p.1: Subsequently, by incorporating an improved spatial-channel attention
- p.1: County, Guangxi Province, China.
- p.1: cutting the images into small patches for network input, enabling

### KRD0064
- p.1: Guiyang 550025, China; pandapo8341@163.com
- p.1: 3 State Key Laboratory of Remote Sensing and Digital Earth, Aerospace Information Research Institute,
- p.1: Karst mountain areas, as complex geological systems formed by carbonate rock development, possess unique three-dimensional spatial structures and hydrogeological processes
- p.1: fine-grained land use mapping and quantitative characterization of spatial heterogeneity

### KRD0068
- p.1: Propagation-Guided Semantic
- p.1: RAP-Net: A Region Affinity Propagation-Guided Semantic
- p.1: 1 Department of Surveying & Mapping Engineering, College of Earth and Planetary Sciences, Chengdu
- p.1: 2 Sichuan Coalfield 141 Construction Investment Co., Ltd., Deyang 618029, China


## Main findings

Record only findings explicitly supported in each PDF. This map stores result evidence anchors, not unsupported synthesized numerical claims.
### KRD0051
- p.1: show that MDNA-1DCNN achieves an overall accuracy (OA)
- p.1: of 97.67% and a Kappa coefficient of 97.07% in multiclass
- p.1: tasks, with F1-score (F1) and Intersection Over Union (IoU)
- p.1: Goals, Beijing 100094, China, and also with the College of Resources

### KRD0064
- p.1: notable accuracy metrics with an overall accuracy (OA) of 0.815 and a mean intersection
- p.1: The approach provides a robust mapping framework for
- p.2: fragmented land features, result in a scarcity of high-quality satellite imagery data and
- p.2: region-based [17], supervised and unsupervised [ 18], traditional and deep learning approaches [19], as well as single-scale and multi-scale methods based on segmentation

### KRD0068
- p.1: However, this approach is limited by its dependence on expert knowledge and manual
- p.1: support geological mapping in the Dalmatian karst region of Croatia, thereby improving
- p.1: Compared with traditional manual interpretation, these machine learning approaches have significantly improved mapping efficiency
- p.1: and reduced human workload.


## Limitations

### KRD0051
- p.2: However, these methods still face limitations in capturing
- p.11: 68% in Ziyun, with some limitations in distinguishing between
- p.14: limitations, and the segmentation quality depends on the

### KRD0064
- p.5: This complexity introduces substantial uncertainty
- p.11: or roads due to limitations in the spatial resolution of remote sensing imagery and the
- p.18: However, several limitations warrant consideration.

### KRD0068
- p.2: To overcome these limitations, researchers have adopted machine learning techniques
- p.4: To address this limitation, we propose an
- p.12: Context Attention Branch by compensating for its limitations in modeling local patterns.


## Relevance to our manuscript

- KRD0051: KRD classification/information extraction; semantic segmentation baseline/model; DEM/topographic factors
- KRD0064: machine-learning classification; Remote Sensing/KRD relevance
- KRD0068: semantic segmentation baseline/model

## Possible sentences or writing patterns

- Introduce KRD monitoring as a remote-sensing mapping problem, then separate continuous FBR inversion from categorical desertification-level classification.
- In Methods, report data sources, preprocessing, feature construction, model baselines, validation split, and metric type explicitly.
- In Results, pair spatial maps with class-level or continuous-variable metrics as appropriate.
- In Discussion, explain why spectral, terrain, temporal, or model-architecture choices affect mapped KRD patterns.

## What should be added to the future Skill

- Canonical distinction between FBR continuous inversion metrics and classification metrics.
- Checklist for KRD data sources: Sentinel/Landsat/GF, DEM/topographic variables, field/UAV/reference samples.
- Reader extraction warning: figure/table captions from text layer do not replace manual visual inspection.
