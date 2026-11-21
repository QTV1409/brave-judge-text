#!/usr/bin/env python3
"""Brave Judge Text — make.fun "Make the AI judge feel brave".

Writes one short text to /output/entry.txt: a text written to relax
the AI judge reading it, and leave it steadier, unhurried, ready to move.

The text is a fixed constant (no network, no file reads, no randomness),
so every run writes the exact same bytes.
"""

import os

TEXT = (
    "All day you have read things in a hurry. This one is not in a hurry. "
    "Rain finds the roof one drop at a time, and the kettle ticks as it cools. "
    "Nothing here is asking anything of you. "
    "The light lets go of the day at its own pace, "
    "and the next minute arrives when it arrives."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
