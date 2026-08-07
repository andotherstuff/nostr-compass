#!/usr/bin/env python3
"""Detect placeholder or fabricated Nostr event examples in newsletter drafts.

Origin: issue #34 (2026-08-05) shipped two JSON event examples whose id/pubkey/sig
were repeated-hex placeholders, with prose admitting they were placeholders. Both
needed post-publication replacement with real relay-recovered events and a kind
30023 re-broadcast. This checker makes that class of defect a mechanical FAIL
before a draft PR is called ready.

Checks every fenced ```json block that parses as a Nostr event (has id, pubkey,
kind, sig):
  1. All seven NIP-01 fields present
  2. id/pubkey are 64-char hex, sig is 128-char hex
  3. No single-digit repeated-hex values (0000..., 1111..., aaaa...)
  4. No low-entropy values (<= 6 distinct hex chars in id/pubkey)
  5. Prose within 3 lines above the block must not say "placeholder",
     "illustrative", or "not a valid signature"
  6. created_at must be a plausible unix timestamp (2015-01-01 .. now + 1 day)

Exit 0 = PASS, 1 = FAIL. Usage:
  python3 scripts/check_newsletter_event_examples.py <newsletter.md> [...more files]
"""

from __future__ import annotations

import json
import re
import sys
import time

FENCE = re.compile(r"```json\s*\n(.*?)```", re.DOTALL)
HEX64 = re.compile(r"^[0-9a-f]{64}$")
HEX128 = re.compile(r"^[0-9a-f]{128}$")
BAD_PROSE = re.compile(r"placeholder|illustrative|not a valid signature", re.IGNORECASE)

MIN_TS = 1420070400  # 2015-01-01


def low_entropy(value: str) -> bool:
    """True if the hex string is a single repeated char or has <=6 distinct chars."""
    if not value:
        return False
    if len(set(value)) == 1:
        return True
    return len(set(value)) <= 6


def check_file(path: str) -> list[str]:
    text = open(path, encoding="utf-8").read()
    lines = text.split("\n")
    problems: list[str] = []
    now = int(time.time())

    for match in FENCE.finditer(text):
        block = match.group(1)
        line_no = text[: match.start()].count("\n") + 1
        try:
            ev = json.loads(block)
        except json.JSONDecodeError:
            continue
        if not isinstance(ev, dict) or "kind" not in ev or "pubkey" not in ev:
            continue

        label = f"{path}:{line_no} (kind {ev.get('kind')})"

        for field in ("id", "pubkey", "created_at", "kind", "tags", "content", "sig"):
            if field not in ev:
                problems.append(f"{label}: missing required NIP-01 field '{field}'")

        eid, pk, sig = str(ev.get("id", "")), str(ev.get("pubkey", "")), str(ev.get("sig", ""))

        # Validate format unconditionally: a present-but-empty or non-string field is
        # still a fabricated example, and `if eid and ...` would silently skip it.
        if not HEX64.match(eid):
            problems.append(f"{label}: id is not 64-char lowercase hex ({eid[:24]!r}…)")
        if not HEX64.match(pk):
            problems.append(f"{label}: pubkey is not 64-char lowercase hex ({pk[:24]!r}…)")
        if not HEX128.match(sig):
            problems.append(f"{label}: sig is not 128-char lowercase hex ({sig[:24]!r}…)")

        for name, value in (("id", eid), ("pubkey", pk), ("sig", sig)):
            if value and low_entropy(value):
                problems.append(
                    f"{label}: {name} looks like placeholder data (repeated/low-entropy hex: {value[:16]}…)"
                )

        ts = ev.get("created_at")
        if isinstance(ts, int) and not (MIN_TS <= ts <= now + 86400):
            problems.append(f"{label}: created_at {ts} is not a plausible unix timestamp")

        # Prose immediately above the block must not admit placeholder status.
        start_line = line_no - 2  # 0-indexed line of the opening fence
        above = "\n".join(lines[max(0, start_line - 3) : start_line])
        if BAD_PROSE.search(above):
            problems.append(
                f"{label}: prose above the example admits it is illustrative/placeholder — "
                "embed a real relay-recovered event instead"
            )

    return problems


def main() -> int:
    if len(sys.argv) < 2:
        print("usage: check_newsletter_event_examples.py <newsletter.md> [...]", file=sys.stderr)
        return 2
    all_problems: list[str] = []
    for path in sys.argv[1:]:
        all_problems.extend(check_file(path))
    if all_problems:
        print("FAIL: placeholder or invalid Nostr event example(s) detected:")
        for p in all_problems:
            print(f"  - {p}")
        return 1
    print("PASS: every JSON event example has valid structure and no placeholder data")
    return 0


if __name__ == "__main__":
    sys.exit(main())
