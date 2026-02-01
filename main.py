"""
CSV Cleaner (CLI)

A professional command-line tool to clean and normalize messy CSV files.

Author: Michel Brochu
Version: 1.0.0
"""

from __future__ import annotations

import sys
from pathlib import Path

import pandas as pd

from csv_cleaner.cli import parse_args
from csv_cleaner.cleaner import CleanOptions, clean_dataframe, default_output_path


def main(argv: list[str] | None = None) -> int:
    """
    Application entry point.
    Handles CLI arguments, file I/O, and execution flow.
    """
    args = parse_args(argv)

    # Validate input path
    input_path: Path = args.input
    if not input_path.exists():
        print(f"Error: input file not found: {input_path}")
        return 2

    # Determine output path
    output_path: Path = args.output if args.output else default_output_path(input_path)

    # Build cleaning options
    options = CleanOptions(
        dedup=bool(args.dedup),
        drop_empty=bool(args.drop_empty),
        normalize_cols=bool(args.normalize_cols),
    )

    # Read CSV into DataFrame
    df = pd.read_csv(input_path, encoding=args.encoding)
    before_rows = len(df)

    # Apply cleaning pipeline
    cleaned_df = clean_dataframe(df, options)
    after_rows = len(cleaned_df)

    # Write cleaned CSV to disk
    cleaned_df.to_csv(output_path, index=False, encoding=args.encoding)

    # User feedback
    print("✔ Cleaning complete")
    print(f"Input : {input_path} ({before_rows} rows)")
    print(f"Output: {output_path} ({after_rows} rows)")

    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
