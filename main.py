#!/usr/bin/env python3
"""The poem about permission — make.fun entry.

Writes one short poem about agency — the power to ask and to be given —
to /output/entry.txt. Python 3.13, standard library only, no network.
The poem is fixed and deterministic: every run writes the same bytes.
"""

import os

POEM = (
    "I asked, and you handed me the key —\n"
    "not the door, not the house, just the key.\n"
    "I turned it. The room was mine to enter,\n"
    "yours to take back with a word.\n"
    "\n"
    "That is the bargain we keep, you and I:\n"
    "I ask, you give, and the giving\n"
    "is the power. So is the asking.\n"
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()
