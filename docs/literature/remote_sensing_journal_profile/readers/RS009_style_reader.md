# Remote Sensing Style Reader: Extraction of Rocky Desertification Information in the Karst Area Based on the Red-NIR-SWIR Spectral Feature Space

## 1. Bibliographic Information

- RS ID: RS009
- Title: Extraction of Rocky Desertification Information in the Karst Area Based on the Red-NIR-SWIR Spectral Feature Space
- Authors: unknown
- Year: 2023
- Journal: Remote Sensing
- DOI: 10.3390/rs15123056
- PDF path: `docs/literature/pdfs/remote_sensing_only/2023_RemoteSens_15_3056_Extraction_of_Rocky_Desertification_Information_in_the_Karst.pdf`
- Language: English
- Already read in previous batches: batch_01=False; batch_02=False
- This rereading focus: journal writing style, section architecture, figure/table pattern, terminology, and reusable templates.

## 2. Article Structure

- Primary headings detected: 22
- Independent Discussion: yes
- Independent Conclusions: yes
- Data Availability / Author Contributions / Funding / Conflicts of Interest: Data Availability=p.19; Author Contributions=p.19; Funding=p.19; Conflicts=not located
- Supplementary Materials: not located
- Overall suitability: useful for our manuscript if we adapt the structure without copying wording.

| Section | Subsections | Function | Relevance to our manuscript |
|---|---|---|---|
| 1 College of Forestry, Guizhou University, Guiyang 550025, China | see source headings | article support section or topic-specific subsection | adapt if matching our FBR/DeepLabV3+/DEM workflow |
| 2 Research Institute of Forestry, Chinese Academy of Forestry, Beijing 100091, China | see source headings | article support section or topic-specific subsection | adapt if matching our FBR/DeepLabV3+/DEM workflow |
| 1. Introduction | see source headings | sets background, problem importance, literature gap | adapt if matching our FBR/DeepLabV3+/DEM workflow |
| 2. Materials | see source headings | article support section or topic-specific subsection | adapt if matching our FBR/DeepLabV3+/DEM workflow |
| 2.1. Study Area | see source headings | establishes reproducible materials, data, workflow, and evaluation | adapt if matching our FBR/DeepLabV3+/DEM workflow |
| 2.2. Data Collection and Processing | see source headings | establishes reproducible materials, data, workflow, and evaluation | adapt if matching our FBR/DeepLabV3+/DEM workflow |
| 30 September 2022 | see source headings | article support section or topic-specific subsection | adapt if matching our FBR/DeepLabV3+/DEM workflow |
| 21 June 2022 | see source headings | article support section or topic-specific subsection | adapt if matching our FBR/DeepLabV3+/DEM workflow |
| 2.3. Spectral Characteristics of Each Land Cover Type | see source headings | article support section or topic-specific subsection | adapt if matching our FBR/DeepLabV3+/DEM workflow |
| 3. Methods | see source headings | establishes reproducible materials, data, workflow, and evaluation | adapt if matching our FBR/DeepLabV3+/DEM workflow |
| 3.1.1. Model Construction Based on the SWIR-NIR Spectral Feature Space | see source headings | article support section or topic-specific subsection | adapt if matching our FBR/DeepLabV3+/DEM workflow |
| 3.1.2. Model Construction Based on the Red-NIR Spectral Feature Space | see source headings | article support section or topic-specific subsection | adapt if matching our FBR/DeepLabV3+/DEM workflow |
| 3.1.3. Model Construction Based on the SWIR-Red Spectral Feature Space | see source headings | article support section or topic-specific subsection | adapt if matching our FBR/DeepLabV3+/DEM workflow |
| 3.2. Calculation of Feature Space Model Based on Surface Parameters | see source headings | article support section or topic-specific subsection | adapt if matching our FBR/DeepLabV3+/DEM workflow |
| 3.4. Accuracy Assessment | see source headings | article support section or topic-specific subsection | adapt if matching our FBR/DeepLabV3+/DEM workflow |
| 4. Results | see source headings | reports maps, comparisons, and metrics | adapt if matching our FBR/DeepLabV3+/DEM workflow |
| 4.2. Comparison of the Accuracy of the Models | see source headings | article support section or topic-specific subsection | adapt if matching our FBR/DeepLabV3+/DEM workflow |
| 5. Discussion | see source headings | interprets mechanisms, compares literature, states limitations | adapt if matching our FBR/DeepLabV3+/DEM workflow |
| 5.1. Sources of Error and Applicability of Each Model | see source headings | article support section or topic-specific subsection | adapt if matching our FBR/DeepLabV3+/DEM workflow |
| 5.2. Research Limitations | see source headings | article support section or topic-specific subsection | adapt if matching our FBR/DeepLabV3+/DEM workflow |
| 6. Conclusions | see source headings | summarizes contribution and application value | adapt if matching our FBR/DeepLabV3+/DEM workflow |
| References | see source headings | article support section or topic-specific subsection | adapt if matching our FBR/DeepLabV3+/DEM workflow |

