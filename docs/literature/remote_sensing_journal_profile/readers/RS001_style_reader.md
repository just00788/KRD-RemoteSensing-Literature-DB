# Remote Sensing Style Reader: Is Forest Restoration in the Southwest China Karst Promoted Mainly by Climate Change or Human-Induced Factors?

## 1. Bibliographic Information

- RS ID: RS001
- Title: Is Forest Restoration in the Southwest China Karst Promoted Mainly by Climate Change or Human-Induced Factors?
- Authors: unknown
- Year: 2014
- Journal: Remote Sensing
- DOI: 10.3390/rs6109895
- PDF path: `docs/literature/pdfs/remote_sensing_only/2014_RemoteSens_6_9895_Is_Forest_Restoration_in_the_Southwest_China_Karst_Promoted_.pdf`
- Language: English
- Already read in previous batches: batch_01=False; batch_02=False
- This rereading focus: journal writing style, section architecture, figure/table pattern, terminology, and reusable templates.

## 2. Article Structure

- Primary headings detected: 21
- Independent Discussion: yes
- Independent Conclusions: yes
- Data Availability / Author Contributions / Funding / Conflicts of Interest: Data Availability=not located; Author Contributions=p.13; Funding=not located; Conflicts=p.13
- Supplementary Materials: not located
- Overall suitability: useful for our manuscript if we adapt the structure without copying wording.

| Section | Subsections | Function | Relevance to our manuscript |
|---|---|---|---|
| 1 State Key Laboratory of Resources and Environmental Information Systems, Institute of | see source headings | article support section or topic-specific subsection | adapt if matching our FBR/DeepLabV3+/DEM workflow |
| 1. Introduction | see source headings | sets background, problem importance, literature gap | adapt if matching our FBR/DeepLabV3+/DEM workflow |
| 2. Materials and Methods | see source headings | establishes reproducible materials, data, workflow, and evaluation | adapt if matching our FBR/DeepLabV3+/DEM workflow |
| 2.1. Study Area | see source headings | establishes reproducible materials, data, workflow, and evaluation | adapt if matching our FBR/DeepLabV3+/DEM workflow |
| 2.2. Materials | see source headings | article support section or topic-specific subsection | adapt if matching our FBR/DeepLabV3+/DEM workflow |
| 2.2.1. Moderate-Resolution Imaging Spectroradiometer (MODIS) NDVI Time Series Data | see source headings | establishes reproducible materials, data, workflow, and evaluation | adapt if matching our FBR/DeepLabV3+/DEM workflow |
| 2.2.2. Land Use Data | see source headings | establishes reproducible materials, data, workflow, and evaluation | adapt if matching our FBR/DeepLabV3+/DEM workflow |
| 2.2.3. Climate Data | see source headings | establishes reproducible materials, data, workflow, and evaluation | adapt if matching our FBR/DeepLabV3+/DEM workflow |
| 2.2.4. Out-Migrant Population (OMP) | see source headings | article support section or topic-specific subsection | adapt if matching our FBR/DeepLabV3+/DEM workflow |
| 2.3. Methods | see source headings | establishes reproducible materials, data, workflow, and evaluation | adapt if matching our FBR/DeepLabV3+/DEM workflow |
| 2.3.1. NDVI Trend Analysis | see source headings | article support section or topic-specific subsection | adapt if matching our FBR/DeepLabV3+/DEM workflow |
| 2.3.2. Regression Analyses of NDVI and Climate Change | see source headings | article support section or topic-specific subsection | adapt if matching our FBR/DeepLabV3+/DEM workflow |
| 2.3.3. Relationship between Out-Migration and Changes in the Forest NDVI | see source headings | article support section or topic-specific subsection | adapt if matching our FBR/DeepLabV3+/DEM workflow |
| 3. Results and Discussion | see source headings | reports maps, comparisons, and metrics | adapt if matching our FBR/DeepLabV3+/DEM workflow |
| 3.1. Trends in annNDVI and sumNDVI | see source headings | article support section or topic-specific subsection | adapt if matching our FBR/DeepLabV3+/DEM workflow |
| 3.2. Trends in Temperature and Precipitation over the Year and during Summer | see source headings | article support section or topic-specific subsection | adapt if matching our FBR/DeepLabV3+/DEM workflow |
| 3.3. The Relationship between NDVI and Climate Change | see source headings | article support section or topic-specific subsection | adapt if matching our FBR/DeepLabV3+/DEM workflow |
| 3.4. The Effects of Afforestation and Out-Migration on Changes in the Forest NDVI | see source headings | article support section or topic-specific subsection | adapt if matching our FBR/DeepLabV3+/DEM workflow |
| 3.4.1. Changes in the Forest NDVI in relation to Ecological Afforestation | see source headings | article support section or topic-specific subsection | adapt if matching our FBR/DeepLabV3+/DEM workflow |
| 3.4.2. The Relationship between OMP and Changes in the Forest NDVI | see source headings | article support section or topic-specific subsection | adapt if matching our FBR/DeepLabV3+/DEM workflow |
| 4. Conclusions | see source headings | summarizes contribution and application value | adapt if matching our FBR/DeepLabV3+/DEM workflow |

