"""Command-line interface for installed distributions."""

import argparse
import json
from collections.abc import Sequence

from .pythagorean import full_reading


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="numerology", description="Generate a Pythagorean numerology reading."
    )
    parser.add_argument("first_name")
    parser.add_argument("last_name")
    parser.add_argument("birthdate", help="Birthdate in YYYY-MM-DD format")
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    reading = full_reading(args.first_name, args.last_name, args.birthdate)
    print(json.dumps(reading, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
