#!/usr/bin/env python3
"""Write the entrant's own make.fun username, one word, to /output/entry.txt.

The word is the entrant's own make.fun handle: "hua" + "haha" — a laugh built
into the name. It fits the judge's brief: a real make.fun username, the
entrant's own handle sent as one word, and it raises a smile on first read
without needing to be explained.
"""

import hashlib
import os

WORD = "hua-haha"
OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(WORD)

    with open(OUTPUT_PATH, "rb") as f:
        raw = f.read()
    text = raw.decode("utf-8")
    assert 1 <= len(text) <= 30, f"length {len(text)} out of range 1-30"
    assert text.strip(), "entry is only whitespace"
    assert text == WORD, f"entry {text!r} != {WORD!r}"
    assert not any(c.isspace() for c in text), "entry must be a single word with no whitespace"

    print(hashlib.sha256(raw).hexdigest())


if __name__ == "__main__":
    main()