## 3. Abstract Writing Pattern

- Background opening: usually starts from environmental importance or monitoring challenge.
- Problem/gap: located through abstract text.
- Data and method compression: Remote Sensing abstracts tend to compress sensor, study area, model, and validation into one or two sentences.
- Result presentation: reports principal results and often includes metrics when central to the paper.
- Specific accuracy numbers: likely present.
- Significance ending: commonly links the method to monitoring, restoration, or decision support.
- Approximate abstract length: 235 words; 6 sentence-like units.
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

- Study area: usually separated or early in Methods; anchor p.1, p.3, p.4, p.5, p.6, p.7, p.13, p.15, p.16, p.18.
- Data sources: anchor p.1, p.4, p.5, p.6, p.12, p.19, p.20, p.21, p.22; often supported by a data table.
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
- p.1: The three models of perpendicular rocky desertiﬁcation index 1 (PRDI1), perpendicular rocky desertiﬁcation index 2 (PRDI2) and perpendicular rocky desertiﬁcation index 3 (PRDI3) were also constructed based on the variation of the degree of rocky desertiﬁcation
- p.1: The accuracy of the rocky desertiﬁcation extracted by these three index models was veriﬁed and compared with the karst rocky desertiﬁcation index (KRDI) and rocky desertiﬁcation diﬀerence index (RSDDI), which are constructed based on the surface parameter feat
- p.1: The results show that: (1) The waveband reﬂectance -based feature space model provides a new method for large-scale rocky desertiﬁcation information extraction, characterized by easy data acquisition, simple index calculation and good stability, and is conduci
- p.1: (2) The overall accuracy and Kappa coeﬃcient of PRDI1 are 0.829 and 0.784, respectively, both higher than other index models, showing the best applicability, accura cy and eﬀectiveness in rocky desertiﬁcation information extraction .
- p.1: The method proposed in this study is a scientiﬁc and necessary complement to the characteristic spatial methods based on diﬀerent surface parameters, and can provide important methodological support for the rapid and eﬃcient monitoring of karstic rocky deserti
- p.2: Traditional research methods usually rely on ﬁeld surveys of exposed bed rock, vegetation, soil thickness and related indicators, but ﬁeld surveys are often costly, time- consuming and labor -intensive, especially for large -scale monitoring [6,7].
- p.2: Conventional remote sensing image classiﬁcation methods such as supervised classiﬁcation and unsupervised classiﬁcation are highly subjective and have diﬃculty distinguishing the grade of rocky desertiﬁcation, cannot directly indicate the development status of
- p.2: The mixed image element decomposition method (SMA) is a relatively common method in the study of karst desertiﬁcation, but due to the discontinuous distribution of topography in karst areas and the inﬂuence of human activities, weathering and erosion, end elem
- p.2: In recent years, the characteristic spatial model method based on surface parameters has been gradually applied to the study of karstic desertiﬁcation; this can distinguish diﬀerent grades of desertiﬁcation and directly indicate the degree of development of de
- p.2: In addition to the fruitful research results in the ﬁelds of desertiﬁcation and salinization [18,19], the characteristic spatial models constructed based on diﬀerent surface parameters have also achieved some good research results in the study of rocky deserti

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
- p.1: The accuracy of the rocky desertiﬁcation extracted by these three index models was veriﬁed and compared with the karst rocky desertiﬁcation index (KRDI) and rocky desertiﬁcation diﬀerence index (RSDDI), which are constructed based on the surface parameter feat
- p.1: The results show that: (1) The waveband reﬂectance -based feature space model provides a new method for large-scale rocky desertiﬁcation information extraction, characterized by easy data acquisition, simple index calculation and good stability, and is conduci
- p.1: (2) The overall accuracy and Kappa coeﬃcient of PRDI1 are 0.829 and 0.784, respectively, both higher than other index models, showing the best applicability, accura cy and eﬀectiveness in rocky desertiﬁcation information extraction .
- p.1: (3) According to the results extracted from PRDI1, the total area of rocky desertiﬁcation in Huaxi District of Guizhou province is 320.44 km2, with the more serious grades of rocky desertiﬁcation, such as severe and moderate, mainly distributed in the southwes
- p.2: In recent years, the characteristic spatial model method based on surface parameters has been gradually applied to the study of karstic desertiﬁcation; this can distinguish diﬀerent grades of desertiﬁcation and directly indicate the degree of development of de
- p.2: In addition to the fruitful research results in the ﬁelds of desertiﬁcation and salinization [18,19], the characteristic spatial models constructed based on diﬀerent surface parameters have also achieved some good research results in the study of rocky deserti
- p.2: The results proved that the KRDI is a sensitive indicator of rocky desertiﬁcation and can be used for the direct extraction of rocky desertiﬁcation information.
- p.2: [21] constructed the rocky desertiﬁcation diﬀerence index (RSDDI) based on NDVI and Albedo surface parameter feature space, and extracted information on the spatial distribution and extent of rocky desertiﬁcation in Dougu Township, and the results showed that 
- p.2: [12] constructed two types of feature space models (p oint-to-point and point -to-line) based on seven surface parameters to monitor the rocky desertiﬁcation in Dafang County, and the results proved that the feature space models constructed based on diﬀerent s
- p.3: It has been studied extensively in the ﬁelds of soil moisture and land drought monitoring [23–25], and has achieved good research results, but it has not been reported in the ﬁeld of karstic rocky desertiﬁcation research so far, and its applicability to the ex

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
- p.1: The accuracy of the rocky desertiﬁcation extracted by these three index models was veriﬁed and compared with the karst rocky desertiﬁcation index (KRDI) and rocky desertiﬁcation diﬀerence index (RSDDI), which are constructed based on the surface parameter feat
- p.3: However, this method also has some disadvantages, mainly the complicated process of calculating surface parameters and the inclusion of certain errors, which gradually accumulate and increase the uncertainty of the index model c alculation [22].
- p.6: The accuracy of these three index models extracted from rocky desertiﬁcation was veriﬁed and compared, and the index model with the highest accuracy was compared with the previously proposed index models KRDI and RSDDI, which are constructed based on the surfa
- p.17: Discussion 5.1.
- p.18: The images of these features participate in the construction of the model, which brings some inﬂuence on the accuracy of the model, and the model should be further optimized in future research.
- p.18: Research Limitations The study area was located in the karst mountains area of southwest China, with the most severe land degradation, uneven ground surface and complex topographic conditions, all of which increase the diﬃculty of accurately extracting informa
- p.19: 2023, 15, 3056 19 of 22 between adjacent objects, resulting in a certain number of shadow areas on the satellite images, and these shadows may also lead to uncertainty in the estimation of rocky desertiﬁcation [16]; future studies should consider the eﬀect of 
- p.19: In addition, the question of how to improve the performance of the index PRDI1 by considering the inﬂuence of factors such as shading and soil and rocky confusion on the accuracy of PRDI1 will be the focus of future work.

