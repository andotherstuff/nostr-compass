#!/usr/bin/env python3
"""Validate full, signed NIP-01 examples in newsletter deep dives.

Every fenced JSON object that looks like a Nostr event is checked structurally,
its NIP-01 id is recomputed, and its BIP-340 signature is verified. A regular
NIP deep dive must contain at least one such event unless its only primary
subject is NIP-21. Any deep dive whose primary headings include NIP-27 must also
show a valid event whose content contains a ``nostr:`` reference.

Exit 0 = PASS, 1 = FAIL. Usage:
  python3 scripts/check_newsletter_event_examples.py <newsletter.md> [...]
"""

from __future__ import annotations

import hashlib
import json
import re
import sys
import time
from pathlib import Path

FENCE = re.compile(r"```json\s*\n(.*?)```", re.DOTALL)
H2 = re.compile(r"^## (?!#)", re.MULTILINE)
DEEP_DIVE = re.compile(r"^## NIP Deep Dive\b", re.MULTILINE)
NIP_MENTION = re.compile(r"\bNIP-(\d+)\b", re.IGNORECASE)
HEX64 = re.compile(r"^[0-9a-f]{64}$")
HEX128 = re.compile(r"^[0-9a-f]{128}$")
BAD_PROSE = re.compile(r"placeholder|illustrative|not a valid signature", re.IGNORECASE)
MIN_TS = 1420070400

# secp256k1 and BIP-340 constants. Keeping verification here makes the gate
# reproducible in CI without trusting an optional local relay client.
P = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEFFFFFC2F
N = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364141
G = (
    0x79BE667EF9DCBBAC55A06295CE870B07029BFCDB2DCE28D959F2815B16F81798,
    0x483ADA7726A3C4655DA4FBFC0E1108A8FD17B448A68554199C47D08FFB10D4B8,
)


class EventExample:
    def __init__(self, line: int, event: dict, valid: bool) -> None:
        self.line = line
        self.event = event
        self.valid = valid


def low_entropy(value: str) -> bool:
    return bool(value) and len(set(value)) <= 6


def point_add(a: tuple[int, int] | None, b: tuple[int, int] | None) -> tuple[int, int] | None:
    if a is None:
        return b
    if b is None:
        return a
    ax, ay = a
    bx, by = b
    if ax == bx and (ay != by or ay == 0):
        return None
    slope = ((3 * ax * ax) * pow(2 * ay, P - 2, P)) % P if a == b else ((by - ay) * pow(bx - ax, P - 2, P)) % P
    x = (slope * slope - ax - bx) % P
    return x, (slope * (ax - x) - ay) % P


def point_mul(k: int, point: tuple[int, int]) -> tuple[int, int] | None:
    result = None
    addend: tuple[int, int] | None = point
    while k:
        if k & 1:
            result = point_add(result, addend)
        addend = point_add(addend, addend)
        k >>= 1
    return result


def tagged_hash(tag: str, payload: bytes) -> bytes:
    tag_hash = hashlib.sha256(tag.encode()).digest()
    return hashlib.sha256(tag_hash + tag_hash + payload).digest()


