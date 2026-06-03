# Start With Ask DongFeng

Ask DongFeng is bundled in this distribution as a built-in Hermes skill.

## List The Skill

```bash
hermes skills list --source builtin --enabled-only
```

Look for:

```text
ask-dongfeng
```

## Start Chat With The Skill

```bash
hermes chat --skills ask-dongfeng
```

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

