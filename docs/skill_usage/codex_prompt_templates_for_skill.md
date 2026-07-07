# Codex Prompt Templates for krd-remote-sensing

## Template 1: Load Skill Rules

Please read `AGENTS.md` and then load the krd-remote-sensing Skill rules from:

```text
skill_build/krd-remote-sensing/SKILL.md
```

For this task, also load these references:

```text
[INSERT REFERENCE FILES]
```

Follow the Skill's scientific rules and do not invent data, metrics, citations, or experiment results.

## Template 2: Experiment Design Task

Please use the krd-remote-sensing Skill rules to review or design the experiment framework for my KRD Remote Sensing manuscript.

Focus on:

- FBR / LSMM / MESMA.
- DeepLabV3+ main model.
- FCN and U-Net baselines.
- Open-source DEM terrain-factor ablation.
- Area 1 to Area 2 cross-region transfer.
- GF-7 stereo DEM as Study Area 2 local enhancement only.
- Spatial block split.
- Class-level accuracy metrics.

Output:

- Experiment design checklist.
- Risks and corrections.
- Reproducible Codex implementation plan.
- Files to create or modify.

## Template 3: Manuscript Writing Task

Please use the krd-remote-sensing Skill rules to revise this manuscript section for Remote Sensing.

Load:

- `remote-sensing-journal-writing.md`
- `remote-sensing-style-and-phrases.md`
- `remote-sensing-terminology.md`
- `review-checklist.md`

Requirements:

- Preserve scientific meaning.
- Improve Remote Sensing style.
- Avoid overclaiming.
- Mark uncertain claims as `needs_verification`.
- Do not invent results or citations.

## Template 4: Methods Implementation Task

Please use the krd-remote-sensing Skill rules to generate Codex-ready implementation steps for:

```text
[INSERT TASK]
```

Load:

- `experiment-design.md`
- `fbr-lsmm-guidelines.md`
- `dem-guidelines.md`
- `semantic-segmentation-guidelines.md`
- `codex-prompts.md`

Requirements:

- No random patch split.
- Use spatial block split.
- Separate continuous FBR validation from classification metrics.
- Keep GF-7 stereo DEM local to Study Area 2.
- Output reproducible scripts, configs, logs, and result tables.

## Template 5: Skill Update Task

Please update the krd-remote-sensing Skill source based on new literature or experiment results.

Do not edit `skill.zip`.

Update in this order:

1. `docs/literature/skill_source/`
2. `skill_build/krd-remote-sensing/references/`
3. `skill_build/krd-remote-sensing/SKILL.md` only if routing or core rules change
4. `final_prepackage_check.md`
5. Prepare a review zip for ChatGPT final packaging

Do not include PDFs or large files in the Skill source.
