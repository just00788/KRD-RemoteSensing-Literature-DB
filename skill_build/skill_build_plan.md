# Skill Build Plan: krd-remote-sensing

## 1. Skill Purpose

The `krd-remote-sensing` skill is intended to support:

- Karst rocky desertification (KRD) remote sensing research design.
- FBR, LSMM, SMA, and MESMA explanation and experiment planning.
- Gaofen, Sentinel, Landsat, DeepLabV3+, FCN/U-Net baselines, DEM terrain-constraint experiments, cross-region validation, and accuracy assessment.
- Remote Sensing journal manuscript outlining, rewriting, structural review, terminology control, and pre-submission quality checks.
- Follow-up paper writing, manuscript revision, reviewer-response preparation, and Codex experiment task generation.

## 2. Main User Scenarios

1. Design a KRD remote sensing experiment.
2. Explain FBR, LSMM, SMA, or MESMA.
3. Check DeepLabV3+, FCN, U-Net, DEM, and ablation experiment logic.
4. Rebuild a Remote Sensing manuscript outline.
5. Draft or revise an Introduction.
6. Draft or revise Methods.
7. Organize Results.
8. Strengthen Discussion.
9. Normalize Remote Sensing terminology.
10. Run a pre-submission checklist.
11. Generate a Codex experiment or analysis task.
12. Draft response-to-reviewers material.

## 3. Skill Modules

### Module A: KRD Scientific Reasoning

- `research-framework.md`
- `experiment-design.md`
- `fbr-lsmm-guidelines.md`
- `dem-guidelines.md`
- `semantic-segmentation-guidelines.md`
- `literature-map.md`
- `review-checklist.md`

### Module B: Remote Sensing Journal Writing

- `remote-sensing-journal-writing.md`
- `remote-sensing-style-and-phrases.md`
- `remote-sensing-terminology.md`
- `remote-sensing-submission-checklist.md`
- `remote-sensing-manuscript-template.md`

## 4. What Must Not Be Included

- No PDFs.
- No complete article full text.
- No long copyrighted source passages.
- No unverified DOI, author, journal, or year.
- No fabricated experimental results.
- No claim that GF-7 stereo-derived DEM improves Area 1 to Area 2 cross-region transfer.
- No treatment of continuous FBR as a classification map.
- No mixing of continuous metrics such as R2/RMSE with classification metrics such as OA/Kappa/F1/IoU.

## 5. Packaging Notes

For formal packaging later:

- Convert `SKILL_DRAFT.md` into `SKILL.md`.
- Validate YAML frontmatter.
- Validate `agents/openai.yaml`.
- Keep references concise.
- Keep `assets/templates/` limited to reusable templates.
- Keep the final skill zip under 25 MB.
- Do not package raw PDFs or large literature extraction files.

