# FBR, LSMM, SMA, and MESMA Guidelines

## When to use this reference

Use this reference for FBR explanation, LSMM/SMA/MESMA method design, continuous fraction validation, thresholding, and avoiding metric confusion.

## Definitions

- FBR: bare-rock fraction or exposed-bedrock fraction, normally a continuous proportion.
- LSMM/SMA: linear spectral mixture analysis for estimating sub-pixel fractions.
- MESMA: multiple endmember spectral mixture analysis, allowing endmember combinations to vary.

## Correct Interpretation

LSMM/SMA/MESMA produce continuous fraction estimates. They become classification evidence only after thresholds are defined and applied.

## Recommended Workflow

1. Select spectral bands or indices sensitive to vegetation, soil, and exposed rock.
2. Define or estimate endmembers.
3. Estimate continuous FBR.
4. Validate FBR against field/UAV/reference fractions.
5. If needed, threshold FBR into KRD grades.
6. Compare thresholded grades with classification or segmentation outputs.

## Continuous Metrics

Use R2, RMSE, MAE, bias, and regression slope. Do not use OA or Kappa for continuous FBR unless FBR has first been converted into discrete classes.

## Thresholded Classes

If the manuscript uses NRD/LRD/MRD/SRD or similar categories, state the thresholds explicitly and cite their source or mark them as study-defined.

## Cautions

- `caution`: Endmember selection and shadow/topography effects can introduce uncertainty.
- `needs verification`: Any numeric FBR thresholds must be checked against the user's actual classification standard.
- Do not invent FBR validation values.
- Batch 03 quick reading strengthened FBR-adjacent coverage through feature-space, red-edge, vegetation-index, object-oriented, and bare-rock information extraction papers, but it did not fully close the LSMM/SMA/MESMA evidence gap.
- Do not treat feature-space indices, vegetation-index enhancement, or object-oriented KRD extraction as LSMM/SMA/MESMA evidence unless the method explicitly performs spectral mixture analysis.
- Use Batch 03 notes only as method-taxonomy and caution support; do not copy numerical results or assert verified thresholds from quick readers.
