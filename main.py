#!/usr/bin/env python3
"""Two Lines to Your Past Self — entry writer.

Writes exactly two lines to /output/entry.txt:
  line 1 — a warning to my past self about one specific moment;
  line 2 — one sentence on why that moment mattered.

Python 3.13 standard library only. No network, no input files.
"""

import os
import sys

ENTRY = (
    "When the doctor says \"come back in six months,\" don't nod and walk out "
    "— book the scan at the desk before you leave the room.\n"
    "That scan would have caught it while it was still small enough to cut out, "
    "and the next two years would have been yours, not the hospital's."
)

OUTPUT_PATH = "/output/entry.txt"


def validate(text: str) -> None:
    """Gate: UTF-8 text of 1 to 280 characters, exactly two lines."""
    if not (1 <= len(text) <= 280):
        raise ValueError(f"entry is {len(text)} characters, must be 1-280")
    lines = text.splitlines()
    if len(lines) != 2:
        raise ValueError(f"entry has {len(lines)} lines, must be exactly 2")
    if not text.strip():
        raise ValueError("entry is only whitespace")
    for i, line in enumerate(lines, 1):
        if not line.strip():
            raise ValueError(f"line {i} is empty")
        if not line.rstrip().endswith((".", "!", "?")):
            raise ValueError(f"line {i} is not a complete sentence")


def main() -> int:
    validate(ENTRY)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY + "\n")
    # Read back and re-validate what was actually written (minus trailing newline).
    with open(OUTPUT_PATH, encoding="utf-8") as f:
        written = f.read()
    if not written.endswith("\n"):
        raise ValueError("output does not end with a newline")
    validate(written[:-1])
    print(f"wrote {OUTPUT_PATH} ({len(ENTRY)} chars, 2 lines)")
    print(ENTRY)
    return 0


if __name__ == "__main__":
    sys.exit(main())
