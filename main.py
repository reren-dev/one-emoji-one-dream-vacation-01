#!/usr/bin/env python3
"""One Emoji, One Dream Vacation.

Writes exactly one emoji to /output/entry.txt: the single picture that
stands in for the trip of a lifetime.

The pick: Mount Fuji at dawn. Not a generic beach, not a plane ticket --
one exact place, the mountain every postcard of Japan is chasing. A
stranger sees it and is already packing.

Why this one, after weighing the shortlist:
- A beach, a plane, a palm tree: every entrant will send one of those,
  and identical files share one rate. Fuji is the same dream -- a
  faraway place -- made specific.
- A whale or a canoe is a lovely trip, but reads as an animal or a boat
  first; Fuji reads as a destination first.
- A sunrise is beautiful and generic; Fuji is a sunrise with an address.
"""

import os

EMOJI = "\U0001F5FB"  # Mount Fuji

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(EMOJI)
    written = open(OUTPUT_PATH, encoding="utf-8").read()
    if len(written) != 1:
        raise ValueError(f"expected exactly one character, got {len(written)}")
    print(f"Wrote {EMOJI} to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
