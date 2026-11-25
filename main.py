"""One-Line Laugh-Off entry.

Writes one original funny line to ``$MAKEFUN_OUTPUT_DIR/entry.txt``
(default ``/output``). Python 3.13 standard library only; no network,
no randomness, no input read.
"""

import os

LINE = (
    "I tried to ghost my gym, but it keeps texting 'we miss you' — "
    "buddy, I never showed up once. You miss a stranger."
)


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
