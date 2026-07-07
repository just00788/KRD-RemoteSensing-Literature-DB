# Remote Sensing Style Reader: Analysis of Landsat-8 OLI Imagery for Estimating Exposed Bedrock Fractions in Typical Karst Regions of Southwest China

## 1. Bibliographic Information

- RS ID: RS003
- Title: Analysis of Landsat-8 OLI Imagery for Estimating Exposed Bedrock Fractions in Typical Karst Regions of Southwest China
- Authors: unknown
- Year: 2018
- Journal: Remote Sensing
- DOI: 10.3390/rs10091321
- PDF path: `docs/literature/pdfs/remote_sensing_only/2018_RemoteSens_10_1321_Analysis_of_Landsat-8_OLI_Imagery_for_Estimating_Exposed_Bed.pdf`
- Language: English
- Already read in previous batches: batch_01=False; batch_02=False
- This rereading focus: journal writing style, section architecture, figure/table pattern, terminology, and reusable templates.

## 2. Article Structure

- Primary headings detected: 16
- Independent Discussion: yes
- Independent Conclusions: yes
- Data Availability / Author Contributions / Funding / Conflicts of Interest: Data Availability=not located; Author Contributions=p.16; Funding=p.16; Conflicts=not located
- Supplementary Materials: not located
- Overall suitability: useful for our manuscript if we adapt the structure without copying wording.

| Section | Subsections | Function | Relevance to our manuscript |
|---|---|---|---|
| 5 International Research Center on Karst, UNESCO, Qixing Road, Guilin 541004, China | see source headings | article support section or topic-specific subsection | adapt if matching our FBR/DeepLabV3+/DEM workflow |
| 1. Introduction | see source headings | sets background, problem importance, literature gap | adapt if matching our FBR/DeepLabV3+/DEM workflow |
| 2. Materials and Methods | see source headings | establishes reproducible materials, data, workflow, and evaluation | adapt if matching our FBR/DeepLabV3+/DEM workflow |
| 2.1. Study Area | see source headings | establishes reproducible materials, data, workflow, and evaluation | adapt if matching our FBR/DeepLabV3+/DEM workflow |
| 2.2. Landsat-8 Data and Preprocessing | see source headings | establishes reproducible materials, data, workflow, and evaluation | adapt if matching our FBR/DeepLabV3+/DEM workflow |
| 2.3. Auxiliary Data and Accuracy Assessment | see source headings | establishes reproducible materials, data, workflow, and evaluation | adapt if matching our FBR/DeepLabV3+/DEM workflow |
| 2.4. The Karst Bare-Rock Index (KBRI) | see source headings | article support section or topic-specific subsection | adapt if matching our FBR/DeepLabV3+/DEM workflow |
| 2.5. Comparison with Related Indices | see source headings | article support section or topic-specific subsection | adapt if matching our FBR/DeepLabV3+/DEM workflow |
| 2.6. A Linear Regression Model | see source headings | article support section or topic-specific subsection | adapt if matching our FBR/DeepLabV3+/DEM workflow |
| 3. Results | see source headings | reports maps, comparisons, and metrics | adapt if matching our FBR/DeepLabV3+/DEM workflow |
| 3.1. Index Images | see source headings | article support section or topic-specific subsection | adapt if matching our FBR/DeepLabV3+/DEM workflow |
| 3.2. Mapping of EBF in Xiaojiang Watershed | see source headings | article support section or topic-specific subsection | adapt if matching our FBR/DeepLabV3+/DEM workflow |
| 3.3. An Independent Validation | see source headings | article support section or topic-specific subsection | adapt if matching our FBR/DeepLabV3+/DEM workflow |
| 4. Discussion | see source headings | interprets mechanisms, compares literature, states limitations | adapt if matching our FBR/DeepLabV3+/DEM workflow |
| 5. Conclusions | see source headings | summarizes contribution and application value | adapt if matching our FBR/DeepLabV3+/DEM workflow |
| References | see source headings | article support section or topic-specific subsection | adapt if matching our FBR/DeepLabV3+/DEM workflow |

## 3. Abstract Writing Pattern

