# Prose / Anti-Slop Review — 2026-07-22 draft

- Draft: `content/en/newsletters/2026-07-22-newsletter.md`
- Reviewer: ProseReview (Stage 7 swarm)
- Rules applied: `~/.claude/rules/base-antislop.md`, `skills/_COMPASS/SKILL.md`
- Method: mechanical grep scans for each banned category; every hit below verified by hand in context. Report only, draft untouched.

## Scan evidence (grep hit counts)

| Scan | Pattern | Hits |
|---|---|---|
| Em dashes | `—` | 0 |
| Curly/smart quotes | `[‘’“”]` | 0 |
| Exclamation marks | `!` | 0 |
| "not X but Y" | `not ... but` | 0 |
| "could not be more X" | `could not be more\|couldn't be more` | 0 |
| AI buzzwords | banned-word list | 9 (ecosystem ×8, streamline ×1) |
| Filler intensifiers | actually/basically/.../very/virtually (word-boundary) | 2 (actually L26, simply L112) |
| "matters" amplifier | `\bmatters?\b` | 1 (L90) |
| "rather than" | `rather than` | 5 (L66, L94, L106, L116, L124) |
| Banned filler phrases | worth noting/watching/following/flagging, interestingly, at the end of the day, etc. | 2 (L86 "worth watching", L118 "worth following") |
| Hedging "just/merely/only" | `just\|merely` (word-boundary) | 3 (L26, L116, L182) |
| Semicolons | `;` | 12 lines — mostly legitimate spec listings, no semicolon-negation flourishes |

Total flagged hits: 22.

## Fix list

1. **L12 / L7 / L26 / L40 / L70 (×2) / L88 / L90 — "ecosystem" (8 occurrences)**
   - Current: "the Iris ecosystem ships...", "For an ecosystem that usually talks about protocols replacing platforms..."
   - Suggested: keep "Iris ecosystem" only if treated as the project's own branding (it is mmalmi's Iris Stack framing); otherwise "Iris stack"/"Iris orbit" (L42 already uses "Iris orbit"). For L26: "For a space that usually talks about protocols replacing platforms..."
   - Reason: "ecosystem" is on the banned-word list. Note for editor: this draft uses it as a proper-noun-ish label for the Iris project cluster; flagging per rules, but a blanket exemption for "Iris ecosystem" as branding is defensible.

2. **L26 — "actually"**
   - Current: "so artists can actually remove their work"
   - Suggested: "so artists can remove their work" (or "...can have their work deleted" for force)
   - Reason: filler intensifier, banned.

3. **L26 — "not just a statement of intent"**
   - Current: "the pivot arrived with working client code, not just a statement of intent"
   - Suggested: "the pivot arrived with working client code behind it"
   - Reason: "not just X" negation structure.

4. **L66 — "rather than"**
   - Current: "an incremental follow-up to the alpha line covered in #31 rather than a new headline"
   - Suggested: "an incremental follow-up to the alpha line covered in #31, not a new headline" → better: "an incremental follow-up to the alpha line covered in #31"
   - Reason: banned "rather than" structure; the clause adds nothing.

5. **L90 — "it matters this week as connective tissue"**
   - Current: "On its own this is plumbing, but it matters this week as connective tissue:"
   - Suggested: "On its own this is plumbing, but this week it is connective tissue:"
   - Reason: "matters" as rhetorical amplifier, banned.

6. **L94 — "rather than"**
   - Current: "giving clients a standard way to reason about which relays to trust rather than hardcoding operator lists"
   - Suggested: "giving clients a standard way to reason about which relays to trust, replacing hardcoded operator lists"
   - Reason: banned "rather than" structure.

7. **L106 — "rather than"**
   - Current: "each `kind:9010` replaces the whole list rather than toggling single entries"
   - Suggested: "each `kind:9010` replaces the whole list instead of toggling single entries" → better: "each `kind:9010` replaces the whole list in one shot; single entries are never toggled"
   - Reason: banned "rather than" structure.

8. **L108 — "streamline"**
   - Current: "to streamline admission to closed groups"
   - Suggested: "to speed up admission to closed groups" or "to simplify admission to closed groups"
   - Reason: banned word "streamline".

9. **L112 — "simply"**
   - Current: "could simply never respond"
   - Suggested: "could never respond"
   - Reason: filler intensifier, banned.

10. **L86 — "worth watching"**
    - Current: "a structural split of its core spec is a discussion worth watching even before any merge decision"
    - Suggested: "a structural split of its core spec deserves attention even before any merge decision"
    - Reason: banned phrase family ("worth X-ing").

11. **L118 — "worth following"**
    - Current: "the restructuring discussion is worth following for any wallet or app that speaks NWC"
    - Suggested: "any wallet or app that speaks NWC should track the restructuring discussion"
    - Reason: banned phrase family.

12. **L116 — "just-merged"**
    - Current: "Moves the just-merged favorite follow sets list..."
    - Suggested: "Moves the newly merged favorite follow sets list..."
    - Reason: hedging "just" as qualifier.

13. **L182 — "just shipped"**
    - Current: "That two-layer shape is what nostream just shipped"
    - Suggested: "That two-layer shape is what nostream shipped this week"
    - Reason: hedging "just" as qualifier.

14. **L116 — "rather than"**
    - Current: "should track this PR and target the final number rather than shipping against `10011`"
    - Suggested: "should track this PR and target the final number, not `10011`"
    - Reason: banned "rather than" structure.

15. **L124 — "rather than"**
    - Current: "sender identification via the unforgeable `MessageEvent.source` window reference rather than `event.origin`"
    - Suggested: "sender identification via the unforgeable `MessageEvent.source` window reference, not `event.origin`"
    - Reason: banned "rather than" structure.

## Notes (not violations)

- Semicolons (12 lines) are used for list separation and spec enumeration; none are the "X; Y is not" negation flourish.
- No em dashes, curly quotes, or exclamation marks anywhere in the draft.
- "no longer mandatory" (L26), "no longer starts over" (L34), "simply never respond" (L112, flagged above) — the "no longer" constructions are factual negations, allowed.

## Verdict

Draft is clean on punctuation and free of the worst AI vocabulary, but carries 9 banned-word hits ("ecosystem" ×8, "streamline" ×1), 5 banned "rather than" structures, 2 banned "worth X-ing" phrases, 1 "matters" amplifier, and 5 hedging/intensifier hits. If the editor grants "Iris ecosystem" a branding exemption, the remaining 14 hits are all mechanical one-line fixes; the "rather than" and "worth watching/following" clusters are unambiguous rule violations.

GATE: FAIL — 5 "rather than" structures, 2 "worth X-ing" phrases, "matters" amplifier, "streamline", and filler intensifiers (14 non-"ecosystem" hits; 22 total) require fixes before publish.
