# DEM and Terrain Guidelines

## When to use this reference

Use this reference when the user asks about DEM, slope/aspect/elevation, terrain constraints, GF-7 stereo DEM, open-source DEM, or cross-region transfer.

## DEM Role

DEM-derived terrain variables can help represent KRD-relevant topographic controls, including elevation, slope, aspect, relief, and terrain position.

## Open-Source DEM Rule

Use open-source DEM for Area 1 to Area 2 transfer because it covers both study areas consistently. This makes the DEM feature space available during both training and transfer testing.

## GF-7 Stereo DEM Rule

Use GF-7 stereo-derived DEM only for local high-precision terrain enhancement in Study Area 2.

Do not claim that GF-7 stereo-derived DEM improves Area 1 to Area 2 cross-region transfer unless the user supplies a validated experiment proving that claim.

## Recommended Experiments

- Spectral baseline.
- Spectral + open-source DEM.
- Cross-region transfer using open-source DEM.
- Study Area 2 local enhancement with GF-7 stereo DEM.
- DEM ablation by terrain variable group.

## Writing Guidance

Phrase DEM claims narrowly:

- Suggested: "Open-source DEM variables were used to maintain feature consistency across study areas."
- Suggested: "GF-7 stereo-derived DEM was evaluated as a local high-resolution terrain enhancement for Study Area 2."
- Avoid: "GF-7 DEM improved cross-region transfer."

## Cautions

- `caution`: DEM resolution mismatch can affect model inputs and interpretation.
- `needs verification`: Any claimed DEM improvement requires real ablation results.

