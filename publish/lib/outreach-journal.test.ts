import { describe, expect, setDefaultTimeout, test } from "bun:test";
setDefaultTimeout(20_000);
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

  test("adds newly eligible recipients without rewriting confirmed intent", async () => {
    const out = await mkdtemp(join(tmpdir(), "compass-outreach-expand-"));
    await prepareCampaign({ outDir: out, issue: 10, identity: "review", message: "same", recipients: [{ npub: "npub1old", names: ["Old"] }] });
    await finishRecipient(out, 10, "review", "npub1old", "confirmed");
    const campaign = await prepareCampaign({ outDir: out, issue: 10, identity: "review", message: "same", recipients: [{ npub: "npub1old", names: ["Old"] }, { npub: "npub1new", names: ["New"] }] });
    expect(campaign.recipients.npub1old.effect.state).toBe("confirmed");
    expect(campaign.recipients.npub1new.effect.state).toBe("prepared");
  });

  test("keeps reminder and rerecord campaigns independent", async () => {
    const out = await mkdtemp(join(tmpdir(), "compass-outreach-types-")); const recipients = [{ npub: "npub1person", names: ["Person"] }];
    await prepareCampaign({ outDir: out, issue: 11, identity: "review", message: "initial", recipients });
    await prepareCampaign({ outDir: out, issue: 11, identity: "reminder", message: "reminder", recipients });
    const rerecord = await prepareCampaign({ outDir: out, issue: 11, identity: "rerecord", message: "rerecord", recipients });
    expect(rerecord.identity).toBe("rerecord");
  });
});