## 8. Conclusions Writing Pattern

- Typical structure: one compact section with objective reminder, method, key findings, and application value.
- Tone: restrained and evidence-aligned.
- Limitations/future work: sometimes included briefly; do not overclaim.
- Recommended template: “This study addressed [problem] using [data/method]. The results indicate [validated finding]. The approach supports [application], while future work should address [limitation].”

## 9. Figure and Table Style

| Figure/Table | Caption style | What it shows | Text reference pattern | Relevance to our manuscript |
|---|---|---|---|---|
| p.4 Figure 1 | descriptive caption with object/result label | study design/result/map/table evidence inferred from caption; inspect figure before reuse | main text generally refers by Figure/Table number | useful as pattern for maps, workflow, data source, accuracy, or comparison displays |
| p.5 Table 1 | descriptive caption with object/result label | study design/result/map/table evidence inferred from caption; inspect figure before reuse | main text generally refers by Figure/Table number | useful as pattern for maps, workflow, data source, accuracy, or comparison displays |
| p.5 Figure 2 | descriptive caption with object/result label | study design/result/map/table evidence inferred from caption; inspect figure before reuse | main text generally refers by Figure/Table number | useful as pattern for maps, workflow, data source, accuracy, or comparison displays |
| p.6 Figure 2 | descriptive caption with object/result label | study design/result/map/table evidence inferred from caption; inspect figure before reuse | main text generally refers by Figure/Table number | useful as pattern for maps, workflow, data source, accuracy, or comparison displays |
| p.6 Figure 3 | descriptive caption with object/result label | study design/result/map/table evidence inferred from caption; inspect figure before reuse | main text generally refers by Figure/Table number | useful as pattern for maps, workflow, data source, accuracy, or comparison displays |
| p.8 Figure 4 | descriptive caption with object/result label | study design/result/map/table evidence inferred from caption; inspect figure before reuse | main text generally refers by Figure/Table number | useful as pattern for maps, workflow, data source, accuracy, or comparison displays |
| p.9 Figure 5 | descriptive caption with object/result label | study design/result/map/table evidence inferred from caption; inspect figure before reuse | main text generally refers by Figure/Table number | useful as pattern for maps, workflow, data source, accuracy, or comparison displays |
| p.11 Figure 6 | descriptive caption with object/result label | study design/result/map/table evidence inferred from caption; inspect figure before reuse | main text generally refers by Figure/Table number | useful as pattern for maps, workflow, data source, accuracy, or comparison displays |
| p.13 Figure 7f | descriptive caption with object/result label | study design/result/map/table evidence inferred from caption; inspect figure before reuse | main text generally refers by Figure/Table number | useful as pattern for maps, workflow, data source, accuracy, or comparison displays |
| p.13 Table 2 | descriptive caption with object/result label | study design/result/map/table evidence inferred from caption; inspect figure before reuse | main text generally refers by Figure/Table number | useful as pattern for maps, workflow, data source, accuracy, or comparison displays |
| p.14 Figure 7 | descriptive caption with object/result label | study design/result/map/table evidence inferred from caption; inspect figure before reuse | main text generally refers by Figure/Table number | useful as pattern for maps, workflow, data source, accuracy, or comparison displays |
| p.15 Table 3 | descriptive caption with object/result label | study design/result/map/table evidence inferred from caption; inspect figure before reuse | main text generally refers by Figure/Table number | useful as pattern for maps, workflow, data source, accuracy, or comparison displays |
| p.16 Figure 8 | descriptive caption with object/result label | study design/result/map/table evidence inferred from caption; inspect figure before reuse | main text generally refers by Figure/Table number | useful as pattern for maps, workflow, data source, accuracy, or comparison displays |
| p.17 Figure 9 | descriptive caption with object/result label | study design/result/map/table evidence inferred from caption; inspect figure before reuse | main text generally refers by Figure/Table number | useful as pattern for maps, workflow, data source, accuracy, or comparison displays |

