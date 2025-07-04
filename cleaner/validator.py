import pandas as pd

def clean_types(df):
    report = {}
    for col in df.columns:
        if df[col].dtype == object:
            try:
                df[col] = pd.to_datetime(df[col])
                report[col] = "Converted to datetime"
            except:
                pass
    return df, report