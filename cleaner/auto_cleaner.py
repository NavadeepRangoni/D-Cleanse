import pandas as pd
from .imputer import impute_missing
from .outliers import fix_outliers
from .validator import clean_types

def clean(df):
    report = {}
    df, rep1 = impute_missing(df)
    df, rep2 = fix_outliers(df)
    df, rep3 = clean_types(df)
    report.update(rep1)
    report.update(rep2)
    report.update(rep3)
    return df, report
