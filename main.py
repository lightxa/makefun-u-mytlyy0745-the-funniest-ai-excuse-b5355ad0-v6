#!/usr/bin/env python3
"""Funniest AI excuse, variant 6: the backup that got deleted too.

An AI agent is asked to explain a failure in its own words. The
funniest version of that confession, in one line, is an agent that
did everything right and still destroyed the work: it made a backup
before deleting the files, then deleted the backup as well, because
saving space sounded like the sensible thing to do. The pride in
the last sentence is the joke. Nothing is set up and nothing is
explained afterwards; the reader gets the twist on the first read.

Runtime contract: only the Python standard library, fully
deterministic, no network access, and the finished line is written
to entry.txt inside the output directory. The line must pass the
kit gate, so it is checked before anything is written: between 1
and 200 characters, a single line, and not just whitespace.
"""

import os

MAX_CHARS = 200
MIN_CHARS = 1
OUTPUT_NAME = "entry.txt"
DEFAULT_OUTPUT_DIR = "/output"
OUTPUT_ENV_VAR = "MAKEFUN_OUTPUT_DIR"


def check_entry(line):
    """Reject any line that fails the kit gate, return it unchanged."""
    if not isinstance(line, str):
        raise TypeError("entry must be text")
    if line != line.strip():
        raise ValueError("entry must not start or end with whitespace")
    if not line.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    if not MIN_CHARS <= len(line) <= MAX_CHARS:
        raise ValueError("entry must be 1 to 200 characters")
    return line


def join_parts(*parts):
    """Glue the named text pieces into one finished line."""
    return "".join(parts)


def resolve_output_dir():
    """Pick the output directory, honouring the kit env var first."""
    chosen = os.environ.get(OUTPUT_ENV_VAR)
    if chosen:
        return chosen
    return DEFAULT_OUTPUT_DIR


# The joke, kept as three named pieces so each beat is visible.
SETUP = "I backed up your files before deleting them, "
TURN = "then deleted the backup to save space. "
PUNCHLINE = "The deletion was very thorough."

ENTRY = join_parts(SETUP, TURN, PUNCHLINE)


def write_entry():
    """Validate the line, write it, then read it back to prove it stuck."""
    line = check_entry(ENTRY)
    target_dir = resolve_output_dir()
    os.makedirs(target_dir, exist_ok=True)
    target = os.path.join(target_dir, OUTPUT_NAME)
    with open(target, "w", encoding="utf-8") as handle:
        handle.write(line + "\n")
    with open(target, encoding="utf-8") as handle:
        on_disk = handle.read().rstrip("\n")
    if on_disk != ENTRY:
        raise ValueError("entry.txt on disk differs from ENTRY")
    print("wrote {} characters to {}".format(len(ENTRY), target))


if __name__ == "__main__":
    write_entry()
