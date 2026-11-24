#!/usr/bin/env python3
"""The Dog Ate My Homework: Funniest Excuse.

Writes one line -- the excuse a dog gives after being caught eating the
homework -- to <OUTPUT_DIR>/entry.txt (default /output).

Stdlib only, offline, deterministic: the same line every run.
"""

import os

ENTRY = (
    "You said sit. You said stay. "
    "Nobody said don't eat the homework, "
    "so I followed the only instructions I had."
)


def main() -> None:
    # Fail loudly rather than ship an entry the gate would refuse.
    assert 1 <= len(ENTRY) <= 200, "entry must be 1-200 characters"
    assert ENTRY.strip(), "entry must not be only whitespace"
    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
