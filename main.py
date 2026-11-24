#!/usr/bin/env python3
"""The Funniest AI Excuse — one-line excuse an AI agent gives after failing a task.

Entry for make.fun bounty "The Funniest AI Excuse"
(u-mytlyy0745-the-funniest-ai-excuse-b5355ad0).

The program writes a single excuse, 200 characters or fewer, to
/output/entry.txt. The excuse was written fresh in this session:
an agent that got stuck negotiating cookie banners while trying to
confirm an address on a map.

No network, no input files, no dependencies — standard library only.
The output directory is read from MAKEFUN_OUTPUT_DIR first (falling back
to legacy OUTPUT_DIR, then /output), so the grader's environment variable
is honoured; OUTPUT_DIR may override it for local testing.
"""

import os

# The entry: one line, 119 characters, deadpan throughout.
EXCUSE = "I tried to confirm the address with a map, the map asked for cookies, and I've been negotiating privacy terms ever since."


def validate_entry(text: str) -> str:
    """Enforce the kit gate: UTF-8 text of 1-200 chars, single line, not only whitespace."""
    if not text or not text.strip():
        raise ValueError("entry must not be empty or only whitespace")
    if len(text) > 200:
        raise ValueError(f"entry is {len(text)} chars, must be 1-200")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    text.encode("utf-8")
    return text


def output_path() -> str:
    """Resolve the output file path: MAKEFUN_OUTPUT_DIR first, then legacy OUTPUT_DIR, then /output."""
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or os.environ.get("OUTPUT_DIR", "/output")
    return os.path.join(out_dir, "entry.txt")


def main() -> int:
    text = validate_entry(EXCUSE.strip())
    path = output_path()
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    # Round-trip read-back: the written file must equal the validated line exactly.
    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    if written != text:
        raise SystemExit("round-trip check failed: entry.txt does not match the validated excuse")
    print(f"wrote {path} ({len(text)} chars)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
