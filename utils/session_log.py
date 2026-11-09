
import streamlit as st
import json


def initialize_log():
    """Initialize the cleaning log for the current session."""
    if "log" not in st.session_state:
        st.session_state.log = []


def log_step(action, summary):
    """Record a cleaning action."""
    initialize_log()

    st.session_state.log.append({
        "step": len(st.session_state.log) + 1,
        "action": action,
        "summary": summary
    })


def undo_last(df):
    """Remove the last log entry (does not revert dataframe changes)."""
    initialize_log()

    if st.session_state.log:
        st.session_state.log.pop()
        st.warning(
            "Last action removed from the log. "
            "DataFrame changes have not been reverted."
        )
    else:
        st.info("Nothing to undo.")

    return df


def show_log():
    """Display the cleaning history."""
    initialize_log()

    st.subheader("🧾 Cleaning Log")

    if st.session_state.log:
        for entry in st.session_state.log:
            st.text(
                f"Step {entry['step']}: "
                f"{entry['action']} → {entry['summary']}"
            )
    else:
        st.info("No cleaning actions recorded yet.")


def get_log():
    """Return the cleaning log."""
    initialize_log()
    return st.session_state.log


def clear_log():
    """Clear the cleaning history."""
    initialize_log()
    st.session_state.log = []
