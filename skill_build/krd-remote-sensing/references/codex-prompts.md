# Codex Prompts

## When to use this reference

Use this reference when generating a Codex task for experiments, manuscript drafting, database updates, quality checks, or reviewer-response work.

## General Task Template

```text
Please read AGENTS.md first and strictly follow the scientific rules.

Repository path:
[INSERT REPO PATH]

Task goal:
[INSERT GOAL]

Required inputs:
[INSERT INPUT FILES]

Required outputs:
[INSERT OUTPUT FILES]

Rules:
- Do not fabricate data, citations, DOI values, authors, journals, years, or results.
- Keep continuous FBR and classification outputs separate.
- Use correct metric families.
- Do not claim GF-7 stereo DEM improves cross-region transfer.

After completion:
- Run the relevant checks.
- Report created files, checks, commit status, and push status.
```

## Manuscript Revision Prompt

```text
Revise [SECTION] for a Remote Sensing-style KRD manuscript.
Use the project rules for FBR, LSMM, DEM, DeepLabV3+, FCN/U-Net, and metric families.
Keep all unverified results as placeholders.
Return revised text plus a short list of unresolved items marked needs verification.
```

## Experiment Audit Prompt

```text
Audit the experiment design for KRD remote sensing.
Check target variables, data sources, validation split, DEM role, model baselines, ablation design, and metrics.
Flag scientific red lines and propose specific fixes.
```

