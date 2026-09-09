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
import { broadcastIssue } from "./stages/broadcast.ts";
import { mergeIssue, type PullRequestIdentity } from "./stages/merge.ts";
import { verifyAndRecordDeployment } from "./stages/deploy.ts";
import { logIssue } from "./stages/log.ts";
import { IssueLock, validateNumber } from "./lib/safety.ts";
import { closeBunker } from "./lib/bunker.ts";
import { notifyMilestone, prLink } from "./lib/notify.ts";
import { loadJournal, prepareDeployment } from "./lib/journal.ts";
import { assertSigningAuthorized, recordEditionAuthorization } from "./lib/authorization.ts";
import { recordCompositeQuality, recordFeedbackSnapshot, QUALITY_ROLES } from "./lib/gates.ts";

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
  const meta = await parseIssue(issue);
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
  console.log(`              wrote out/${issue}/metadata.json`);
}

async function runSign(issue: number, dryRun: boolean): Promise<void> {
  console.log(`[2/6] SIGN          issue=${issue}`);
  if (dryRun) {
    console.log(`              [dry-run] would request bunker signature for kind 30023`);
    return;
  }
  const author = JSON.parse(await readFile(join(import.meta.dir, "config/author.json"), "utf8")) as { pubkey_hex: string };
  await assertSigningAuthorized(OUT_DIR, issue, 30023, author.pubkey_hex);
  await signArticle(issue);
  await notifyMilestone(issue, "signed", ["kind:30023 article signed via the Amber bunker."]);
}

async function runAnnounceSign(issue: number, dryRun: boolean): Promise<void> {
  console.log(`[3/6] ANNOUNCE-SIGN issue=${issue}`);
  if (dryRun) {
    console.log(`              [dry-run] would request bunker signature for kind:1`);
    return;
  }
  const author = JSON.parse(await readFile(join(import.meta.dir, "config/author.json"), "utf8")) as { pubkey_hex: string };
  await assertSigningAuthorized(OUT_DIR, issue, 1, author.pubkey_hex);
  await signAnnouncement(issue);
  await notifyMilestone(issue, "announced", ["kind:1 announcement signed and pointing at the article naddr."]);
}

async function runBroadcast(issue: number, reallyBroadcast: boolean): Promise<void> {
  console.log(`[4/6] BROADCAST     issue=${issue}`);
  const result = await broadcastIssue(issue, reallyBroadcast);
  await notifyMilestone(issue, "broadcast", [
    `Article accepted by ${result.article_ok} relays, announcement by ${result.announcement_ok}.`,
    "Website does not update until the merge stage runs.",
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

  if (args.dryRun) {
    console.log(`[dry-run] issue=${args.issue} stage=${args.stage}; zero mutation preview`);
    console.log("[dry-run] would validate local source, signatures, exact PR/head/base, deployment evidence, and relay floor");
    return;
  }

  const lock = await IssueLock.acquire(args.issue, OUT_DIR);
  try {
    if ((args.stage === "all" || args.stage === "merge") && args.pageUrl) await prepareDeployment(OUT_DIR, args.issue, args.pageUrl);
    if (args.stage === "all" || args.stage === "parse") {
      await runParse(args.issue);
      if (args.stage === "parse") return;
    }

    if (args.authorizationReceipt) await recordEditionAuthorization(OUT_DIR, args.issue, args.authorizationReceipt);
    let receiptState = await loadJournal(OUT_DIR, args.issue);
    if (args.qualityReceiptDir) {
      if (!receiptState.source) throw new Error("quality receipt ingestion requires a journaled publication source");
      const receiptPaths = Object.fromEntries(
        QUALITY_ROLES.map((role) => [role, join(args.qualityReceiptDir!, `${role}.json`)]),
      ) as Record<(typeof QUALITY_ROLES)[number], string>;
      await recordCompositeQuality(OUT_DIR, args.issue, receiptState.source.path, receiptPaths);
      receiptState = await loadJournal(OUT_DIR, args.issue);
    }
    if (args.feedbackReceipt) {
      if (!receiptState.source) throw new Error("feedback receipt ingestion requires a journaled publication source");
      await recordFeedbackSnapshot(OUT_DIR, args.issue, receiptState.source.path, args.feedbackReceipt);
    }

    if (args.stage === "all" || args.stage === "merge") {
      if (args.dryRun) {
        console.log("[dry-run] would reconcile/merge the exact pinned pull request");
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
        console.log("Merge is confirmed; stopping cleanly until exact Pages and served-content verification completes.");
        console.log(`Resume with: compass-publish ${args.issue} --stage deploy`);
        return;
      }
    }

    if (args.stage === "deploy") {
      await runDeploy(args.issue);
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
        console.log("[dry-run] would broadcast the exact signed payloads");
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
      if (args.dryRun) console.log("[dry-run] would generate evidence and create/update its pull request");
      else await runLog(args.issue, args.logPr);
    }

    if (args.stage === "all") {
      console.log("");
      console.log("✓ pipeline complete");
    }
  } finally {
    await closeBunker();
    await lock.release();
  }
}

main().catch(async (e) => {
  const message = (e as Error).message;
  console.error(`error: ${message}`);
  // Surface the halt on the same channel as the successes. A publish that dies
  // silently after broadcast is how #37 ended up on Nostr with no log.
  const issue = Number(process.argv.find((a) => /^\d+$/.test(a)));
  if (!process.argv.includes("--dry-run") && Number.isFinite(issue) && issue > 0) {
    await notifyMilestone(issue, "failed", [message.split("\n")[0]]);
  }
  process.exit(1);
});
