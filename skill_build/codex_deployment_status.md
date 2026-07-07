# Codex Deployment Status for krd-remote-sensing

## 1. Deployment Goal

Deploy the krd-remote-sensing Skill source as Codex-readable project knowledge.

## 2. Files Checked

- `skill_build/krd-remote-sensing/SKILL.md`: exists.
- `skill_build/krd-remote-sensing/references/`: exists.
- `skill_build/krd-remote-sensing/assets/templates/`: exists.
- `skill_build/dist/skill.zip`: exists.
- `skill_build/dist/skill.zip` size: 26,208 bytes.

## 3. Codex Usage

Codex should use `AGENTS.md` and `skill_build/krd-remote-sensing/SKILL.md` as routing and rule sources.

Codex should load only the reference files needed for the current KRD remote sensing, experiment design, manuscript writing, terminology, or review task.

## 4. GitHub Backup

The final `skill.zip` exists and is included for GitHub backup. Its size is below 25 MB, so normal Git commit is acceptable and Git LFS is not required for this file.

## 5. Warnings

- Do not modify `skill.zip` directly.
- Do not include PDFs in the Skill source.
- Do not overclaim limited evidence.
- Do not generate experimental results without data.
- Do not skip manual verification for uncertain metadata or result values.
