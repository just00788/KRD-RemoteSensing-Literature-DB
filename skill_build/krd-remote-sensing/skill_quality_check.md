# Skill Quality Check

Generated for draft source tree: `skill_build/krd-remote-sensing`

## Checks

| Check | Status | Notes |
|---|---|---|
| Contains scientific module | pass | Scientific references generated under `references/`. |
| Contains Remote Sensing writing module | pass | Journal-writing references generated under `references/`. |
| Contains templates | pass | Eight templates generated under `assets/templates/`. |
| Contains PDFs or large files | pass | No PDFs intentionally added. |
| Contains long article full text | pass | References are rule/template/checklist oriented. |
| Contains unverified results | pass with caution | Templates use placeholders; some literature-derived source files contained OCR-corrupted text, not copied into the skill. |
| Contains mutually contradictory scientific rules | pass | FBR, metric, DEM, and segmentation rules are aligned with `AGENTS.md`. |
| Explains FBR, LSMM, DEM, DeepLabV3+, open-source DEM, and GF-7 stereo DEM | pass | Rules appear in `SKILL_DRAFT.md` and references. |
| Explains Remote Sensing structure, terminology, phrasing, and submission checks | pass | Covered by journal-writing references. |
| Suitable for later formal packaging | pass with caution | `SKILL_DRAFT.md` must be converted to `SKILL.md`; `agents/openai.yaml` is draft metadata. |

## Manual Review Items

- Review `agents/openai.yaml` against the final packaging schema.
- Confirm whether the final skill system allows optional `icon` and `color` fields.
- Convert `SKILL_DRAFT.md` to `SKILL.md` only during the formal packaging stage.

