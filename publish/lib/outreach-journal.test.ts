import { describe, expect, setDefaultTimeout, test } from "bun:test";
setDefaultTimeout(20_000);
import { mkdtemp } from "node:fs/promises";
import { join } from "node:path";
import { tmpdir } from "node:os";
import { finishRecipient, prepareCampaign, recordRecipientReadback, recordRecipientReceipt, reuseOrBuildRecipient } from "./outreach-journal.ts";
import { loadJournal } from "./journal.ts";

const signed = (id = "a".repeat(64)) => ({ id, pubkey: "b".repeat(64), sig: "c".repeat(128), kind: 1059, created_at: 1, tags: [], content: "cipher" });

describe("outreach recipient replay", () => {
  test("campaign identity reuses confirmed exact signed payload", async () => {
    const out = await mkdtemp(join(tmpdir(), "compass-outreach-")); const npub = "npub1recipient"; let builds = 0;
    await prepareCampaign({ outDir: out, issue: 9, identity: "review", message: "review url", recipients: [{ npub, names: ["A"] }] });
    const build = async () => { builds++; return signed(); };
    const first = await reuseOrBuildRecipient({ outDir: out, issue: 9, campaign: "review", npub, intent: { protocol: "nip17", relays: ["r"] }, build });
    await recordRecipientReadback(out, 9, "review", npub, "r", true);
    await finishRecipient(out, 9, "review", npub, "confirmed");
    const second = await reuseOrBuildRecipient({ outDir: out, issue: 9, campaign: "review", npub, intent: { protocol: "nip17", relays: ["r"] }, build });
    expect(second).toEqual(first); expect(builds).toBe(1);
    await expect(prepareCampaign({ outDir: out, issue: 9, identity: "review", message: "changed", recipients: [{ npub, names: ["A"] }] })).rejects.toThrow("campaign intent changed");
  });

  test("fails closed when the immutable recipient manifest expands", async () => {
    const out = await mkdtemp(join(tmpdir(), "compass-outreach-expand-"));
    await prepareCampaign({ outDir: out, issue: 10, identity: "review", message: "same", recipients: [{ npub: "npub1old", names: ["Old"] }] });
    await expect(prepareCampaign({ outDir: out, issue: 10, identity: "review", message: "same", recipients: [{ npub: "npub1old", names: ["Old"] }, { npub: "npub1new", names: ["New"] }] })).rejects.toThrow("campaign intent changed");
  });

  test("keeps campaign identities independent", async () => {
    const out = await mkdtemp(join(tmpdir(), "compass-outreach-types-")); const recipients = [{ npub: "npub1person", names: ["Person"] }];
    await prepareCampaign({ outDir: out, issue: 11, identity: "review", message: "initial", recipients });
    await prepareCampaign({ outDir: out, issue: 11, identity: "podcast-invitation", message: "podcast", recipients });
    expect((await loadJournal(out, 11)).outreach["podcast-invitation"].identity).toBe("podcast-invitation");
  });

  test("journals every terminal recipient disposition and separates acceptance from readback", async () => {
    const out = await mkdtemp(join(tmpdir(), "compass-outreach-terminal-")); const send = "npub1send";
    await prepareCampaign({ outDir: out, issue: 12, identity: "review", message: "same", binding: { obligation_sha256: "a".repeat(64) }, recipients: [
      { npub: send, names: ["Sent"] },
      { npub: "npub1nodm", names: ["No DM"], disposition: "no_dm", reason: "policy" },
      { key: "identity:unknown", names: ["Unknown"], disposition: "unknown_identity", reason: "unresolved" },
      { key: "identity:missing", names: ["Missing"], disposition: "missing_identity", reason: "missing" },
      { npub: "npub1noinbox", names: ["No inbox"] },
      { npub: "npub1failed", names: ["Failed"] },
    ] });
    await reuseOrBuildRecipient({ outDir: out, issue: 12, campaign: "review", npub: send, intent: { relays: ["r1", "r2"] }, build: async () => signed() });
    await recordRecipientReceipt(out, 12, "review", send, { relay: "r1", ok: true, ms: 1 });
    await recordRecipientReadback(out, 12, "review", send, "r2", true);
    await finishRecipient(out, 12, "review", send, "confirmed");
    await finishRecipient(out, 12, "review", "npub1noinbox", "failed", "no kind-10050 inbox", "no_nip17_inbox");
    await finishRecipient(out, 12, "review", "npub1failed", "failed", "relay failure", "failed");
    const recipients = (await loadJournal(out, 12)).outreach.review.recipients;
    expect(recipients.npub1nodm.effect.disposition).toBe("no_dm");
    expect(recipients["identity:unknown"].effect.disposition).toBe("unknown_identity");
    expect(recipients["identity:missing"].effect.disposition).toBe("missing_identity");
    expect(recipients.npub1noinbox.effect.disposition).toBe("no_nip17_inbox");
    expect(recipients.npub1failed.effect.disposition).toBe("failed");
    expect(recipients[send].effect.disposition).toBe("confirmed");
    expect(Object.keys(recipients[send].effect.receipts ?? {})).toEqual(["r1"]);
    expect(Object.keys(recipients[send].effect.readbacks ?? {})).toEqual(["r2"]);
  });

  test("requires exact readback, not acceptance, before confirmation", async () => {
    const out = await mkdtemp(join(tmpdir(), "compass-outreach-evidence-")); const npub = "npub1recipient";
    await prepareCampaign({ outDir: out, issue: 14, identity: "review", message: "same", recipients: [{ npub, names: ["A"] }] });
    await reuseOrBuildRecipient({ outDir: out, issue: 14, campaign: "review", npub, intent: {}, build: async () => signed() });
    await recordRecipientReceipt(out, 14, "review", npub, { relay: "r", ok: true, ms: 1 });
    await expect(finishRecipient(out, 14, "review", npub, "confirmed")).rejects.toThrow("readback evidence");
  });

  test("rejects changed access binding and changed retained confirmed payload", async () => {
    const out = await mkdtemp(join(tmpdir(), "compass-outreach-immutable-")); const npub = "npub1recipient";
    const args = { outDir: out, issue: 13, identity: "podcast-invitation", message: "podcast https://record.example/old", recipients: [{ npub, names: ["A"] }], binding: { access_receipt_sha256: "a".repeat(64) } };
    await prepareCampaign(args);
    await expect(prepareCampaign({ ...args, message: "podcast https://record.example/changed" })).rejects.toThrow("campaign intent changed");
    await expect(prepareCampaign({ ...args, binding: { access_receipt_sha256: "b".repeat(64) } })).rejects.toThrow("campaign intent changed");
    const event = signed("d".repeat(64));
    await reuseOrBuildRecipient({ outDir: out, issue: 13, campaign: args.identity, npub, intent: { relays: ["r"] }, build: async () => event });
    await recordRecipientReadback(out, 13, args.identity, npub, "r", true);
    await finishRecipient(out, 13, args.identity, npub, "confirmed");
    const effect = (await loadJournal(out, 13)).outreach[args.identity].recipients[npub].effect;
    await Bun.write(effect.payload_path!, JSON.stringify({ ...event, content: "changed" }, null, 2));
    await expect(reuseOrBuildRecipient({ outDir: out, issue: 13, campaign: args.identity, npub, intent: { relays: ["r"] }, build: async () => event })).rejects.toThrow("payload hash mismatch");
  });
});
