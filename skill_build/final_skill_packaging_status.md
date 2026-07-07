# Final Skill Packaging Status

## Skill

- Skill name: krd-remote-sensing
- Final package: `skill_build/dist/skill.zip`
- Source directory: `skill_build/krd-remote-sensing/`
- Review archive: `skill_build/krd-remote-sensing_for_chatgpt_review.zip`
- Packaging tool: ChatGPT skill-creator final review
- Validation status: source prepackage check passed; final `skill.zip` is missing
- Package size: not available because `skill_build/dist/skill.zip` does not exist

Final skill.zip is missing. Please copy the ChatGPT-generated skill.zip into:

`D:\7.1\KRD-RemoteSensing-Literature-DB\skill_build\dist\skill.zip`

## GitHub Storage

The final Skill source is stored in this repository for backup and future updates. The final installable `skill.zip` still needs to be copied into `skill_build/dist/` before it can be stored in GitHub.

## Important Notes

- The Skill does not include original PDFs or CAJ files.
- The Skill contains only instructions, references, templates, and review/checklist resources.
- Original literature PDFs remain under `docs/literature/pdfs/` and are not part of the Skill package.
- Future updates should modify `docs/literature/skill_source/` first, then rebuild `skill_build/krd-remote-sensing/` and regenerate `skill.zip` through ChatGPT.

## Scientific Cautions

- FBR is a continuous bare-rock fraction variable.
- LSMM/SMA/MESMA outputs are continuous and should be evaluated with R2, RMSE, MAE, bias, and slope.
- Thresholded FBR can be compared with classification maps; continuous FBR metrics should not be mixed with OA/Kappa/F1/IoU.
- DeepLabV3+ is the main segmentation model; FCN and U-Net are baselines.
- Open-source DEM supports Area 1 to Area 2 transfer.
- GF-7 stereo-derived DEM is only for Study Area 2 local enhancement.
- Do not claim GF-7 stereo DEM improves Area 1 to Area 2 transferability.
- Batch 03 was quick reading, not full reading.
- LSMM/SMA/MESMA and GF/Gaofen evidence should still be stated cautiously.
