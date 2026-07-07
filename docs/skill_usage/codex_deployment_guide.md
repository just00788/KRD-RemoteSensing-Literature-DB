# Codex Deployment Guide for krd-remote-sensing

## 1. Purpose

This document explains how Codex should use the krd-remote-sensing Skill source in this repository.

The Skill is installed in ChatGPT through `skill.zip`, but Codex should use the repository version as project knowledge and operating rules.

## 2. Important Distinction

- ChatGPT installs the Skill using `skill_build/dist/skill.zip`.
- Codex does not need to install `skill.zip` as a plugin.
- Codex should read `AGENTS.md` and the Skill source under `skill_build/krd-remote-sensing/`.
- Codex should follow the scientific rules, writing rules, and caution rules defined there.

## 3. Skill Source Location

Skill source:

```text
skill_build/krd-remote-sensing/
```

Final installable package:

```text
skill_build/dist/skill.zip
```

Key files:

- `skill_build/krd-remote-sensing/SKILL.md`
- `skill_build/krd-remote-sensing/references/research-framework.md`
- `skill_build/krd-remote-sensing/references/experiment-design.md`
- `skill_build/krd-remote-sensing/references/fbr-lsmm-guidelines.md`
- `skill_build/krd-remote-sensing/references/dem-guidelines.md`
- `skill_build/krd-remote-sensing/references/semantic-segmentation-guidelines.md`
- `skill_build/krd-remote-sensing/references/remote-sensing-journal-writing.md`
- `skill_build/krd-remote-sensing/references/remote-sensing-terminology.md`
- `skill_build/krd-remote-sensing/references/review-checklist.md`
- `skill_build/krd-remote-sensing/assets/templates/`

## 4. How Codex Should Use This Skill

When the user asks for KRD remote sensing work, Codex should:

1. Read `AGENTS.md`.
2. Read `skill_build/krd-remote-sensing/SKILL.md`.
3. Load only the relevant reference files.
4. Follow the scientific caution rules.
5. Never invent experimental results.
6. Never claim GF-7 stereo DEM improves cross-region transfer.
7. Keep LSMM/FBR continuous metrics separate from classification metrics.
8. Use Remote Sensing manuscript style when writing paper sections.
9. Produce reproducible scripts and logs when generating code.
10. Mark uncertain values as `needs_manual_check` or `needs_verification`.

## 5. Typical Codex Tasks

Codex can use this Skill source to:

- Generate experiment scripts.
- Build config files.
- Validate raster and label paths.
- Implement DeepLabV3+, FCN, and U-Net baselines.
- Implement DEM ablation experiments.
- Generate manuscript outlines.
- Rewrite Methods or Results.
- Create review checklists.
- Prepare response-to-reviewers drafts.

## 6. What Codex Must Not Do

Codex must not:

- Treat `skill.zip` as a source database.
- Modify `skill.zip` directly.
- Invent result values.
- Mix continuous FBR metrics with classification metrics.
- Treat GF-7 stereo DEM as cross-region evidence.
- Overwrite raw data.
- Move or delete PDFs.
- Add raw PDFs into the Skill source.
- Claim literature support beyond what is in references or readers.

## 7. Recommended Workflow

For each KRD task:

1. Read `AGENTS.md`.
2. Identify whether the task is experiment design, coding, manuscript writing, terminology, or review.
3. Read the corresponding Skill reference files.
4. Produce a short execution plan.
5. Ask only if critical information is missing.
6. Execute only the requested phase.
7. Save outputs in the appropriate `docs/`, `scripts/`, `configs/`, `results/`, or `logs/` folder.
8. Report changed files and next steps.
