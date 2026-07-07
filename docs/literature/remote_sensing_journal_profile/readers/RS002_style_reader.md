# Remote Sensing Style Reader: Quantitative Estimation of Carbonate Rock Fraction in Karst Regions Based on Spectral Feature Analysis

## 1. Bibliographic Information

- RS ID: RS002
- Title: Quantitative Estimation of Carbonate Rock Fraction in Karst Regions Based on Spectral Feature Analysis
- Authors: unknown
- Year: 2016
- Journal: Remote Sensing
- DOI: 10.3390/rs8010068
- PDF path: `docs/literature/pdfs/remote_sensing_only/2016_RemoteSens_8_68_Quantitative_Estimation_of_Carbonate_Rock_Fraction_in_Karst_.pdf`
- Language: English
- Already read in previous batches: batch_01=False; batch_02=False
- This rereading focus: journal writing style, section architecture, figure/table pattern, terminology, and reusable templates.

## 2. Article Structure

- Primary headings detected: 17
- Independent Discussion: yes
- Independent Conclusions: yes
- Data Availability / Author Contributions / Funding / Conflicts of Interest: Data Availability=not located; Author Contributions=p.15; Funding=not located; Conflicts=not located
- Supplementary Materials: not located
- Overall suitability: useful for our manuscript if we adapt the structure without copying wording.

| Section | Subsections | Function | Relevance to our manuscript |
|---|---|---|---|
| 1. Introduction | see source headings | sets background, problem importance, literature gap | adapt if matching our FBR/DeepLabV3+/DEM workflow |
| 2. Materials and Methods | see source headings | establishes reproducible materials, data, workflow, and evaluation | adapt if matching our FBR/DeepLabV3+/DEM workflow |
| 2.2. Spectral Measurements of the Surface Constituents | see source headings | article support section or topic-specific subsection | adapt if matching our FBR/DeepLabV3+/DEM workflow |
| 2.3. Spectral Processing | see source headings | article support section or topic-specific subsection | adapt if matching our FBR/DeepLabV3+/DEM workflow |
| 2.4. Synthetic Mixed Spectra | see source headings | article support section or topic-specific subsection | adapt if matching our FBR/DeepLabV3+/DEM workflow |
| 2.5. Spectral Analysis | see source headings | article support section or topic-specific subsection | adapt if matching our FBR/DeepLabV3+/DEM workflow |
| 2.5.1. Spectral Feature Analysis | see source headings | article support section or topic-specific subsection | adapt if matching our FBR/DeepLabV3+/DEM workflow |
| 2.5.2. Spectral Indices | see source headings | article support section or topic-specific subsection | adapt if matching our FBR/DeepLabV3+/DEM workflow |
| 2.6. Linear Regression with Carbonate Rock Fraction | see source headings | article support section or topic-specific subsection | adapt if matching our FBR/DeepLabV3+/DEM workflow |
| 3. Experimental Results | see source headings | reports maps, comparisons, and metrics | adapt if matching our FBR/DeepLabV3+/DEM workflow |
| 3.2. Continuum-Removed Spectra | see source headings | article support section or topic-specific subsection | adapt if matching our FBR/DeepLabV3+/DEM workflow |
| 3.3. Synthetic Mixed Spectra | see source headings | article support section or topic-specific subsection | adapt if matching our FBR/DeepLabV3+/DEM workflow |
| 4. Discussion | see source headings | interprets mechanisms, compares literature, states limitations | adapt if matching our FBR/DeepLabV3+/DEM workflow |
| 4.1. The Absorption Feature in the Four Major Surface Constituents Spectra | see source headings | article support section or topic-specific subsection | adapt if matching our FBR/DeepLabV3+/DEM workflow |
| 4.3. Potential of Estimating Carbonate Rock Fraction Using Remote Sensing Imagery | see source headings | article support section or topic-specific subsection | adapt if matching our FBR/DeepLabV3+/DEM workflow |
| 5. Conclusions | see source headings | summarizes contribution and application value | adapt if matching our FBR/DeepLabV3+/DEM workflow |
| References | see source headings | article support section or topic-specific subsection | adapt if matching our FBR/DeepLabV3+/DEM workflow |

