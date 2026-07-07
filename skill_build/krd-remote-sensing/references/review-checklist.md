# Review Checklist

## When to use this reference

Use this reference when auditing a draft, diagnosing reviewer-risk, or preparing a pre-submission internal review.

## High-Risk Issues

- Continuous FBR is described as a class map.
- LSMM is compared with classifiers without thresholding.
- R2/RMSE and OA/Kappa/F1/IoU are mixed.
- GF-7 stereo DEM is claimed to improve cross-region transfer.
- Random patch split is used without spatial leakage discussion.
- DeepLabV3+, FCN, and U-Net roles are unclear.
- Results contain unsupported numerical claims.
- Literature claims lack citation or verification.

## Scientific Review Questions

- What is the target variable?
- Is it continuous or categorical?
- Are metrics matched to the target variable?
- Is the validation spatially independent?
- Is DEM use scientifically justified?
- Are ablation experiments sufficient?
- Are limitations explicit?

## Writing Review Questions

- Does the Abstract state gap, data, method, result, and significance?
- Does the Introduction end with concrete objectives?
- Can another researcher reproduce Methods?
- Are Results separated from Discussion?
- Are figure/table captions informative?
- Are claims restrained?

