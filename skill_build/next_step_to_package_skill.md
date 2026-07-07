# Next Step to Package Skill

1. The current `skill_build/krd-remote-sensing` directory is a draft source tree, not a final packaged skill.
2. Convert `SKILL_DRAFT.md` into formal `SKILL.md`.
3. Check that frontmatter contains only valid `name` and `description` fields.
4. Validate `agents/openai.yaml` against the active ChatGPT/Codex skill packaging requirements.
5. Confirm again that no PDFs, large files, or copyrighted article full text are included.
6. Use the ChatGPT/Codex `skill-creator` workflow to package the skill formally.
7. The user can compress `skill_build/krd-remote-sensing` and provide it to ChatGPT for formal inspection.
8. ChatGPT should inspect the draft tree and then generate `skill.zip`.

