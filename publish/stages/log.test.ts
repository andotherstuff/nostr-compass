import { describe, expect, test } from "bun:test";
import { gateStatus, isBlaster, matchesIssueTitle, renderLog, resolveIssueDate, selectDeployRun } from "./log.ts";
import { mkdir, mkdtemp, rm, writeFile } from "node:fs/promises";
import { tmpdir } from "node:os";
import { join } from "node:path";
import { spawnSync } from "node:child_process";

const run = (cmd: string, args: string[]) =>
  Promise.resolve(spawnSync(cmd, args, { encoding: "utf8" }));


const LEDGER = {
  issue: 37,
  event_id: "a".repeat(64),
  announcement_id: "b".repeat(64),
  first_published_at: 1787763698,
  banner_url: "https://image.nostr.build/x.png",
  relays_ok: [],
  relays_fail: [],
};

function base(overrides: Partial<Parameters<typeof renderLog>[0]> = {}) {
  const configured = ["wss://a.example", "wss://b.example", "wss://sendit.nosflare.com"];
  const ok = (relay: string) => ({ relay, ok: true, ms: 10 });
  return renderLog({
    issue: 37,
    date: "2026-08-26",
    title: "Nostr Compass #37",
    pr: { number: 139, mergeCommit: "1acecf4ffffffffffffffffffffffffffffffffff", mergedAt: "2026-08-26T16:57:47Z" },
    prerequisites: ["- Pre-publication refresh (`prepublish_refresh_2026-08-26.md`): ends in GATE: PASS"],
    deploy: { id: "32991457973", conclusion: "success" },
    page: "HTTP 200 and contained `Nostr Compass #37`",
    ledger: LEDGER,
    configured,
    receipts: { article: configured.map(ok), announcement: configured.map(ok) },
    readback: [
      { relay: "wss://a.example", article: true, announcement: true },
      { relay: "wss://b.example", article: true, announcement: true },
    ],
    naddr: "naddr1test",
    nevent: "nevent1test",
    announcementCreatedAt: 1787763754,
    ...overrides,
  });
}

describe("matchesIssueTitle", () => {
  test("matches the exact issue", () => {
    expect(matchesIssueTitle('title: "Nostr Compass #37"\ndate: 2026-08-26', 37)).toBe(true);
  });

  test("does not match a longer number that starts with the issue", () => {
    expect(matchesIssueTitle('title: "Nostr Compass #37"', 3)).toBe(false);
    expect(matchesIssueTitle('title: "Nostr Compass #3"', 37)).toBe(false);
  });

  test("tolerates an unquoted title", () => {
    expect(matchesIssueTitle("title: Nostr Compass #12", 12)).toBe(true);
  });

  test("ignores the issue number appearing in body prose", () => {
    expect(matchesIssueTitle("description: covers Nostr Compass #37 topics", 37)).toBe(false);
  });
});

describe("isBlaster", () => {
  test("identifies the write-only NIP-66 blaster", () => {
    expect(isBlaster("wss://sendit.nosflare.com")).toBe(true);
    expect(isBlaster("wss://nos.lol")).toBe(false);
  });
});

