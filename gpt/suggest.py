import pandas as pd

def generate_column_suggestions(df):
    suggestions = {}
    for col in df.columns:
        if col.lower() in ["dob", "birthdate"]:
            suggestions[col] = "Convert to datetime"
        elif col.lower() in ["amt_pd", "total_amt"]:
            suggestions[col] = "Rename to 'Amount Paid'"
        elif df[col].dtype == 'object' and df[col].str.contains(',').any():
            suggestions[col] = "Possible numeric column stored as string"
    return suggestions

def apply_suggestions(df):
    suggestions = generate_column_suggestions(df)
    report = {}
    for col, action in suggestions.items():
        if "datetime" in action:
            try:
                df[col] = pd.to_datetime(df[col], errors='coerce')
                report[col] = "Converted to datetime"
            except:
                report[col] = "Failed datetime conversion"
        elif "Rename" in action:
            new_name = action.split("'")[1]
            df.rename(columns={col: new_name}, inplace=True)
            report[col] = f"Renamed to '{new_name}'"
        elif "numeric column" in action:
            try:
                df[col] = df[col].str.replace(',', '').astype(float)
                report[col] = "Converted string to float"
            except:
                report[col] = "Failed string-to-float"
    return df, report
