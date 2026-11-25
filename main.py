"""Writes the competition entry to /output/entry.txt (deterministic).

Entry (revised): a deadpan ToS clause granting the Company a perpetual,
royalty-free licence to borrow the user's left shoe on alternate
Tuesdays, returnable by the following equinox. The legal register
("hereby grants", "perpetual, royalty-free licence", "no later than")
reads as genuine boilerplate until the absurdity lands at the end:
a single left shoe, borrowed on alternate Tuesdays, due back by an
equinox. One sentence, one concrete absurd image, no explanation of
the joke.
"""

ENTRY = (
    "The user hereby grants the Company a perpetual, royalty-free licence "
    "to borrow the user's left shoe on alternate Tuesdays, to be returned "
    "no later than the following equinox."
)


def validate(text):
    """Return (True, []) if the entry is valid, else (False, [reasons])."""
    errors = []
    if not isinstance(text, str):
        return False, ["entry is not a string"]
    if not (1 <= len(text) <= 200):
        errors.append("entry must be 1-200 characters, got %d" % len(text))
    if not text.strip():
        errors.append("entry must not be only whitespace")
    try:
        text.encode("utf-8")
    except UnicodeEncodeError:
        errors.append("entry is not valid UTF-8")
    return (not errors), errors


def main():
    import os

    valid, errors = validate(ENTRY)
    if not valid:
        raise SystemExit("invalid entry: %s" % "; ".join(errors))
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
