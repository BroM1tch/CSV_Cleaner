from __future__ import annotations

import argparse
from pathlib import Path


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="csv-cleaner",
        description="Clean and normalize messy CSV files.",
    )

    parser.add_argument(
        "input",
        type=Path,
        help="Path to input CSV file",
    )

    parser.add_argument(
        "-o",
        "--output",
        type=Path,
        default=None,
        help="Path to output CSV file (default: <input>_cleaned.csv)",
    )

    parser.add_argument(
        "--dedup",
        action="store_true",
        help="Remove duplicate rows",
    )

    parser.add_argument(
        "--drop-empty",
        action="store_true",
        help="Drop fully empty rows",
    )

    parser.add_argument(
        "--normalize-cols",
        action="store_true",
        help="Normalize column names (lowercase, underscores)",
    )

    parser.add_argument(
        "--encoding",
        default="utf-8",
        help="CSV encoding (default: utf-8)",
    )

    return parser


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = build_parser()
    return parser.parse_args(argv)
