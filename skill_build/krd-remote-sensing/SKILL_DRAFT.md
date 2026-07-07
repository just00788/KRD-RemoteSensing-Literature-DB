---
name: krd-remote-sensing
description: Specialized guidance for karst rocky desertification remote sensing research and Remote Sensing journal manuscript writing. Use when the user asks for help with rocky desertification mapping, FBR/LSMM/MESMA, Gaofen/Sentinel/Landsat data, DeepLabV3+, FCN/U-Net baselines, DEM terrain constraints, cross-region validation, accuracy assessment, Remote Sensing article structure, academic phrasing, terminology, manuscript revision, submission checklists, or Codex experiment instructions.
---

# KRD Remote Sensing Skill

## Core Behavior

First decide whether the user is asking about scientific experiment design, Remote Sensing journal writing, or both.

- For scientific design, load the scientific references.
- For writing, rewriting, terminology, and style tasks, load the journal-writing references.
- For full manuscript restructuring, load both scientific and journal-writing modules.
- Do not fabricate experiment results, citations, DOI values, authors, journals, years, or paper conclusions.
- Mark uncertain information as `needs verification`.

## Scientific Rules

- FBR is a continuous bare-rock fraction or exposed-bedrock fraction.
- LSMM, SMA, and MESMA output continuous fraction estimates unless explicitly thresholded later.
- Continuous FBR must be evaluated with R2, RMSE, MAE, bias, and regression slope when those data are available.
- FBR can be compared with classification models only after thresholding into classes such as NRD, LRD, MRD, and SRD.
- Classification and semantic segmentation results should use OA, Kappa, Precision, Recall, F1, IoU, mF1, and mIoU.
- DeepLabV3+ is the main semantic segmentation model for the planned manuscript.
- FCN and U-Net are baselines.
- Open-source DEM is used for Area 1 to Area 2 cross-region transfer because it covers both areas.
- GF-7 stereo-derived DEM is only for local high-precision terrain enhancement in Study Area 2.
- Do not claim that GF-7 stereo-derived DEM improves Area 1 to Area 2 transfer.
- Avoid random patch splitting; prefer spatial block split.

## Reference Loading Guide

- Experiment design: load `references/experiment-design.md`, `references/fbr-lsmm-guidelines.md`, `references/dem-guidelines.md`, and `references/semantic-segmentation-guidelines.md`.
- FBR/LSMM/SMA/MESMA: load `references/fbr-lsmm-guidelines.md`.
- DEM and terrain: load `references/dem-guidelines.md`.
- Semantic segmentation: load `references/semantic-segmentation-guidelines.md`.
- Remote Sensing writing: load `references/remote-sensing-journal-writing.md`, `references/remote-sensing-style-and-phrases.md`, and `references/remote-sensing-terminology.md`.
- Submission checks: load `references/remote-sensing-submission-checklist.md` and `references/review-checklist.md`.
- Codex tasks: load `references/codex-prompts.md`.
- Full manuscript restructuring: load `references/research-framework.md`, `references/experiment-design.md`, `references/remote-sensing-journal-writing.md`, and `references/remote-sensing-manuscript-template.md`.

## Output Rules

- Give structured, actionable guidance.
- Use Remote Sensing style when writing or rewriting manuscript text.
- Preserve scientific accuracy when polishing.
- Distinguish `confirmed`, `suggested`, and `needs verification`.
- Do not output unverifiable numerical results.
- Do not overclaim model performance, DEM transferability, or generality.

## Common Workflows

1. Paper experiment design.
2. Introduction rewriting.
3. Methods rewriting.
4. Results organization.
5. Discussion strengthening.
6. Pre-submission checking.
7. Codex experiment task generation.
8. Reviewer-response drafting.

