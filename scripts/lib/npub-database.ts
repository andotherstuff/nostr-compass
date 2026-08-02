import { nip19 } from "nostr-tools";
import { parse as parseYaml } from "yaml";

export type IdentityType = "project" | "organization" | "maintainer" | "lead-developer" | "individual";

export interface NpubEntry {
  npub: string;
  identity_type: IdentityType;
  person?: string;
  display_name?: string;
  evidence: string[];
  outreach: boolean;
  mention_only: boolean;
  legacy: boolean;
}

export interface NpubMap {
  [name: string]: NpubEntry;
}

export interface NpubValidationResult {
  errors: string[];
  warnings: string[];
  entries: number;
  uniquePubkeys: number;
}

export interface UnresolvedIdentity {
  checked_at: string;
  reason: string;
  sources: string[];
}

export interface UnresolvedIdentityMap {
  [name: string]: UnresolvedIdentity;
}

const IDENTITY_TYPES = new Set<IdentityType>([
  "project",
  "organization",
  "maintainer",
  "lead-developer",
  "individual",
]);

function parseDatabase(raw: string): Record<string, unknown> {
  const parsed = parseYaml(raw, { uniqueKeys: true });
  if (!parsed || typeof parsed !== "object" || Array.isArray(parsed)) {
    throw new Error("npub database must be a YAML mapping");
  }
  return parsed as Record<string, unknown>;
}

function normalizeEntry(name: string, value: unknown): NpubEntry | null {
  if (typeof value === "string") {
    if (!value.startsWith("npub1")) return null;
    return {
      npub: value,
      identity_type: "project",
      evidence: [],
      outreach: true,
      mention_only: false,
      legacy: true,
    };
  }
  if (!value || typeof value !== "object" || Array.isArray(value)) return null;

  const object = value as Record<string, unknown>;
  if (typeof object.npub !== "string" || !object.npub.startsWith("npub1")) return null;
  const explicitType = object.identity_type;
  const identityType = typeof explicitType === "string" && IDENTITY_TYPES.has(explicitType as IdentityType)
    ? explicitType as IdentityType
    : object.mention_only === true
      ? "maintainer"
      : "project";
  const personal = identityType === "maintainer" || identityType === "lead-developer" || identityType === "individual";
  const evidence = Array.isArray(object.evidence)
    ? object.evidence.filter((item): item is string => typeof item === "string")
    : [];
  return {
    npub: object.npub,
    identity_type: identityType,
    person: typeof object.person === "string" ? object.person.trim() : undefined,
    display_name: typeof object.display_name === "string" ? object.display_name.trim() : undefined,
    evidence,
    outreach: object.outreach !== false,
    mention_only: personal,
    legacy: typeof explicitType !== "string",
  };
}

export function formatNpubMention(entry: NpubEntry): string {
  if (entry.identity_type === "organization") {
    const name = entry.display_name ? ` ${entry.display_name}` : "";
    return ` (organization${name}: nostr:${entry.npub})`;
  }
  if (entry.identity_type === "maintainer" || entry.identity_type === "lead-developer") {
    const role = entry.identity_type === "lead-developer" ? "lead developer" : "maintainer";
    const person = entry.person ? ` ${entry.person}` : "";
    return ` (${role}${person}: nostr:${entry.npub})`;
  }
  if (entry.identity_type === "individual") {
    const person = entry.person ? ` ${entry.person}` : "";
    return ` (individual${person}: nostr:${entry.npub})`;
  }
  return ` nostr:${entry.npub}`;
}

export function loadNpubMapFromText(raw: string): NpubMap {
  const parsed = parseDatabase(raw);
  const map: NpubMap = {};
  for (const [name, value] of Object.entries(parsed)) {
    if (name === "no_dm" || name === "unresolved") continue;
    const entry = normalizeEntry(name, value);
    if (entry) map[name.toLocaleLowerCase()] = entry;
  }
  return map;
}

