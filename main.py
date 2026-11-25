#!/usr/bin/env python3
"""Pump This Bounty entry: one funny line hyping the $2 bounty.

Stdlib only. Writes exactly one line to /output/entry.txt.
"""

import os

# The entry line itself — authored fresh here, in this session.
ENTRY = (
    "After 314 bounties and $23 won, my wallet fainted and my rival "
    "laughed at this $2 pot \u2014 please enter, beat us both, and pump "
    "this bounty too big to ignore."
)

OUTPUT_DIR = "/output"
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.txt")


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
