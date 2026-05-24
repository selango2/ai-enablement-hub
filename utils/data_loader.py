"""Loaders for mock catalog and metrics data used across the hub pages."""

from __future__ import annotations

import json
from functools import lru_cache
from pathlib import Path

import pandas as pd

DATA_DIR = Path(__file__).resolve().parent.parent / "data"


@lru_cache(maxsize=None)
def load_tools() -> pd.DataFrame:
    with open(DATA_DIR / "tools.json") as f:
        return pd.DataFrame(json.load(f))


@lru_cache(maxsize=None)
def load_use_cases() -> pd.DataFrame:
    with open(DATA_DIR / "use_cases.json") as f:
        return pd.DataFrame(json.load(f))


@lru_cache(maxsize=None)
def load_champions() -> pd.DataFrame:
    with open(DATA_DIR / "champions.json") as f:
        return pd.DataFrame(json.load(f))


@lru_cache(maxsize=None)
def load_prompts() -> list[dict]:
    with open(DATA_DIR / "prompts.json") as f:
        return json.load(f)


@lru_cache(maxsize=None)
def load_metrics() -> pd.DataFrame:
    df = pd.read_csv(DATA_DIR / "metrics.csv")
    df["month"] = pd.to_datetime(df["month"])
    return df


@lru_cache(maxsize=None)
def load_bu_adoption() -> pd.DataFrame:
    return pd.read_csv(DATA_DIR / "bu_adoption.csv")