describe("renderLog", () => {
  test("names the real relay config, not the path the skill doc used to claim", () => {
    const out = base();
    expect(out).toContain("publish/config/relays.json");
    expect(out).not.toContain("compass_relays.txt");
  });

  test("passes the gate when both events broadcast and read back", () => {
    expect(base().trimEnd().split("\n").filter((l) => l.startsWith("GATE:")).at(-1)).toStartWith(
      "GATE: PASS",
    );
  });

  test("excludes the blaster from the durable readback count", () => {
    // 3 configured, one of which is the blaster, so 2 durable relays.
    expect(base()).toContain("the 2 durable configured relays");
  });

  // The prerequisites block quotes upstream "GATE: PASS" lines verbatim, so the
  // verdict must be read off the final gate line, not searched for anywhere.
  const verdict = (log: string) =>
    log.trimEnd().split("\n").filter((l) => l.startsWith("GATE:")).at(-1) ?? "";

  test("fails the gate when nothing reads back, even though every relay accepted", () => {
    expect(verdict(base({ readback: [] }))).toStartWith("GATE: FAIL");
  });

  test("links the draft PR by number", () => {
    expect(base()).toContain("/pull/139");
    expect(base()).not.toContain("[object Object]");
  });

  test("reports a relay that accepted but cannot serve the announcement back", () => {
    const out = base({
      readback: [
        { relay: "wss://a.example", article: true, announcement: true },
        { relay: "wss://b.example", article: true, announcement: false },
      ],
    });
    expect(out).toContain("only the article returned by `wss://b.example`");
    expect(out).toContain("GATE: PASS");
  });

  test("records a rejection with its reason instead of rounding it up to success", () => {
    const configured = ["wss://a.example", "wss://b.example"];
    const out = base({
      configured,
      receipts: {
        article: [
          { relay: "wss://a.example", ok: true, ms: 5 },
          { relay: "wss://b.example", ok: false, reason: "Expected 101 status code", ms: 5 },
        ],
        announcement: [
          { relay: "wss://a.example", ok: true, ms: 5 },
          { relay: "wss://b.example", ok: false, reason: "Expected 101 status code", ms: 5 },
        ],
      },
      readback: [{ relay: "wss://a.example", article: true, announcement: true }],
    });
    expect(out).toContain("article, `wss://b.example`: Expected 101 status code");
    expect(out).toContain("The article was accepted by 1 and the announcement by 1.");
  });

  test("says so plainly when no merged PR or deploy could be read", () => {
    const out = base({ pr: null, deploy: null });
    expect(out).toContain("No merged PR was found");
    expect(out).toContain("deploy status could not be read");
  });

  test("names the merge commit and time so the deploy can be tied to this issue", () => {
    const out = base();
    expect(out).toContain("as commit `1acecf4`");
    expect(out).toContain("at `2026-08-26T16:57:47Z`");
  });

  test("records the d tag, announcement time, and announcement link", () => {
    const out = base();
    expect(out).toContain("`d` tag `newsletter-37`");
    expect(out).toContain("Created at `1787763754`");
    expect(out).toContain("https://njump.me/nevent1test");
  });

  test("omits the announcement timestamp rather than inventing one", () => {
    expect(base({ announcementCreatedAt: null })).not.toContain("Created at");
  });

  test("carries the prerequisite gate lines through verbatim", () => {
    expect(base()).toContain("ends in GATE: PASS");
  });

  test("flags a deployed page that does not carry the issue title", () => {
    const out = base({ page: "HTTP 200 but did NOT contain the issue title" });
    expect(out).toContain("did NOT contain the issue title");
  });
});

describe("selectDeployRun", () => {
  const pages = (databaseId: number, event: string, conclusion = "success") => ({
    databaseId,
    conclusion,
    name: "Deploy Hugo site to Pages",
    event,
  });

  test("credits the push-triggered deploy, not a manual rerun that sorts first", () => {
    expect(
      selectDeployRun([pages(32991457973, "workflow_dispatch"), pages(32992017015, "push")])?.databaseId,
    ).toBe(32992017015);
  });

  test("prefers a Pages workflow over an unrelated workflow on the same commit", () => {
    expect(
      selectDeployRun([
        { databaseId: 1, conclusion: "success", name: "CodeQL", event: "push" },
        pages(2, "push"),
      ])?.databaseId,
    ).toBe(2);
  });

  test("falls back to the only run when none was push-triggered", () => {
    expect(selectDeployRun([pages(7, "workflow_dispatch")])?.databaseId).toBe(7);
  });

  test("returns null when the commit has no runs", () => {
    expect(selectDeployRun([])).toBeNull();
  });
});

describe("naddr hint relays", () => {
  const configured = ["wss://a.example", "wss://b.example", "wss://sendit.nosflare.com"];
  test("warns when a rejecting relay is also an naddr hint", () => {
    const out = renderLog({
      issue: 37,
      date: "2026-08-26",
      title: "Nostr Compass #37",
      pr: { number: 139, mergeCommit: "1acecf4", mergedAt: "2026-08-26T16:57:47Z" },
      prerequisites: [],
      deploy: { id: "1", conclusion: "success" },
      page: "HTTP 200",
      ledger: LEDGER,
      configured,
      receipts: {
        article: [
          { relay: "wss://a.example", ok: true, ms: 1 },
          { relay: "wss://b.example", ok: false, reason: "Expected 101 status code", ms: 1 },
        ],
        announcement: [
          { relay: "wss://a.example", ok: true, ms: 1 },
          { relay: "wss://b.example", ok: false, reason: "Expected 101 status code", ms: 1 },
        ],
      },
      readback: [{ relay: "wss://a.example", article: true, announcement: true }],
      naddr: "naddr1test",
      nevent: "nevent1test",
      announcementCreatedAt: 1787763754,
    });
    expect(out).toContain("will not resolve there until the event is rebroadcast");
    expect(out).toContain("`wss://b.example`");
  });
});

