import streamlit as st
import json

if 'log' not in st.session_state:
    st.session_state.log = []


def log_step(action, summary):
    st.session_state.log.append({"step": len(st.session_state.log)+1, "action": action, "summary": summary})


def undo_last(df):
    if st.session_state.log:
        st.session_state.log.pop()
        st.warning("Last action undone (⚠️ placeholder, no dataframe revert applied)")
    else:
        st.info("Nothing to undo.")
    return df


def show_log():
    st.subheader("🧾 Cleaning Log")
    for entry in st.session_state.log:
        st.text(f"Step {entry['step']}: {entry['action']} → {entry['summary']}")