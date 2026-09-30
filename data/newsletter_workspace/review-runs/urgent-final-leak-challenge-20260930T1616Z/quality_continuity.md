# Distinct weekly milestones, prior issue continuity and month-end history

Article SHA256: `406c7db2562afa1d5eda16e0bae940ec406d7cfa17683ecd16722a720387a217`

Actual reviewer: cursor/composer-2.5[fast=true]. Supplied-text review only; no network/build checks. This is one scope of a single five-scope invocation, not a separate model call.

Verdict: FAIL

The two supplied mechanical corrections were applied correctly: Iris Meet now reads "This is default-branch implementation progress" and the Hubstr Relay paragraph no longer carries the "This can share the existing Hubstr Blossom section" placement note, without altering the adjacent source-claim boundaries. A mandatory full-article scan of snapshot 406c7db still finds unreremoved internal writer/editor directives in the Buzz and Marmot MDK sections. Those leaks are independent of the fixed Iris/Hubstr edits and block a PASS on this correction-only scope; pending substantive delta review remains separate.

Findings: [{"evidence": "In the Buzz desktop 0.5.26 paragraph: \"Preserve the existing explanation that NIP-AR and NIP-FI are Buzz's project specifications.\" The preceding sentences already state that NIP-AR is Buzz's own proposal and NIP-FI is a project specification; \"Preserve the existing explanation\" is placement guidance to the writer, not reader-facing newsletter prose.", "recommendation": "Delete the preservation directive and, if needed, fold its substance into ordinary reader-facing sentences already present earlier in the Buzz section.", "severity": "major", "title": "Buzz section retains an editorial preservation directive"}, {"evidence": "Closing sentence of the in-development Marmot MDK item: \"These source changes should be described separately from the already tagged MDK release.\" This tells an editor how to organize coverage rather than reporting project behavior to readers.", "recommendation": "Remove the meta-instruction; if separation matters to readers, state it as factual scope (for example, that the merges follow the tagged 0.11.0 release) without a directive to the writer.", "severity": "major", "title": "Marmot MDK in-development section carries a section-placement instruction"}]