describe("replacement disclosure", () => {
  // A NIP-23 replacement keeps the d tag and published_at but gets a new event
  // id. #37 was rebroadcast on 2026-08-27 to carry the added Nail section.
  const edited = { ...LEDGER, last_edited_at: LEDGER.first_published_at + 52072 };

  test("says the event was replaced when last_edited_at differs", () => {
    const out = base({ ledger: edited });
    expect(out).toContain("Replaced after first publication");
    expect(out).toContain("same `d` tag");
  });

  test("stays silent when the event was never edited", () => {
    expect(base()).not.toContain("Replaced after first publication");
  });

  test("stays silent when last_edited_at equals first_published_at", () => {
    const same = { ...LEDGER, last_edited_at: LEDGER.first_published_at };
    expect(base({ ledger: same })).not.toContain("Replaced after first publication");
  });
});

describe("resolveIssueDate falls back to origin/main", () => {
  // The shared checkout is not kept current by the weekly automation: on
  // 2026-08-27 it was 27 commits behind and had neither #36 nor #37 on disk.
  // The log stage runs after merge, so origin/main always has the issue.
  const fixture = async () => {
    const dir = await mkdtemp(join(tmpdir(), "compass-log-"));
    const git = (...args: string[]) => run("git", ["-C", dir, ...args]);
    await mkdir(join(dir, "content/en/newsletters"), { recursive: true });
    await git("init", "-q", "-b", "main");
    await git("config", "user.email", "t@t");
    await git("config", "user.name", "t");
    await writeFile(join(dir, "content/en/newsletters/2026-09-02-newsletter.md"), 'title: "Nostr Compass #38"\n');
    await git("add", "-A");
    await git("commit", "-qm", "issue 38");
    // Publish the commit as origin/main, then remove the file from the tree so
    // only the ref carries it — exactly the stale-checkout shape.
    await git("update-ref", "refs/remotes/origin/main", "HEAD");
    await rm(join(dir, "content/en/newsletters/2026-09-02-newsletter.md"));
    return dir;
  };

  test("resolves an issue present only on origin/main", async () => {
    const dir = await fixture();
    expect(await resolveIssueDate(dir, 38)).toBe("2026-09-02");
    await rm(dir, { recursive: true, force: true });
  });

  test("still throws when neither the tree nor origin/main has the issue", async () => {
    const dir = await fixture();
    await expect(resolveIssueDate(dir, 99)).rejects.toThrow(/Nostr Compass #99/);
    await rm(dir, { recursive: true, force: true });
  });
});

describe("gateStatus reads the run's worktree", () => {
  test("finds gates outside compassDir and says where", async () => {
    const root = await mkdtemp(join(tmpdir(), "compass-gate-"));
    const compassDir = join(root, "compass");
    const workspace = join(root, "workspace");
    await mkdir(join(compassDir, "data/newsletter_workspace"), { recursive: true });
    await mkdir(join(workspace, "data/newsletter_workspace"), { recursive: true });
    await writeFile(
      join(workspace, "data/newsletter_workspace/prepublish_refresh_2026-09-02.md"),
      "evidence\n\nGATE: PASS\n",
    );
    process.env.COMPASS_WORKSPACE_DIR = workspace;
    const lines = await gateStatus(compassDir, "2026-09-02");
    delete process.env.COMPASS_WORKSPACE_DIR;

    expect(lines[0]).toContain("ends in GATE: PASS");
    expect(lines[0]).toContain(workspace);
    // A gate that exists nowhere is still reported missing, not assumed passed.
    expect(lines[1]).toContain("missing");
    await rm(root, { recursive: true, force: true });
  });
});