- Background opening: usually starts from environmental importance or monitoring challenge.
- Problem/gap: located through abstract text.
- Data and method compression: Remote Sensing abstracts tend to compress sensor, study area, model, and validation into one or two sentences.
- Result presentation: reports principal results and often includes metrics when central to the paper.
- Specific accuracy numbers: not detected in abstract sample.
- Significance ending: commonly links the method to monitoring, restoration, or decision support.
- Approximate abstract length: 231 words; 13 sentence-like units.
- Suitable expression modes: concise background-gap-data-method-result-significance sequence.

- Background sentence pattern: [Research object] is important for [ecological or management problem], and remote sensing provides scalable monitoring evidence.
- Gap sentence pattern: However, existing methods remain limited in [spatial detail / class discrimination / bare-rock fraction estimation / transferability].
- Data sentence pattern: This study used [sensor/data sources] covering [study area/time span] to characterize [target variable].
- Method sentence pattern: We developed or compared [method/model] using [features/data] and evaluated it with [metric family].
- Result sentence pattern: The results showed that [method/data combination] improved [mapping or estimation target] according to [appropriate metrics].
- Significance sentence pattern: These findings provide a basis for [KRD monitoring / restoration / transferable mapping / method design].

## 4. Introduction Writing Pattern

| Paragraph / Function | What it does | Typical writing move | Useful for our manuscript |
|---|---|---|---|
| Background | establishes ecological/monitoring importance | broad problem -> KRD/karst/land degradation | high |
| Remote sensing value | explains scalable observation | sensor capability -> mapping target | high |
| Literature review | layers prior methods | spectral indices / SMA / ML / DL / DEM | high |
| Gap | names remaining limitation | resolution, heterogeneity, validation, transfer | high |
| Objectives | states study aim and contributions | “This study aims to...” pattern | high |

- Paragraph 1: KRD background and ecological importance.
- Paragraph 2: Remote sensing and FBR relevance.
- Paragraph 3: Existing spectral unmixing and ML methods.
- Paragraph 4: Deep learning and terrain constraints.
- Paragraph 5: Research gap.
- Paragraph 6: Objectives and contributions.

Reusable moves: move from regional ecological problem -> remote sensing need -> limitations of existing methods -> our data/model/validation gap -> explicit contributions.

Located Introduction anchors: p.1

## 5. Materials and Methods Writing Pattern

- Study area: usually separated or early in Methods; anchor p.3, p.5, p.6, p.10, p.12, p.13, p.14, p.16.
- Data sources: anchor p.1, p.2, p.3, p.4, p.5, p.6, p.8, p.14, p.15, p.16, ...; often supported by a data table.
- Data table design: include sensor, date, resolution, bands, preprocessing, and role.
- Preprocessing: describe corrections and derived features before model details.
- Samples and labels: should define class system or reference values.
- Classification/FBR system: keep continuous FBR and categorical classes separate.
- Model/algorithm: introduce architecture/model choices after data/features.
- Formula presentation: place equations near variable definitions.
- Experimental design: separate comparison, ablation, validation, and transfer.
- Accuracy assessment: report metric family matched to target type.
- Workflow figure: recommended for our manuscript.

- Study Area writing template: locate the region, explain karst/environmental characteristics, and link them to mapping difficulty.
- Data Sources writing template: list sensors, dates, resolution, preprocessing, and why each source is needed.
- Reference Sample and Label Construction template: describe sample source, labeling standard, class system, and quality control.
- FBR / LSMM writing template: define continuous FBR, endmembers/features, constraints, and continuous metrics.
- DeepLabV3+ writing template: specify architecture, backbone, ASPP/decoder, input features, training settings, and baselines.
- DEM Fusion writing template: distinguish open-source DEM for cross-area use from GF-7 stereo DEM for local enhancement.
- Experimental Design writing template: define baseline comparison, ablation, transfer, and spatial split.
- Accuracy Assessment writing template: separate continuous metrics from classification metrics.

