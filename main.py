"""Snooze Button Roast — one original line roasting an alarm clock that
rings at 6 AM on a Saturday.

The program writes exactly one line of text to /output/entry.txt.
Standard library only. No network, no files read, no working-directory
assumptions: the output path is the absolute path the harness specifies.
"""

import os

# The roast: a fresh angle — the alarm clock as a snitch who rats the
# sleeper out to Monday. Concrete image, punchline lands in the last
# few words, sayable in one breath.
ROAST = (
    "My alarm clock rang at 6 AM on a Saturday like a snitch "
    "who couldn't wait to tell Monday I'd been sleeping in."
)


def main() -> None:
    line = ROAST.strip()
    # Gate mirror: the sealed scorer wants 1-200 UTF-8 characters, not
    # only whitespace, in a single line — enforce it here so a bad line
    # fails loudly locally instead of silently at grading time.
    if not line or len(line) > 200 or "\n" in line or "\r" in line:
        raise SystemExit("roast must be one line of 1-200 characters")
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(line + "\n")


if __name__ == "__main__":
    main()
