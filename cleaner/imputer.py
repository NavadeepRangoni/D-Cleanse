import pandas as pd

def impute_missing(df):
    report = {}
    for col in df.columns:
        if df[col].isnull().sum() > 0:
            if df[col].dtype == 'object':
                df[col].fillna(df[col].mode()[0], inplace=True)
                report[col] = "Filled with mode"
            else:
                df[col].fillna(df[col].median(), inplace=True)
                report[col] = "Filled with median"
    return df, report