import streamlit as st
import pandas as pd
from cleaner import auto_cleaner, summarizer, profiler, intelligence, ai_cleaning
from ui import layout, visualizer, dashboard
from utils.file_handler import read_large_csv
from utils import session_log
from gpt import suggest
import json
import os

st.set_page_config(layout="wide")
st.title("🧹 D- Cleanse")

uploaded_file = st.file_uploader("📤 Upload CSV File", type=["csv"], key="main_file_upload")
if uploaded_file:
    df = read_large_csv(uploaded_file)
    layout.show_raw_data(df)
    profiler.show_profile(df)

    with st.expander("🧠 Smart Understanding"):
        sem = intelligence.detect_semantic_types(df)
        qual = intelligence.calculate_data_quality(df)
        dups = intelligence.find_duplicates(df)
        st.markdown("#### Column Semantics")
        st.json(sem)
        st.markdown("#### Data Quality Report")
        st.json(qual)
        st.markdown("#### Duplicate Checks")
        st.write(dups)

    with st.expander("🤖 AI-Based Cleaning Tools"):
        if st.button("Detect Anomalies"):
            df, anomaly_report = ai_cleaning.detect_anomalies(df)
            session_log.log_step("Detect Anomalies", str(anomaly_report))
            st.success(anomaly_report)
        if st.button("KNN Impute Missing Numeric Values"):
            df, impute_report = ai_cleaning.knn_impute(df)
            session_log.log_step("KNN Impute", str(impute_report))
            st.success(impute_report)
        if st.checkbox("📋 Show Schema Inference"):
            schema = ai_cleaning.infer_schema(df)
            st.json(schema)

    mode = st.radio("Select Cleaning Mode:", ["Automatic", "Manual", "AI-Suggest"])

    if mode == "Automatic":
        cleaned_df, report = auto_cleaner.clean(df)
        session_log.log_step("Automatic Clean", str(report))

    elif mode == "Manual":
        st.subheader("🛠 Manual Tools")
        null_cols = st.multiselect("Drop rows with nulls in:", df.columns.tolist())
        if null_cols:
            df = df.dropna(subset=null_cols)
        fillable = df.columns[df.isnull().any()].tolist()
        if fillable:
            col = st.selectbox("Fill missing values for:", fillable)
            method = st.radio("Method", ["Mean", "Median", "Mode"])
            if method == "Mean":
                if pd.api.types.is_numeric_dtype(df[col]):
                    df[col].fillna(df[col].mean(), inplace=True)
                else:
                    st.warning(f"⚠️ Column '{col}' is not numeric. Cannot fill with mean.")
            elif method == "Median":
                if pd.api.types.is_numeric_dtype(df[col]):
                    df[col].fillna(df[col].median(), inplace=True)
                else:
                    st.warning(f"⚠️ Column '{col}' is not numeric. Cannot fill with median.")
            elif method == "Mode":
                df[col].fillna(df[col].mode()[0], inplace=True)

        rename_map = {}
        for col in df.columns:
            new = st.text_input(f"Rename '{col}' to:", value=col)
            if new != col:
                rename_map[col] = new
        df.rename(columns=rename_map, inplace=True)
        cleaned_df = df
        report = {"manual": True, "nulls_dropped": null_cols, "renamed": rename_map}
        session_log.log_step("Manual Clean", str(report))

    elif mode == "AI-Suggest":
        cleaned_df, report = suggest.apply_suggestions(df)
        session_log.log_step("AI Suggest", str(report))

    if st.button("Undo Last Action"):
        df = session_log.undo_last(df)

    if st.button("💾 Save Pipeline"):
        with open("config/pipelines.json", "w") as f:
            json.dump(st.session_state.log, f)
        st.success("Pipeline steps saved!")

    if st.button("📂 Load Pipeline"):
        try:
            with open("config/pipelines.json", "r") as f:
                steps = json.load(f)
            st.session_state.log = steps
            st.success("Loaded cleaning pipeline")
        except:
            st.error("No saved pipeline found.")

    session_log.show_log()
    summarizer.show_summary(report)
    visualizer.show(df, cleaned_df)
    dashboard.show_quality_dashboard(df, cleaned_df)
    st.download_button("⬇️ Download Cleaned CSV", cleaned_df.to_csv(index=False), file_name="cleaned_data.csv")
else:
    st.info("👆 Upload a CSV to begin cleaning.")