Located Methods evidence:
- p.1: Box 9718, Datun Road, Chaoyang, Beijing 100101, China; peijie@radi.ac.cn (J.P .); huangni@radi.ac.cn (N.H.) 2 University of Chinese Academy of Sciences, Yuquan Road 19, Shijingshan, Beijing 100049, China; gengjing15@mails.ucas.ac.cn 3 Key Laboratory of Ecosyst
- p.1: Remote-sensing indices provide a useful method for the quick mapping of the EBF at large scales.
- p.1: A linear regression model was thus established between KBRI and the EBF derived from in situ measurements.
- p.1: The model developed here was then validated with an independent experiment and applied over a large geographic area to produce regional maps of EBF in southwest China.
- p.1: The advantages of the proposed method are reﬂected in its simplicity and minimal requirements for auxiliary data while still achieving comparatively better accuracy than existing related indices.
- p.1: Results of this study provide baseline data for the KRD assessment and karst-ecosystem management in southwest China.
- p.2: By contrast, remote-sensing technology has the great advantages of low cost of data acquisition, large-area coverage, long time-series observations, and spatial continuity [ 16,17], rendering it an indispensable means for the quantitative extraction of EBF inf
- p.2: Nevertheless, the applications of these two methods in the research of karst feature extraction have some limitations.
- p.2: On the other hand, the SMA method makes a basic assumption that mixed pixels in which land surface is composed of a limited number of primary features (i.e., endmembers), and the observed mixed reﬂectance is the function of an endmember’s spectrum and its corr
- p.2: Therefore, it is very difﬁcult to select the endmembers and thus not easily applicable to employ the SMA method to obtain land-cover information in highly heterogeneous landscapes of karst regions [4,7].

## 6. Results Writing Pattern

- Results order: often data/feature separability -> model/metric comparison -> maps/spatial pattern -> uncertainty or driving factors.
- Overall accuracy first: common when classification is central.
- Class-level metrics: should be reported for class maps when available.
- Maps: normally paired with text interpretation and accuracy evidence.
- Confusion matrix: useful where class confusion matters.
- Ablation: should be separated from main comparison.
- Cross-region validation: should be a dedicated subsection if used.
- Figure/table descriptions: concise, point to the evidence and interpret the pattern.
- Avoid repeating tables: describe the key trend rather than narrating every cell.

Recommended Results structure:
- 4.1 LSMM-Based Bare-Rock Fraction Inversion
- 4.2 Rocky Desertification Grade Mapping from Thresholded FBR
- 4.3 Multi-Source GF and Multi-Model Comparison
- 4.4 FCN, U-Net, and DeepLabV3+ Baseline Comparison
- 4.5 Open-Source DEM Terrain-Factor Ablation
- 4.6 Cross-Region Transferability
- 4.7 GF-7 Stereo DEM Local Enhancement
- 4.8 Error and Class-Level Confusion Analysis

