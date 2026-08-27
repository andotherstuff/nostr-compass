import { describe, expect, test } from "bun:test";
import { prLink, renderCommand, renderMessage, runLink } from "./notify.ts";

describe("forge references", () => {
  // MARMOT_MESSAGE_MARKDOWN.md § "Linked git-forge refs": every PR number in
  // user-facing text must be a link, never a bare `PR #N`.
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

  test("names the repeated unit in the heading so per-language steps are distinguishable", () => {
    expect(renderMessage(37, "translated-language", ["committed"], "German")).toStartWith(
      "**Nostr Compass issue 37 — Language translated (German)**",
    );
  });

  test("drops blank lines so a missing value cannot emit an empty bullet", () => {
    expect(renderMessage(37, "merged", ["merged", "", "   "])).toBe(
      "**Nostr Compass issue 37 — Newsletter PR merged**\n- merged",
    );
  });

  test("emits a bare heading when there is nothing to report", () => {
    expect(renderMessage(37, "deployed", [])).toBe("**Nostr Compass issue 37 — Website deployed**");
  });

  test("drops the merged label's old wording in favour of the explicit one", () => {
    expect(renderMessage(37, "merged", [])).toContain("Newsletter PR merged");
  });

  test("labels each finished step distinctly", () => {
    expect(renderMessage(37, "log-pr-opened", [])).toContain("Publication log PR opened");
    expect(renderMessage(37, "outreach-sent", [])).toContain("Outreach DMs sent");
    expect(renderMessage(37, "translated", [])).toContain("Translations merged");
  });

  test("labels a halt distinctly from a success", () => {
    expect(renderMessage(37, "failed", ["broadcast rejected by every relay"])).toContain(
      "Publish halted",
    );
  });
});

describe("delivery command", () => {
  // The transport is configured, not compiled in, so the repo carries no
  // host-specific messaging command. Placeholders are substituted positionally
  // so a body containing spaces or newlines stays one argv entry.
  test("substitutes target and body without splitting either", () => {
    const argv = renderCommand(
      ["msg", "send", "--to", "{target}", "--quiet", "{body}"],
      "group:Compass Newsletter",
      "Issue 38 broadcast\naccepted by 5 relays",
    );
    expect(argv).toEqual([
      "msg",
      "send",
      "--to",
      "group:Compass Newsletter",
      "--quiet",
      "Issue 38 broadcast\naccepted by 5 relays",
    ]);
  });

  test("leaves an argv with no placeholders untouched", () => {
    expect(renderCommand(["notify-hook"], "t", "b")).toEqual(["notify-hook"]);
  });
});
