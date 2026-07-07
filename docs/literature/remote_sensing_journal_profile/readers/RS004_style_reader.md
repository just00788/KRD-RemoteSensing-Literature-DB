# Remote Sensing Style Reader: How Can We Realize Sustainable Development Goals in Rocky Desertified Regions by Enhancing Crop Yield and Restoring Ecological Function?

## 1. Bibliographic Information

- RS ID: RS004
- Title: How Can We Realize Sustainable Development Goals in Rocky Desertified Regions by Enhancing Crop Yield and Restoring Ecological Function?
- Authors: unknown
- Year: 2021
- Journal: Remote Sensing
- DOI: 10.3390/rs13091614
- PDF path: `docs/literature/pdfs/remote_sensing_only/2021_RemoteSens_13_1614_How_Can_We_Realize_Sustainable_Development_Goals_in_Rocky_De.pdf`
- Language: English
- Already read in previous batches: batch_01=False; batch_02=False
- This rereading focus: journal writing style, section architecture, figure/table pattern, terminology, and reusable templates.

## 2. Article Structure

- Primary headings detected: 20
- Independent Discussion: yes
- Independent Conclusions: yes
- Data Availability / Author Contributions / Funding / Conflicts of Interest: Data Availability=p.15; Author Contributions=p.15; Funding=p.15; Conflicts=p.15
- Supplementary Materials: not located
- Overall suitability: useful for our manuscript if we adapt the structure without copying wording.

| Section | Subsections | Function | Relevance to our manuscript |
|---|---|---|---|
| 1. Introduction | see source headings | sets background, problem importance, literature gap | adapt if matching our FBR/DeepLabV3+/DEM workflow |
| 2. Data and Method | see source headings | establishes reproducible materials, data, workflow, and evaluation | adapt if matching our FBR/DeepLabV3+/DEM workflow |
| 2.1. Study Region | see source headings | article support section or topic-specific subsection | adapt if matching our FBR/DeepLabV3+/DEM workflow |
| 2.2. Dataset | see source headings | establishes reproducible materials, data, workflow, and evaluation | adapt if matching our FBR/DeepLabV3+/DEM workflow |
| 2.3. Calculation of Yield Gap | see source headings | article support section or topic-specific subsection | adapt if matching our FBR/DeepLabV3+/DEM workflow |
| 2.3.2. Calculation of Yield Gap | see source headings | article support section or topic-specific subsection | adapt if matching our FBR/DeepLabV3+/DEM workflow |
| 2.4. Ensembled BP (Back Propagation) Artificial Neural Networks | see source headings | article support section or topic-specific subsection | adapt if matching our FBR/DeepLabV3+/DEM workflow |
| 2.4.1. Single BP Network | see source headings | article support section or topic-specific subsection | adapt if matching our FBR/DeepLabV3+/DEM workflow |
| 2.4.2. Evaluating Accuracy of Simulation | see source headings | article support section or topic-specific subsection | adapt if matching our FBR/DeepLabV3+/DEM workflow |
| 2.4.3. Ensemble Approach | see source headings | article support section or topic-specific subsection | adapt if matching our FBR/DeepLabV3+/DEM workflow |
| 2.4.4. Scenario Settings and Convergence Test of Ensembled ANNs | see source headings | article support section or topic-specific subsection | adapt if matching our FBR/DeepLabV3+/DEM workflow |
| 3. Results | see source headings | reports maps, comparisons, and metrics | adapt if matching our FBR/DeepLabV3+/DEM workflow |
| 3.1. Simulation of Single BP Network | see source headings | article support section or topic-specific subsection | adapt if matching our FBR/DeepLabV3+/DEM workflow |
| 3.2. Convergence Test for Ensembled Networks | see source headings | article support section or topic-specific subsection | adapt if matching our FBR/DeepLabV3+/DEM workflow |
| 3.3. Yield Gap in Guizhou Province | see source headings | article support section or topic-specific subsection | adapt if matching our FBR/DeepLabV3+/DEM workflow |
| 3.4. Crop Yield and Fertilization Efficiency under Different Scenarios | see source headings | article support section or topic-specific subsection | adapt if matching our FBR/DeepLabV3+/DEM workflow |
| 3.5. Yield Gap Closing | see source headings | article support section or topic-specific subsection | adapt if matching our FBR/DeepLabV3+/DEM workflow |
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
- Approximate abstract length: 182 words; 9 sentence-like units.
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

Located Introduction anchors: p.1, p.4

## 5. Materials and Methods Writing Pattern

