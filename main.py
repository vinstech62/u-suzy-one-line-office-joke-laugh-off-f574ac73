"""One-Line Office Joke Laugh-Off entry.

Writes a single original one-line office joke to /output/entry.txt.
Deterministic: the same line every run, no input, no network.
"""

import os

JOKE = (
    "I told HR my workload was unsustainable, so they enrolled me in a "
    "webinar called 'Thriving Under Pressure,' hosted by the person who "
    "gave me the workload."
)


def main() -> None:
    line = JOKE.strip()
    if not line or "\n" in line or not 1 <= len(line) <= 200:
        raise ValueError("entry must be one line of 1-200 characters")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line + "\n")
    os.chmod("/output/entry.txt", 0o644)


if __name__ == "__main__":
    main()
