# Remote Sensing Journal Writing Rules

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
