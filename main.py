"""Entry program for make.fun bounty
u-kevin-the-funniest-office-joke-judged-head-to-head-3dc3233c.

Writes one single-line office joke to $MAKEFUN_OUTPUT_DIR/entry.txt
(falling back to /output/entry.txt), as the gate requires:
UTF-8 text, 1 to 200 characters, not only white space.
"""

import os

JOKE = (
    "The meeting that could have been an email ended with a follow-up "
    "meeting to schedule another meeting about why it couldn't have "
    "been an email."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
