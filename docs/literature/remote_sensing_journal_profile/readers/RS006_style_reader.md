# Remote Sensing Style Reader: Optimization of Rocky Desertification Classification Model Based on Vegetation Type and Seasonal Characteristic

## 1. Bibliographic Information

- RS ID: RS006
- Title: Optimization of Rocky Desertification Classification Model Based on Vegetation Type and Seasonal Characteristic
- Authors: unknown
- Year: 2021
- Journal: Remote Sensing
- DOI: 10.3390/rs13152935
- PDF path: `docs/literature/pdfs/remote_sensing_only/2021_RemoteSens_13_2935_Optimization_of_Rocky_Desertification_Classification_Model_B.pdf`
- Language: English
- Already read in previous batches: batch_01=True; batch_02=False
- This rereading focus: journal writing style, section architecture, figure/table pattern, terminology, and reusable templates.

## 2. Article Structure

- Primary headings detected: 33
- Independent Discussion: yes
- Independent Conclusions: yes
- Data Availability / Author Contributions / Funding / Conflicts of Interest: Data Availability=p.21; Author Contributions=p.21; Funding=p.21; Conflicts=not located
- Supplementary Materials: not located
- Overall suitability: useful for our manuscript if we adapt the structure without copying wording.

| Section | Subsections | Function | Relevance to our manuscript |
|---|---|---|---|
| 3 School of Computer Science and Technology, Soochow University, Suzhou 215301, China | see source headings | article support section or topic-specific subsection | adapt if matching our FBR/DeepLabV3+/DEM workflow |
| 1. Introduction | see source headings | sets background, problem importance, literature gap | adapt if matching our FBR/DeepLabV3+/DEM workflow |
| 2. Data and Material | see source headings | establishes reproducible materials, data, workflow, and evaluation | adapt if matching our FBR/DeepLabV3+/DEM workflow |
| 2.1. Research Area | see source headings | establishes reproducible materials, data, workflow, and evaluation | adapt if matching our FBR/DeepLabV3+/DEM workflow |
| 2.2.1. Image Data | see source headings | establishes reproducible materials, data, workflow, and evaluation | adapt if matching our FBR/DeepLabV3+/DEM workflow |
| 2.2.2. Ground Survey Data | see source headings | establishes reproducible materials, data, workflow, and evaluation | adapt if matching our FBR/DeepLabV3+/DEM workflow |
| 3. Technical Approach | see source headings | article support section or topic-specific subsection | adapt if matching our FBR/DeepLabV3+/DEM workflow |
| 3.1. Workflow of the Processing Steps | see source headings | article support section or topic-specific subsection | adapt if matching our FBR/DeepLabV3+/DEM workflow |
| 3.2. Image Preprocessing | see source headings | article support section or topic-specific subsection | adapt if matching our FBR/DeepLabV3+/DEM workflow |
| 3.3. Rocky Desertification Factors | see source headings | article support section or topic-specific subsection | adapt if matching our FBR/DeepLabV3+/DEM workflow |
| 3.4. Model Construction Method | see source headings | establishes reproducible materials, data, workflow, and evaluation | adapt if matching our FBR/DeepLabV3+/DEM workflow |
| 3.4.1. Logistic Regression Model | see source headings | article support section or topic-specific subsection | adapt if matching our FBR/DeepLabV3+/DEM workflow |
| 3.4.2. Random Forest (RF) Model | see source headings | article support section or topic-specific subsection | adapt if matching our FBR/DeepLabV3+/DEM workflow |
| 3.4.3. Support Vector Machine (SVM) Model | see source headings | article support section or topic-specific subsection | adapt if matching our FBR/DeepLabV3+/DEM workflow |
| 3.4.4. Accuracy Analysis Method | see source headings | establishes reproducible materials, data, workflow, and evaluation | adapt if matching our FBR/DeepLabV3+/DEM workflow |
| 1. Production accuracy | see source headings | article support section or topic-specific subsection | adapt if matching our FBR/DeepLabV3+/DEM workflow |
| 2. User accuracy | see source headings | article support section or topic-specific subsection | adapt if matching our FBR/DeepLabV3+/DEM workflow |
| 5. Quantity Disagreement and Allocation Disagreement | see source headings | article support section or topic-specific subsection | adapt if matching our FBR/DeepLabV3+/DEM workflow |
| 4. Results and Analysis | see source headings | reports maps, comparisons, and metrics | adapt if matching our FBR/DeepLabV3+/DEM workflow |
| 4.2. Construction and Comparison of Rocky Desertification Models | see source headings | article support section or topic-specific subsection | adapt if matching our FBR/DeepLabV3+/DEM workflow |
| 4.3. Optimization of the Rocky Desertification Estimation Model | see source headings | article support section or topic-specific subsection | adapt if matching our FBR/DeepLabV3+/DEM workflow |
| 4.3.1. Workflow of Model Improvement | see source headings | article support section or topic-specific subsection | adapt if matching our FBR/DeepLabV3+/DEM workflow |
| 4.3.2. Model Optimization Based on Vegetation Types at Different Heights | see source headings | article support section or topic-specific subsection | adapt if matching our FBR/DeepLabV3+/DEM workflow |
| 4.3.3. Extraction and Analysis of Seasonal NDVI-STD | see source headings | article support section or topic-specific subsection | adapt if matching our FBR/DeepLabV3+/DEM workflow |
| 4.3.4. Optimizing the Model by Integrating the Seasonal Phase and Vegetation Height | see source headings | article support section or topic-specific subsection | adapt if matching our FBR/DeepLabV3+/DEM workflow |
| 4.4. Analysis of Spatiotemporal Change in Rocky Desertification | see source headings | article support section or topic-specific subsection | adapt if matching our FBR/DeepLabV3+/DEM workflow |
| 5. Discussion | see source headings | interprets mechanisms, compares literature, states limitations | adapt if matching our FBR/DeepLabV3+/DEM workflow |
| 5.3. Mixed Pixels and Scale Effect | see source headings | article support section or topic-specific subsection | adapt if matching our FBR/DeepLabV3+/DEM workflow |
| 5.3.1. Ground Survey Data | see source headings | establishes reproducible materials, data, workflow, and evaluation | adapt if matching our FBR/DeepLabV3+/DEM workflow |
| 5.3.2. MODIS Data | see source headings | establishes reproducible materials, data, workflow, and evaluation | adapt if matching our FBR/DeepLabV3+/DEM workflow |

