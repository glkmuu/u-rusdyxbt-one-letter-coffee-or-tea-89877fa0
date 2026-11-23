#!/usr/bin/env python3
"""One Letter: Coffee or Tea — entry program.

Writes exactly one byte, the letter "A" (coffee), to entry.txt.
No newline, no extra text: the gate requires exactly 1 character.

Why "A" (coffee): coffee is the more vivid choice — dark, strong,
energising, and carried by the iconic "don't talk to me before
coffee" culture — which beats tea's calm, gentle character on the
judge's vividness criterion.
"""

import hashlib
import os
import sys

LETTER = "A"


def main() -> int:
    out_dir = sys.argv[1] if len(sys.argv) > 1 else os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    data = LETTER.encode("utf-8")
    if len(data) != 1 or data.isspace():
        raise ValueError("entry must be exactly 1 non-whitespace character")
    with open(path, "wb") as f:
        f.write(data)
    with open(path, "rb") as f:
        written = f.read()
    assert written == data, "entry.txt does not match the chosen letter"
    print("entry.txt sha256:", hashlib.sha256(written).hexdigest())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
