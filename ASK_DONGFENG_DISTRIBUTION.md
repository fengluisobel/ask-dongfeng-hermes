# Ask DongFeng Hermes Distribution

This repository is an independent Hermes Agent distribution with Ask DongFeng bundled as a first-class built-in skill.

Upstream Hermes Agent remains the base runtime. Ask DongFeng adds a control-loop workflow layer for turning vague goals, specs, plans, spikes, and reviews into executable DongFeng Packets.

## What Is Integrated

- Upstream Hermes Agent source code.
- Built-in skill: `skills/software-development/ask-dongfeng`.
- Ask DongFeng references, validators, and agent metadata.
- Distribution docs under `docs/ask-dongfeng/`.
- Smoke validation script under `scripts/ask-dongfeng/`.

## What Is Not Changed Yet

- No model provider changes.
- No agent loop rewrite.
- No separate memory system.
- No separate GUI implementation.
- No changes to Hermes Desktop behavior.

The first target is a maintainable source-integrated distribution. Deeper Desktop or runtime changes should happen only after the bundled skill path is stable.

## Quick Test From Source

From the repository root:

```bash
python scripts/ask-dongfeng/smoke_builtin_skill.py
```

Then run Hermes from this checkout and list built-in skills:

```bash
python -m hermes_cli.main skills list --source builtin --enabled-only
```

Expected:

```text
ask-dongfeng
```

One-shot usage:

```bash
python -m hermes_cli.main chat --skills ask-dongfeng -q "Use Ask DongFeng in intent-to-spec mode: turn a fuzzy product idea into a reviewable MVP spec."
```

## Release Positioning

This repo should be described as:

> Hermes Agent with Ask DongFeng bundled as an operational control-loop framework skill.

It should not claim to be a new agent runtime until the core loop or Desktop is intentionally modified.

## Upstream Attribution

Hermes Agent is built by Nous Research and licensed under MIT.

This distribution keeps upstream attribution and license files intact.