Located Results evidence:
- p.1: Experimental results showed good performance on root mean square error (5.59%), mean absolute error (4.63%), root mean absolute percentage error (13.59%), and coefﬁcient of determination (0.72), respectively.
- p.1: The advantages of the proposed method are reﬂected in its simplicity and minimal requirements for auxiliary data while still achieving comparatively better accuracy than existing related indices.
- p.1: Results of this study provide baseline data for the KRD assessment and karst-ecosystem management in southwest China.
- p.5: Auxiliary Data and Accuracy Assessment Auxiliary data used in this study mainly refer to ﬁeld-survey data, consisting of 340 quadrats, each measuring a 30 m square.
- p.5: Several indicators were introduced in this paper in order to quantitatively assess the accuracy of the developed model, including the root mean square error (RMSE), mean absolute error (MAE), root mean absolute percentage error (RMAPE), and coefﬁcient of deter
- p.5: These assessment indicators were widely used in model evaluation studies and their mathematical expressions were described as the following equations [36–38]: δRMSE = √ 1 n n ∑ i=1 (yi− ˆyi)2 (1) δMAE = 1 n n ∑ i=1 |yi− ˆyi| (2) δRMAPE = 1 n √ n ∑ i=1 [(yi− ˆy
- p.6: When RMSE, MAE, and RMAPE are low and R 2 is high, then the best-ﬁt model is achieved [39].
- p.8: Results 3.1.
- p.9: Four indicators, RMSE, MAE, RMAPE, and R 2, were employed to evaluate the performance of the developed models.
- p.9: Four indicators, RMSE, MAE, RMAPE, and R 2, were employed to evaluate the

## 7. Discussion Writing Pattern

- Mechanism explanation: connect results to spectral, terrain, model, or ecological mechanism.
- Previous studies: compare directionally and cautiously.
- Model advantages: explain why an approach helps, not just that it performs better.
- Data source differences: link bands/resolution/coverage to mapping effects.
- DEM/topographic role: discuss terrain factors without overstating transfer.
- Limitations/future work: state uncertainty, data limitations, validation constraints, and next steps.
- Avoid repeating Results: Discussion should interpret, compare, and delimit claims.

Recommended Discussion structure:
- 5.1 Advantages of DeepLabV3+ for Fragmented Karst Rocky Desertification Mapping
- 5.2 Physical Meaning of FBR and LSMM-Based Continuous Inversion
- 5.3 Contribution of DEM-Derived Terrain Factors
- 5.4 Open-Source DEM for Transferability and GF-7 Stereo DEM for Local Enhancement
- 5.5 Comparison with Previous Studies
- 5.6 Limitations and Future Work

Located Discussion-style evidence:
- p.2: Nevertheless, the applications of these two methods in the research of karst feature extraction have some limitations.
- p.5: To validate the model robustness, another 76 quadrats, investigated during 8–10 March 2017, were used to derive the in situ measurements of EBF in the Nandong watershed, which were then compared with the EBF obtained from the developed model.
- p.8: Here, 264 in situ measurements of EBF across the Xiaojiang watershed were then compared with the EBF values obtained from the linear-regression model using the assessment indicators listed in Section 2.3.
- p.8: In this test experiment, 76 additional samples were collected throughout Nandong to be compared with the EBF information obtained from the original model, using the quantitative assessment indicators.
- p.10: Meanwhile, it is easily il lustrated that the KBRI values ranged more widely compared with other spectral indices, which confor med to the actual conditions in the study area.
- p.10: Meanwhile, it is easily illustrated that the KBRI values ranged more widely compared with other spectral indices, which conformed to the actual conditions in the study area.
- p.12: For KBRI, compared with the estimation accuracy in Xiaojiang, the RMSE and MAE increased, while the indicator of RMAPE and R2 decreased, indicating that the overall accuracy of the model developed with KBRI has slightly declined in Nandong, but could still mee
- p.14: Discussion Fractional ground cover extracted from remotely-sensed imagery has been widely used to estimate land degradation and human disturbances [44–46].

## 8. Conclusions Writing Pattern

- Typical structure: one compact section with objective reminder, method, key findings, and application value.
- Tone: restrained and evidence-aligned.
- Limitations/future work: sometimes included briefly; do not overclaim.
- Recommended template: “This study addressed [problem] using [data/method]. The results indicate [validated finding]. The approach supports [application], while future work should address [limitation].”

## 9. Figure and Table Style

| Figure/Table | Caption style | What it shows | Text reference pattern | Relevance to our manuscript |
|---|---|---|---|---|
| p.4 Figure 1 | descriptive caption with object/result label | study design/result/map/table evidence inferred from caption; inspect figure before reuse | main text generally refers by Figure/Table number | useful as pattern for maps, workflow, data source, accuracy, or comparison displays |
| p.4 Figure 1 | descriptive caption with object/result label | study design/result/map/table evidence inferred from caption; inspect figure before reuse | main text generally refers by Figure/Table number | useful as pattern for maps, workflow, data source, accuracy, or comparison displays |
| p.5 Table 1 | descriptive caption with object/result label | study design/result/map/table evidence inferred from caption; inspect figure before reuse | main text generally refers by Figure/Table number | useful as pattern for maps, workflow, data source, accuracy, or comparison displays |
| p.7 Figure 2 | descriptive caption with object/result label | study design/result/map/table evidence inferred from caption; inspect figure before reuse | main text generally refers by Figure/Table number | useful as pattern for maps, workflow, data source, accuracy, or comparison displays |
| p.7 Figure 2 | descriptive caption with object/result label | study design/result/map/table evidence inferred from caption; inspect figure before reuse | main text generally refers by Figure/Table number | useful as pattern for maps, workflow, data source, accuracy, or comparison displays |
| p.9 Figure 3 | descriptive caption with object/result label | study design/result/map/table evidence inferred from caption; inspect figure before reuse | main text generally refers by Figure/Table number | useful as pattern for maps, workflow, data source, accuracy, or comparison displays |
| p.9 Figure 3 | descriptive caption with object/result label | study design/result/map/table evidence inferred from caption; inspect figure before reuse | main text generally refers by Figure/Table number | useful as pattern for maps, workflow, data source, accuracy, or comparison displays |
| p.10 Figure 4 | descriptive caption with object/result label | study design/result/map/table evidence inferred from caption; inspect figure before reuse | main text generally refers by Figure/Table number | useful as pattern for maps, workflow, data source, accuracy, or comparison displays |
| p.10 Table 2 | descriptive caption with object/result label | study design/result/map/table evidence inferred from caption; inspect figure before reuse | main text generally refers by Figure/Table number | useful as pattern for maps, workflow, data source, accuracy, or comparison displays |
| p.10 Figure 4 | descriptive caption with object/result label | study design/result/map/table evidence inferred from caption; inspect figure before reuse | main text generally refers by Figure/Table number | useful as pattern for maps, workflow, data source, accuracy, or comparison displays |
| p.10 Table 2 | descriptive caption with object/result label | study design/result/map/table evidence inferred from caption; inspect figure before reuse | main text generally refers by Figure/Table number | useful as pattern for maps, workflow, data source, accuracy, or comparison displays |
| p.11 Figure 5 | descriptive caption with object/result label | study design/result/map/table evidence inferred from caption; inspect figure before reuse | main text generally refers by Figure/Table number | useful as pattern for maps, workflow, data source, accuracy, or comparison displays |
| p.11 Figure 5 | descriptive caption with object/result label | study design/result/map/table evidence inferred from caption; inspect figure before reuse | main text generally refers by Figure/Table number | useful as pattern for maps, workflow, data source, accuracy, or comparison displays |
| p.12 Table 3 | descriptive caption with object/result label | study design/result/map/table evidence inferred from caption; inspect figure before reuse | main text generally refers by Figure/Table number | useful as pattern for maps, workflow, data source, accuracy, or comparison displays |
| p.12 Table 2 | descriptive caption with object/result label | study design/result/map/table evidence inferred from caption; inspect figure before reuse | main text generally refers by Figure/Table number | useful as pattern for maps, workflow, data source, accuracy, or comparison displays |
| p.12 Table 3 | descriptive caption with object/result label | study design/result/map/table evidence inferred from caption; inspect figure before reuse | main text generally refers by Figure/Table number | useful as pattern for maps, workflow, data source, accuracy, or comparison displays |

Figure/table style lessons:
- Captions should state what is shown, not just name the figure.
- Text should cite figures/tables when interpreting evidence.
- Accuracy tables should separate metric types and class-level indicators.
- Suggested figures for our paper: study area, workflow, architecture, FBR map, grade map, DEM ablation, cross-region transfer, error/confusion analysis.

Located text reference patterns:
- p.3: Study Area The Xiaojiang watershed is located in eastern Yunnan Province, southwest China (24◦10′–24◦45′N, 103◦30′–104◦05′E; Figure 1), which has been suffering from serious KRD for decades due to the fragile karst ecosystem and serious conﬂicts between human beings and land reso
- p.3: The total area of the whole watershed attains 1008.39 km2, with 80.36% of the area covered by karst environment (Figure 1c).
- p.3: It is located in the southeast of Yunnan (23◦10′–23◦43′N, 103◦10′–103◦42′E; Figure 1), which is a typical super-large underground river watershed in southwest China [31], and also known as a serious KRD region [32].
- p.3: The total area of the Nandong watershed is 1617.13 km 2, in which 88.74% of the whole area is covered by karst landscape (Figure 1d).
- p.4: 2018, 10, x FOR PEER REVIEW 4 of 19 Figure 1.
- p.4: The L1TP products are composed of eight multispectral bands with a spatial resolution of 30 m, one panchromatic band with a resolution of 15 m, and two thermal bands collected at 100 m, but resampled to 30 m to match the multispectral Figure 1.
- p.5: The detailed description of Landsat-8 OLI images is shown in Table 1.
- p.5: Table 1.
- p.6: As shown in Figure 2, the spectral difference between bare rock and other land-cover types is apparent at SWIR bands, especially SWIR1 (band 6 in OLI image).
- p.7: 2018, 10, x FOR PEER REVIEW 7 of 19 Figure 2.

## 10. Terminology and Noun Phrase Extraction

| Recommended English term | Chinese equivalent | Use when | Avoid | Example pattern |
|---|---|---|---|---|
| karst rocky desertification | 喀斯特石漠化 | naming the process/problem | vague “rock desert” | mapping karst rocky desertification |
| bare-rock fraction | 裸岩率/裸岩覆盖比例 | continuous/proportional target | calling it a class map | estimate bare-rock fraction |
| exposed bedrock fraction | 基岩裸露率 | bedrock exposure target | mixing with vegetation cover | estimate exposed bedrock fraction |
| spectral mixture analysis | 光谱混合分析 | sub-pixel fraction estimation | classification metrics for regression | SMA-derived fraction |
| semantic segmentation | 语义分割 | pixel-level DL mapping | generic “deep learning” only | semantic segmentation model |
| DeepLabV3+ | DeepLabV3+ | main segmentation model | unexplained DL name | DeepLabV3+-based mapping |
| DEM-derived topographic factors | DEM 派生地形因子 | slope/aspect/elevation inputs | GF-7 transfer overclaim | DEM-derived terrain factors |
| class-level accuracy | 类别级精度 | categorical maps | OA only | report class-level accuracy |

Terms located in this paper: rocky desertification, karst rocky desertification, bare rock, exposed bedrock fraction, fractional vegetation cover, spectral mixture analysis, DEM, slope, aspect, Sentinel, Landsat, independent validation, overall accuracy.

## 11. Academic Phrase Bank

### Abstract phrases
- [Problem] poses a challenge for [region/application].
- Remote sensing provides an effective means for [monitoring/mapping target].
- This study used [data] to [objective].
- The proposed/comparative method was evaluated using [metrics].
- The results indicate that [method/data] improves [target mapping].
- These findings support [application or management goal].

### Introduction phrases
- [Phenomenon] has become an important ecological issue in [region].
- Previous studies have used [method family] to address [target].
- However, [limitation] remains insufficiently resolved.
- To address this gap, this study [objective].
- The main contributions are as follows: [contribution list].

### Methods phrases
- The overall workflow is shown in Figure X.
- The dataset was divided using [split strategy].
- Accuracy was evaluated using [metric family].
- To assess the contribution of [factor], an ablation experiment was conducted.
- [Model] was used as a baseline for comparison.

### Results phrases
- As shown in Figure X, [spatial pattern] was observed.
- Table X summarizes the performance of [models/data].
- Compared with [baseline], [method] achieved [metric improvement].
- The confusion matrix indicates that [class confusion pattern].
- The ablation results show the contribution of [factor].

### Discussion phrases
- This improvement may be attributed to [mechanism].
- The result is consistent with/ differs from previous studies because [reason].
- Although [method] performed well, [limitation] remains.
- Future work should further evaluate [uncertainty/transferability].
- These findings should be interpreted cautiously because [constraint].

### Conclusions phrases
- This study developed/evaluated [method] for [target].
- The main findings can be summarized as follows.
- The method provides a practical tool for [application].
- Further studies are needed to [future work].

### Figure/Table reference phrases
- Figure X illustrates the spatial distribution of [target].
- Table X lists the data sources and preprocessing steps.
- Figure X compares the mapping results of different methods.
- Table X reports the class-level accuracy metrics.
- The workflow in Figure X summarizes the main procedure.

### Limitation phrases
- A limitation of this study is [constraint].
- The uncertainty may arise from [source].
- The transferability of the method requires further validation.
- Future work should incorporate [data/validation].
- The results should not be generalized beyond [scope] without additional validation.

### Contribution phrases
- The contribution of this study lies in [method/data/validation].
- This work provides evidence for [scientific or applied value].
- The proposed framework improves [target] by integrating [components].
- The study offers a reproducible workflow for [application].
- The findings can support [monitoring/restoration/management].

## 12. Remote Sensing Style Lessons for Our Manuscript

- What to imitate: clear sectioning, data-method-result linkage, figure/table-supported argument.
- What not to imitate: do not blur continuous FBR inversion with categorical classification.
- Useful structure: background -> data/method -> validation -> spatial interpretation -> limitations.
- Useful phrases: use cautious, metric-specific, source-grounded claims.
- Useful terminology: use canonical KRD/FBR/DEM/segmentation terms consistently.
- Useful figure/table design: combine workflow, data table, maps, accuracy table, ablation, and confusion/error figures.
- Useful caution style: state data and validation constraints explicitly.
- Relevance level: high.

## 13. Manual Review Items

- none
