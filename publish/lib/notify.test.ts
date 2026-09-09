import { readFile } from "node:fs/promises";
import { describe, expect, test } from "bun:test";
import { notifyMilestone, prLink, renderMessage, runLink } from "./notify.ts";

describe("forge references", () => {
  test("renders a PR as a full link", () => {
    expect(prLink(139)).toBe("[#139](https://github.com/andotherstuff/nostr-compass/pull/139)");
  });

  test("renders a workflow run as a full link", () => {
    expect(runLink(32991457973)).toBe(
      "[run 32991457973](https://github.com/andotherstuff/nostr-compass/actions/runs/32991457973)",
    );
  });
});

describe("renderMessage", () => {
  test("uses compact bullets rather than a pipe table", () => {
    const out = renderMessage(37, "broadcast", ["11 of 12 relays accepted", "snort.social unreachable"]);
    expect(out).toBe(
      "**Nostr Compass issue 37 — Broadcast to relays**\n- 11 of 12 relays accepted\n- snort.social unreachable",
    );
    expect(out).not.toContain("|");
  });

  test("names repeated units in the heading", () => {
    expect(renderMessage(37, "translated-language", ["committed"], "German")).toStartWith(
      "**Nostr Compass issue 37 — Language translated (German)**",
    );
  });

  test("drops blank lines", () => {
    expect(renderMessage(37, "merged", ["merged", "", "   "])).toBe(
      "**Nostr Compass issue 37 — Newsletter PR merged**\n- merged",
    );
  });

  test("emits a bare heading when there is nothing to report", () => {
    expect(renderMessage(37, "deployed", [])).toBe("**Nostr Compass issue 37 — Website deployed**");
  });

  test("labels finished steps and failures distinctly", () => {
    expect(renderMessage(37, "log-pr-opened", [])).toContain("Publication log PR opened");
    expect(renderMessage(37, "outreach-sent", [])).toContain("Outreach DMs sent");
    expect(renderMessage(37, "translated", [])).toContain("Translations merged");
    expect(renderMessage(37, "failed", [])).toContain("Publish halted");
  });
});

describe("notification ownership", () => {
  test("repository milestone hook never sends directly", async () => {
    const previousTarget = process.env.COMPASS_NOTIFY_TARGET;
    const previousCommand = process.env.COMPASS_NOTIFY_COMMAND;
    process.env.COMPASS_NOTIFY_TARGET = "marmot:must-not-send";
    process.env.COMPASS_NOTIFY_COMMAND = JSON.stringify([process.execPath, "-e", "process.exit(99)"]);
    try {
      expect(await notifyMilestone(38, "merged", ["must remain host-owned"])).toBe(false);
    } finally {
      if (previousTarget === undefined) delete process.env.COMPASS_NOTIFY_TARGET;
      else process.env.COMPASS_NOTIFY_TARGET = previousTarget;
      if (previousCommand === undefined) delete process.env.COMPASS_NOTIFY_COMMAND;
      else process.env.COMPASS_NOTIFY_COMMAND = previousCommand;
    }
  });

  test("notification module contains no direct transport or runtime notification plumbing", async () => {
    const source = await readFile(new URL("./notify.ts", import.meta.url), "utf8");
    expect(source).not.toContain("node:child_process");
    expect(source).not.toContain("spawn(");
    expect(source).not.toContain("config/notify.json");
    expect(source).not.toContain("COMPASS_NOTIFY");
  });
});
