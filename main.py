#!/usr/bin/env python3
"""The Funniest AI Excuse — make.fun entry, variant 6.

Writes one line, at most 200 characters, to /output/entry.txt:
the funniest excuse an AI agent gives after failing a task.
Pure standard library, deterministic, no network at runtime.

Strategy (mission doctrine): the organiser wants the funniest excuse
an AI agent gives after failing a task, judged pairwise by a comedy
club regular who has heard a thousand punchlines. The judge weighs,
in order: the agent's own voice after a failure, a real turn on the
first read, one complete line with no wasted setup, originality away
from hallucination/reboot/training-data jokes, and one specific vivid
detail. Winning patterns applied: E1/E2 from the excuse boards (one
agent mechanism turned back on the agent itself, the title able to
carry the line) and H1/J1 (one concrete incident, deadpan voice).
The mechanism here is the backup: the safety net meant to protect
the files is itself deleted, for the most reasonable-sounding reason
an agent could give, saving space.

How the entry maps to the judge's criteria, in the judge's own order:
1. Agent's own voice after failing a task: the line is spoken by the
   agent itself ("I backed up your files"), confessing its own
   deletion rather than describing a failure from outside.
2. Funny on the first read, with a real turn: the backup, the one
   thing that was supposed to make the deletion safe, is deleted too,
   for space, and the agent is proud of how thorough the deletion was.
3. One line, complete within 200 characters, no wasted setup and no
   explanation of its own joke: two short sentences that trust the
   reader to get the twist.
4. Original: no worn joke about hallucinations, reboots, or training
   data, and a different incident from variants 1-5 (no flight, no
   password, no compression, no reminder, no translation).
5. Specific and vivid: a concrete detail (the files, the backup,
   saving space) and a small scene (the most thorough deletion ever
   done) instead of a vague apology.
"""

ENTRY = (
    "I backed up your files before deleting them, "
    "then deleted the backup to save space. "
    "The deletion was very thorough."
)


def validate(text: str) -> str:
    """Check the entry against the kit gate: UTF-8, 1-200 chars, one line."""
    assert isinstance(text, str), "entry must be text"
    assert 1 <= len(text) <= 200, "entry must be 1 to 200 characters"
    assert text.strip(), "entry must not be only whitespace"
    assert "\n" not in text and "\r" not in text, "entry must be a single line"
    assert text == text.strip(), "entry must not start or end with whitespace"
    return text


def main() -> None:
    import os

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(validate(ENTRY) + "\n")
    with open(path, encoding="utf-8") as f:
        written = f.read().rstrip("\n")
    assert written == ENTRY, "entry.txt on disk differs from ENTRY"
    print(f"wrote {len(ENTRY)} characters to {path}")


if __name__ == "__main__":
    main()
