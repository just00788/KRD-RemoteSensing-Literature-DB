# Remote Sensing Journal Style Synthesis

## 1. Papers Re-Read for Style

- RS001: Is Forest Restoration in the Southwest China Karst Promoted Mainly by Climate Change or Human-Induced Factors? (2014); DOI: 10.3390/rs6109895; captions located: 10
- RS002: Quantitative Estimation of Carbonate Rock Fraction in Karst Regions Based on Spectral Feature Analysis (2016); DOI: 10.3390/rs8010068; captions located: 15
- RS003: Analysis of Landsat-8 OLI Imagery for Estimating Exposed Bedrock Fractions in Typical Karst Regions of Southwest China (2018); DOI: 10.3390/rs10091321; captions located: 19
- RS004: How Can We Realize Sustainable Development Goals in Rocky Desertified Regions by Enhancing Crop Yield and Restoring Ecological Function? (2021); DOI: 10.3390/rs13091614; captions located: 9
- RS005: Extracting Information on Rocky Desertification from Satellite Images: A Comparative Study (2021); DOI: 10.3390/rs13132497; captions located: 20
- RS006: Optimization of Rocky Desertification Classification Model Based on Vegetation Type and Seasonal Characteristic (2021); DOI: 10.3390/rs13152935; captions located: 35
- RS007: The Changes of Spatiotemporal Pattern of Rocky Desertification and Its Dominant Driving Factors in Typical Karst Mountainous Areas under the Background of Global Change (2022); DOI: 10.3390/rs14102351; captions located: 24
- RS008: Spatiotemporal Evolution Analysis and Future Scenario Prediction of Rocky Desertification in a Subtropical Karst Region (2022); DOI: 10.3390/rs14020292; captions located: 35
- RS009: Extraction of Rocky Desertification Information in the Karst Area Based on the Red-NIR-SWIR Spectral Feature Space (2023); DOI: 10.3390/rs15123056; captions located: 14
- RS010: Classification of Karst Rocky Desertification Levels in Jinsha County Using a Feature Space Method Based on SDGSAT-1 Multispectral Data (2024); DOI: 10.3390/rs16244786; captions located: 20
- RS011: Spatiotemporal Evolution and Driving Factors of Karst Rocky Desertification in Guangxi, China, Under Climate Change and Human Activities (2025); DOI: 10.3390/rs17132294; captions located: 25

## 2. Common Article Structure

Remote Sensing papers commonly use a conventional IMRaD-like structure: Abstract, Introduction, Materials and Methods, Results, Discussion, Conclusions, plus back-matter sections such as Data Availability, Author Contributions, Funding, Conflicts of Interest, and sometimes Supplementary Materials. For our KRD manuscript, this structure is suitable, but Methods and Results should be subdivided more explicitly around FBR inversion, semantic segmentation, DEM ablation, transfer validation, and error analysis.

## 3. Abstract Style

The dominant abstract sequence is background -> problem/gap -> data -> method -> key result -> significance. Accuracy values appear when central to the claim, but they should remain metric-specific. Our abstract should not mix continuous FBR metrics with classification metrics.

## 4. Introduction Style

Introductions generally move from ecological/land-degradation importance to remote-sensing monitoring, then review method families and identify a precise limitation. Our manuscript should use a six-paragraph structure: KRD context, FBR/remote sensing, spectral unmixing and ML, deep learning and terrain constraints, research gap, objectives/contributions.

## 5. Materials and Methods Style

Methods sections are most effective when they begin with study area and data, then move into preprocessing, model/workflow, experiment design, and metrics. Our paper should include a workflow figure and a data-source table. Spatial split, cross-region transfer, and ablation design should be stated explicitly.

## 6. Results Style

Results should be organized around evidence objects: maps, metrics, comparison tables, ablation tables, and confusion/error analysis. Continuous FBR inversion results should be separated from thresholded KRD-grade classification and semantic-segmentation results.

## 7. Discussion Style

Discussion should interpret why results occur, not repeat Results. It should connect model behavior to spectral/terrain mechanisms, compare with prior studies, identify limitations, and propose future validation. Claims about DEM must distinguish open-source DEM for transfer from GF-7 stereo DEM for local enhancement.

## 8. Conclusions Style

Conclusions are concise, restrained, and application-oriented. They usually restate objective, summarize method and validated findings, and close with application value or future work.

## 9. Figure and Table Style

Common figures/tables include study area maps, workflow diagrams, data-source tables, classification or fraction maps, accuracy tables, confusion matrices, ablation tables, and spatial/error maps. Captions should be descriptive enough to explain what is shown.

## 10. Terminology and Noun Phrase Standards

Use consistent terms: karst rocky desertification, bare-rock fraction, exposed bedrock fraction, spectral mixture analysis, semantic segmentation, DEM-derived topographic factors, class-level accuracy, and cross-region transferability. Avoid literal or inconsistent translations such as “rock desert class” for KRD levels.

## 11. Academic Phrase Bank for Our Manuscript

Use template-style language rather than copying source sentences: “To address this gap...”, “The overall workflow is shown in Figure X”, “Accuracy was evaluated using...”, “Compared with the baseline...”, “This improvement may be attributed to...”, and “Future work should...”.

## 12. Recommended Remote Sensing Manuscript Structure for Our Paper

1. Introduction
   - KRD background and monitoring challenge
   - FBR and remote-sensing relevance
   - Existing LSMM/ML/DL/DEM studies
   - Research gap and contributions
2. Materials and Methods
   - Study areas
   - Remote-sensing and DEM data
   - Reference samples and classification system
   - LSMM/FBR inversion
   - FCN, U-Net, and DeepLabV3+
   - DEM fusion and ablation
   - Transfer validation and metrics
3. Results
   - FBR inversion
   - Thresholded KRD grade mapping
   - Model comparison
   - DEM ablation
   - Cross-region transfer
   - GF-7 local enhancement
   - Error and class-level analysis
4. Discussion
   - Model advantages
   - Physical meaning of FBR
   - DEM/topographic factors
   - Transferability and local enhancement
   - Comparison, limitations, future work
5. Conclusions

## 13. Recommended Length and Layout

- Abstract: 180-250 words.
- Introduction: 5-6 paragraphs.
- Methods: 6-8 subsections.
- Results: 6-8 subsections.
- Discussion: 5-6 subsections.
- Figures: 8-10 main figures.
- Tables: 4-6 main tables.
- Supplementary Materials: model settings, extra ablation tables, sample details, and extended maps.

## 14. Submission-Oriented Checklist

- Metrics are matched to target type.
- Continuous FBR is not described as a class map.
- Thresholded FBR classes are clearly defined before comparison.
- Class-level metrics are reported for classification/segmentation.
- Spatial split and transfer validation are explicit.
- Open-source DEM and GF-7 stereo DEM claims are separated.
- Figures and tables are cited in text and captions are descriptive.
- Data availability, author contributions, funding, conflicts, and supplementary materials are prepared.
