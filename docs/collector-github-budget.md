# GitHub collection budget

Bulk research shares the account with publishing and CI operations. On Hermes,
the project collector selects `/opt/data/.local/bin/gh`; elsewhere,
`COMPASS_GITHUB_GH` selects a maintained authenticated CLI. Without either
configuration the portable HTTP client remains available. Once a guarded CLI
is selected, failures never cause a raw-HTTP fallback or credential rotation.

Guarded requests use one page at a time, preserve response bodies and `Link`
pagination, reject links outside the GitHub API origin, and set
`HERMES_GH_BULK=1`. Hermes's guard serializes admission and leaves 1,500 REST
core requests for other work. GraphQL and search are separate buckets. Obtain
GraphQL availability from its own `rateLimit` query, never REST's GraphQL entry.

Freeze absolute UTC `--since` and `--until` timestamps and a caller-owned pass
ID. Use `fetch_all.sh` once; resume it with the same values after a deferral.
Do not run a standalone sweep first, repeat `--fresh`, or overlap collectors.
Full REST collection can span resets; a complete sweep plus the reserve may
exceed one hourly allocation. Prefer already verified exact-window receipts
and exhaustive receipt-producing GraphQL deltas. A small spot-check cannot
replace complete coverage.

Exit 75 stops collection promptly, preserves completed repositories, and
propagates through the master script. Failed repository pages are not recorded
as quiet successful repositories. No complete collector receipt is emitted
until all required repositories finish. Resume fetches unfinished repositories;
a new cutoff has its own timestamp-bound filename and cannot reuse stale data.
Compact/full mode and the complete project-input scope also have separate checkpoints.
Interrupted checkpoints persist repaired page evidence before receipt creation,
while an existing sealed receipt prevents an artifact rewrite.

The shared short response cache is discovery data. Retained ETags require
live authenticated revalidation before a body is reused; only a successful
304 establishes that it is unchanged. Exact publication preconditions, PR
heads, CI gates, and mutation readbacks use `HERMES_GH_NO_CACHE=1`, which bypasses
both response caching and conditional reuse. Do not change these gates to
unblock a quota-limited publisher.

Gitcrawl remains the source for broad discovery in repositories already covered
by the local mirror. Do not launch an agent-owned sync or add hundreds of
Compass repositories to its hot poller. The mirror does not provide universal,
exact-window newsletter coverage.

Verification:

```sh
python3 -m unittest tests/test_fetch_project_updates_guarded.py tests/test_fetch_project_updates_resume.py tests/test_fetch_app_discovery.py
```
