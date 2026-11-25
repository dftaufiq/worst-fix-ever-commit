#!/usr/bin/env python3
"""Worst Fix Ever: Funniest Commit Message — make.fun entry.

Writes one commit message, the funniest line about a bug fix that made
everything worse, to /output/entry.txt.

The line is a literal in this file: deterministic, no network, no secrets,
no environment reads. Two runs produce byte-identical output.

Structure (2-beat + reveal, per the winning one-liner pattern): beat 1 is a
sensible maintenance fix — deduplicate the backups; the twist, mid-line, is
that the one copy kept was the corrupted one; the reveal, in the final
clause, is the consequence — 7 years of family photos gone. Specific number,
concrete loss, fresh angle (no backup entry in the field at build time), and
a real commit subject voice.
"""

import os

ENTRY = "fix: deduplicate the backups - kept one copy, the corrupted one; 7 years of family photos gone"


def main() -> None:
    text = ENTRY
    if not (1 <= len(text) <= 100):
        raise SystemExit(f"entry must be 1-100 chars, got {len(text)}")
    if not text.strip():
        raise SystemExit("entry must not be only whitespace")
    # Plain ASCII: byte count equals char count, which is the ranking
    # tie-break after playoff games (smaller text wins).
    if not text.isascii():
        raise SystemExit("entry must be plain ASCII")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(text)


if __name__ == "__main__":
    main()