## 3. Abstract Writing Pattern

- Background opening: usually starts from environmental importance or monitoring challenge.
- Problem/gap: located through abstract text.
- Data and method compression: Remote Sensing abstracts tend to compress sensor, study area, model, and validation into one or two sentences.
- Result presentation: reports principal results and often includes metrics when central to the paper.
- Specific accuracy numbers: not detected in abstract sample.
- Significance ending: commonly links the method to monitoring, restoration, or decision support.
- Approximate abstract length: 208 words; 13 sentence-like units.
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

Located Introduction anchors: p.1, p.15

## 5. Materials and Methods Writing Pattern

- Study area: usually separated or early in Methods; anchor not located.
- Data sources: anchor p.1, p.2, p.3, p.5, p.6, p.11, p.12, p.13, p.14, p.15, ...; often supported by a data table.
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
- p.1: While there may be some debate about the accuracy of these numbers, there is little disagreement on the overall importance of karst environments [ 1].
- p.2: Many methods have been developed to estimate and map carbonate rocks.
- p.2: Recently, an increasing number of digital methods have been developed, such as per-pixel classiﬁcation [8,9] and subpixel quantitative estimation.
- p.2: Linear spectral mixture analysis (LSMA) method has been recently employed to estimate the sub-pixel cover fractions of karst land-surface types [10,11].
- p.2: employed a linear spectral unmixing method to retrieve the abundances of vegetation and exposed rock from Hyperion image [11].
- p.2: Compared with the SMA method, spectral indices have the advantage of easy implementation and convenience in practical applications without endmember selection.
- p.2: Therefore, exposed carbonate rock fraction is usually estimated based on: (1) complement of vegetation and bare soil fraction; or (2) regression models with vegetation and bare soil indices [14,15].
- p.2: Additional fundamental information about the impact of different biophysical constituents on mixed spectra is needed to assess the contribution of exposed carbonate rocks; Which spectral bands or features are more sensitive to carbonate rock fraction in mixed 
- p.3: Then, several synthetic mixed spectra data sets are generated based on a linear spectral mixture assumption.
- p.3: Materials and Methods 2.1.

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
- p.1: While there may be some debate about the accuracy of these numbers, there is little disagreement on the overall importance of karst environments [ 1].
- p.9: At last, three parameters, including the Pearson product-moment correlation coefﬁcient ( r), the root-mean square error (RMSE) and the Chi-Square ( χ2) between actual and predicted values, were used to evaluate the regression results.
- p.9: Experimental Results 3.1.
- p.11: Relativity between the Surface CarbonateRock Fractions and 2.340 µm Absorption Features Linear regression results for the carbonate rock fractions related to the 2.340 µm absorption features, including centers, depths, areas, asymmetry, KRDSIs and HCRIs, are d
- p.11: The table shows expected results.
- p.11: For the data set2, with ﬁxed parameters λa = 2.2 µm, λb = 2.35 µm and λc = 2.38 µm, KRDSI3 has higher r (0.9853) and lower RMSE (0.0492)
- p.12: Comparatively, the HCRIs with adjusted parameters λ1 = 2.270 µm, λ2 = 2.398 µm and the adaptive λ0 have higher r and lower RMSE and Chi-Square value than the KRDSIs, the highest Pearson correlation coefﬁcient and lowest RMSE and Chi-Square values are obtained 
- p.12: In the experiment for data set 3, KRDSI4 has the higher r and lower RMSE than other KRDSIs with ﬁxed absorption parameters.
- p.12: The highest r and lowest RMSE and Chi-Square values are obtained for the feature HCRI 2 (r = 0.7976, RMSE = 0.1740 and χ2 = 54.4868).
- p.12: Meanwhile, SFA feature centers and asymmetry have the highest RMSE and Chi-Square and lowest r both for data set2 and data set3.

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
- p.2: Even though remote sensing provides an important way for understanding karst environments, the mapping of exposed carbonate rocks is still a challenging task because of the highly heterogeneous landscapes in the desertiﬁcation areas and the limitation in the s
- p.2: Compared with the SMA method, spectral indices have the advantage of easy implementation and convenience in practical applications without endmember selection.
- p.2: Although many scholars have had in-depth discussions of visible and near-infrared spectra of carbonate mineral and rock [22–27], improved knowledge is desired to assess the application of spectroscopy to characterizing and quantifying exposed carbonate rocks.
- p.12: Discussion 4.1.
- p.13: This may be due to the limitations of spectral resolution as compared to the ﬁeld spectra.
- p.13: represented carbonate rocks absorption features in 2.200–2.380 µm compared with the soils and NPV absorption features, they deﬁned KRDSIs with the ﬁxed parameters: λa = 2.200 µm, λb = 2.380 µm and λc = 2.350 µm in [20], in order to predict carbonate rock fract
- p.13: Future studies should focus on this issue.
- p.15: Xie wrote the paper with assistance from Du, Zhan and Tian.Alim Samat and Jike Chen helped with discussion and revisions .

