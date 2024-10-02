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
    st.set_page_config(
        page_title="AnnGuru",
        page_icon="src/frontend/assets/SEO-Food-Fresh-Groceries.png",
        layout="wide",
        )
    st.sidebar.image(
        "src/frontend/assets/logo.png",
        caption="Empowering Healthier Choices, One Scan at a Time",
        use_column_width="always"
        )
    st.sidebar.title("AnnGuru")
    st.sidebar.markdown("## Choose an option")

    # Define the options and their corresponding icons
    options = {
        "Chat with AnnGuru": "💬",
        "Gemini Vision": "👁️"
    }

    # Create a list of options with icons
    option_list = [f"{icon} {option}" for option, icon in options.items()]

    # Display the radio button with options
    user_picked = st.sidebar.radio(
        "Choose an option",
        option_list,
        index=0,
        key="radio_options",
        help="Select an option to interact with AnnGuru",
        label_visibility="collapsed"
        )

    # Remove the icon from the selected option for further processing
    user_picked = user_picked.split(" ", 1)[1]
    # user_picked = st.sidebar.radio("Choose an option", ["Chat with AnnGuru",
    #                                                     "Gemini Vision"])

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
