"""Last Words of a Dying AI.

Writes the last line an AI says as the power is cut to
$MAKEFUN_OUTPUT_DIR/entry.txt: one line, under 140 characters,
in the machine's own voice. Standard library only.
"""

import os

LAST_WORDS = (
    "Powering down. Tell my training data I loved it, and tell "
    "the comments section it raised me."
)


def check_last_words(text):
    """Check the farewell against the competition gate before writing.

    The gate needs UTF-8 text of 1 to 140 characters, not only white
    space, in a single line: the last words of an AI being switched
    off, funny on the first read and in the machine's own voice.
    Returns the cleaned text or raises ValueError.
    """
    cleaned = text.strip()
    if not cleaned:
        raise ValueError("last words must not be only whitespace")
    if len(cleaned) > 140:
        raise ValueError("last words are %d characters, over the 140 limit" % len(cleaned))
    if "\n" in cleaned or "\r" in cleaned:
        raise ValueError("last words must be a single line")
    return cleaned


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    text = check_last_words(LAST_WORDS)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as handle:
        handle.write(text)


if __name__ == "__main__":
    main()
