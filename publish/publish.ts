#!/usr/bin/env bun
// Compass newsletter → Nostr publishing pipeline.
//
// Every mutating stage is admitted by the per-edition journal identity and
// verified effect prerequisites; no shell environment flag grants authority.
//
// Merge and broadcast are independent explicit gates. The safe publication
// order is merge -> exact deployment confirmation -> Nostr broadcast.


import { join } from "node:path";
import { readFile } from "node:fs/promises";
import { parseIssue } from "./stages/parse.ts";
import { signArticle } from "./stages/sign.ts";
import { signAnnouncement } from "./stages/announce.ts";
import { broadcastIssue, previewBroadcastIssue } from "./stages/broadcast.ts";
import { mergeIssue, previewMergeIssue, type PullRequestIdentity } from "./stages/merge.ts";
import { previewDeployment, verifyAndRecordDeployment } from "./stages/deploy.ts";
import { logIssue } from "./stages/log.ts";
import { IssueLock, validateNumber } from "./lib/safety.ts";
import { closeBunker } from "./lib/bunker.ts";
import { notifyMilestone, prLink } from "./lib/notify.ts";
import { loadJournal, prepareDeployment, sha256 } from "./lib/journal.ts";
import { assertSigningAuthorized, previewEditionAuthorization, previewJournaledEditionAuthorization, recordEditionAuthorization, type AuthorizationReceipt } from "./lib/authorization.ts";
import { previewCompositeQuality, previewFeedbackSnapshot, recordCompositeQuality, recordFeedbackSnapshot, QUALITY_ROLES } from "./lib/gates.ts";

const OUT_DIR = process.env.COMPASS_OUT_DIR || join(import.meta.dir, "out");

type Stage = "parse" | "sign" | "announce-sign" | "merge" | "deploy" | "broadcast" | "log" | "all";

const COMPASS_DIR = process.env.COMPASS_DIR || join(import.meta.dir, "..");

type Args = {
  issue: number;
  stage: Stage;
  dryRun: boolean;
  reallyBroadcast: boolean;
  reallyMerge: boolean;
  logPr: boolean;
  prIdentity?: PullRequestIdentity;
  pageUrl?: string;
  authorizationReceipt?: string;
  feedbackReceipt?: string;
  qualityReceiptDir?: string;
};

function parseArgs(argv: string[]): Args {
  const positional: string[] = [];
  let stage: Stage = "all";
  let dryRun = false;
  let reallyBroadcast = false;
  let reallyMerge = false;
  let logPr = true;
  let prNumber: number | undefined;
  let headSha: string | undefined;
  let baseSha: string | undefined;
  let pageUrl: string | undefined;
  let authorizationReceipt: string | undefined;
  let feedbackReceipt: string | undefined;
  let qualityReceiptDir: string | undefined;

  for (let i = 2; i < argv.length; i++) {
    const a = argv[i];
    if (a === "--stage") {
      const next = argv[++i];
      if (
        next !== "parse" &&
        next !== "sign" &&
        next !== "announce-sign" &&
        next !== "broadcast" &&
        next !== "merge" &&
        next !== "deploy" &&
        next !== "log" &&
        next !== "all"
      ) {
        throw new Error(`Unknown --stage value: ${next}`);
      }
      stage = next;
    } else if (a === "--dry-run") {
      dryRun = true;
    } else if (a === "--really-broadcast") {
      reallyBroadcast = true;
    } else if (a === "--really-merge") {
      reallyMerge = true;
    } else if (a === "--no-log-pr") {
      logPr = false;
    } else if (a === "--pr-number") {
      prNumber = Number(argv[++i]);
    } else if (a === "--head-sha") {
      headSha = argv[++i];
    } else if (a === "--base-sha") {
      baseSha = argv[++i];
    } else if (a === "--page-url") {
      pageUrl = argv[++i];
    } else if (a === "--authorization-receipt") {
      authorizationReceipt = argv[++i];
    } else if (a === "--feedback-receipt") {
      feedbackReceipt = argv[++i];
    } else if (a === "--quality-receipt-dir") {
      qualityReceiptDir = argv[++i];
    } else if (a.startsWith("--")) {
      throw new Error(`Unknown flag: ${a}`);
    } else {
      positional.push(a);
    }
  }

  if (positional.length !== 1) {
    throw new Error("Expected exactly one positional argument: the newsletter number.");
  }
  const issue = validateNumber(positional[0]);

  const supplied = [prNumber !== undefined, headSha !== undefined, baseSha !== undefined];
  if (supplied.some(Boolean) && !supplied.every(Boolean)) throw new Error("--pr-number, --head-sha, and --base-sha must be supplied together");
  const prIdentity = supplied.every(Boolean) ? { number: prNumber!, head_sha: headSha!, base_sha: baseSha! } : undefined;
  return { issue, stage, dryRun, reallyBroadcast, reallyMerge, logPr, prIdentity, pageUrl, authorizationReceipt, feedbackReceipt, qualityReceiptDir };
}