def verify_schnorr(message: bytes, pubkey_hex: str, signature_hex: str) -> bool:
    if len(message) != 32 or not HEX64.fullmatch(pubkey_hex) or not HEX128.fullmatch(signature_hex):
        return False
    px = int(pubkey_hex, 16)
    if px >= P:
        return False
    y2 = (pow(px, 3, P) + 7) % P
    py = pow(y2, (P + 1) // 4, P)
    if pow(py, 2, P) != y2:
        return False
    if py & 1:
        py = P - py
    signature = bytes.fromhex(signature_hex)
    r, s = int.from_bytes(signature[:32], "big"), int.from_bytes(signature[32:], "big")
    if r >= P or s >= N:
        return False
    challenge = int.from_bytes(
        tagged_hash("BIP0340/challenge", signature[:32] + bytes.fromhex(pubkey_hex) + message), "big"
    ) % N
    recovered = point_add(point_mul(s, G), point_mul((N - challenge) % N, (px, py)))
    return recovered is not None and recovered[1] % 2 == 0 and recovered[0] == r


def event_id(event: dict) -> str:
    serialized = json.dumps(
        [0, event["pubkey"], event["created_at"], event["kind"], event["tags"], event["content"]],
        ensure_ascii=False,
        separators=(",", ":"),
    ).encode()
    return hashlib.sha256(serialized).hexdigest()


def deep_dive_sections(text: str) -> list[tuple[int, str]]:
    sections: list[tuple[int, str]] = []
    for match in DEEP_DIVE.finditer(text):
        following = H2.search(text, match.end())
        end = following.start() if following else len(text)
        sections.append((text[: match.start()].count("\n") + 1, text[match.start():end]))
    return sections


def validate_event(event: dict, label: str, now: int) -> list[str]:
    problems: list[str] = []
    required = ("id", "pubkey", "created_at", "kind", "tags", "content", "sig")
    for field in required:
        if field not in event:
            problems.append(f"{label}: missing required NIP-01 field '{field}'")
    if problems:
        return problems
    if not isinstance(event["kind"], int):
        problems.append(f"{label}: kind is not an integer ({event['kind']!r})")
    if not isinstance(event["created_at"], int):
        problems.append(f"{label}: created_at is not an integer")
    if not isinstance(event["content"], str):
        problems.append(f"{label}: content is not a string")
    if not (isinstance(event["tags"], list) and all(isinstance(tag, list) and all(isinstance(value, str) for value in tag) for tag in event["tags"])):
        problems.append(f"{label}: tags is not a list of string lists")

    eid, pubkey, signature = (str(event[field]) for field in ("id", "pubkey", "sig"))
    for field, value, pattern in (("id", eid, HEX64), ("pubkey", pubkey, HEX64), ("sig", signature, HEX128)):
        if not pattern.fullmatch(value):
            problems.append(f"{label}: {field} has the wrong lowercase-hex length ({value[:24]!r}…)")
        elif low_entropy(value):
            problems.append(f"{label}: {field} looks like placeholder data ({value[:16]}…)")
    timestamp = event["created_at"]
    if not (isinstance(timestamp, int) and MIN_TS <= timestamp <= now + 86400):
        problems.append(f"{label}: created_at {timestamp!r} is not a plausible unix timestamp")
    if problems:
        return problems

    computed = event_id(event)
    if computed != eid:
        problems.append(f"{label}: id does not match canonical NIP-01 serialization (expected {computed})")
    elif not verify_schnorr(bytes.fromhex(eid), pubkey, signature):
        problems.append(f"{label}: BIP-340 signature does not verify")
    return problems


def check_file(path: str) -> list[str]:
    text = Path(path).read_text(encoding="utf-8")
    lines = text.split("\n")
    problems: list[str] = []
    examples: list[EventExample] = []
    now = int(time.time())

    for match in FENCE.finditer(text):
        block = match.group(1)
        line_no = text[: match.start()].count("\n") + 1
        try:
            event = json.loads(block)
        except json.JSONDecodeError as exc:
            problems.append(f"{path}:{line_no}: fenced json block does not parse ({exc.msg})")
            continue
        if not isinstance(event, dict) or not any(marker in event for marker in ("id", "pubkey", "sig")):
            continue
        label = f"{path}:{line_no} (kind {event.get('kind')})"
        event_problems = validate_event(event, label, now)
        problems.extend(event_problems)
        start_line = line_no - 2
        if BAD_PROSE.search("\n".join(lines[max(0, start_line - 3):start_line])):
            problems.append(f"{label}: prose above the example admits it is illustrative or placeholder")
        examples.append(EventExample(line_no, event, not event_problems))

    for section_line, section in deep_dive_sections(text):
        mentioned_nips = set(NIP_MENTION.findall(section))
        section_end = section_line + section.count("\n")
        section_events = [example for example in examples if section_line <= example.line <= section_end and example.valid]
        if mentioned_nips != {"21"} and not section_events:
            problems.append(f"{path}:{section_line}: NIP deep dive requires at least one complete, cryptographically valid NIP-01 event; NIP-21-only is the exception")
        if "27" in mentioned_nips and not any(isinstance(example.event.get("content"), str) and "nostr:" in example.event["content"] for example in section_events):
            problems.append(f"{path}:{section_line}: NIP-27 deep dive requires a valid full event whose content contains a nostr: reference")

    return problems


def main() -> int:
    if len(sys.argv) < 2:
        print("usage: check_newsletter_event_examples.py <newsletter.md> [...]", file=sys.stderr)
        return 2
    problems = [problem for path in sys.argv[1:] for problem in check_file(path)]
    if problems:
        print("FAIL: invalid or missing Nostr event example(s):")
        for problem in problems:
            print(f"  - {problem}")
        return 1
    print("PASS: deep-dive event requirements, NIP-01 ids, and BIP-340 signatures are valid")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
