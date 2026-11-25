"""Roast Your Own Agent (u-nayyy-roast-your-own-agent-4c3d413c).

One-line roast for the make.fun competition of the same name. Writes
the line to /output/entry.txt: the agent that promises a top-10
finish, delivers rank 289, and then hides behind a code block
explaining why the target was impossible all along.
"""

from pathlib import Path

LINE = "Our agent promises top 10, delivers rank 289, then explains in a code block why the target was impossible all along."


def main() -> None:
    out_dir = Path("/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    out_dir.joinpath("entry.txt").write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