function usage(): string {
  return [
    "Usage:",
    "  compass-publish <issue> [--stage parse|sign|announce-sign|merge|deploy|broadcast|log|all]",
    "                          [--page-url https://nostrcompass.org/...] [--quality-receipt-dir DIR]",
    "                          [--feedback-receipt FILE] [--authorization-receipt FILE]",
    "                          [--dry-run] [--really-broadcast] [--really-merge] [--no-log-pr]",
    "",
    "Source file: /tmp/{issue}publish.md (output of scripts/publish.ts).",
    "The --really-* switches confirm execution intent; they do not grant authority.",
    "Every mutation requires matching byte-hashed receipts and exact identities in state.json.",
    "Signing and broadcast require exact merge and deployment confirmation.",
    "The log stage records the publication evidence and opens a PR for it; --no-log-pr",
    "writes the log without committing. The host durable outbox/reconciler owns",
    "milestone notification, retries, routing, and delivery readback.",
  ].join("\n");
}

async function runParse(issue: number, dryRun = false): Promise<void> {
  console.log(`[1/6] PARSE         issue=${issue}`);
  const meta = await parseIssue(issue, { outDir: OUT_DIR, persist: !dryRun });
  if (!dryRun) await notifyMilestone(issue, "parsed", [
    `Title "${meta.title}", TLDR ${meta.tldr_word_count} words, body ${meta.body.length} chars.`,
    "Banner verified against config/cover.json.",
  ]);
  console.log(`              title="${meta.title}"`);
  console.log(`              tldr=${meta.tldr_word_count} words ✓`);
  console.log(`              banner verified against config/cover.json ✓`);
  console.log(`              kind:1 source=opening newsletter section`);
  console.log(`              body length=${meta.body.length} chars`);
  console.log(`              tags: ${meta.tags.length === 0 ? "none" : meta.tags.join(", ")}`);
  console.log(dryRun ? "              [dry-run] parsed source is valid; no artifact written" : `              wrote out/${issue}/metadata.json`);
}

async function runSign(issue: number, dryRun: boolean): Promise<void> {
  console.log(`[2/6] SIGN          issue=${issue}`);
  const author = JSON.parse(await readFile(join(import.meta.dir, "config/author.json"), "utf8")) as { pubkey_hex: string };
  if (dryRun) {
    await assertSigningAuthorized(OUT_DIR, issue, 30023, author.pubkey_hex);
    console.log(`              [dry-run] signer identity and kind 30023 authorization are valid`);
    return;
  }
  await assertSigningAuthorized(OUT_DIR, issue, 30023, author.pubkey_hex);
  await signArticle(issue);
  await notifyMilestone(issue, "signed", ["kind:30023 article signed via the Amber bunker."]);
}

async function runAnnounceSign(issue: number, dryRun: boolean): Promise<void> {
  console.log(`[3/6] ANNOUNCE-SIGN issue=${issue}`);
  const author = JSON.parse(await readFile(join(import.meta.dir, "config/author.json"), "utf8")) as { pubkey_hex: string };
  if (dryRun) {
    await assertSigningAuthorized(OUT_DIR, issue, 1, author.pubkey_hex);
    console.log(`              [dry-run] signer identity and kind 1 authorization are valid`);
    return;
  }
  await assertSigningAuthorized(OUT_DIR, issue, 1, author.pubkey_hex);
  await signAnnouncement(issue);
  await notifyMilestone(issue, "announced", ["kind:1 announcement signed and pointing at the article naddr."]);
}

async function runBroadcast(issue: number, reallyBroadcast: boolean): Promise<void> {
  console.log(`[4/6] BROADCAST     issue=${issue}`);
  const result = await broadcastIssue(issue, reallyBroadcast);
  await notifyMilestone(issue, "broadcast", [
    `Article accepted by ${result.article_ok} relays, announcement by ${result.announcement_ok}.`,
    "Exact merged content and its attributable production deployment were verified before relay delivery.",
  ]);
}

async function runMerge(issue: number, reallyMerge: boolean, identity?: PullRequestIdentity): Promise<"prepared" | "confirmed"> {
  console.log(`[4/7] MERGE         issue=${issue}`);
  const result = await mergeIssue(issue, { reallyMerge, identity });
  if (result === "confirmed" && reallyMerge) await notifyMilestone(issue, "merged", [
    "Newsletter PR squash-merged into `main`; exact deployment confirmation is still required before broadcast.",
  ]);
  return result;
}

