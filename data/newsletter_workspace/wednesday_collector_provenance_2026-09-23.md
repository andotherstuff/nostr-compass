# Compass #41 Wednesday collector provenance repair

The frozen Wednesday source pass was collected with `scripts/fetch_project_updates.py` at Git commit `29bab1a` (SHA-256 `dbe9996128d93f3bf46468c311b7f2dd93b92e8ab4e5eb1fd313eb80fd2ba5ae`). Main subsequently updated that script for complete merged-PR activity coverage (current SHA-256 `e40e59dcec5d53fe14c46a723118564be00e41b7856dbfd2b434fb4af0bc7790`). The newer code must remain active, but a finalized source receipt must continue to identify the bytes that actually collected its data.

An exact `git archive 29bab1a scripts/fetch_project_updates.py` extraction now lives at `data/source_runs/collector_snapshots/scripts/fetch_project_updates.py`. Its SHA-256 is unchanged from the original receipt. Only the collector path in the Wednesday manifest and its project-family receipt was rebound to that immutable snapshot; collector hash, query, candidate identities, dispositions, artifact paths, and artifact hashes are unchanged. No source collection was replayed or retroactively attributed to the newer code.

The Wednesday manifest's new SHA-256 is `4fc99ed313aea0db36e082b89bcc5e90b60466361e1fd51f7c2337015346771d`; its predecessor was `bcac650f8267bb5eecd808bd79c7dd31d308d18081176fc138081d6d0adb70c8`. The successor ledger and exact-draft coverage receipt must be rebuilt from the re-bound manifest. Historical independent-review snapshots remain immutable and document their earlier source identity.

Validation: `source_run_manifest.py verify-finalized` and `verify-family --family projects` both pass on the re-bound Wednesday manifest. The separate late and final cutoff manifests still verify against the untouched source worktree.