## 3. Abstract Writing Pattern

- Background opening: usually starts from environmental importance or monitoring challenge.
- Problem/gap: located through abstract text.
- Data and method compression: Remote Sensing abstracts tend to compress sensor, study area, model, and validation into one or two sentences.
- Result presentation: reports principal results and often includes metrics when central to the paper.
- Specific accuracy numbers: not detected in abstract sample.
- Significance ending: commonly links the method to monitoring, restoration, or decision support.
- Approximate abstract length: 236 words; 17 sentence-like units.
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

- Study area: usually separated or early in Methods; anchor p.3.
- Data sources: anchor p.1, p.2, p.3, p.4, p.5, p.6, p.7, p.8, p.12, p.13, ...; often supported by a data table.
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
- p.1: remote sensing Article Optimization of Rocky Desertiﬁcation Classiﬁcation Model Based on Vegetation Type and Seasonal Characteristic Chunhua Qian 1,2 , Hequn Qiang 2,3 , Feng Wang 2 and Mingyang Li 1,* /gid00030/gid00035/gid00032/gid00030/gid00038/gid00001/gid
- p.1: Optimization of Rocky Desertiﬁcation Classiﬁcation Model Based on Vegetation Type and Seasonal Characteristic.
- p.1: 1 School of Forestry, Nanjing Forestry University, Nanjing 210037, China; chqian@szai.edu.cn 2 School of Smart Agricultural, Suzhou Polytechnic Institute of Agriculture, Suzhou 215008, China; hqqiang@szai.edu.cn (H.Q.); cfwf96@163.com (F.W.) 3 School of Comput
- p.1: Taking Guizhou province as the research area and based on MODIS and continuous forest inventory data in China, we used a machine learning algorithm to build a rocky desertiﬁcation model with bedrock exposure rate, temperature difference, humidity, and other ch
- p.1: The results showed the following: (1) The supervised classiﬁcation method was used to build a rocky desertiﬁcation model, and the logical model, RF model, and SVM model were constructed separately.
- p.1: The accuracies of the models were 73.8%, 78.2%, and 80.6%, respectively, and the kappa coefﬁcients were 0.61, 0.672, and 0.707, respectively.
- p.1: After combining them, the model accuracy and kappa coefﬁcient improved to 91.1% and 0.861.
- p.1: In conclusion, combining the vertical spatial structure of vegetation and the differences in seasonal phase is an effective method to improve the modeling accuracy of rocky desertiﬁcation, and the SVM model has the highest rocky desertiﬁcation classiﬁcation ac
- p.1: The research results provide data support for exploring the spatiotemporal evolution pattern of rocky desertiﬁcation in Guizhou.
- p.1: Keywords: rocky desertiﬁcation; supervised classiﬁcation method; MODIS data; feature extraction; spatial and temporal distribution 1.

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
- p.1: Taking Guizhou province as the research area and based on MODIS and continuous forest inventory data in China, we used a machine learning algorithm to build a rocky desertiﬁcation model with bedrock exposure rate, temperature difference, humidity, and other ch
- p.1: The results showed the following: (1) The supervised classiﬁcation method was used to build a rocky desertiﬁcation model, and the logical model, RF model, and SVM model were constructed separately.
- p.1: The accuracies of the models were 73.8%, 78.2%, and 80.6%, respectively, and the kappa coefﬁcients were 0.61, 0.672, and 0.707, respectively.
- p.1: After combining them, the model accuracy and kappa coefﬁcient improved to 91.1% and 0.861.
- p.1: In conclusion, combining the vertical spatial structure of vegetation and the differences in seasonal phase is an effective method to improve the modeling accuracy of rocky desertiﬁcation, and the SVM model has the highest rocky desertiﬁcation classiﬁcation ac
- p.1: The research results provide data support for exploring the spatiotemporal evolution pattern of rocky desertiﬁcation in Guizhou.
- p.2: The results showed that the overall classiﬁcation accuracy of the three models was more than 80%, which indicated that the three feature space models are feasible for extracting desertiﬁcation information from the Mongolian Plateau.
- p.2: The results showed that there were significant differences in the LST of different land use types, with the highest being recorded for construction land and the lowest being recorded for forests.
- p.2: The results showed that it is accurate and reliable in estimating rocky desertiﬁcation information.
- p.2: [29] used ALOS images, the dichotomous pixel model (DPM), and spectral hybrid analysis (SMA) methods to improve the accuracy of rocky desertiﬁcation estimation in Southwest China up to 80.5%.

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
- p.12: Compared with the traditional factor weight accumulation method or decision tree method, the accuracy of the rocky desertiﬁcation monitoring model constructed by the three algorithms in this study is higher than that of the traditional method [ 43,59].
- p.17: Discussion Rocky desertiﬁcation monitoring can provide reliable data support for precise rocky desertiﬁcation control and ecological restoration.
- p.18: In future research, we will attempt the accurate discrimination of severe and extremely severe rocky desertiﬁcation using the sample equilibrium method.
- p.18: More samples will be obtained to achieve more precise differentiation of vegetation types in future research to improve the accuracy of rocky desertiﬁcation estimation.
- p.19: In the future, the data ﬁlling method for areas with cloud interference will be researched and more groups of data will be used to express the temporal differences of samples in a year in order to improve the accuracy of temporal data and to improve the accura
- p.19: The seasonal temporal differences and the vegetation index characteristics of the samples will be combined as the basis of classiﬁcation modeling to optimize the estimation model of rocky desertiﬁcation in future research.
- p.19: Instrument stability, light saturation imaging, and shadows in optical sensors may also have caused problems, so SAR data can be integrated to compensate for the shortcomings of optical images in future research.
- p.20: The model results in 2005 and 2015 were compared with the NFCI data in the same year, and the overall accuracy was more than 90%, indicating that the proposed rocky desertiﬁcation monitoring model was reliable.

