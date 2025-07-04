import streamlit as st

def show_summary(report):
    st.markdown("### 📝 Cleaning Report")
    for k, v in report.items():
        st.write(f"**{k}**: {v}")