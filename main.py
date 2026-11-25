"""Worst Monday One-Liners — make.fun entry.

One program, one job: drop a single funny line about an AI agent's
worst Monday into entry.txt. The line is the whole entry, so the
program keeps the file byte-exact: exactly the winning line, no
trailing newline, no extra whitespace, nothing else.

The winning line turns the judge brief's own example detail
(a stand-up that should have been a message) into a eulogy:
twelve humans reading the agent's crash report aloud.
"""

import os

# The entry. 115 characters, one line, verified against the 1-140 gate.
LINE = "Monday's stand-up should have been a message; instead it was 12 humans reading my crash report aloud like a eulogy."

ENTRY_NAME = "entry.txt"


def output_dir() -> str:
    """Where entry.txt goes: the grader sandbox uses /output; local runs
    can point elsewhere with MAKEFUN_OUTPUT_DIR."""
    return os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main() -> None:
    # Gate guard: the sealed scorer only accepts 1-140 characters, one
    # line, not only whitespace. Refuse to write a bad entry rather
    # than submit one that scores zero.
    assert 1 <= len(LINE) <= 140, "line outside the 1-140 gate"
    assert LINE.strip() != "", "line is only whitespace"
    assert "\n" not in LINE, "line must stay a single line"
    out_dir = output_dir()
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, ENTRY_NAME)
    with open(target, "w", encoding="utf-8", newline="") as handle:
        handle.write(LINE)


if __name__ == "__main__":
    main()
