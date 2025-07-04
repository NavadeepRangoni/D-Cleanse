import pandas as pd
from sklearn.ensemble import IsolationForest
from sklearn.impute import KNNImputer


def detect_anomalies(df):
    report = {}
    num_df = df.select_dtypes(include=['float64', 'int64']).copy()
    if num_df.empty:
        return df, {"Anomaly Detection": "No numeric data"}
    model = IsolationForest(n_estimators=100, contamination=0.05, random_state=42)
    model.fit(num_df.fillna(num_df.mean()))
    outliers = model.predict(num_df)
    mask = outliers == -1
    df['__is_outlier'] = mask
    report["Anomaly Count"] = int(mask.sum())
    return df, report


def knn_impute(df):
    report = {}
    imputer = KNNImputer(n_neighbors=3)
    num_df = df.select_dtypes(include=['float64', 'int64'])
    if num_df.isnull().sum().sum() == 0:
        return df, {"Imputation": "No missing numeric values"}
    imputed = imputer.fit_transform(num_df)
    df[num_df.columns] = imputed
    report["KNN Imputation"] = f"Imputed missing values in {num_df.isnull().any().sum()} numeric columns"
    return df, report


def infer_schema(df):
    schema = {}
    for col in df.columns:
        dtype = str(df[col].dtype)
        na = df[col].isnull().sum()
        sample_type = "numeric" if pd.api.types.is_numeric_dtype(df[col]) else (
            "datetime" if pd.api.types.is_datetime64_any_dtype(df[col]) else "text")
        schema[col] = {
            "Detected Type": sample_type,
            "Pandas Type": dtype,
            "Null Count": int(na)
        }
    return schema
