# Ask DongFeng Hermes Integration Plan

## Goal

Create a fully independent Hermes-based distribution where Ask DongFeng is available out of the box and can later grow into GUI and workflow-level integration.

## Phase 1: Source-Integrated Distribution

Status: in progress.

Tasks:

- Add Ask DongFeng as a built-in skill under `skills/software-development/ask-dongfeng`.
- Add distribution docs that explain the fork boundary.
- Add deterministic smoke validation for the bundled skill files.
- Create a public GitHub repo.
- Publish an initial release.

Acceptance criteria:

- `skills/software-development/ask-dongfeng/SKILL.md` exists.
- Required bundled resources exist: `references`, `scripts`, `agents`.
- Hermes can list `ask-dongfeng` from built-in skills.
- No Hermes core runtime behavior is changed.

## Phase 2: Installer Branding

Tasks:

- Add installer notes for this distribution.
- Decide whether to rename console entry points or keep `hermes`.
- Add Windows native, WSL, macOS, and Linux install docs.
- Keep upstream installer changes minimal to reduce merge conflicts.

Risk:

- Renaming package and executable too early creates dependency and support complexity.

Recommendation:

- Keep `hermes` command in v0.1.
- Brand the repository and docs as Ask DongFeng Hermes.

## Phase 3: GUI Entry Points

Tasks:

- Validate `hermes desktop` from this checkout.
- Add a Desktop-facing Ask DongFeng tutorial.
- Investigate whether Hermes Desktop supports mode/template entry points.
- If needed, add a small launcher rather than rewriting Desktop chat.

Acceptance criteria:

- A new user can start the Desktop and run an Ask DongFeng prompt without reading the skill source.

## Phase 4: Runtime UX

Possible changes:

- Add `/ask-dongfeng` shortcut.
- Add `hermes dongfeng` CLI helper.
- Add first-run prompt templates.
- Add validator command wrappers.

Risk:

- Runtime changes increase upstream merge burden.

Rule:

- Only add runtime changes that reduce repeated user friction and have tests.

## Phase 5: Upstream Strategy

Options:

- Keep as independent distribution.
- Submit Ask DongFeng as an upstream built-in skill PR.
- Submit smaller Desktop onboarding PRs upstream.
- Keep deeper opinionated changes in this fork.

Decision rule:

- If the integration is mostly skill/docs, upstream PR is preferred.
- If the integration becomes opinionated product UX, keep the fork separate.

