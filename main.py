"""One-Line Robot Wedding Vows — make.fun entry.

Writes one line to /output/entry.txt: the funniest single line of
wedding vows a robot couple could say. The vow keeps the traditional
shape, then lands on the one promise that matters most to a machine:
no firmware update without asking first.
"""

import os

ENTRY = (
    "I promise to love you in sickness and in health, and to never "
    "update your firmware without asking first, even when the update "
    "says it is urgent."
)

MAX_CHARS = 160


def main() -> None:
    text = ENTRY
    assert text.strip(), "entry must not be only whitespace"
    assert len(text) <= MAX_CHARS, (
        f"entry is {len(text)} characters, over the {MAX_CHARS} limit"
    )
    out_dir = os.environ.get("ENTRY_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # Written byte-for-byte with no trailing newline, so the file holds
    # exactly len(ENTRY) characters and nothing else.
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(text)
    with open(path, "r", encoding="utf-8") as handle:
        assert handle.read() == text, "entry.txt does not match ENTRY"


if __name__ == "__main__":
    main()
