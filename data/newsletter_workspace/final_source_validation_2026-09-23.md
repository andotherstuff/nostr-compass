# Compass #41 final-cutoff source validation

The distinct 2026-09-23T23:44:00Z..2026-09-24T00:41:00Z source pass is finalized. All ten maintained families have a terminal `complete`, `empty_verified`, or `not_applicable` state. This validates source collection only; editorial, PR-head, CI and publication gates are separate.

Manifest: `data/source_runs/source_run_2026-09-23_final-20260924T0041Z.json`
SHA-256: `43e3059de6af088b4c8b71d33c5a74a4c97d6350c29595ae1bdb9be3a0ffcd81`

The exact specs collector has complete pagination and zero in-window includes; seven specification families are quiet. The final source manifest and ten collector receipts were copied byte-for-byte from the isolated cutoff worktree into this branch.

Validation run in this newsletter worktree:

```text
jq -e '(.finalized == true) and (.window == {since: "2026-09-23T23:44:00Z", until: "2026-09-24T00:41:00Z"}) and ((.families | keys | length) == 10) and ([.families[].status] | all(. == "complete" or . == "empty_verified" or . == "not_applicable"))' data/source_runs/source_run_2026-09-23_final-20260924T0041Z.json
true
```