## 3. Abstract Writing Pattern

- Background opening: usually starts from environmental importance or monitoring challenge.
- Problem/gap: located through abstract text.
- Data and method compression: Remote Sensing abstracts tend to compress sensor, study area, model, and validation into one or two sentences.
- Result presentation: reports principal results and often includes metrics when central to the paper.
- Specific accuracy numbers: not detected in abstract sample.
- Significance ending: commonly links the method to monitoring, restoration, or decision support.
- Approximate abstract length: 248 words; 14 sentence-like units.
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

Located Introduction anchors: p.2, p.16

## 5. Materials and Methods Writing Pattern

- Study area: usually separated or early in Methods; anchor p.1, p.3.
- Data sources: anchor p.1, p.2, p.4, p.5, p.6, p.12, p.13, p.14, p.15; often supported by a data table.
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
- p.1: Based on Mode rate-Resolution Imaging Spectroradiometer (MODIS) Normalized Di fference Vegetation Index (NDVI) data, we found general greening trends of the forest from 2000 to 2010.
- p.2: Based on a time series of NDVI observations and on model predictions, many studies have reported general greeni ng trends (increasing trends in ve getation indices) in the northern mid–high latitudes [8,9], which have mainly been at tributed to the warming cli
- p.3: Materials and Methods 2.1.
- p.4: (a) The location of the Southwest China Karst and ( b) the spatial distribution of forest in Guizhou Province according to land use data derived from Landsat TM/ETM+ and HJ-1 images in 2010.
- p.4: Moderate-Resolution Imaging Spectroradiometer (MODIS) NDVI Time Series Data To investigate the inter-annual an d seasonal trends of the forest , the MODIS monthly vegetation indices (VI) product (Collection 5, MOD13A3 at a spatial resoluti on of 1 km) from 200
- p.4: In this study, monthly NDVI data were used to derive the summer and annual NDVI.
- p.4: Land Use Data Land use and its change data from 2000 to 2010 we re collected from the National Resources and Environmental Scientific Data Center (RESDC) of the Chinese Academy of Sciences (CAS).
- p.4: These data were manually interpreted from Landsat TM/ETM+ and HJ-1 CCD images and then corrected and validated through fieldwork [28].
- p.4: There were six classes in the land use data: cropland, forest, grassland, water bodies, built-up land, and unused land [29].
- p.5: 2014, 6 9899 use data used in this study were raster data pr oduced by a 1 × 1 km area proportion model [30].

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
- p.2: 2014, 6 9896 changes showed that a warming climate coupled with a decrease in pr ecipitation explained some of the changes in the forest NDVI, but the results were not conclusive.
- p.3: The results will provide useful information for ecological protection and redevelopm ent in this region.
- p.6: Results and Discussion 3.1.
- p.9: The red dot s with black circles indicate that the results are statistically significant ( p < 0.1).
- p.13: In addition, according to our results, forest restoration can be pr imarily attributed to human factors.
- p.13: All the authors were involved in data analysis, as well as the discussion of the results.

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
- p.6: To reduce the influence of the misregistration of a climate station and MODIS NDVI pixels, NDVI values averaged for pixels within a window (2 × 2 km) surrounding the climate station were compared with c limate data.
- p.6: Results and Discussion 3.1.
- p.6: Compared with the NDVI trends from 1982 to 2003 [38,39], the forest greening trends during 2000–2010 observed in this study has spread westward and northward, and browning (decreasing) trends were only found in small patches in the south and east regions.
- p.10: Compared with these relationships, the positive relationship between the NDVI trends and changes in OMP was not as strong (Figure 7b).
- p.12: Another uncertainty related with data is from OMP data.
- p.13: All the authors were involved in data analysis, as well as the discussion of the results.
- p.15: Impact s of present and future climate variability on agriculture and forestry in the humid and sub-humid tropics.

## 8. Conclusions Writing Pattern

- Typical structure: one compact section with objective reminder, method, key findings, and application value.
- Tone: restrained and evidence-aligned.
- Limitations/future work: sometimes included briefly; do not overclaim.
- Recommended template: “This study addressed [problem] using [data/method]. The results indicate [validated finding]. The approach supports [application], while future work should address [limitation].”

