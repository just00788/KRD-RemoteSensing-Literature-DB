# Experiment Design

## When to use this reference

Use this reference when designing or auditing KRD experiments, model comparisons, ablation studies, validation splits, or result sections.

## Minimum Experiment Blocks

1. Study areas and transfer setting.
2. Remote-sensing data sources.
3. Reference samples and label system.
4. FBR inversion workflow.
5. Classification or segmentation workflow.
6. DEM/topographic feature integration.
7. Ablation experiments.
8. Accuracy assessment and uncertainty analysis.

## Data Inputs

Document the sensor, spatial resolution, date/season, preprocessing, cloud masking, atmospheric correction, and band/index construction for each source.

Typical sources include:

- Sentinel-2.
- Landsat 8/9.
- Gaofen imagery.
- UAV or field reference data.
- Open-source DEM.
- GF-7 stereo-derived DEM for local Study Area 2 enhancement only.

## Validation Design

Prefer spatial block split or region-independent validation. Avoid random patch split when spatial autocorrelation can inflate accuracy.

For transfer validation:

- Train or tune on Area 1.
- Test on Area 2.
- Use open-source DEM if DEM features are needed in both areas.
- Keep GF-7 stereo DEM as a local enhancement experiment for Area 2.

## Ablation Design

Recommended ablations:

- Spectral-only vs spectral + index.
- Without DEM vs with open-source DEM.
- DeepLabV3+ vs FCN vs U-Net.
- Area-specific training vs cross-region transfer.
- Open-source DEM vs local GF-7 enhancement in Study Area 2, if true data exist.

## Metrics

Continuous FBR:

- R2.
- RMSE.
- MAE.
- bias.
- regression slope.

Classification or segmentation:

- OA.
- Kappa.
- Precision.
- Recall.
- F1.
- IoU.
- mF1.
- mIoU.