## 8. Conclusions Writing Pattern

- Typical structure: one compact section with objective reminder, method, key findings, and application value.
- Tone: restrained and evidence-aligned.
- Limitations/future work: sometimes included briefly; do not overclaim.
- Recommended template: “This study addressed [problem] using [data/method]. The results indicate [validated finding]. The approach supports [application], while future work should address [limitation].”

## 9. Figure and Table Style

| Figure/Table | Caption style | What it shows | Text reference pattern | Relevance to our manuscript |
|---|---|---|---|---|
| p.5 Figure 1 | descriptive caption with object/result label | study design/result/map/table evidence inferred from caption; inspect figure before reuse | main text generally refers by Figure/Table number | useful as pattern for maps, workflow, data source, accuracy, or comparison displays |
| p.5 Figure 1 | descriptive caption with object/result label | study design/result/map/table evidence inferred from caption; inspect figure before reuse | main text generally refers by Figure/Table number | useful as pattern for maps, workflow, data source, accuracy, or comparison displays |
| p.6 Figure 2 | descriptive caption with object/result label | study design/result/map/table evidence inferred from caption; inspect figure before reuse | main text generally refers by Figure/Table number | useful as pattern for maps, workflow, data source, accuracy, or comparison displays |
| p.6 Figure 2 | descriptive caption with object/result label | study design/result/map/table evidence inferred from caption; inspect figure before reuse | main text generally refers by Figure/Table number | useful as pattern for maps, workflow, data source, accuracy, or comparison displays |
| p.7 Figure 3 | descriptive caption with object/result label | study design/result/map/table evidence inferred from caption; inspect figure before reuse | main text generally refers by Figure/Table number | useful as pattern for maps, workflow, data source, accuracy, or comparison displays |
| p.7 Table 1 | descriptive caption with object/result label | study design/result/map/table evidence inferred from caption; inspect figure before reuse | main text generally refers by Figure/Table number | useful as pattern for maps, workflow, data source, accuracy, or comparison displays |
| p.7 Figure 3 | descriptive caption with object/result label | study design/result/map/table evidence inferred from caption; inspect figure before reuse | main text generally refers by Figure/Table number | useful as pattern for maps, workflow, data source, accuracy, or comparison displays |
| p.7 Table 1 | descriptive caption with object/result label | study design/result/map/table evidence inferred from caption; inspect figure before reuse | main text generally refers by Figure/Table number | useful as pattern for maps, workflow, data source, accuracy, or comparison displays |
| p.11 Figure 4 | descriptive caption with object/result label | study design/result/map/table evidence inferred from caption; inspect figure before reuse | main text generally refers by Figure/Table number | useful as pattern for maps, workflow, data source, accuracy, or comparison displays |
| p.11 Figure 5 | descriptive caption with object/result label | study design/result/map/table evidence inferred from caption; inspect figure before reuse | main text generally refers by Figure/Table number | useful as pattern for maps, workflow, data source, accuracy, or comparison displays |
| p.11 Figure 5 | descriptive caption with object/result label | study design/result/map/table evidence inferred from caption; inspect figure before reuse | main text generally refers by Figure/Table number | useful as pattern for maps, workflow, data source, accuracy, or comparison displays |
| p.11 Figure 4 | descriptive caption with object/result label | study design/result/map/table evidence inferred from caption; inspect figure before reuse | main text generally refers by Figure/Table number | useful as pattern for maps, workflow, data source, accuracy, or comparison displays |
| p.11 Figure 4 | descriptive caption with object/result label | study design/result/map/table evidence inferred from caption; inspect figure before reuse | main text generally refers by Figure/Table number | useful as pattern for maps, workflow, data source, accuracy, or comparison displays |
| p.11 Figure 5 | descriptive caption with object/result label | study design/result/map/table evidence inferred from caption; inspect figure before reuse | main text generally refers by Figure/Table number | useful as pattern for maps, workflow, data source, accuracy, or comparison displays |
| p.11 Figure 5 | descriptive caption with object/result label | study design/result/map/table evidence inferred from caption; inspect figure before reuse | main text generally refers by Figure/Table number | useful as pattern for maps, workflow, data source, accuracy, or comparison displays |
| p.11 Figure 5 | descriptive caption with object/result label | study design/result/map/table evidence inferred from caption; inspect figure before reuse | main text generally refers by Figure/Table number | useful as pattern for maps, workflow, data source, accuracy, or comparison displays |

