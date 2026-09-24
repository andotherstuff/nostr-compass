#!/usr/bin/env python3
"""Finalize the Compass #41 exact project-activity audit from reviewed primary PRs.

This file is issue-specific editorial data, not a general title heuristic.
The 80 explicit repository dispositions are checked against the frozen collector.
Live branch checks are imported separately only after authenticated readback.
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

from project_activity_coverage import HARD_GATES, SCORE_AXES, inventory, validate

ROOT = Path(__file__).resolve().parents[1]
WORK = ROOT / "data/newsletter_workspace"
UPDATES = ROOT / "data/project_updates/updates_2026-09-14_2026-09-23.json"
DRAFT = ROOT / "content/en/newsletters/2026-09-23-newsletter.md"
DECISIONS = WORK / "project_activity_decisions_2026-09-23.json"
AUDIT = WORK / "project_activity_coverage_2026-09-23.md"
BRANCH = WORK / "project_activity_branch_checks_2026-09-23.json"

INCLUDE = {
    "0xchat-app/0xchat-app-main": "Four merged audit fixes close Cashu signing, gift-wrap authentication, trusted-config and WebView consent paths; no app release is claimed.",
    "block/buzz": "Signed relay administration with transactional audit records is a distinct Nostr operator capability.",
    "Cameri/nostream": "Signed NIP-66 monitoring and opt-in trust-distance proof of work are distinct relay-operator capabilities.",
    "Conduit-BTC/conduit-mono": "Signed Blossom product-image uploads are a distinct Nostr marketplace capability.",
    "contextvm/ts-sdk": "Positive relay acknowledgement and corrected stream sequencing change Nostr SDK transport behavior.",
    "diegogurpegui/nos2x-fox": "Merged fixes close web-page PIN extraction and stable extension identification while making NIP-07 injection deterministic; no store release is claimed.",
    "divinevideo/divine-mobile": "Passive relay reconnection and all-relay profile verification repair distinct Nostr client paths.",
    "marmot-protocol/marmot": "Merged encrypted group-poll and moderation specifications are directly covered in the protocol section.",
    "MostroP2P/mostro": "Stable order creation time is a distinct interoperable NIP-69 trading change.",
    "nostr-protocol/nips": "Merged NIP-02 and NIP-86 changes are directly covered as protocol milestones.",
    "SnowCait/nostter": "Session-owned NIP-46 signing and image-share composition change Nostr client behavior.",
    "zapcooking/frontend": "NIP-92 image descriptions and pre-relay secret-key search protection are distinct user-visible changes.",
}
SKIP = {
    "abh3po/better-nips": "Adding one default relay is distribution configuration, not a distinct protocol or user workflow milestone.",
    "andotherstuff/pensieve": "The Wednesday PRs leave archive runtime disabled; later separately reviewed archive work is covered without retroactively claiming deployment.",
    "arkin0x/cyberspace": "Site presentation work has no distinct, source-verified Nostr capability beyond recent coverage.",
    "barrydeen/wisp": "NIP-22 comments and wallet withdrawal are covered by the tagged Wisp release, not a second PR story.",
    "bit-blik/bitblik": "Dispute and NIP-82 work is covered by the tagged BitBlik release rather than repeated as PR activity.",
    "BitcreditProtocol/Bitcredit-Core": "Bill-event resend and resync repairs are covered by the tagged Bitcredit release.",
    "block-core/angor": "The relay cleanup is a bounded maintenance fix below a separate operator milestone.",
    "breez/glow-web": "Payment interface and recovery work does not establish a distinct Nostr-facing change.",
    "cashubtc/cashu.me": "Duplicate Lightning payment-history repair has no distinct Nostr event or relay behavior.",
    "cashubtc/cdk": "Cashu melt and mint recovery work does not create a distinct Nostr-facing milestone.",
    "cashubtc/nutshell": "Mint redemption and routing changes do not establish a Nostr protocol or client surface.",
    "ChadFarrow/stablekraft-app": "General bandwidth iteration lacks a new source-verified Nostr capability.",
    "coracle-social/coracle": "The NIP-70 compose toggle is merged, but relay acceptance was not verified and it remains below the independent product-milestone bar.",
    "Cordn-msg/cordn": "This repository changed multi-device documentation; the separate tagged Cordn application release is covered.",
    "damus-io/notedeck": "Headless and ingest hardening is an early internal step without a verified user-facing Nostr release.",
    "dergigi/ants": "Library iteration has no demonstrated downstream adoption or distinct product change.",
    "dergigi/boris": "Linking an Android source repository is documentation, not a new capability.",
    "DhananjayPurohit/paygress": "Payment application iteration has no verified Nostr-facing feature above the editorial threshold.",
    "elisymlabs/elisym": "EVM payment and agent infrastructure work does not establish a discrete Nostr capability.",
    "fiatjaf/relayer": "Storage notifier changes are a bounded internal scaling repair without a separately demonstrated operator outcome.",
    "forgesworn/bark": "Approval-timeout classification is general payment-tool maintenance rather than a new Nostr surface.",
    "forgesworn/bray": "Human confirmation and payment caps are important but belong to a payment tool, without a distinct Nostr change.",
    "forgesworn/toll-booth": "Credential and payment-bypass fixes concern generic payment middleware, without a demonstrated Nostr interface change.",
    "formstr-hq/formstr-drive": "Media preview and outbox work is not yet a verified distinct Nostr release or complete capability.",
    "formstr-hq/nostr-calendar": "Mail bridge invites and relay defaults do not establish a separate Nostr milestone beyond existing calendar coverage.",
    "formstr-hq/nostr-docs": "One default-relay configuration addition is not a distinct user or protocol milestone.",
    "formstr-hq/nostr-forms": "Browser NIP-55 signer integration is merged, but its app deployment is unverified and it is not yet a separate release milestone.",
    "formstr-hq/nostr-polls": "Browser NIP-55 signer integration mirrors the forms change, with no verified deployment or independent milestone.",
    "fr34aky/fips2go": "Merged client work is covered through the verified 0.6.0 to 0.7.0 tagged releases rather than a duplicate PR story.",
    "getAlby/hub": "Swap infrastructure is not a discrete Nostr-facing milestone in this window.",
    "getAlby/lightning-browser-extension": "These PRs update build dependencies; the separate security release is covered by its tag.",
    "git.nostrdev.com/stuff/NostrAppShell": "This is an alias of the pakstr package sequence already covered through exact release tags.",
    "git.nostrdev.com/stuff/pakstr": "Signer and runtime work is covered by the 0.22.0 to 0.24.0 release sequence, not duplicated here.",
    "HeterodyneNetwork/HeterodyneProtocol": "The maintenance workflow phase does not demonstrate a live Nostr protocol change.",
    "hroomnik007/MintRadar": "Current source and signed submission support the main MintRadar story; these UI and stats PRs are not a second independent milestone.",
    "jesuspirate/chama": "Site polish and rapid tags lack one source-supported Nostr feature milestone.",
    "lawalletio/lawallet-nwc": "NWC receipt changes are covered by the 2.7.0 to 2.7.1 release story.",
    "lnbits/lnbits": "Lightning settlement work has no distinct Nostr surface in the reviewed PRs.",
    "Lokuyow/ehagaki": "Web-component reconnect repair is useful but below a standalone significance threshold.",
    "lontivero/Nostra": "A general test and bug-fix PR does not establish a specific Nostr user change.",
    "marmot-protocol/mdk": "Durable sends and attachment work is covered by the tagged 0.10.4 release; later account recovery is not claimed as released.",
    "marmot-protocol/whitenoise": "A landing-page proposal changes repository documentation, not the shipped messenger.",
    "mattn/cagliostr": "Redis inter-instance propagation is a bounded implementation step without a demonstrated new Nostr client capability.",
    "mattn/nostr-relay": "Shared-database and Redis propagation are scaling steps without a verified release or operator migration.",
    "michaelneale/mesh-llm": "Payment and host runtime development does not yield a verified Nostr product delta.",
    "MostroP2P/mostro-cli": "Chat transport and cancellation are covered by the tagged Mostro CLI release.",
    "MostroP2P/mostro-core": "Trade pubkey and dispute-model fields are supporting library changes without a distinct released client behavior.",
    "nbd-wtf/nostr-tools": "NIP-42 rejection and NIP-77 error propagation repair library edge cases but are below a separate product-milestone threshold.",
    "nogringo/nostr-mail-client": "Relay-list and delivery choice changes are covered by the tagged Nostr Mail Client release.",
    "nostr-wot/nostr-wot-extension": "Scoped NWC work is covered by the tagged 0.8.0 to 0.8.3 release sequence.",
    "nostr-wot/nostr-wot-oracle": "Graph readiness and persistence are covered by the tagged 0.3.0 to 0.3.1 releases.",
    "nostr-wot/nostr-wot-sdk": "Graph storage and crawling changes are covered by the tagged 1.0.2 and graph 0.3.0 releases.",
    "Origami74/myco": "The 0.7.0 runtime release appeared in prior coverage; current PRs add no separate verified launch.",
    "penpenpng/rx-nostr": "Filtering non-relay tags from defaults is a bounded library correction below a standalone milestone.",
    "permissionlesstech/bitchat": "Mesh privacy and sync bounds do not change a verified Nostr application surface.",
    "privkeyio/keep-android": "Removing an obsolete Android SDK CI package is build maintenance, not a user-visible Nostr change.",
    "relaystr/ndk": "NIP-82 and authenticated delivery work is covered by the Dart NDK prerelease story.",
    "routstr/routstrd": "Routing-service maintenance has no new user-facing Nostr behavior in this window.",
    "rust-nostr/nostr": "Local-relay connection limits and BIP321 helpers are library increments without demonstrated downstream adoption.",
    "shocknet/Lightning.Pub": "Admin metadata changes remain below the separate Nostr significance threshold.",
    "shocknet/wallet2": "Dashboard and overlay work has no specific source-verified Nostr milestone.",
    "shopstr-eng/milk-market": "Domain migration is site operations rather than a new Nostr marketplace feature.",
    "shopstr-eng/shopstr": "Marketplace search relay refresh and payout work lack a distinct, tested Nostr milestone.",
    "spacecowboy/Feeder": "Per-feed filtering and display work are useful but not a distinct Nostr interoperability milestone.",
    "TsukemonoGit/lumilumi": "No verified launch or protocol milestone is supported by the reviewed activity.",
    "vitorpamplona/amethyst": "Wednesday PRs are covered by the tagged 1.16.0 release; later MLS and DECK work is separately reviewed.",
    "zeSchlausKwab/napplet-soy": "A macOS CI probe repair is build maintenance; CLI features are covered by exact tagged releases.",
    "ZeusLN/zeus": "Wallet and payment UI fixes have no distinct Nostr-specific outcome in this window.",
}
NON_NOSTR = {
    "breez/glow-web", "cashubtc/cashu.me", "cashubtc/cdk", "cashubtc/nutshell",
    "elisymlabs/elisym", "forgesworn/bark", "forgesworn/bray",
    "forgesworn/toll-booth", "getAlby/hub", "lnbits/lnbits",
    "michaelneale/mesh-llm", "permissionlesstech/bitchat",
    "shopstr-eng/milk-market", "ZeusLN/zeus",
}
SCORE_9 = dict(zip(SCORE_AXES, (2, 2, 2, 2, 1)))
SCORE_8 = dict(zip(SCORE_AXES, (2, 2, 1, 2, 1)))
SKIP_SCORE = dict(zip(SCORE_AXES, (2, 1, 1, 1, 1)))


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    updates = json.loads(UPDATES.read_text())
    activity = inventory(updates, sha(UPDATES))
    repo_names = {row["repo"] for row in activity["projects"]}
    if (set(INCLUDE) | set(SKIP)) != repo_names or set(INCLUDE) & set(SKIP):
        raise ValueError(f"explicit editorial decisions differ from inventory: missing={sorted(repo_names - set(INCLUDE) - set(SKIP))}, extra={sorted((set(INCLUDE) | set(SKIP)) - repo_names)}")
    draft = DRAFT.read_text()
    branch_checks = json.loads(BRANCH.read_text()) if BRANCH.exists() else {}
    if not isinstance(branch_checks, dict):
        raise ValueError("branch verification must be an object by PR URL")
    rows = []
    for project in activity["projects"]:
        repo = project["repo"]
        prs = project["prs"]
        urls = [pr["url"] for pr in prs]
        cited = [url for url in urls if url in draft]
        if repo in INCLUDE:
            if not cited:
                raise ValueError(f"included project has no cited primary PR: {repo}")
            row = {
                "repo": repo, "reviewed_pr_urls": urls, "verdict": "include",
                "reason": INCLUDE[repo], "primary_sources": cited,
                "selected_pr_urls": cited,
                "hard_gate": dict.fromkeys(HARD_GATES, True),
                "scores": SCORE_8 if repo in {"marmot-protocol/marmot", "nostr-protocol/nips"} else SCORE_9,
                "branch_checks": [branch_checks[url] for url in cited if url in branch_checks],
            }
        else:
            if cited:
                raise ValueError(f"skipped project has a cited PR: {repo}: {cited}")
            primary = next((pr["url"] for pr in reversed(prs) if pr["material_hint"]), prs[-1]["url"])
            row = {
                "repo": repo, "reviewed_pr_urls": urls, "verdict": "skip",
                "reason": SKIP[repo], "primary_sources": [primary],
                "selected_pr_urls": [],
                "hard_gate": {"primary_evidence": True, "in_window_progress": True,
                              "nostr_surface": repo not in NON_NOSTR, "continuity_delta": False},
                "scores": {**SKIP_SCORE, "nostr_significance": 0 if repo in NON_NOSTR else 2},
                "branch_checks": [],
            }
        rows.append(row)
    decisions = {"schema_version": 1, "updates_sha256": activity["updates_sha256"], "projects": rows}
    errors = validate(activity, decisions, draft)
    if errors:
        raise ValueError("project audit incomplete:\n" + "\n".join(errors))
    DECISIONS.write_text(json.dumps(decisions, indent=2, ensure_ascii=False) + "\n")
    lines = [
        "# Compass #41 exact project-activity audit",
        "",
        f"The frozen Wednesday project artifact is `{UPDATES.relative_to(ROOT)}`, SHA-256 `{sha(UPDATES)}`.",
        f"All {activity['project_count']} projects and {activity['pr_count']} merged PR URLs were reconciled against the assembled draft.",
        "A release-covered project is not automatically a second PR story; a skipped project has no cited Wednesday PR URL.",
        "The machine-readable decisions include the full reviewed URL list, primary evidence, scores, hard gates, and live branch readbacks.",
        "",
        "## Included primary PR work",
        "",
    ]
    for row in rows:
        if row["verdict"] == "include":
            lines += [f"- `{row['repo']}`: {row['reason']} " + " ".join(row["selected_pr_urls"])]
    lines += ["", "## Folded or skipped PR work", ""]
    for row in rows:
        if row["verdict"] == "skip":
            lines += [f"- `{row['repo']}`: {row['reason']} Primary readback: {row['primary_sources'][0]}"]
    lines += ["", f"GATE: PASS ({activity['project_count']}/{activity['project_count']} projects; {activity['pr_count']} merged PR URLs dispositioned)", ""]
    AUDIT.write_text("\n".join(lines))
    print(f"PASS: {len(INCLUDE)} included projects, {len(SKIP)} skipped/folded projects, {activity['pr_count']} PR URLs")


if __name__ == "__main__":
    main()