- Study area: usually separated or early in Methods; anchor not located.
- Data sources: anchor p.2, p.3, p.4, p.5, p.7, p.13, p.15, p.22, p.23, p.24; often supported by a data table.
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
- p.2: Despite changes in agricultural management strategies in Guizhou Province since the 1960s [28], the yield improvement of some staple crops like wheat and rice has stagnated by comparing yield data from 1985 and 2005 [29].
- p.2: Until now, the existing crop yield estimation models mainly contained statistical approaches and process-based mo dels (including large-scale global gridded crop models) [35,36].
- p.2: Ho wever, the underground environment of the critical zone in karst region is complex, with multiple elements (such as limestone fissures) having a large impact on natural vegetation growth [40,41], as well as crop production, so this compromise may cause unce
- p.2: In contrast, process-based models require different procedures for parameterization and calibration.
- p.2: However, the karst environment’s highly he terogeneous nature and the prevalence of small-scale subsistence farming in Guizhou im pede the applicability of existing processbased models used for large-scale applications [43,44].
- p.3: 2021, 13, 1614 3 of 24 learning methods, such as artificial neural networks (ANN), provides a new solution to identify the relationship of different factors and crop yield with nonlinear regressions [45].
- p.3: Based on ANN training, higher accuracy in the simulation of crop yield could be achieved [46,47].
- p.3: Data and Method 2.1.
- p.3: Dataset To simulate crop yield (per unit area), 14 variables were selected as input factors (Table 1, excluding crop yield, crop area, N and P balance), of which annual total rainfall, soil bulk density, irrigation, nitrogen (N) fertilizer rate, phosphorus (P)
- p.3: Specifically, we extracted all the data from (circa) year 2000 and unified their spatial resolution into 5 ′ by aggregation (overlaying meteorological data with a spatial resolution of 5° on 5′ data and extracted meteorological

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
- p.1: Results showed that the total yield of the selected crops had, on average, reached over 72.
- p.1: For example, in karst regions, rocky desertification, a process of land degradation involving serious soil erosion, results in extensive exposure of basement rocks, a drastic decrease in soil productivity, and the appearance of a desert-like landscape [7–9].
- p.3: Based on ANN training, higher accuracy in the simulation of crop yield could be achieved [46,47].
- p.3: The results of this work are useful as a DS T for policymakers and other stakeholders to optimize food demand and environmental impact in agriculture development.
- p.4: First, we conducted an unsupervised spatial classification method (self-organizing feature mapping, or SOFM) to define different zones of “natural environment” (natural zones hereinafter) based on temperature, rainfall, shortwave radiation and slope, which hum
- p.4: They use a neighborhood function to preserve the input space's topological properties and realize unsupervised classification by different data resources.
- p.4: The whole process of this work is to reflect the input variables into lower dimensional space to realize the classification.
- p.5: Process of classification of natural zones.
- p.6: Single BP Network BP network is widely applied in classification, simulation and forecast across different research disciplines, and in our previous work it offered the best balance between accuracy in predicting crop yield in Guizhou Province and time cost [6
- p.6: This supervised learning is conducted using the mean square error and gradient descent algorithm to achieve the correction of the network connection weights, to minimize the difference between the mean square error of the actual output to achieve prediction ac

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
- p.1: This is especially evident for some underdeveloped areas due to their environmental and economic al limitations [6].
- p.2: The yield gap can be classified as either the difference in crop yield between the optimal experimental environment (without growth limitations) and the natural environment, or the yield potential in farmland over a specified spatial and temporal scale of inte
- p.8: Scenario Settings and Convergence Test of Ensembled ANNs To evaluate different future scenarios of agricultural management, we changed the input of N&P fertilizer (by ±10%) and irrigation rates (only by +10%, as the study region was proven to be lacking water 
- p.8: For example, groundnut simulation had the best performance, indicated by the largest R (0.87) and least RME (11.67%), compared with the worst performance for potato (with R of 0.68 and RME of 15.38%).
- p.9: Yield Gap in Guizhou Province The extent of yield gap (or potential yield) varied among the different pairs of crop and prefecture, with some crop species having relatively more potential for yield improvement in some of the prefectures compared with others.
- p.13: Discussion Establishing the quantitative relationship between crop yield and the environment is essential for understanding each factor's interaction and predicting future crop yield under different climate or agricultural scenarios.
- p.13: Clustering of multiple networks (forming ensembled networks) can resolve these issues, providing a more reliable forecast of crop yield under future scenarios, but the time cost should also be fully considered.
- p.14: Second, the facilitation of crop growth via fertilization requires reasonable consideration of the ratios of different fertilizers (N, P and K) specific to the local area’s nutrient limitations and the crop species physiology, rather than a prescribed addition

## 8. Conclusions Writing Pattern

- Typical structure: one compact section with objective reminder, method, key findings, and application value.
- Tone: restrained and evidence-aligned.
- Limitations/future work: sometimes included briefly; do not overclaim.
- Recommended template: “This study addressed [problem] using [data/method]. The results indicate [validated finding]. The approach supports [application], while future work should address [limitation].”

## 9. Figure and Table Style

| Figure/Table | Caption style | What it shows | Text reference pattern | Relevance to our manuscript |
|---|---|---|---|---|
| p.3 Figure 1 | descriptive caption with object/result label | study design/result/map/table evidence inferred from caption; inspect figure before reuse | main text generally refers by Figure/Table number | useful as pattern for maps, workflow, data source, accuracy, or comparison displays |
| p.4 Table 1 | descriptive caption with object/result label | study design/result/map/table evidence inferred from caption; inspect figure before reuse | main text generally refers by Figure/Table number | useful as pattern for maps, workflow, data source, accuracy, or comparison displays |
| p.5 Figure 2 | descriptive caption with object/result label | study design/result/map/table evidence inferred from caption; inspect figure before reuse | main text generally refers by Figure/Table number | useful as pattern for maps, workflow, data source, accuracy, or comparison displays |
| p.6 Figure 3 | descriptive caption with object/result label | study design/result/map/table evidence inferred from caption; inspect figure before reuse | main text generally refers by Figure/Table number | useful as pattern for maps, workflow, data source, accuracy, or comparison displays |
| p.7 Figure 4 | descriptive caption with object/result label | study design/result/map/table evidence inferred from caption; inspect figure before reuse | main text generally refers by Figure/Table number | useful as pattern for maps, workflow, data source, accuracy, or comparison displays |
| p.10 Figure 5 | descriptive caption with object/result label | study design/result/map/table evidence inferred from caption; inspect figure before reuse | main text generally refers by Figure/Table number | useful as pattern for maps, workflow, data source, accuracy, or comparison displays |
| p.11 Figure 6 | descriptive caption with object/result label | study design/result/map/table evidence inferred from caption; inspect figure before reuse | main text generally refers by Figure/Table number | useful as pattern for maps, workflow, data source, accuracy, or comparison displays |
| p.12 Figure 7 | descriptive caption with object/result label | study design/result/map/table evidence inferred from caption; inspect figure before reuse | main text generally refers by Figure/Table number | useful as pattern for maps, workflow, data source, accuracy, or comparison displays |
| p.12 Figure 8 | descriptive caption with object/result label | study design/result/map/table evidence inferred from caption; inspect figure before reuse | main text generally refers by Figure/Table number | useful as pattern for maps, workflow, data source, accuracy, or comparison displays |

Figure/table style lessons:
- Captions should state what is shown, not just name the figure.
- Text should cite figures/tables when interpreting evidence.
- Accuracy tables should separate metric types and class-level indicators.
- Suggested figures for our paper: study area, workflow, architecture, FBR map, grade map, DEM ablation, cross-region transfer, error/confusion analysis.

Located text reference patterns:
- p.3: Study Region Guizhou Province is located in southwest China, at the heart of the East Asia Karst, one of the three largest areas of almost unbroken karst globally [48] (Figure 1).
- p.3: Figure 1.
- p.3: Dataset To simulate crop yield (per unit area), 14 variables were selected as input factors (Table 1, excluding crop yield, crop area, N and P balance), of which annual total rainfall, soil bulk density, irrigation, nitrogen (N) fertilizer rate, phosphorus (P) fertilizer rate and
- p.4: Table 1.
- p.4: SOFM The SOFM network (Figure 2) consists of a fully interconnected array of neurons with a topology input layer and the competition la yer [67].
- p.5: Figure 2.
- p.5: Calculation of Yield Gap The yield gap was calculated using three steps: (1) For each natural zone, the grid cells were sorted by their yield value, ranked from lowest to highest; (2) The grid cells’ respective harvested areas were accumulated into a histogram, then the percentil
- p.6: Figure 3.
- p.7: Ensemble Approach The ensemble approach for ANN is to inte grate a finite number of ANNs that are trained for the same purpose whose predictions are combined to generate a unique output (Figure 4).
- p.7: Figure 4.

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

Terms located in this paper: rocky desertification, karst rocky desertification, machine learning, random forest, DEM, slope.

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
