"""Main application file for the Streamlit app."""
import os
import streamlit as st
from dotenv import load_dotenv
import google.generativeai as genai
from src.frontend.chat import chat_interface
from src.frontend.vision import vision_interface

load_dotenv()

GOOGLE_API_KEY = os.getenv("api_key")
genai.configure(api_key=GOOGLE_API_KEY)


def main():
    """Main function for the Streamlit app."""
    st.sidebar.title("AnnGuru")
    user_picked = st.sidebar.radio("Choose an option", ["Chat with AnnGuru",
                                                        "Gemini Vision"])

    if user_picked == "Chat with AnnGuru":
        model = genai.GenerativeModel("gemini-pro")
        chat_interface(model=model)
    elif user_picked == "Gemini Vision":
        gemini_model = genai.GenerativeModel(
            'models/gemini-1.5-flash-002',
            generation_config={"response_mime_type": "application/json"}
            )
        vision_interface(gemini_model=gemini_model)


if __name__ == "__main__":
    main()
