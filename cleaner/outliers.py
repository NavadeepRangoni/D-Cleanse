import pandas as pd
import numpy as np

def fix_outliers(df):
    report = {}
    for col in df.select_dtypes(include=['float64', 'int64']):
        q1 = df[col].quantile(0.25)
        q3 = df[col].quantile(0.75)
        iqr = q3 - q1
        lower = q1 - 1.5 * iqr
        upper = q3 + 1.5 * iqr
        before = df[col].copy()
        df[col] = np.clip(df[col], lower, upper)
        changes = sum(before != df[col])
        if changes:
            report[col] = f"Capped {changes} outliers"
    return df, report