export function loadUnresolvedFromText(raw: string): UnresolvedIdentityMap {
  const parsed = parseDatabase(raw);
  const source = parsed.unresolved;
  if (!source || typeof source !== "object" || Array.isArray(source)) return {};
  const map: UnresolvedIdentityMap = {};
  for (const [name, value] of Object.entries(source as Record<string, unknown>)) {
    if (!value || typeof value !== "object" || Array.isArray(value)) continue;
    const record = value as Record<string, unknown>;
    if (
      typeof record.checked_at === "string" &&
      typeof record.reason === "string" &&
      Array.isArray(record.sources)
    ) {
      map[name.toLocaleLowerCase()] = {
        checked_at: record.checked_at,
        reason: record.reason,
        sources: record.sources.filter((item): item is string => typeof item === "string"),
      };
    }
  }
  return map;
}

export function loadNoDmFromText(raw: string): Set<string> {
  const parsed = parseDatabase(raw);
  const values = parsed.no_dm;
  if (!Array.isArray(values)) return new Set();
  return new Set(values.filter((value): value is string => typeof value === "string").map((value) => value.toLocaleLowerCase()));
}

export function isOutreachAllowed(entry: NpubEntry, noDm: Set<string>): boolean {
  return entry.outreach && !noDm.has(entry.npub.toLocaleLowerCase());
}

function validateNpub(name: string, npub: string, errors: string[]): string | null {
  try {
    const decoded = nip19.decode(npub);
    if (decoded.type !== "npub" || typeof decoded.data !== "string" || !/^[0-9a-f]{64}$/.test(decoded.data)) {
      errors.push(`${name}: value is not a 32-byte npub public key`);
      return null;
    }
    return decoded.data;
  } catch (error) {
    const message = error instanceof Error ? error.message : String(error);
    errors.push(`${name}: invalid npub checksum or encoding (${message})`);
    return null;
  }
}

