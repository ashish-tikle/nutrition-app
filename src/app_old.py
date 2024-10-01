import os
import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
from streamlit_option_menu import option_menu
from PIL import Image
from nutri_code import generate_nutri_score_image
from frontend.new import extract_nutrition_facts

load_dotenv()

GOOGLE_API_KEY = os.getenv("api_key")
genai.configure(api_key=GOOGLE_API_KEY)


def gemini_pro():
    model = genai.GenerativeModel("gemini-pro")
    return model

st.set_page_config(
    page_title="AnnaGuru",
    page_icon="🧠",
    layout="centered",
    initial_sidebar_state="expanded")

with st.sidebar:
    user_picked = option_menu(
        "Select a model", 
        ["Gemini Pro", "Gemini Vision"],
        menu_icon="robot",
        icons=["chat-dots-fill","image-fill"],
        default_index=0
        )
    
def roleForStreamlit(user_role):
    if user_role == 'model':
        return 'asssitant'
    else:
        return user_role
    
if user_picked == "Gemini Pro":
    model = gemini_pro()

    if "chat_history" not in st.session_state:
        st.session_state['chat_history'] = model.start_chat(history=[])

    st.title("AnnaGuru")
    
    for message in st.session_state.chat_history.history:
        with st.chat_message(roleForStreamlit(message.role)):
            st.markdown(message.parts[0].text)

    user_input = st.chat_input("Message AnnaGuru...")
    if user_input:
        st.chat_message("user").markdown(user_input)
        response = st.session_state.chat_history.send_message(user_input)
        with st.chat_message("assistant"):
            st.markdown(response.text)
    

if user_picked == "Gemini Vision":
    # model = gemini_vision()

    st.title("Nutrition Facts Image Captioning")

    image_nutrition_facts = st.file_uploader("Upload Nutrition facts image", type=["jpg", "jpeg", "png"], key="image1")

    if st.button("Generate Captioning"):
        load_image_nutrition = Image.open(image_nutrition_facts)

        colLeft, colRight = st.columns(2)

        with colLeft:
            st.image(load_image_nutrition.resize((800,500)))

        caption_response = extract_nutrition_facts(image_nutrition_facts)

        with colRight:
            st.write(caption_response)

        st.subheader("Nutri-Score Prediction")
            
        score = caption_response['nutri_class']
        if score:
            generate_nutri_score_image(score)

        st.write("Nutri-Score: ", caption_response['nutri_score'])