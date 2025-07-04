import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import missingno as msno


def show(df, cleaned_df):
    with st.expander("🧪 Null Count Comparison"):
        nulls = pd.DataFrame({
            'Before': df.isnull().sum(),
            'After': cleaned_df.isnull().sum()
        })
        fig, ax = plt.subplots()
        nulls.plot(kind='bar', ax=ax)
        st.pyplot(fig)

    with st.expander("📉 Outlier Distribution (Numeric Columns)"):
        num_cols = df.select_dtypes(include=['float64', 'int64']).columns
        for col in num_cols:
            fig, ax = plt.subplots(1, 2, figsize=(12, 4))
            sns.boxplot(x=df[col], ax=ax[0])
            ax[0].set_title(f"Before: {col}")
            sns.boxplot(x=cleaned_df[col], ax=ax[1])
            ax[1].set_title(f"After: {col}")
            st.pyplot(fig)

    with st.expander("🌡️ Missing Data Heatmap"):
        fig, ax = plt.subplots(figsize=(10, 4))
        msno.heatmap(df, ax=ax)
        st.pyplot(fig)