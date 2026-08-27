#!/usr/bin/env bun
// Compass newsletter → Nostr publishing pipeline.
//
// MANUAL INVOCATION ONLY. This script runs only when COMPASS_PUBLISH_INVOCATION
// is set to "manual" in the invoking shell. It must not be triggered from
// cron, file watchers, hooks, slash-commands, or scheduled tasks.
//
// Broadcast is gated: stage 4 refuses to run without the explicit
// --really-broadcast flag. Stage 5 merges the newsletter PR so Hugo
// deploys; it refuses to run unless broadcast recorded at least one
// successful relay receipt in published.json.

if (process.env.COMPASS_PUBLISH_INVOCATION !== "manual") {
  console.error(
    [
      "Refusing to run.",
      "",
      "COMPASS_PUBLISH_INVOCATION must be set to 'manual' in the invoking shell.",
      "This pipeline runs only on explicit operator instruction.",
      "",
      "Recommended alias:",
      "  alias compass-publish='COMPASS_PUBLISH_INVOCATION=manual bun ~/compass/publish/publish.ts'",
    ].join("\n"),
  );
  process.exit(2);
}

import { join } from "node:path";
import { parseIssue } from "./stages/parse.ts";
import { signArticle } from "./stages/sign.ts";
import { signAnnouncement } from "./stages/announce.ts";
import { broadcastIssue } from "./stages/broadcast.ts";
import { mergeIssue } from "./stages/merge.ts";
import { logIssue } from "./stages/log.ts";
import { IssueLock, validateNumber } from "./lib/safety.ts";
import { closeBunker } from "./lib/bunker.ts";
import { notifyMilestone, prLink } from "./lib/notify.ts";

const OUT_DIR = join(import.meta.dir, "out");

type Stage = "parse" | "sign" | "announce-sign" | "broadcast" | "merge" | "log" | "all";

const COMPASS_DIR = process.env.COMPASS_DIR || join(import.meta.dir, "..");

type Args = {
  issue: number;
  stage: Stage;
  dryRun: boolean;
  reallyBroadcast: boolean;
  reallyMerge: boolean;
  logPr: boolean;
};

function parseArgs(argv: string[]): Args {
  const positional: string[] = [];
  let stage: Stage = "all";
  let dryRun = false;
  let reallyBroadcast = false;
  let reallyMerge = false;
  let logPr = true;

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

  return { issue, stage, dryRun, reallyBroadcast, reallyMerge, logPr };
}

function usage(): string {
  return [
    "Usage:",
    "  compass-publish <issue> [--stage parse|sign|announce-sign|broadcast|merge|log|all]",
    "                          [--dry-run] [--really-broadcast] [--really-merge] [--no-log-pr]",
    "",
    "Source file: /tmp/{issue}publish.md (output of ~/compass/scripts/publish.ts).",
    "Broadcast is gated by --really-broadcast.",
    "Merge is gated by --really-merge AND a successful broadcast ledger entry.",
    "In --stage all, pass both flags to do the full publish + GitHub merge in one shot.",
    "The log stage records the publication evidence and opens a PR for it; --no-log-pr",
    "writes the log without committing. Milestones post to the target configured",
    "in config/notify.json; COMPASS_NOTIFY=0 silences them.",
  ].join("\n");
}

async function runParse(issue: number): Promise<void> {
  console.log(`[1/6] PARSE         issue=${issue}`);
  const meta = await parseIssue(issue);
  await notifyMilestone(issue, "parsed", [
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
  await signArticle(issue);
  await notifyMilestone(issue, "signed", ["kind:30023 article signed via the Amber bunker."]);
}

async function runAnnounceSign(issue: number, dryRun: boolean): Promise<void> {
  console.log(`[3/6] ANNOUNCE-SIGN issue=${issue}`);
  if (dryRun) {
    console.log(`              [dry-run] would request bunker signature for kind:1`);
    return;
  }
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

async function runMerge(issue: number, reallyMerge: boolean): Promise<void> {
  console.log(`[5/6] MERGE         issue=${issue}`);
  await mergeIssue(issue, { reallyMerge });
  await notifyMilestone(issue, "merged", [
    "Newsletter PR squash-merged into `main`; the Pages deploy is running.",
  ]);
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

  const lock = await IssueLock.acquire(args.issue, OUT_DIR);
  try {
    if (args.stage === "all" || args.stage === "parse") {
      await runParse(args.issue);
      if (args.stage === "parse") return;
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
      if (args.stage === "all" && !args.reallyBroadcast) {
        console.log("");
        console.log("Stopping before broadcast: pass --really-broadcast to send to relays.");
        console.log("Signed events are on disk and ready to broadcast when you are.");
        return;
      }
      await runBroadcast(args.issue, args.reallyBroadcast);
      if (args.stage === "broadcast") return;
    }

    if (args.stage === "all" || args.stage === "merge") {
      if (args.stage === "all" && !args.reallyMerge) {
        console.log("");
        console.log("Stopping before merge: pass --really-merge to merge the GitHub PR.");
        console.log("The newsletter is on Nostr but the website will not update until merged.");
        return;
      }
      await runMerge(args.issue, args.reallyMerge);
      if (args.stage === "merge") return;
    }

    if (args.stage === "all" || args.stage === "log") {
      await runLog(args.issue, args.logPr);
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
  if (Number.isFinite(issue) && issue > 0) {
    await notifyMilestone(issue, "failed", [message.split("\n")[0]]);
  }
  process.exit(1);
});
