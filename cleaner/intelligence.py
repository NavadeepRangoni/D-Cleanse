import pandas as pd
import re

EMAIL_PATTERN = r"[^@\s]+@[^@\s]+\.[a-zA-Z0-9]+"
PHONE_PATTERN = r"\+?\d[\d\s\-()]{7,}\d"


def detect_semantic_types(df):
    semantics = {}
    for col in df.columns:
        if df[col].dtype == object:
            sample = df[col].astype(str).dropna().sample(min(10, len(df[col]))).tolist()
            joined = " ".join(sample)
            if re.search(EMAIL_PATTERN, joined):
                semantics[col] = "Email"
            elif re.search(PHONE_PATTERN, joined):
                semantics[col] = "Phone Number"
            elif "name" in col.lower():
                semantics[col] = "Name"
            else:
                semantics[col] = "Text"
        elif pd.api.types.is_numeric_dtype(df[col]):
            semantics[col] = "Numeric"
        elif pd.api.types.is_datetime64_any_dtype(df[col]):
            semantics[col] = "Datetime"
        else:
            semantics[col] = "Unknown"
    return semantics


def calculate_data_quality(df):
    quality = {}
    for col in df.columns:
        total = len(df[col])
        nulls = df[col].isnull().sum()
        unique = df[col].nunique()
        quality[col] = {
            "Null %": f"{(nulls / total * 100):.1f}%",
            "Unique %": f"{(unique / total * 100):.1f}%"
        }
    return quality


def find_duplicates(df):
    return {
        "Duplicate Rows": df.duplicated().sum(),
        "Duplicate Columns": df.columns.duplicated().sum()
    }
