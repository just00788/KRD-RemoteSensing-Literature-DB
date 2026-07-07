# Research Framework

## When to use this reference

Use this reference when the user asks for the overall scientific framework, manuscript logic, contribution design, or how FBR, LSMM, semantic segmentation, DEM, and cross-region validation fit together.

## Core Framework

The manuscript should separate four linked layers:

1. Continuous FBR inversion.
2. Thresholded rocky desertification grade mapping.
3. Semantic segmentation and classification model comparison.
4. DEM/topographic enhancement and cross-region transfer validation.

## Recommended Contribution Logic

- Establish FBR as a physically meaningful continuous indicator of exposed bedrock or bare-rock fraction.
- Use LSMM/SMA/MESMA as fraction-inversion methods, not as classification maps.
- Use DeepLabV3+ as the main segmentation model and FCN/U-Net as baselines.
- Use open-source DEM for cross-region transfer because it covers both study areas.
- Use GF-7 stereo-derived DEM only for local high-resolution terrain enhancement in Study Area 2.
- Report metric families separately for continuous FBR and classification/segmentation outputs.

## Suggested Manuscript Spine

1. KRD monitoring problem and ecological significance.
2. FBR and bare-rock exposure as key remote-sensing variables.
3. Limits of traditional feature-space, ML, and fraction methods.
4. Need for segmentation, terrain constraints, and transfer validation.
5. Proposed multi-source workflow.
6. Results separated by target type.
7. Discussion of mechanism, transferability, uncertainty, and limitations.

## Red Lines

- Do not claim that GF-7 stereo DEM improves cross-region transfer.
- Do not compare continuous FBR directly with categorical maps.
- Do not report classification accuracy for a continuous fraction result.
- Do not invent experiment results or literature claims.