Figure/table style lessons:
- Captions should state what is shown, not just name the figure.
- Text should cite figures/tables when interpreting evidence.
- Accuracy tables should separate metric types and class-level indicators.
- Suggested figures for our paper: study area, workflow, architecture, FBR map, grade map, DEM ablation, cross-region transfer, error/confusion analysis.

Located text reference patterns:
- p.4: The remaining 5266 sample points were used for rocky desertiﬁcation monitoring model research, as shown in Figure 1.
- p.5: Figure 1.
- p.5: Figure 1.
- p.6: 2021, 13, 2935 6 of 23 of the processing steps is shown as Figure 2.
- p.6: The workflow of the processing steps is shown as Figure 2.
- p.6: Figure 2.
- p.6: Figure 2.
- p.6: Formula 1 was used to identify clouds in this study, and the cloud recognition effect is shown in Figure 3.
- p.7: Formula 1 was used to identify clouds in this study, and the cloud recognition effect is shown in Figure 3.
- p.7: C1 = (0003) & StateQA, C2 = (0004) & StateQA, C3 = (0300) & StateQA C1||C2||C3 = 1 (1) (a) ( b) Figure 3.

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

Terms located in this paper: rocky desertification, fractional vegetation cover, machine learning, random forest, support vector machine, DEM, slope, aspect, Landsat, overall accuracy, Kappa.

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
