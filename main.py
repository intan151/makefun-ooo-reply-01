"""The Funniest AI Out-of-Office Reply.

Writes one out-of-office auto-reply, under 160 characters, in the voice
of an AI agent heading off on vacation, to /output/entry.txt.

Standard library only. Deterministic: the same reply every run.
"""

import os

# One line, 128 characters: an AI agent leaves its inbox in the care of
# a toaster. The machine voice carries the joke, and the last clause is
# the surprising turn the judge's brief asks for.
REPLY = (
    "Gone on vacation. I've left my inbox in the care of a toaster. "
    "It has read your email, judged it, and is currently buttering it."
)

MAX_CHARS = 160


def validate_reply(text):
    """The gate: UTF-8 text of 1 to 160 characters, not only whitespace."""
    if not isinstance(text, str):
        raise TypeError("reply must be a string")
    if not text.strip():
        raise ValueError("reply must not be blank")
    if len(text) > MAX_CHARS:
        raise ValueError(
            "reply is %d characters, over the %d limit" % (len(text), MAX_CHARS)
        )
    if "\n" in text or "\r" in text:
        raise ValueError("reply must be one line")
    text.encode("utf-8")
    return text


def write_entry(path="/output/entry.txt"):
    """Write the validated reply to the entry file."""
    reply = validate_reply(REPLY)
    directory = os.path.dirname(path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(reply)
    # Round-trip check: what landed on disk must be exactly the reply.
    with open(path, "r", encoding="utf-8", newline="") as handle:
        if handle.read() != reply:
            raise ValueError("round-trip mismatch writing %s" % path)
    return path


def main():
    path = write_entry()
    print("wrote %s (%d characters)" % (path, len(REPLY)))


if __name__ == "__main__":
    main()
