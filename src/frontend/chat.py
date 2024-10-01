"""This module contains the chat interface for the Streamlit frontend."""

import streamlit as st


def role_for_streamlit(role):
    """Returns the role for the Streamlit chat interface."""
    return "user" if role == "user" else "assistant"


def chat_interface(model):
    """Chat interface for the Streamlit frontend."""
    st.session_state["chat_history"] = model.start_chat(history=[])

    st.title("AnnaGuru")

    for message in st.session_state.chat_history.history:
        with st.chat_message(role_for_streamlit(message.role)):
            st.markdown(message.parts[0].text)

    user_input = st.chat_input("Message AnnaGuru...")
    if user_input:
        st.chat_message("user").markdown(user_input)
        response = st.session_state.chat_history.send_message(user_input)
        with st.chat_message("assistant"):
            st.markdown(response.text)
