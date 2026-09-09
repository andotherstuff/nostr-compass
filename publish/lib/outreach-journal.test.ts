import { describe, expect, test } from "bun:test";
import { mkdtemp } from "node:fs/promises";
import { join } from "node:path";
import { tmpdir } from "node:os";
import { finishRecipient, prepareCampaign, reuseOrBuildRecipient } from "./outreach-journal.ts";

describe("outreach recipient replay", () => {
  test("--only-independent campaign identity reuses confirmed exact signed payload", async () => {
    const out = await mkdtemp(join(tmpdir(), "compass-outreach-")); const npub = "npub1recipient"; let builds = 0;
    await prepareCampaign({ outDir: out, issue: 9, identity: "review", message: "review url", recipients: [{ npub, names: ["A"] }] });
    const build = async () => { builds++; return { id: "a".repeat(64), pubkey: "b".repeat(64), sig: "c".repeat(128), kind: 4, created_at: 1, tags: [], content: "cipher" }; };
    const first = await reuseOrBuildRecipient({ outDir: out, issue: 9, campaign: "review", npub, intent: { protocol: "nip04", relays: ["r"] }, build });
    await finishRecipient(out, 9, "review", npub, "confirmed");
    const second = await reuseOrBuildRecipient({ outDir: out, issue: 9, campaign: "review", npub, intent: { protocol: "nip04", relays: ["r"] }, build });
    expect(second).toEqual(first); expect(builds).toBe(1);
    await expect(prepareCampaign({ outDir: out, issue: 9, identity: "review", message: "changed", recipients: [{ npub, names: ["A"] }] })).rejects.toThrow("campaign intent changed");
  });
});
