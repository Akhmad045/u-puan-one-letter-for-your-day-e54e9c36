#!/usr/bin/env python3
"""Entry for make.fun competition
"u-puan-one-letter-for-your-day-e54e9c36": One Letter for Your Day.

Writes exactly one letter, A-Z, to /output/entry.txt: the letter K,
standing for the word "kaput" — the day broke down completely, the
machine gave up, nothing left to salvage. One sharp picture, funny
the moment it lands, and honest about a real day that fell apart.
Standard library only, no network.
"""

import os

# The word behind the letter: "kaput" — the day broke down completely,
# the machine gave up, nothing left to salvage. The letter is the
# word's own initial, so the entry stays honest to the judge's brief.
WORD = "kaput"
LETTER = WORD[0].upper()


def main() -> None:
    assert LETTER == "K" and len(LETTER) == 1 and LETTER.isalpha()
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LETTER)


if __name__ == "__main__":
    main()
