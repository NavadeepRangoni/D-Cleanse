import streamlit as st

def show_raw_data(df):
    with st.expander("🔍 Raw Data Preview"):
        st.dataframe(df.head())
