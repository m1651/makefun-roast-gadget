#!/usr/bin/env python3
"""One-Line Roast: The Gadget You Use Every Day.

Writes a single original roast line to entry.txt in the output
directory (MAKEFUN_OUTPUT_DIR, default /output). Deterministic:
every run writes the exact same bytes, no network, stdlib only.
"""

import os

ROAST = (
    "My phone unlocks instantly for my cat's paw, but when I'm "
    "carrying groceries in the rain it wants my face, my passcode, "
    "and a blood oath."
)


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(ROAST)


if __name__ == "__main__":
    main()
