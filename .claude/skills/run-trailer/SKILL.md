---
name: run-trailer
description: Run, drive, and smoke-test striatum decision panels in the trailer repo — start a panel run, claim work packets, publish artifacts, record verdicts, recover wedged runs. Use when asked to run a panel, resolve an open question through striatum, or check/drive a striatum run here.
---

This repo has no software to launch — it's the build sheet for a physical trailer. What *runs* here is the decision process: **striatum multi-model panels** (claude/codex/gemini) whose accepted outcomes land as `docs/DECISION_LOG.md` rows + binding gates in `docs/juplaya-trailer-context.md`. The handle is **`.claude/skills/run-trailer/driver.sh`** — a thin wrapper over the striatum CLI with every flag shape verified live against striatum 2.22.0 (2026-06-04). The generic `striatum-*` skills in this repo are vendor-generated (stamped 2.8.0, stale vs the CLI); trust this driver first.

All paths relative to repo root.

## Prerequisites

Already on this box — verify, don't install:

```bash
which striatum codex gemini          # all in ~/.local/bin
ls /run/user/1000/striatum/          # daemon socket dir: client-token, discovery.json, daemon-go.sock
striatum list runs --json | jq .count
```

No daemon? `striatum daemon --help`. Token bricked (`daemon RPC authorization failed` on *read* verbs)? Recover it: copy the `client_token` value from `/run/user/1000/striatum/discovery.json` over `/run/user/1000/striatum/client-token`.

## Run (agent path) — the driver

```bash
D=.claude/skills/run-trailer/driver.sh

$D smoke                 # end-to-end self-test: one-job run through the full claim loop -> SMOKE PASS
$D status                # all runs + states
$D summary RUN_ID        # state, jobs, artifacts, verdicts

# Start a panel and drive one job:
RUN=$($D start docs/operator/workflows/<panel>/workflow.json main)
eval "$($D work $RUN <role> <lane>)"        # registers+claims+acks; sets $SESS $JOB $LEASE
$D hb $SESS $LEASE &  HB=$!                  # keepalive — lease reaps at 300s; ALWAYS background this
# ...do the work; packet (objective, prompt path, byline) is at /tmp/striatum-packet-$JOB.json
$D publish  $SESS $JOB $LEASE handoff <logical_name> runs/<panel>/<file>.md
$D complete $SESS $JOB $LEASE
kill $HB
```

Reviews: `$D review $SESS $JOB $LEASE <path> accept|needs_revision`. If submit-review refuses on a re-claimed review job (immutability), use the escape hatch: `$D verdict $SESS $JOB $LEASE accept`.

External lanes (codex/gemini jobs — run the model, then publish its output yourself):

```bash
$D lane-codex  /tmp/prompt.md   # codex exec, sandbox bypassed, stdin closed, 600s timeout
$D lane-gemini /tmp/prompt.md   # gemini -p yolo, 600s timeout
```

Recovery: `$D recover RUN_ID JOB_ID` (requeue-stale mints a fresh message for a zombie queued job).

## Authoring a new panel

Copy `docs/operator/workflows/juplaya-design-panel/` (workflow.json + prompts/ + roles/) as the template; `.claude/skills/run-trailer/smoke-workflow/` is the minimal one-job shape. Then `striatum workflow validate <path>` until `valid`. Accepted outcomes get a DECISION_LOG row (`proposed` until the owner ratifies) and gates in the build sheet; freeze run artifacts under `runs/<panel>/`.

## Gotchas (all hit for real)

- **`--help` is useless for daemon verbs** — "flags are derived from the daemon method." The claimed packet's `commands{}` block carries the exact CLI lines; error messages name missing params. Don't guess, claim and read.
- **Byline:** artifact front matter must match the packet's `author_line` **exactly** (`author: operator`). Schema'd kinds need more: `synthesis` → `schema_version: striatum.synthesis.v1` + `artifact_kind`; `finding` → those + `verdict_intent`. The rejection error contains the minimal valid block.
- **300s lease reaping is real.** Long writes between heartbeats lose the lease mid-job. Background `$D hb` before doing anything slow. If reaped: `$D work` again (`--replace` is built in) and republish.
- **Concurrent repo-write runs wedge** on the shared checkout (3 such runs from 2026-06-03 still sit `running`: run_9e484dba…, run_57a530fd…, run_5b03c224…). `run start` refuses new repo-write runs while they're active — the fix is `"worktree_isolation": "per_job"` on the lane (smoke-workflow has it).
- **…but publish still resolves repo_root.** Even with per_job isolation, write the artifact at the repo-root path (inside the job's `allowed_paths`); a file inside `.striatum/worktrees/...` is "outside the write scope". You never need `worktree create` unless you want the isolation for actual repo edits.
- **`branch confirm --branch main` works** — `records_only` mode, no branch switch, no `--create`. Panels that should land on a branch: `--branch striatum/<name> --create`.
- **codex hangs without `</dev/null`** ("Reading additional input from stdin..."). **agy `--print` silently hangs ~50%** — use `gemini -p` for one-shot gemini. Everything external gets `timeout -k 10 600`.
- **Workflow JSON requires `context_docs` (list) and `cycles` (list)** even when empty-ish; `cycles` as an object fails with "must be a list".
- **`git commit-apply` → `daemon RPC authorization failed`** with the plain client token; not needed for the artifact flow — skip it.

## Troubleshooting

| Symptom | Fix |
|---|---|
| `run start` → "run … already active … would share the main checkout" | `worktree_isolation: per_job` on the repo-write lane, re-prepare |
| `publish-artifact` → "artifact file does not exist" | file must exist at **repo_root** path, not in the worktree |
| `publish-artifact` → "outside the job write scope" | path must be inside the packet's `allowed_paths` |
| `submit-review` → "verdict-capable job must be claimed or running" | re-claim via `$D work`, or bare `$D verdict` |
| job stuck `queued`, claim-next returns nothing | `$D recover RUN_ID JOB_ID` |
| any verb → "daemon RPC authorization failed" | token bricked → recover from `discovery.json` (Prerequisites) |
| run prepared but never started, sits `ready` | `striatum run cancel --run-id …` |
