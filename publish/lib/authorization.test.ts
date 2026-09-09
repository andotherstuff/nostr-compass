import { expect, test } from "bun:test";
import { mkdtemp, writeFile } from "node:fs/promises";
import { join } from "node:path";
import { tmpdir } from "node:os";
import { assertSigningAuthorized, recordEditionAuthorization } from "./authorization.ts";
import { loadOrCreateJournal, mutateJournal, saveJournal, sha256 } from "./journal.ts";

const head = "a".repeat(40), base = "b".repeat(40), tree = "c".repeat(40), signer = "d".repeat(64);

async function setup(notBefore = "2026-09-09T16:00:00Z") {
  const root = await mkdtemp(join(tmpdir(), "compass-sign-auth-"));
  const source = join(root, "source.md");
  const receipt = join(root, "authorization.json");
  await writeFile(source, "source");
  const journal = await loadOrCreateJournal(root, 42);
  journal.source = { path: source, sha256: sha256("source") };
  journal.pull_request = { number: 7, head_sha: head, base_sha: base, prospective_tree_sha: tree };
  await saveJournal(root, journal);
  const value = {
    schema_version: 1, receipt_type: "edition-authorization", issue: 42, phase_id: "2026-09-09-publication",
    head_sha: head, base_sha: base, prospective_tree_sha: tree, source_sha256: sha256("source"),
    hold_version: "no-hold@1", not_before: notBefore, final_feedback_scan_at: notBefore,
    authorized_by: "scheduled-compass-policy", signer_pubkey: signer, purpose: "weekly-publication",
    allowed_event_kinds: [30023, 1], edition_date: notBefore.slice(0, 10), final: true,
  } as const;
  await writeFile(receipt, JSON.stringify(value, null, 2));
  await recordEditionAuthorization(root, 42, receipt);
  const gateEvidence = await Promise.all((["quality", "feedback"] as const).map(async (gate) => {
    const path = join(root, `${gate}.json`); const bytes = JSON.stringify({ gate, head });
    await writeFile(path, bytes);
    return { gate, path, bytes };
  }));
  await mutateJournal(root, 42, (journal) => {
    for (const { gate, path, bytes } of gateEvidence) journal.effects[gate] = { state: "confirmed", intent_sha256: gate, payload_path: path, payload_sha256: sha256(bytes), event_id: head };
  });
  return { root, receipt };
}

test("direct signing is refused until exact merge and deployment are confirmed", async () => {
  const { root } = await setup();
  await expect(assertSigningAuthorized(root, 42, 30023, signer, new Date("2026-09-09T16:01:00Z"))).rejects.toThrow("before exact merge and deployment");
  await mutateJournal(root, 42, (journal) => {
    journal.effects.merge = { state: "confirmed", intent_sha256: "merge", event_id: "e".repeat(40) };
    journal.effects.deploy = { state: "confirmed", intent_sha256: "deploy", event_id: "123" };
  });
  await expect(assertSigningAuthorized(root, 42, 30023, signer, new Date("2026-09-09T16:01:00Z"))).resolves.toBeUndefined();
  await expect(assertSigningAuthorized(root, 42, 1, "e".repeat(64), new Date("2026-09-09T16:01:00Z"))).rejects.toThrow("does not cover this signer");
});

test("signing rejects changed authorization bytes and conflicting future-edition authorization", async () => {
  const { root, receipt } = await setup();
  await mutateJournal(root, 42, (journal) => {
    journal.effects.merge = { state: "confirmed", intent_sha256: "merge", event_id: "e".repeat(40) };
    journal.effects.deploy = { state: "confirmed", intent_sha256: "deploy", event_id: "123" };
  });
  await writeFile(receipt, "{}\n");
  await expect(assertSigningAuthorized(root, 42, 1, signer, new Date("2026-09-09T16:01:00Z"))).rejects.toThrow("receipt bytes changed");
  const { root: fresh } = await setup("2026-09-16T16:00:00Z");
  await mutateJournal(fresh, 42, (journal) => {
    journal.effects.merge = { state: "confirmed", intent_sha256: "merge", event_id: "e".repeat(40) };
    journal.effects.deploy = { state: "confirmed", intent_sha256: "deploy", event_id: "123" };
  });
  await expect(assertSigningAuthorized(fresh, 42, 1, signer, new Date("2026-09-10T16:01:00Z"))).rejects.toThrow("current admitted Wednesday occurrence");
});

test("Thursday post-deploy recovery retains the exact Wednesday authorization", async () => {
  const { root } = await setup();
  await mutateJournal(root, 42, (journal) => {
    journal.effects.merge = { state: "confirmed", intent_sha256: "merge", event_id: "e".repeat(40) };
    journal.effects.deploy = { state: "confirmed", intent_sha256: "deploy", event_id: "123" };
  });
  await expect(assertSigningAuthorized(root, 42, 30023, signer, new Date("2026-09-10T01:00:00Z"))).resolves.toBeUndefined();
  await expect(assertSigningAuthorized(root, 42, 1, signer, new Date("2026-09-17T01:00:00Z"))).resolves.toBeUndefined();
});

test("post-deploy recovery rejects stale exact-head feedback evidence", async () => {
  const { root } = await setup();
  await mutateJournal(root, 42, (journal) => {
    journal.effects.merge = { state: "confirmed", intent_sha256: "merge", event_id: "e".repeat(40) };
    journal.effects.deploy = { state: "confirmed", intent_sha256: "deploy", event_id: "123" };
  });
  await writeFile(join(root, "feedback.json"), "changed");
  await expect(assertSigningAuthorized(root, 42, 1, signer, new Date("2026-09-10T01:00:00Z"))).rejects.toThrow("current exact-head feedback evidence");
});