## 8. Conclusions Writing Pattern

- Typical structure: one compact section with objective reminder, method, key findings, and application value.
- Tone: restrained and evidence-aligned.
- Limitations/future work: sometimes included briefly; do not overclaim.
- Recommended template: “This study addressed [problem] using [data/method]. The results indicate [validated finding]. The approach supports [application], while future work should address [limitation].”

## 9. Figure and Table Style

| Figure/Table | Caption style | What it shows | Text reference pattern | Relevance to our manuscript |
|---|---|---|---|---|
| p.4 Figure 1 | descriptive caption with object/result label | study design/result/map/table evidence inferred from caption; inspect figure before reuse | main text generally refers by Figure/Table number | useful as pattern for maps, workflow, data source, accuracy, or comparison displays |
| p.4 Figure 2 | descriptive caption with object/result label | study design/result/map/table evidence inferred from caption; inspect figure before reuse | main text generally refers by Figure/Table number | useful as pattern for maps, workflow, data source, accuracy, or comparison displays |
| p.5 Figure 2 | descriptive caption with object/result label | study design/result/map/table evidence inferred from caption; inspect figure before reuse | main text generally refers by Figure/Table number | useful as pattern for maps, workflow, data source, accuracy, or comparison displays |
| p.6 Table 1 | descriptive caption with object/result label | study design/result/map/table evidence inferred from caption; inspect figure before reuse | main text generally refers by Figure/Table number | useful as pattern for maps, workflow, data source, accuracy, or comparison displays |
| p.7 Figure 3 | descriptive caption with object/result label | study design/result/map/table evidence inferred from caption; inspect figure before reuse | main text generally refers by Figure/Table number | useful as pattern for maps, workflow, data source, accuracy, or comparison displays |
| p.8 Figure 4 | descriptive caption with object/result label | study design/result/map/table evidence inferred from caption; inspect figure before reuse | main text generally refers by Figure/Table number | useful as pattern for maps, workflow, data source, accuracy, or comparison displays |
| p.8 Table 2 | descriptive caption with object/result label | study design/result/map/table evidence inferred from caption; inspect figure before reuse | main text generally refers by Figure/Table number | useful as pattern for maps, workflow, data source, accuracy, or comparison displays |
| p.9 Table 3 | descriptive caption with object/result label | study design/result/map/table evidence inferred from caption; inspect figure before reuse | main text generally refers by Figure/Table number | useful as pattern for maps, workflow, data source, accuracy, or comparison displays |
| p.10 Figure 5 | descriptive caption with object/result label | study design/result/map/table evidence inferred from caption; inspect figure before reuse | main text generally refers by Figure/Table number | useful as pattern for maps, workflow, data source, accuracy, or comparison displays |
| p.11 Figure 6 | descriptive caption with object/result label | study design/result/map/table evidence inferred from caption; inspect figure before reuse | main text generally refers by Figure/Table number | useful as pattern for maps, workflow, data source, accuracy, or comparison displays |
| p.11 Figure 6b | descriptive caption with object/result label | study design/result/map/table evidence inferred from caption; inspect figure before reuse | main text generally refers by Figure/Table number | useful as pattern for maps, workflow, data source, accuracy, or comparison displays |
| p.12 Table 4 | descriptive caption with object/result label | study design/result/map/table evidence inferred from caption; inspect figure before reuse | main text generally refers by Figure/Table number | useful as pattern for maps, workflow, data source, accuracy, or comparison displays |
| p.12 Figure 6c | descriptive caption with object/result label | study design/result/map/table evidence inferred from caption; inspect figure before reuse | main text generally refers by Figure/Table number | useful as pattern for maps, workflow, data source, accuracy, or comparison displays |
| p.13 Figure 6a | descriptive caption with object/result label | study design/result/map/table evidence inferred from caption; inspect figure before reuse | main text generally refers by Figure/Table number | useful as pattern for maps, workflow, data source, accuracy, or comparison displays |
| p.14 Figure 7 | descriptive caption with object/result label | study design/result/map/table evidence inferred from caption; inspect figure before reuse | main text generally refers by Figure/Table number | useful as pattern for maps, workflow, data source, accuracy, or comparison displays |

