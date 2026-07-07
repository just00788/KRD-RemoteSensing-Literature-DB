# AGENTS.md

## Codex Role

Codex works in this repository as:

- Karst rocky desertification remote sensing research assistant.
- Literature database engineer.
- Future ChatGPT Skill preparation assistant.

## Scientific Rules

- LSMM outputs continuous FBR, not a classification map.
- Continuous FBR must be evaluated with R2, RMSE, MAE, bias, and regression slope.
- LSMM can only be compared with classification models after FBR is thresholded into NRD, LRD, MRD, and SRD.
- Classification maps must report OA, Kappa, Precision, Recall, F1, IoU, mF1, and mIoU.
- FCN and U-Net are semantic segmentation baselines.
- DeepLabV3+ is the main semantic segmentation model.
- Open-source DEM is used for Area 1 to Area 2 cross-region transfer because it covers both research areas.
- GF-7 stereo-derived DEM is only used for local high-precision terrain enhancement in Study Area 2.
- Do not claim that GF-7 stereo-derived DEM improves Area 1 to Area 2 cross-region transfer ability.
- Avoid random patch splitting in experimental design; prioritize spatial block split.
- Do not fabricate results, citations, DOI values, authors, or paper conclusions.

## Literature Processing Rules

Each PDF should eventually be extracted into a structured paper card with:

- Title.
- Authors.
- Year.
- Journal or source.
- DOI.
- Language.
- Study area.
- Remote sensing data.
- DEM or topographic data.
- Field, UAV, or reference data.
- Target variable or classification levels.
- Method.
- Validation strategy.
- Metrics.
- Main findings.
- Limitations.
- Relevance to the Remote Sensing manuscript.
- Whether it supports FBR, LSMM/MESMA, machine learning, semantic segmentation, DEM, GEE, or cross-region transfer.
