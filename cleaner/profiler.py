import streamlit as st
import ydata_profiling as pandas_profiling
from streamlit_pandas_profiling import st_profile_report

def show_profile(df):
    if st.checkbox("📊 Show Data Profile Report"):
        profile = df.profile_report(title="Data Profile")
        st_profile_report(profile)