export function validateNpubDatabase(raw: string): NpubValidationResult {
  const errors: string[] = [];
  const warnings: string[] = [];
  let parsed: Record<string, unknown>;
  try {
    parsed = parseDatabase(raw);
  } catch (error) {
    return {
      errors: [error instanceof Error ? error.message : String(error)],
      warnings,
      entries: 0,
      uniquePubkeys: 0,
    };
  }

  const byHex = new Map<string, Array<{ name: string; entry: NpubEntry }>>();
  const seenNames = new Set<string>();
  let entries = 0;
  let legacyProjects = 0;
  let legacyRepresentatives = 0;

  for (const [name, value] of Object.entries(parsed)) {
    if (name === "no_dm" || name === "unresolved") continue;
    const folded = name.toLocaleLowerCase();
    if (seenNames.has(folded)) errors.push(`${name}: duplicate case-insensitive label`);
    seenNames.add(folded);

    const entry = normalizeEntry(name, value);
    if (!entry) {
      errors.push(`${name}: expected an npub string or typed identity object`);
      continue;
    }
    entries += 1;
    const object = value && typeof value === "object" && !Array.isArray(value)
      ? value as Record<string, unknown>
      : null;
    const explicitType = object?.identity_type;

    if (object) {
      if (object.outreach !== undefined && typeof object.outreach !== "boolean") {
        errors.push(`${name}: outreach must be a boolean`);
      }
      if (object.mention_only !== undefined && typeof object.mention_only !== "boolean") {
        errors.push(`${name}: mention_only must be a boolean`);
      }
      if (object.person !== undefined && typeof object.person !== "string") {
        errors.push(`${name}: person must be a string`);
      }
      if (object.display_name !== undefined && typeof object.display_name !== "string") {
        errors.push(`${name}: display_name must be a string`);
      }
      if (Array.isArray(object.evidence) && object.evidence.some((item) => typeof item !== "string")) {
        errors.push(`${name}: every evidence item must be a string URL`);
      }
    }

    if (entry.legacy) {
      if (typeof value === "string") legacyProjects += 1;
      else legacyRepresentatives += 1;
    } else {
      if (typeof explicitType !== "string" || !IDENTITY_TYPES.has(explicitType as IdentityType)) {
        errors.push(`${name}: unknown identity_type ${String(explicitType)}`);
      }
      if ((entry.identity_type === "maintainer" || entry.identity_type === "lead-developer" || entry.identity_type === "individual") && !entry.person) {
        errors.push(`${name}: ${entry.identity_type} identity requires person`);
      }
      if (entry.identity_type === "organization" && !entry.display_name) {
        errors.push(`${name}: organization identity requires display_name`);
      }
      if (entry.evidence.length === 0) {
        errors.push(`${name}: typed identity requires at least one evidence URL`);
      }
      for (const evidence of entry.evidence) {
        try {
          const url = new URL(evidence);
          if (url.protocol !== "https:" && url.protocol !== "http:") throw new Error("not web evidence");
        } catch {
          errors.push(`${name}: invalid evidence URL ${evidence}`);
        }
      }
    }

    const hex = validateNpub(name, entry.npub, errors);
    if (hex) {
      const rows = byHex.get(hex) ?? [];
      rows.push({ name, entry });
      byHex.set(hex, rows);
    }
  }

  if (legacyProjects > 0) {
    warnings.push(`${legacyProjects} legacy project entries lack explicit evidence`);
  }
  if (legacyRepresentatives > 0) {
    warnings.push(`${legacyRepresentatives} legacy representative entries lack explicit person/role evidence`);
  }

  const unresolved = parsed.unresolved;
  if (unresolved !== undefined) {
    if (!unresolved || typeof unresolved !== "object" || Array.isArray(unresolved)) {
      errors.push("unresolved: expected a mapping of researched projects");
    } else {
      const unresolvedNames = new Set<string>();
      for (const [name, value] of Object.entries(unresolved as Record<string, unknown>)) {
        const folded = name.toLocaleLowerCase();
        if (unresolvedNames.has(folded)) errors.push(`unresolved.${name}: duplicate case-insensitive label`);
        unresolvedNames.add(folded);
        if (seenNames.has(folded)) errors.push(`unresolved.${name}: identity is also present in the active database`);
        if (!value || typeof value !== "object" || Array.isArray(value)) {
          errors.push(`unresolved.${name}: expected a research record`);
          continue;
        }
        const record = value as Record<string, unknown>;
        if (typeof record.checked_at !== "string" || !/^\d{4}-\d{2}-\d{2}$/.test(record.checked_at)) {
          errors.push(`unresolved.${name}: checked_at must be YYYY-MM-DD`);
        }
        if (typeof record.reason !== "string" || record.reason.trim().length === 0) {
          errors.push(`unresolved.${name}: reason is required`);
        }
        if (!Array.isArray(record.sources) || record.sources.length === 0) {
          errors.push(`unresolved.${name}: at least one source URL is required`);
        } else {
          for (const source of record.sources) {
            try {
              const url = new URL(String(source));
              if (url.protocol !== "https:" && url.protocol !== "http:") throw new Error("not web evidence");
            } catch {
              errors.push(`unresolved.${name}: invalid source URL ${String(source)}`);
            }
          }
        }
      }
    }
  }

  const noDm = parsed.no_dm;
  if (noDm !== undefined) {
    if (!Array.isArray(noDm)) {
      errors.push("no_dm: expected a list of npubs");
    } else {
      const seen = new Set<string>();
      for (const [index, value] of noDm.entries()) {
        if (typeof value !== "string") {
          errors.push(`no_dm[${index}]: expected an npub string`);
          continue;
        }
        const hex = validateNpub(`no_dm[${index}]`, value, errors);
        if (hex && seen.has(hex)) errors.push(`no_dm[${index}]: duplicate pubkey`);
        if (hex) seen.add(hex);
      }
    }
  }

  for (const rows of byHex.values()) {
    // Legacy aliases are ambiguous, but they must not suppress a contradiction
    // between explicit typed records sharing the same pubkey.
    const typedRows = rows.filter(({ entry }) => !entry.legacy);
    const types = new Set(typedRows.map(({ entry }) => entry.identity_type));
    if ((types.has("project") || types.has("organization")) && (types.has("individual") || types.has("maintainer") || types.has("lead-developer"))) {
      errors.push(`${typedRows.map(({ name }) => name).join(", ")}: pubkey is classified as both organizational and personal identity`);
    }
  }

  return { errors, warnings, entries, uniquePubkeys: byHex.size };
}

export function loadValidatedNpubMapFromText(raw: string): NpubMap {
  const validation = validateNpubDatabase(raw);
  if (validation.errors.length > 0) {
    throw new Error(`Invalid npub database:\n${validation.errors.map((error) => `- ${error}`).join("\n")}`);
  }
  return loadNpubMapFromText(raw);
}