## 9. Figure and Table Style

| Figure/Table | Caption style | What it shows | Text reference pattern | Relevance to our manuscript |
|---|---|---|---|---|
| p.4 Figure 1 | descriptive caption with object/result label | study design/result/map/table evidence inferred from caption; inspect figure before reuse | main text generally refers by Figure/Table number | useful as pattern for maps, workflow, data source, accuracy, or comparison displays |
| p.6 Figure 2 | descriptive caption with object/result label | study design/result/map/table evidence inferred from caption; inspect figure before reuse | main text generally refers by Figure/Table number | useful as pattern for maps, workflow, data source, accuracy, or comparison displays |
| p.7 Figure 2 | descriptive caption with object/result label | study design/result/map/table evidence inferred from caption; inspect figure before reuse | main text generally refers by Figure/Table number | useful as pattern for maps, workflow, data source, accuracy, or comparison displays |
| p.8 Figure 3 | descriptive caption with object/result label | study design/result/map/table evidence inferred from caption; inspect figure before reuse | main text generally refers by Figure/Table number | useful as pattern for maps, workflow, data source, accuracy, or comparison displays |
| p.8 Figure 4 | descriptive caption with object/result label | study design/result/map/table evidence inferred from caption; inspect figure before reuse | main text generally refers by Figure/Table number | useful as pattern for maps, workflow, data source, accuracy, or comparison displays |
| p.9 Figure 4 | descriptive caption with object/result label | study design/result/map/table evidence inferred from caption; inspect figure before reuse | main text generally refers by Figure/Table number | useful as pattern for maps, workflow, data source, accuracy, or comparison displays |
| p.10 Figure 5 | descriptive caption with object/result label | study design/result/map/table evidence inferred from caption; inspect figure before reuse | main text generally refers by Figure/Table number | useful as pattern for maps, workflow, data source, accuracy, or comparison displays |
| p.11 Figure 6 | descriptive caption with object/result label | study design/result/map/table evidence inferred from caption; inspect figure before reuse | main text generally refers by Figure/Table number | useful as pattern for maps, workflow, data source, accuracy, or comparison displays |
| p.11 Figure 7 | descriptive caption with object/result label | study design/result/map/table evidence inferred from caption; inspect figure before reuse | main text generally refers by Figure/Table number | useful as pattern for maps, workflow, data source, accuracy, or comparison displays |
| p.12 Figure 8 | descriptive caption with object/result label | study design/result/map/table evidence inferred from caption; inspect figure before reuse | main text generally refers by Figure/Table number | useful as pattern for maps, workflow, data source, accuracy, or comparison displays |

Figure/table style lessons:
- Captions should state what is shown, not just name the figure.
- Text should cite figures/tables when interpreting evidence.
- Accuracy tables should separate metric types and class-level indicators.
- Suggested figures for our paper: study area, workflow, architecture, FBR map, grade map, DEM ablation, cross-region transfer, error/confusion analysis.

Located text reference patterns:
- p.3: Study Area The Southwest China Karst area mainly extends through Guizhou, Guangxi, and Yunnan Provinces (Figure 1), and among which Guizhou province has the largest area of karst as well as the most serious rock desertification [25].
- p.3: Except for the southeastern area, Chishui in the western area, and Shanheng and Wangmo in the southern areas, ka rst covers most of the region (Figure 1).
- p.4: 2014, 6 9898 Figure 1.
- p.6: Trends in annNDVI and sumNDVI Figure 2 shows the spatial distribut ion of the temporal trends in forest using the annNDVI and sumNDVI as parameters.
- p.7: Figure 2.
- p.7: Trends in Temperature and Precipitation over the Year and during Summer The regression of the annual average temperature against year from 2000 to 2010 (Figure 3a) shows warming trends at all climate stations, with the trend slopes increasing from 0.003 °C/yr to 0.061 °C/yr.
- p.7: Similarly, summer temperatures in most stations (17 of 19) increased at a warming rate higher than the annual average and slopes of 0.021 °C/yr to 0.083 °C /yr (Figure 3b).
- p.7: During this period, annual and summer pr ecipitation in most of the region decreased (Figure 3c,d).
- p.8: 2014, 6 9902 Figure 3.
- p.8: The Relationship between NDVI and Climate Change Figure 4 shows the spatial distribution of R2 values from the regression equations, with temperature and precipitation as independent va riables and the NDVI as the dependent variable.

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

Terms located in this paper: rocky desertification, karst rocky desertification, DEM, slope, Landsat.

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
