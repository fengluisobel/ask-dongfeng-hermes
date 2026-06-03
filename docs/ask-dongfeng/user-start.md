# Start With Ask DongFeng

Ask DongFeng is bundled in this distribution as a built-in Hermes skill.

## Recommended Start

```bash
hermes dongfeng
```

Single prompt:

```bash
hermes dongfeng -q "Turn this fuzzy product idea into a reviewable MVP spec."
```

Mode-specific prompt:

```bash
hermes dongfeng --mode plan-guard -q "Guard this implementation plan against drift."
```

Machine-readable artifact:

```bash
hermes dongfeng --artifact-only -q "Create a control artifact for this goal."
```

## Check The Skill

```bash
hermes skills list --source all --enabled-only
```

Look for:

```text
ask-dongfeng
```

On a fresh Ask DongFeng Hermes install, it should normally appear as `builtin`.
If it appears as `local`, Hermes found an older local copy first. That copy can
still be used by `hermes dongfeng`.

To replace an older local copy with this distribution's bundled copy:

```bash
hermes skills reset ask-dongfeng --restore
hermes skills list --source builtin --enabled-only
```

## Start Chat With The Skill

```bash
hermes chat --skills ask-dongfeng
```

This is equivalent to `hermes dongfeng`; the shortcut just removes the need
to remember the skill name.

## First Prompt

```text
Use Ask DongFeng in intent-to-spec mode.

Goal:
Build an open-source Hermes skill that turns fuzzy product ideas into reviewable MVP specs.

Output:
A concise DongFeng Packet with boundary, decision, control artifact, execution contract, human gates, and next action.
```

## What It Adds Beyond A Normal Plan

Ask DongFeng should produce:

- system boundary
- controlled object
- controlled, observed, control, disturbance, and lagging variables
- sensors
- green/yellow/red comparators
- controller actions
- feedback cadence
- human review gates
- exact next prompt or action

If the output is only a task list, it failed the intended workflow.

## Long Task Reality

Ask DongFeng can reduce repeated human reminders by making the loop explicit:
sensors, thresholds, correction actions, and review gates are part of the
artifact before execution starts.

It should not be treated as fully autonomous success insurance. Long tasks can
still fail when requirements are wrong, environment state changes, tests are
missing, external APIs drift, or the agent needs permission for irreversible
actions. Use human gates before destructive file changes, public releases,
security-sensitive decisions, or scope expansion.
