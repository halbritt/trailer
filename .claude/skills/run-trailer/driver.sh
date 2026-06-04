#!/usr/bin/env bash
# Striatum panel driver for the trailer repo.
# Every subcommand here was run live against striatum 2.22.0 on 2026-06-04.
# The "app" of this repo is the decision process: striatum multi-model panels
# whose accepted outcomes land as DECISION_LOG rows + gates in the build sheet.
set -euo pipefail

REPO="$(cd "$(dirname "${BASH_SOURCE[0]}")/../../.." && pwd)"
SKILL="$REPO/.claude/skills/run-trailer"
cd "$REPO"

usage() {
  cat <<'EOF'
usage: driver.sh <cmd> [...]

  status                          runs + states in the daemon
  summary RUN_ID                  digest: state, jobs, artifacts, verdicts
  start WORKFLOW_JSON [BRANCH]    validate + prepare + branch confirm + start -> RUN_ID
                                  (BRANCH defaults to the current branch; main => records_only)
  work RUN_ID ROLE LANE           register + claim + ack; prints eval-able exports,
                                  packet -> /tmp/striatum-packet-<job>.json
  hb SESSION_ID LEASE_ID          heartbeat keepalive loop (240s; lease reaps at 300s) — background it
  publish SESS JOB LEASE KIND LOGICAL_NAME PATH
  complete SESS JOB LEASE
  review SESS JOB LEASE PATH VERDICT    submit-review (accept|needs_revision)
  verdict SESS JOB LEASE VERDICT        bare verdict (escape hatch for re-claimed reviews)
  lane-codex PROMPT_FILE          run a prompt through codex (timeout-wrapped, stdin closed)
  lane-gemini PROMPT_FILE         run a prompt through gemini (timeout-wrapped)
  recover RUN_ID JOB_ID           requeue-stale: mint a fresh message for a zombie queued job
  smoke                           end-to-end self-test: one-job run through the full claim loop
EOF
}

cmd="${1:-help}"; shift || true
case "$cmd" in

status)
  striatum list runs --json | jq -r '.items[] | [.state, .run_id, .branch_name] | @tsv' | sort
  ;;

summary)
  striatum run summary --run-id "$1" --json | jq '{
    state: .run.state,
    jobs: [.jobs[] | {job: .workflow_job_id, state, attempt}],
    artifacts: [.artifacts[] | .logical_name],
    verdicts: [.verdicts[] | {job: .job_id, verdict}] }'
  ;;

start)
  WF="$1"; BR="${2:-$(git branch --show-current)}"
  striatum workflow validate "$WF" >&2
  RUN=$(striatum run prepare "$WF" --json | jq -r .run_id)
  striatum branch confirm --run-id "$RUN" --branch "$BR" --json >&2
  striatum run start --run-id "$RUN" --json >&2
  echo "$RUN"
  ;;

work)
  RUN="$1"; ROLE="$2"; LANE="$3"
  SESS=$(striatum register-session --run-id "$RUN" --role "$ROLE" --lane "$LANE" --replace --json | jq -r .session_id)
  PKT=$(striatum claim-next --session-id "$SESS" --json)
  JOB=$(echo "$PKT"  | jq -r .packet.job.job_id)
  LEASE=$(echo "$PKT" | jq -r .packet.lease.lease_id)
  MSG=$(echo "$PKT"  | jq -r .packet.lease.message_id)
  echo "$PKT" | jq .packet > "/tmp/striatum-packet-$JOB.json"
  striatum ack --session-id "$SESS" --message-id "$MSG" --lease-id "$LEASE" --json >&2
  echo "packet: /tmp/striatum-packet-$JOB.json" >&2
  echo "task prompt: $(echo "$PKT" | jq -r .packet.task_prompt.path)" >&2
  echo "byline (front matter MUST match): $(echo "$PKT" | jq -r '.packet.expected_artifacts[0].author_line')" >&2
  echo "export SESS=$SESS JOB=$JOB LEASE=$LEASE"
  ;;

hb)
  while :; do striatum heartbeat --session-id "$1" --lease-id "$2" --json >/dev/null 2>&1 || true; sleep 240; done
  ;;

publish)
  striatum publish-artifact --session-id "$1" --job-id "$2" --lease-id "$3" \
    --kind "$4" --logical-name "$5" --path "$6" --json
  ;;

complete)
  striatum complete --session-id "$1" --job-id "$2" --lease-id "$3" --json
  ;;

review)
  striatum submit-review --session-id "$1" --job-id "$2" --lease-id "$3" --path "$4" --verdict "$5" --json
  ;;

verdict)
  striatum verdict --session-id "$1" --job-id "$2" --lease-id "$3" --verdict "$4" --json
  ;;

lane-codex)
  timeout -k 10 600 codex exec --skip-git-repo-check \
    --dangerously-bypass-approvals-and-sandbox -c approval_policy=never \
    "$(cat "$1")" </dev/null
  ;;

lane-gemini)
  timeout -k 10 600 gemini --approval-mode yolo -p "$(cat "$1")"
  ;;

recover)
  striatum recovery requeue-stale --run-id "$1" --job-id "$2" --json
  ;;

smoke)
  echo "== smoke: full claim loop against the daemon" >&2
  RUN=$("$SKILL/driver.sh" start "$SKILL/smoke-workflow/workflow.json" main)
  eval "$("$SKILL/driver.sh" work "$RUN" author claude_code)"
  mkdir -p runs/skill-smoke
  printf '%s\n' "---" "author: operator" "---" "" \
    "Smoke OK — $(date -u +%FT%TZ) — $RUN" > runs/skill-smoke/smoke_note.md
  "$SKILL/driver.sh" publish  "$SESS" "$JOB" "$LEASE" handoff smoke_note runs/skill-smoke/smoke_note.md
  "$SKILL/driver.sh" complete "$SESS" "$JOB" "$LEASE"
  STATE=$(striatum run summary --run-id "$RUN" --json | jq -r .run.state)
  echo "run $RUN -> $STATE"
  [ "$STATE" = completed ] && echo "SMOKE PASS" || { echo "SMOKE FAIL"; exit 1; }
  ;;

*) usage ;;
esac
