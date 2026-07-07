# Semantic Segmentation Guidelines

## When to use this reference

Use this reference when designing or reviewing DeepLabV3+, FCN, U-Net, segmentation baselines, patch design, class metrics, or bare-rock extraction from images.

## Model Roles

- DeepLabV3+: main semantic segmentation model in the planned manuscript.
- FCN: baseline.
- U-Net: baseline.

Do not retroactively claim that literature papers used DeepLabV3+ unless the paper explicitly did so.

## Experimental Requirements

State:

- Input imagery and bands.
- Patch size and overlap.
- Label classes.
- Training/validation/test split.
- Spatial block split or region-independent split.
- Loss function.
- Baselines.
- Hyperparameters if available.

## Metrics

Report class-level and map-level metrics:

- OA.
- Kappa.
- Precision.
- Recall.
- F1.
- IoU.
- mF1.
- mIoU.

## Results Organization

Separate:

- Bare-rock segmentation output.
- KRD grade classification output.
- FBR continuous inversion output.
- Error maps and confusion matrices.

## Cautions

- Avoid random patch splits that leak spatial texture.
- Do not compare segmentation IoU directly with continuous FBR RMSE.
- Use visual examples only as support; metrics and independent validation carry the claim.

