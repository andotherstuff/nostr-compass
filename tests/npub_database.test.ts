import { describe, expect, test } from "bun:test";
import {
  formatNpubMention,
  isOutreachAllowed,
  loadNoDmFromText,
  loadNpubMapFromText,
  loadValidatedNpubMapFromText,
  validateNpubDatabase,
} from "../scripts/lib/npub-database";

const PROJECT_NPUB = "npub1wav4fae3gyfy3xj298kxj2mj8phavz7vavps34przq02j7w902qq902923";
const PERSON_NPUB = "npub1q6mcr8tlr3l4gus3sfnw6772s7zae6hqncmw5wj27ejud5wcxf7q0nx7d5";

describe("npub database", () => {
  test("loads explicit project, maintainer, lead-developer, and individual identities", () => {
    const raw = `
Compass:
  npub: ${PROJECT_NPUB}
  identity_type: project
  evidence:
    - https://nostrcompass.org/
SafeBox:
  npub: ${PERSON_NPUB}
  identity_type: maintainer
  person: Tim Bouma
  evidence:
    - https://github.com/trbouma/safebox
Developer:
  npub: ${PERSON_NPUB}
  identity_type: individual
  person: Alice
  evidence:
    - https://example.com/profile
`;

    const map = loadNpubMapFromText(raw);
    expect(map.compass.identity_type).toBe("project");
    expect(map.safebox.identity_type).toBe("maintainer");
    expect(map.safebox.person).toBe("Tim Bouma");
    expect(map.developer.identity_type).toBe("individual");
    expect(formatNpubMention(map.developer)).toBe(` (individual Alice: nostr:${PERSON_NPUB})`);
  });

  test("labels personal project representatives explicitly in prose", () => {
    const map = loadNpubMapFromText(`
Project:
  npub: ${PROJECT_NPUB}
  identity_type: project
  evidence: [https://example.com/project]
Maintained Project:
  npub: ${PERSON_NPUB}
  identity_type: maintainer
  person: Tim Bouma
  evidence: [https://example.com/maintainer]
Led Project:
  npub: ${PERSON_NPUB}
  identity_type: lead-developer
  person: Tim Bouma
  evidence: [https://example.com/lead]
Org Project:
  npub: ${PROJECT_NPUB}
  identity_type: organization
  display_name: Example Foundation
  outreach: false
  evidence: [https://example.com/org]
`);

    expect(formatNpubMention(map.project)).toBe(` nostr:${PROJECT_NPUB}`);
    expect(formatNpubMention(map["maintained project"])).toBe(
      ` (maintainer Tim Bouma: nostr:${PERSON_NPUB})`,
    );
    expect(formatNpubMention(map["led project"])).toBe(
      ` (lead developer Tim Bouma: nostr:${PERSON_NPUB})`,
    );
    expect(formatNpubMention(map["org project"])).toBe(
      ` (organization Example Foundation: nostr:${PROJECT_NPUB})`,
    );
    expect(map["org project"].outreach).toBe(false);
  });

  test("rejects invalid checksums and personal project identities without a person", () => {
    const raw = `
Bad: npub1relaystr0ng75ecpd8av2v35kwf3a86vlrr3c4gs02p3gvy57haaqgt3a6p
Unattributed:
  npub: ${PERSON_NPUB}
  identity_type: maintainer
  evidence:
    - https://example.com
`;

    const result = validateNpubDatabase(raw);
    expect(result.errors.some((error) => error.includes("Bad") && error.includes("checksum"))).toBe(true);
    expect(result.errors.some((error) => error.includes("Unattributed") && error.includes("person"))).toBe(true);
  });

  test("rejects unknown explicit identity types instead of normalizing them to project", () => {
    const result = validateNpubDatabase(`
Bad:
  npub: ${PROJECT_NPUB}
  identity_type: corporation
  evidence: [https://example.com/bad]
`);
    expect(result.errors.some((error) => error.includes("unknown identity_type corporation"))).toBe(true);
  });

  test("rejects individual identities without a person", () => {
    const result = validateNpubDatabase(`
Anonymous:
  npub: ${PERSON_NPUB}
  identity_type: individual
  evidence: [https://example.com/anonymous]
`);
    expect(result.errors.some((error) => error.includes("individual identity requires person"))).toBe(true);
  });

  test("rejects a pubkey classified as both a project and a person", () => {
    const raw = `
Project:
  npub: ${PROJECT_NPUB}
  identity_type: project
  evidence:
    - https://example.com/project
Person:
  npub: ${PROJECT_NPUB}
  identity_type: individual
  person: Alice
  evidence:
    - https://example.com/person
`;

    const result = validateNpubDatabase(raw);
    expect(result.errors.some((error) => error.includes("both organizational and personal"))).toBe(true);
  });

  test("a legacy alias cannot suppress a conflict between typed records", () => {
    const result = validateNpubDatabase(`
Legacy: ${PROJECT_NPUB}
Project:
  npub: ${PROJECT_NPUB}
  identity_type: project
  evidence: [https://example.com/project]
Person:
  npub: ${PROJECT_NPUB}
  identity_type: individual
  person: Alice
  evidence: [https://example.com/person]
`);
    expect(result.errors.some((error) => error.includes("both organizational and personal"))).toBe(true);
  });

  test("validated loading fails closed on malformed npubs", () => {
    expect(() => loadValidatedNpubMapFromText("Bad: npub1notavalidkey")).toThrow("Invalid npub database");
  });

  test("allows maintainer and individual aliases for the same personal key", () => {
    const raw = `
SafeBox:
  npub: ${PERSON_NPUB}
  identity_type: maintainer
  person: Tim Bouma
  evidence:
    - https://github.com/trbouma/safebox
Tim Bouma:
  npub: ${PERSON_NPUB}
  identity_type: individual
  person: Tim Bouma
  evidence:
    - https://github.com/trbouma
`;

    expect(validateNpubDatabase(raw).errors).toEqual([]);
  });

  test("keeps legacy entries readable but reports migration warnings", () => {
    const raw = `
Legacy Project: ${PROJECT_NPUB}
Legacy Maintainer:
  npub: ${PERSON_NPUB}
  mention_only: true
`;

    const map = loadNpubMapFromText(raw);
    const result = validateNpubDatabase(raw);
    expect(map["legacy project"].identity_type).toBe("project");
    expect(map["legacy maintainer"].identity_type).toBe("maintainer");
    expect(result.warnings.length).toBe(2);
  });

  test("keeps researched unresolved projects out of the active identity map", () => {
    const raw = `
Project: ${PROJECT_NPUB}
unresolved:
  Granary:
    checked_at: 2026-08-02
    reason: No project or maintainer identity is bound by primary evidence.
    sources:
      - https://github.com/snarfed/granary
`;
    const map = loadNpubMapFromText(raw);
    const result = validateNpubDatabase(raw);
    expect(map.project.npub).toBe(PROJECT_NPUB);
    expect(map.granary).toBeUndefined();
    expect(result.errors).toEqual([]);
  });

  test("rejects incomplete unresolved research records", () => {
    const result = validateNpubDatabase(`
unresolved:
  Granary:
    checked_at: not-a-date
    sources: []
`);
    expect(result.errors.some((error) => error.includes("Granary"))).toBe(true);
  });

  test("rejects malformed typed metadata and active/unresolved overlap", () => {
    const result = validateNpubDatabase(`
Project:
  npub: ${PROJECT_NPUB}
  identity_type: project
  outreach: "false"
  evidence: [https://example.com/project, 42]
unresolved:
  project:
    checked_at: 2026-08-02
    reason: Contradictory stale unresolved record.
    sources: [https://example.com/research]
`);
    expect(result.errors.some((error) => error.includes("outreach must be a boolean"))).toBe(true);
    expect(result.errors.some((error) => error.includes("every evidence item"))).toBe(true);
    expect(result.errors.some((error) => error.includes("also present in the active database"))).toBe(true);
  });

  test("applies outreach false and no_dm before recipient selection", () => {
    const raw = `
Project:
  npub: ${PROJECT_NPUB}
  identity_type: project
  evidence: [https://example.com/project]
Organization:
  npub: ${PERSON_NPUB}
  identity_type: organization
  display_name: Example Org
  outreach: false
  evidence: [https://example.com/org]
no_dm: [${PROJECT_NPUB}]
`;
    const map = loadNpubMapFromText(raw);
    const noDm = loadNoDmFromText(raw);
    expect(isOutreachAllowed(map.project, noDm)).toBe(false);
    expect(isOutreachAllowed(map.organization, noDm)).toBe(false);
    expect(isOutreachAllowed({ ...map.project, npub: PERSON_NPUB }, noDm)).toBe(true);
  });
});