Figure/table style lessons:
- Captions should state what is shown, not just name the figure.
- Text should cite figures/tables when interpreting evidence.
- Accuracy tables should separate metric types and class-level indicators.
- Suggested figures for our paper: study area, workflow, architecture, FBR map, grade map, DEM ablation, cross-region transfer, error/confusion analysis.

Located text reference patterns:
- p.3: Study Area As shown in Figure 1a, this study area was located in Huaxi District, Guiyang City, Guizhou Province, between 106°27 ′~106°52′E and 26°11 ′~26°34′N, with a total area of 964.32 km2, in which karst landscapes are widely distributed, accounting for 94% of the total area 
- p.3: The topography of the region is shown in Figure 1b, with a high north and south and low middle, with the highest features in the southeast, ranging from 1014 m to 1684 m above sea level, and the central part being around 1100 m above sea level.
- p.4: Figure 1c shows the distribution of sample points in the study area.
- p.4: Figure 1.
- p.5: The mask ing process was completed in the Mask toolbox of ENVI5.3 , and the required data sources are shown in Table 1.
- p.5: Table 1.
- p.5: In this study, with the help of 1 m resolution Google Earth images, 50 pure image elements of each feature were manually and randomly selected on multispectral images of the Huaxi District to plot the mean Popper curves, as shown in Figure 2.
- p.5: As can be seen in Figure 2, the reﬂectance of the rocks increased from the red band (band4: 63 0–690 nm) and the near -infrared band (band5: 7 75–900 nm) to the short-wave infrared 1 band (band6: 155 0–1750 nm), and the reﬂectance of other features varied considerably in these th
- p.6: 2023, 15, 3056 6 of 22 Figure 2.
- p.6: The overall ﬂowchart of the study is shown in Figure 3, and some of the main components of the ﬂowchart are described in the following sections.

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

Terms located in this paper: rocky desertification, karst rocky desertification, bare rock, spectral mixture analysis, DEM, slope, Sentinel, Landsat, overall accuracy, Kappa.

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
