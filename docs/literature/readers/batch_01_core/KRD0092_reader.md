# Full-Paper Reader: EN004 Comparing Remote Sensing Methods for Monitoring Karst Rocky

## 1. Bibliographic Information

- Paper ID: KRD0092
- Title: EN004 Comparing Remote Sensing Methods for Monitoring Karst Rocky
- Translated title if applicable: unknown
- Authors: unknown
- Year: unknown
- Journal / Source: unknown
- DOI: unknown
- URL: unknown
- PDF path: `docs/literature/pdfs/package_2000_2026/EN004_Comparing_Remote_Sensing_Methods_for_Monitoring_Karst_Rocky_.pdf`
- Language: unknown
- Readability status: usable_with_caution
- Metadata status: metadata_incomplete

## 2. Reading Scope and Source Anchors

This reader was generated from the full selectable text layer of the PDF. It preserves page-level anchors and section/figure/table signals. It does not reproduce large original-text passages and does not fabricate missing metadata.

- Abstract: p.10, p.11
- Introduction: not located
- Study Area: p.1, p.2, p.3, p.4, p.5, p.6, p.7, p.8, p.9
- Data: p.1, p.2, p.3, p.4, p.5, p.6, p.8, p.10, p.11, p.12
- Methods: p.1, p.2, p.4, p.5, p.6, p.7, p.8, p.9, p.10, p.11
- Experiments: not located
- Results: p.1, p.2, p.3, p.4, p.5, p.6, p.7, p.8, p.9, p.10, p.11, p.12
- Discussion: p.5
- Conclusions: p.8
- References: p.10
- Figures/Tables captions: 8 located
  - p.3: Figure 1. Spectral curves of rocky outcrops, vegetation and shadow in the study area. (a) Was collected from
  - p.3: Table 1. Overall accuracy (OA), and Kappa coefficient (K) of percentage of estimated rocky outcrops.
  - p.4: Table 2. Percentage of rocky outcrops in class confusion matrix in sunlit and shadow areas. (PA: producer’s
  - p.5: Figure 2. Predicted percent of rocky outcrop in sunlit and shadow areas.
  - p.6: Figure 3. Contrast of rocky outcrop cover in sunlit and shadow areas. Panel a is an ALOS sharpened images
  - p.7: Figure 4. Study area and characteristics of KRD. Panel A is a pan-sharpened ALOS image (RGB: NIR, red,
  - p.7: Table 3. Percent area at each KRD level based on different methods.
  - p.9: Figure 5. Typical landscapes of rocky desertification in the study area. The rocky desertification in panels a and

## 3. Abstract-Level Understanding

Source anchors: p.1

基于可抽取的摘要文本，本研究逻辑可按以下方式理解。以下内容只依据摘要和题录可确认的信息，不补造缺失结论。

- 研究背景: 论文主题与 `rocky_desertification_classification` 相关，关键词信号包括 `unknown`。
- 研究目标: EN004 Comparing Remote Sensing Methods for Monitoring Karst Rocky
- 数据: 见下方 Data Sources 中从全文定位到的证据信号。
- 方法: 见下方 Method Workflow 中从全文定位到的证据信号。
- 主要结果: 仅在 Results Reading Notes 中记录可定位的结果/指标信号；未在此处编造具体数值。
- 意义: 其价值主要体现在对 KRD/FBR/分类/遥感制图/验证框架的支撑，具体等级见第 13 节。

Abstract evidence snippet:

> 1Scientific RepoRtS | (2019) 9:13368 | https://doi.org/10.1038/s41598-019-49730-9 www.nature.com/scientificreports comparing Remote Sensing Methods for Monitoring Karst Rocky Desertification at Sub-pixel Scales in a Highly Heterogeneous Karst Region Xiangkun Qi 1,2, Chunhua Zhang 3 & Kelin Wang1,2 Rugged karst terrain relief that creates shadows in satellite imagery, combined with high karst landscape heterogeneity stand in the way of fractional cover retrieval on karst rocky desertification (KRD) monitoring. In this study, we explored the feasibility of applying multispectral high spatial resolution Advanced Land Observing Satellite (ALOS) imagery for the fractional cover extraction of rocky outcrops. Dimidiate pixel model (DPM) and spectral mixture analysis (SMA) approaches (including simple endmember spectral mixture analysis and multiple endmember spectral mixture analysis) were selected to explore their feasibility for KRD monitoring through accuracy improvement for fraction estimation. Results showed fractional cover retrievals at the sub-pixel scale is essential in highly heterogeneous karst landscapes. Indeed, mixed pixels accounted for 93.7% of the study area i

## 4. Introduction Reading Notes

- Source anchors: not located
- Background unfolding: extracted introduction pages should be read around the anchors above; the parser located target/method signals listed below.
- Why the problem matters: only infer from located KRD/desertification/remote-sensing problem statements; do not add unsupported claims.
- Remote sensing role: see satellite/data excerpts in Section 5.
- Existing research categories: classification, FBR/LSMM/MESMA, ML, semantic segmentation, DEM/topography when signaled below.
- Existing research insufficiency / gap / objectives / contributions: inspect Introduction anchors manually for exact wording before using in manuscript.
- Borrowable point for our Introduction: build a clear progression from KRD importance -> remote-sensing monitoring -> method/data limitation -> our FBR/classification/DEM/cross-region contribution.

Located target/method evidence:
- p.1: Rocky Desertification at Sub-pixel
- p.1: landscape heterogeneity stand in the way of fractional cover retrieval on karst rocky desertification
- p.1: Furthermore, the predicted exposed bedrock
- p.1: Karst landscapes, a special environment formed within carbonate bedrock, are among the most ecologically
- p.1: consequently severe environmental problems including karst rocky desertification (KRD).
- p.1: process of land degradation in which soil is partially or completely eroded
- p.1: extracted from remotely sensed images has been widely applied to describe land degradation and human disturbance9,10.
- p.1: When KRD occurs, the most obvious land-surface symptoms are low vegetation cover and bedrock
- p.2: A dimidiate pixel model (DPM) is commonly used to calculate fractional vegetation cover (FVC)
- p.2: Unlike the impervious surface of urban areas, bare rocks are
- p.1: Dimidiate pixel model (DPM) and spectral mixture analysis (SMA) approaches
- p.1: coverage via spectral mixture analysis were similar in sunlit and shadow areas for the same surface
- p.1: This reflected that SMA methods could effectively reduce topographic effects of satellite imagery
- p.1: When KRD occurs, the most obvious land-surface symptoms are low vegetation cover and bedrock


## 5. Study Area and Data Sources

- Study area: locate from Study Area anchors: p.1, p.2, p.3, p.4, p.5, p.6, p.7, p.8, p.9
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
- p.1: Rugged karst terrain relief that creates shadows in satellite imagery, combined with high karst
- p.1: This reflected that SMA methods could effectively reduce topographic effects of satellite imagery
- p.1: largely depend on field surveys of vegetation and rocky outcrop cover, slope and soil distribution.
- p.1: are time consuming, expensive and limited by rugged terrain and large spatial scales
- p.1: Academy of Sciences, Changsha, 410125, China.
- p.1: Chinese Academy of Sciences, Huanjiang, Hechi, 547100, China.
- p.2: Commonly used moderate resolution images include Landsat Multispectral Scanner (MSS) 14 and Landsat
- p.2: In addition to being highly heterogeneous, the relatively high elevation contrast in the karst area causes significant shadow effects in remotely sensed images.
- p.2: The topographic effect in images is limiting because weak
- p.2: NDVI is able to minimize variation in topographic effects on the spectral properties of land surfaces and so is widely used in the DPM for FVC


## 6. Target Variable or Classification System

- Target variable / object: derived from located evidence only.
- KRD/rocky desertification signal: yes
- FBR/fBR/bare-rock fraction signal: yes
- Semantic segmentation class signal: no
- If FBR/fBR is involved, treat it as a continuous/proportional variable unless the paper explicitly thresholds it into classes.
- If rocky desertification levels are involved, inspect the paper for the exact grade system before reuse.

Target evidence:
- p.1: Rocky Desertification at Sub-pixel
- p.1: landscape heterogeneity stand in the way of fractional cover retrieval on karst rocky desertification
- p.1: Furthermore, the predicted exposed bedrock
- p.1: Karst landscapes, a special environment formed within carbonate bedrock, are among the most ecologically
- p.1: consequently severe environmental problems including karst rocky desertification (KRD).
- p.1: process of land degradation in which soil is partially or completely eroded
- p.1: extracted from remotely sensed images has been widely applied to describe land degradation and human disturbance9,10.
- p.1: When KRD occurs, the most obvious land-surface symptoms are low vegetation cover and bedrock
- p.2: A dimidiate pixel model (DPM) is commonly used to calculate fractional vegetation cover (FVC)
- p.2: Unlike the impervious surface of urban areas, bare rocks are


## 7. Method Workflow

The workflow below is derived from located method/data signals. Missing items are explicitly marked.
- preprocessing: located
- feature construction: located
- spectral indices: located
- DEM/topographic variables: located
- LSMM/SMA/MESMA/FCLS: located
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
- p.1: Dimidiate pixel model (DPM) and spectral mixture analysis (SMA) approaches
- p.1: coverage via spectral mixture analysis were similar in sunlit and shadow areas for the same surface
- p.1: This reflected that SMA methods could effectively reduce topographic effects of satellite imagery
- p.1: When KRD occurs, the most obvious land-surface symptoms are low vegetation cover and bedrock
- p.2: land-surface consequences of KRD.
- p.2: densely distributed ditches on land surfaces that coexist with rocky outcrops, bare soil, grass, shrub and forest
- p.2: widely used method is spectral mixture analysis (SMA)25.
- p.2: The aim of SMA is to decompose mixed spectra and calculate proportions of each land cover
- p.2: However, there have been few SMA-related studies
- p.2: A critical step in SMA is endmember selection.
- p.2: Unlike the impervious surface of urban areas, bare rocks are
- p.2: Furthermore, as high albedo endmembers, rocks, cement road surfaces,
- p.1: Rugged karst terrain relief that creates shadows in satellite imagery, combined with high karst
- p.1: This reflected that SMA methods could effectively reduce topographic effects of satellite imagery
- p.1: largely depend on field surveys of vegetation and rocky outcrop cover, slope and soil distribution.
- p.1: are time consuming, expensive and limited by rugged terrain and large spatial scales
- p.1: Academy of Sciences, Changsha, 410125, China.
- p.1: Chinese Academy of Sciences, Huanjiang, Hechi, 547100, China.
- p.2: Commonly used moderate resolution images include Landsat Multispectral Scanner (MSS) 14 and Landsat
- p.2: In addition to being highly heterogeneous, the relatively high elevation contrast in the karst area causes significant shadow effects in remotely sensed images.
- p.2: The topographic effect in images is limiting because weak
- p.2: NDVI is able to minimize variation in topographic effects on the spectral properties of land surfaces and so is widely used in the DPM for FVC


## 8. Validation Strategy and Metrics

- Reference sample source: locate from excerpts below; manual confirmation recommended.
- Sample size: record only if explicitly visible in source excerpts; otherwise unknown.
- Train/test split: see located split/training evidence; otherwise not reported.
- Spatial split: located only if terms such as spatial/block split appear; otherwise not reported.
- Independent validation: located only if explicit evidence appears; otherwise not reported.
- Cross-region validation: located only if explicit evidence appears; otherwise not reported.

- Continuous-variable metrics located: RMSE, slope
- Classification metrics located: OA, overall accuracy, Kappa, IoU, confusion matrix

Metric evidence:
- p.1: Xiangkun Qi 1,2, Chunhua Zhang 3 & Kelin Wang1,2
- p.1: In this study, we explored the feasibility of applying multispectral high spatial
- p.1: Dimidiate pixel model (DPM) and spectral mixture analysis (SMA) approaches
- p.1: analysis) were selected to explore their feasibility for KRD monitoring through accuracy improvement
- p.1: Multiple endmember spectral mixture analysis achieved high overall accuracy (80.5%)
- p.1: to improve the accuracy of fractional cover extraction at sub-pixel level in heterogeneous and rugged
- p.1: process of land degradation in which soil is partially or completely eroded
- p.1: There are various methods available to map KRD.
- p.1: Basic research and qualitative estimates the extent of KRD
- p.1: largely depend on field surveys of vegetation and rocky outcrop cover, slope and soil distribution.
- p.1: are time consuming, expensive and limited by rugged terrain and large spatial scales
- p.1: When KRD occurs, the most obvious land-surface symptoms are low vegetation cover and bedrock


Important distinction enforced for our manuscript: continuous FBR inversion metrics (R2/RMSE/MAE/bias/slope) must not be mixed with classification metrics (OA/Kappa/Precision/Recall/F1/IoU/mF1/mIoU).

## 9. Figures and Tables

### Located Figure/Table 1
- Source anchor: p.3
- Caption: Figure 1. Spectral curves of rocky outcrops, vegetation and shadow in the study area. (a) Was collected from
- What it shows: inferred only from caption wording; inspect the PDF image before reuse.
- Why it matters: directly relevant to study design/results visualization
- Useful for our manuscript: yes
- Similar figure/table for our paper: consider

### Located Figure/Table 2
- Source anchor: p.3
- Caption: Table 1. Overall accuracy (OA), and Kappa coefficient (K) of percentage of estimated rocky outcrops.
- What it shows: inferred only from caption wording; inspect the PDF image before reuse.
- Why it matters: directly relevant to study design/results visualization
- Useful for our manuscript: yes
- Similar figure/table for our paper: consider

### Located Figure/Table 3
- Source anchor: p.4
- Caption: Table 2. Percentage of rocky outcrops in class confusion matrix in sunlit and shadow areas. (PA: producer’s
- What it shows: inferred only from caption wording; inspect the PDF image before reuse.
- Why it matters: directly relevant to study design/results visualization
- Useful for our manuscript: yes
- Similar figure/table for our paper: consider

### Located Figure/Table 4
- Source anchor: p.5
- Caption: Figure 2. Predicted percent of rocky outcrop in sunlit and shadow areas.
- What it shows: inferred only from caption wording; inspect the PDF image before reuse.
- Why it matters: potentially relevant; requires manual inspection
- Useful for our manuscript: maybe
- Similar figure/table for our paper: manual review first

### Located Figure/Table 5
- Source anchor: p.6
- Caption: Figure 3. Contrast of rocky outcrop cover in sunlit and shadow areas. Panel a is an ALOS sharpened images
- What it shows: inferred only from caption wording; inspect the PDF image before reuse.
- Why it matters: potentially relevant; requires manual inspection
- Useful for our manuscript: maybe
- Similar figure/table for our paper: manual review first

### Located Figure/Table 6
- Source anchor: p.7
- Caption: Figure 4. Study area and characteristics of KRD. Panel A is a pan-sharpened ALOS image (RGB: NIR, red,
- What it shows: inferred only from caption wording; inspect the PDF image before reuse.
- Why it matters: directly relevant to study design/results visualization
- Useful for our manuscript: yes
- Similar figure/table for our paper: consider

### Located Figure/Table 7
- Source anchor: p.7
- Caption: Table 3. Percent area at each KRD level based on different methods.
- What it shows: inferred only from caption wording; inspect the PDF image before reuse.
- Why it matters: potentially relevant; requires manual inspection
- Useful for our manuscript: maybe
- Similar figure/table for our paper: manual review first

### Located Figure/Table 8
- Source anchor: p.9
- Caption: Figure 5. Typical landscapes of rocky desertification in the study area. The rocky desertification in panels a and
- What it shows: inferred only from caption wording; inspect the PDF image before reuse.
- Why it matters: directly relevant to study design/results visualization
- Useful for our manuscript: yes
- Similar figure/table for our paper: consider


## 10. Results Reading Notes

- Source anchors: p.1, p.2, p.3, p.4, p.5, p.6, p.7, p.8, p.9, p.10, p.11, p.12
- Main experimental results: use only values and claims visible in the excerpts/PDF tables.
- Model comparison results: inspect metric/table captions before using exact rankings.
- Data source comparison results: record only where Sentinel/Landsat/GF/DEM evidence is explicit.
- FBR/bare-rock inversion results: separate continuous metrics from class metrics.
- Classification accuracy: report OA/Kappa/Precision/Recall/F1/IoU/mF1/mIoU only if explicitly found.
- DEM/topographic factor contribution: note only when DEM/topographic excerpts are explicit.
- Spatial distribution / uncertainty / significance: inspect maps and captions manually.

Located result/metric evidence:
- p.1: Dimidiate pixel model (DPM) and spectral mixture analysis (SMA) approaches
- p.1: analysis) were selected to explore their feasibility for KRD monitoring through accuracy improvement
- p.1: Results showed fractional cover retrievals at the sub-pixel scale is essential in
- p.1: Multiple endmember spectral mixture analysis achieved high overall accuracy (80.5%)
- p.1: to improve the accuracy of fractional cover extraction at sub-pixel level in heterogeneous and rugged
- p.1: Results of KRD include exposure of
- p.2: This approach supposes that reflectance for one pixel
- p.2: Furthermore, as high albedo endmembers, rocks, cement road surfaces,
- p.2: We applied and compared the efficacy of DPM and two SMA methods through (1) accuracy evaluation of extracting rocky outcrop
- p.2: Results from this study serve as a technical reference for applying optical remote sensing in heterogeneous
- p.1: Xiangkun Qi 1,2, Chunhua Zhang 3 & Kelin Wang1,2
- p.1: In this study, we explored the feasibility of applying multispectral high spatial
- p.1: Dimidiate pixel model (DPM) and spectral mixture analysis (SMA) approaches
- p.1: analysis) were selected to explore their feasibility for KRD monitoring through accuracy improvement
- p.1: Multiple endmember spectral mixture analysis achieved high overall accuracy (80.5%)
- p.1: to improve the accuracy of fractional cover extraction at sub-pixel level in heterogeneous and rugged


## 11. Discussion Reading Notes

- Source anchors: p.5
- Mechanism explanations, data-source performance, terrain effects, comparison to previous studies, limitations, and future work should be extracted from these anchors only.
- Borrowable Discussion writing pattern: explain why a data/model/factor improves mapping, then tie the explanation to spatial patterns and validation evidence.

Located discussion/limitation evidence:
- p.2: characteristic changes (e.g., color) of rocky outcrops affected spectral reflectance creating further uncertainty in
- p.6: overcomes SESMA ’s limitations by requiring a model to meet minimum fit, fraction and residual constraints while
- p.11: Monitoring forest succession with multitemporal Landsat images: Factors of uncertainty.


## 12. Conclusion Reading Notes

- Source anchors: p.8
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
- cross-region transfer support: not applicable. Reason: grounded signals were not located in the text layer.
- accuracy assessment support: medium. Reason: grounded signals were located in the text layer.
- Discussion comparison support: not applicable. Reason: grounded signals were not located in the text layer.
- limitations support: medium. Reason: grounded signals were located in the text layer.
- figure/table design support: medium. Reason: grounded signals were located in the text layer.
- terminology support: medium. Reason: grounded signals were located in the text layer.
- Remote Sensing writing style support: medium. Reason: grounded signals were located in the text layer.

## 14. Reusable Knowledge for Future Skill

### Scientific rules
- Relevant target/method signals: rocky_desertification_classification; unknown.
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
- Separate open-source DEM cross-area use from GF-7 stereo-derived DEM local enhancement claims.


## 15. Items Needing Manual Review

- title is provisional filename-derived candidate; verify manually
- year missing in database
- DOI missing in database
- readability_status=usable_with_caution
- DOI needs manual verification
- metadata incomplete
