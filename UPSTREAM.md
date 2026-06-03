# Upstream

This repository is a snapshot-based independent distribution derived from:

- Upstream: https://github.com/NousResearch/hermes-agent
- Base commit: `93e25ceb1326770b369b8c4151cd3b9c3cdc0688`
- Upstream license: MIT

Why snapshot history:

The initial local source checkout available during creation was shallow. Pushing the shallow fork history to GitHub failed because the remote could not receive missing historical objects. This repository therefore starts with a clean snapshot commit while preserving upstream attribution, license, and the base commit reference.

Distribution delta:

- Bundles Ask DongFeng as `skills/software-development/ask-dongfeng`.
- Adds Ask DongFeng distribution docs under `docs/ask-dongfeng/`.
- Adds `scripts/ask-dongfeng/smoke_builtin_skill.py`.

For upstream changes, compare against the base commit above and merge/cherry-pick intentionally.