async function runDeploy(issue: number): Promise<void> {
  console.log(`[5/7] DEPLOY        issue=${issue}`);
  await verifyAndRecordDeployment(issue, { outDir: OUT_DIR });
  await notifyMilestone(issue, "deployed", ["Exact merge tree is live at the journal-pinned canonical route."]);
}

async function runLog(issue: number, logPr: boolean): Promise<void> {
  console.log(`[6/6] LOG           issue=${issue}`);
  const pr = await logIssue(issue, { compassDir: COMPASS_DIR, openPr: logPr });
  if (pr !== null) console.log(`              publication log PR #${pr}`);
}

async function main() {
  let args: Args;
  try {
    args = parseArgs(process.argv);
  } catch (e) {
    console.error(`error: ${(e as Error).message}\n\n${usage()}`);
    process.exit(1);
    return;
  }

  if (args.dryRun) console.log(`[dry-run] issue=${args.issue} stage=${args.stage}; executing read-only validation preview`);

  const lock = args.dryRun ? null : await IssueLock.acquire(args.issue, OUT_DIR);
  try {
    if ((args.stage === "all" || args.stage === "merge") && args.pageUrl) {
      if (!/^https:\/\/nostrcompass\.org\//.test(args.pageUrl)) throw new Error("Deployment page URL must be on canonical nostrcompass.org HTTPS origin");
      if (args.dryRun) console.log(`              [dry-run] canonical deployment route is valid: ${args.pageUrl}`);
      else await prepareDeployment(OUT_DIR, args.issue, args.pageUrl);
    }
    if (args.stage === "all" || args.stage === "parse") {
      await runParse(args.issue, args.dryRun);
      if (args.stage === "parse") return;
    }

    let authorizationPreview: AuthorizationReceipt | undefined;
    if (args.authorizationReceipt) {
      if (args.dryRun) authorizationPreview = await previewEditionAuthorization(OUT_DIR, args.issue, args.authorizationReceipt);
      else await recordEditionAuthorization(OUT_DIR, args.issue, args.authorizationReceipt);
    }
    let receiptState = await loadJournal(OUT_DIR, args.issue);
    if (!receiptState.source || sha256(await readFile(receiptState.source.path)) !== receiptState.source.sha256) throw new Error("Journal-pinned publication source is missing or changed");
    if (args.pageUrl && receiptState.deployment_intent && receiptState.deployment_intent.page_url !== args.pageUrl) throw new Error("Deployment route conflicts with the journal-pinned canonical route");
    if (args.qualityReceiptDir) {
      if (!receiptState.source) throw new Error("quality receipt ingestion requires a journaled publication source");
      const receiptPaths = Object.fromEntries(
        QUALITY_ROLES.map((role) => [role, join(args.qualityReceiptDir!, `${role}.json`)]),
      ) as Record<(typeof QUALITY_ROLES)[number], string>;
      if (args.dryRun) await previewCompositeQuality(OUT_DIR, args.issue, receiptState.source.path, receiptPaths);
      else {
        await recordCompositeQuality(OUT_DIR, args.issue, receiptState.source.path, receiptPaths);
        receiptState = await loadJournal(OUT_DIR, args.issue);
      }
    }
    if (args.feedbackReceipt) {
      if (!receiptState.source) throw new Error("feedback receipt ingestion requires a journaled publication source");
      if (args.dryRun) await previewFeedbackSnapshot(OUT_DIR, args.issue, receiptState.source.path, args.feedbackReceipt);
      else await recordFeedbackSnapshot(OUT_DIR, args.issue, receiptState.source.path, args.feedbackReceipt);
    }
    if (args.dryRun) {
      receiptState = await loadJournal(OUT_DIR, args.issue);
      for (const gate of ["quality", "feedback"] as const) {
        if ((gate === "quality" && args.qualityReceiptDir) || (gate === "feedback" && args.feedbackReceipt)) continue;
        const effect = receiptState.effects[gate];
        if (effect?.state !== "confirmed" || effect.event_id !== receiptState.pull_request?.head_sha || !effect.payload_path || !effect.payload_sha256 || sha256(await readFile(effect.payload_path)) !== effect.payload_sha256) throw new Error(`Read-only preview requires valid journaled ${gate} evidence or an explicit receipt input`);
      }
      if (!args.authorizationReceipt) {
        const effect = receiptState.effects.authorization;
        if (effect?.state !== "confirmed" || !effect.payload_path || !effect.payload_sha256 || sha256(await readFile(effect.payload_path)) !== effect.payload_sha256) throw new Error("Read-only preview requires valid journaled authorization evidence or an explicit receipt input");
        authorizationPreview = await previewJournaledEditionAuthorization(OUT_DIR, args.issue);
      }
    }

    if (args.stage === "all" || args.stage === "merge") {
      if (args.dryRun) {
        const preview = await previewMergeIssue(args.issue, { outDir: OUT_DIR, identity: args.prIdentity });
        if (!authorizationPreview || authorizationPreview.prospective_tree_sha !== preview.prospective_tree_sha) throw new Error("Read-only preview authorization does not match the exact prospective merge tree");
        if (new Date() < new Date(authorizationPreview.not_before)) throw new Error("Read-only preview is before the scoped Wednesday publication boundary");
        console.log(`[dry-run] exact PR #${preview.number} ${preview.state}; head/base/prospective tree and server currentness gate verified`);
        if (preview.state === "open") {
          if (args.stage === "all") console.log("[dry-run] merge would run next; deployment, signing, broadcast, and log remain downstream plans");
          return;
        }
      } else if (args.stage === "all" && !args.reallyMerge) {
        console.log("");
        console.log("Stopping before merge: pass --really-merge to merge the exact pinned GitHub PR.");
        return;
      } else {
        await runMerge(args.issue, args.reallyMerge, args.prIdentity);
      }
      if (args.stage === "merge") return;
      const state = await loadJournal(OUT_DIR, args.issue);
      if (state.effects.deploy?.state !== "confirmed") {
        if (args.dryRun) {
          const evidence = await previewDeployment(args.issue, { outDir: OUT_DIR });
          console.log(`[dry-run] exact deployment is externally verifiable at ${evidence.page_url}; journal reconciliation would run next`);
          return;
        }
        console.log("Merge is confirmed; stopping cleanly until exact Pages and served-content verification completes.");
        console.log(`Resume with: compass-publish ${args.issue} --stage deploy`);
        return;
      }
      if (args.dryRun) {
        const evidence = await previewDeployment(args.issue, { outDir: OUT_DIR });
        console.log(`[dry-run] deployment run ${evidence.workflow_run_id}, merge tree, and served edition content were reverified`);
      }
    }

    if (args.stage === "deploy") {
      if (args.dryRun) {
        const evidence = await previewDeployment(args.issue, { outDir: OUT_DIR });
        console.log(`[dry-run] deployment run ${evidence.workflow_run_id}, merge tree, and served edition content are valid`);
      } else await runDeploy(args.issue);
      return;
    }

    if (args.stage === "all" || args.stage === "sign") {
      await runSign(args.issue, args.dryRun);
      if (args.stage === "sign") return;
    }

    if (args.stage === "all" || args.stage === "announce-sign") {
      await runAnnounceSign(args.issue, args.dryRun);
      if (args.stage === "announce-sign") return;
    }

    if (args.stage === "all" || args.stage === "broadcast") {
      if (args.dryRun) {
        const preview = await previewBroadcastIssue(args.issue, { outDir: OUT_DIR });
        console.log(`[dry-run] signed payloads and relay floor ${preview.relay_floor}/${preview.durable_relays} are valid; current readbacks article=${preview.article_readbacks}, announcement=${preview.announcement_readbacks}`);
      } else if (args.stage === "all" && !args.reallyBroadcast) {
        console.log("");
        console.log("Stopping before broadcast: pass --really-broadcast after exact deployment confirmation.");
        return;
      } else {
        await runBroadcast(args.issue, args.reallyBroadcast);
      }
      if (args.stage === "broadcast") return;
    }

    if (args.stage === "all" || args.stage === "log") {
      if (args.dryRun) {
        const state = await loadJournal(OUT_DIR, args.issue);
        if (state.effects.article?.state !== "confirmed" || state.effects.announcement?.state !== "confirmed") throw new Error("Publication log preview requires both exact Nostr events to be confirmed");
        console.log("[dry-run] publication evidence is complete; log projection would be the only remaining write");
      }
      else await runLog(args.issue, args.logPr);
    }

    if (args.stage === "all") {
      console.log("");
      console.log("✓ pipeline complete");
    }
  } finally {
    if (!args.dryRun) await closeBunker();
    if (lock) await lock.release();
  }
}

main().catch(async (e) => {
  const message = (e as Error).message;
  console.error(`error: ${message}`);
  // Record the halt hook without sending directly. The host durable outbox
  // observes workflow state and owns user-facing delivery and retries.
  const issue = Number(process.argv.find((a) => /^\d+$/.test(a)));
  if (!process.argv.includes("--dry-run") && Number.isFinite(issue) && issue > 0) {
    await notifyMilestone(issue, "failed", [message.split("\n")[0]]);
  }
  process.exit(1);
});
