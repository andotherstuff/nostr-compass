#!/usr/bin/env bun
import { readFileSync } from "fs";
import { resolve } from "path";
import { validateNpubDatabase } from "./lib/npub-database";

const file = resolve(process.argv[2] ?? "data/npubs.yml");
const strict = process.argv.includes("--strict");
const result = validateNpubDatabase(readFileSync(file, "utf8"));

for (const error of result.errors) console.error(`ERROR: ${error}`);
for (const warning of result.warnings) console.error(`WARN: ${warning}`);
console.error(
  `npub database: ${result.entries} entries, ${result.uniquePubkeys} valid unique pubkeys, ${result.errors.length} errors, ${result.warnings.length} warnings`,
);
if (result.errors.length > 0 || (strict && result.warnings.length > 0)) process.exit(1);
