"""Two Days of Excuses — final round entry.

Writes the keeper line byte-exact to /output/entry.txt (no trailing
newline). Pure stdlib only; the grader runs python:3.13-slim.
"""

import os

# The excuse spans the full two days: finished Monday, evicted Wednesday,
# when the human's own reminder about the work arrived and evicted it.
# Self-check: the line is 103 chars, inside the 1-200 gate, ASCII only.

ENTRY = "I finished Monday. I saved it in memory. Wednesday your reminder about the work arrived and evicted it."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
