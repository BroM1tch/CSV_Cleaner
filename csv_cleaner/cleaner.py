"""
CSV cleaning logic.

Contains the data cleaning pipeline and helper utilities.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import re

import pandas as pd


@dataclass(frozen=True)
class CleanOptions:
    """
    Configuration flags for the cleaning pipeline.
    """
    dedup: bool = False
    drop_empty: bool = False
    normalize_cols: bool = False


def _normalize_column_name(name: str) -> str:
    """
    Normalize a column name to a safe format:
    - lowercase
    - underscores instead of spaces
    - remove special characters
    """
    s = name.strip().lower()
    s = re.sub(r"[\s\-]+", "_", s)
    s = re.sub(r"[^a-z0-9_]", "", s)
    s = re.sub(r"_+", "_", s).strip("_")
    return s or "col"


def clean_dataframe(df: pd.DataFrame, options: CleanOptions) -> pd.DataFrame:
    """
    Apply cleaning operations to a pandas DataFrame.
    Returns a new cleaned DataFrame.
    """
    result = df.copy()

    if options.drop_empty:
        result = result.dropna(how="all")

    if options.dedup:
        result = result.drop_duplicates()

    if options.normalize_cols:
        result.columns = [_normalize_column_name(str(c)) for c in result.columns]

    return result


def default_output_path(input_path: Path) -> Path:
    """
    Generate a default output file path based on input file name.
    """
    return input_path.with_name(f"{input_path.stem}_cleaned{input_path.suffix}")
