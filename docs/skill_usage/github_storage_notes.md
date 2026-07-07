# GitHub Storage Notes for krd-remote-sensing Skill

## What is stored in GitHub

- `skill_build/krd-remote-sensing/`: editable Skill source
- `skill_build/dist/skill.zip`: final installable Skill package, once copied from ChatGPT-generated packaging output
- `docs/literature/skill_source/`: upstream source materials
- `docs/skill_usage/`: usage notes and test prompts

## What should not be treated as part of the Skill

- `docs/literature/pdfs/`
- Raw PDF or CAJ files
- Full paper readers
- Large database files
- Raw experiment outputs

## How to restore on another computer

1. Clone the repository:

   ```bash
   git clone https://github.com/just00788/KRD-RemoteSensing-Literature-DB.git
   ```

2. If Git LFS is used:

   ```bash
   git lfs install
   git lfs pull
   ```

3. Find the final Skill package:

   ```text
   skill_build/dist/skill.zip
   ```

4. Upload `skill.zip` to ChatGPT Skills.

## How to update later

1. Add new literature or experiment notes.
2. Update `docs/literature/skill_source/`.
3. Regenerate `skill_build/krd-remote-sensing/`.
4. Ask ChatGPT to review and package a new `skill.zip`.
5. Replace `skill_build/dist/skill.zip`.
6. Commit and push.
