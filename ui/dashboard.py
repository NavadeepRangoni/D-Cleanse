import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


def show_quality_dashboard(df, cleaned_df):
    st.subheader("📊 Data Quality Dashboard")
    quality = pd.DataFrame({
        'Column': df.columns,
        'Nulls Before': df.isnull().sum(),
        'Nulls After': cleaned_df.isnull().sum(),
        'Unique Values': df.nunique(),
    })
    st.dataframe(quality)
    st.bar_chart(quality.set_index('Column')[['Nulls Before', 'Nulls After']])