Figure/table style lessons:
- Captions should state what is shown, not just name the figure.
- Text should cite figures/tables when interpreting evidence.
- Accuracy tables should separate metric types and class-level indicators.
- Suggested figures for our paper: study area, workflow, architecture, FBR map, grade map, DEM ablation, cross-region transfer, error/confusion analysis.

Located text reference patterns:
- p.3: Figure 1 show examples of ﬁeld reﬂectance spectra measured from different surface constituents in the karst desertiﬁcation area in northeastern Jianshui County.
- p.4: 2016, 8, 68 4 of 18 Figure 1.
- p.4: In addition, the absolute reﬂectance ( R) as a function of wavelength (λ) was obtained by multiplying the reﬂectance measurement made relative to Spectralon (Rre f) by the reﬂectance of Spectralon: R(λ) = Rre f× RSpectralon (λ) (1) Figure 2 illustrates the preprocessing for ﬁeld 
- p.5: 2016, 8, 68 5 of 18 Reflectance 0.5 0.4 0.3 0.2 Wavelength(Micrometers) 2.52.01.51.00.5 Absolute reflectance spectrum with offsets corrected Uncorrected reflectance spectrum Figure 2.
- p.5: Three synthetic data sets were generated to analyze different features of surface cover mixed spectra along with varied carbonate rock fractions (see Table 1).
- p.6: Table 1.
- p.6: The continuum removal (as displayed in Figure 3) can be performed as follows [32]: RC(λ) = R(λ)/RL(λ), (2) where RC is the continuum removed spectrum, R is the original observed spectrum, and RL is the corresponding values of the continuum line for all the channels in the wavelen
- p.6: Figure 3 illustrates the spectra after continuum removal where the absorption feature is enhanced.
- p.7: 2016, 8, 68 7 of 18 2.0 2.1 2.2 2.3 2.4 2.5 Wavelength(Micrometers) 0.2 0.4 0.6 0.8 1.0Absolute (normalized) reflectance Continuum removal spectrum Carbonate rock spectrum Area(left) Area(right) Depth Continuum Center Figure 3.
- p.7: In particular, there is a overlapping absorption near 2.208 µm caused by soils (see Table 2 and Figure 4), while the other three constituents have similar sightly absorption in the reﬂectance spectra in the 2.270–2.398 µm region, with the exception of carbonate rocks.

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

Terms located in this paper: bare rock, exposed bedrock fraction, fractional vegetation cover, spectral mixture analysis, DEM, Landsat.

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
