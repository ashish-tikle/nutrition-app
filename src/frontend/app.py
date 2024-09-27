import os
import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
from streamlit_option_menu import option_menu
from PIL import Image

from nutri_code import generate_nutri_score_image

# from src.frontend.utils import generate_text, save_image
# from src.frontend.nutri_code import generate_nutri_score_image

load_dotenv()

GOOGLE_API_KEY = os.getenv("api_key")
genai.configure(api_key=GOOGLE_API_KEY)


def gemini_pro():
    model = genai.GenerativeModel("gemini-pro")
    return model

def gemini_vision():
    model = genai.GenerativeModel("gemini-pro-vision")
    return model

def gemini_vision_response(model, prompt, image):
    response = model.generate_content([prompt, image])
    return response.text

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
    model = gemini_vision()

    st.title("Nutrition Facts Image Captioning")

    image_nutrition_facts = st.file_uploader("Upload Nutrition facts image", type=["jpg", "jpeg", "png"], key="image1")

    image_ingredients_list = st.file_uploader("Upload Ingredients list image", type=["jpg", "jpeg", "png"], key="image2")

    user_prompt = st.text_input("Enter the prompt for image captioning:")

    if st.button("Generate Captioning"):
        load_image_nutrition = Image.open(image_nutrition_facts)
        load_image_ingredients = Image.open(image_ingredients_list)

        colLeft, colRight = st.columns(2)

        with colLeft:
            st.image(load_image_nutrition.resize((800,500)))
            st.image(load_image_ingredients.resize((800,500)))

        # caption_response = gemini_vision_response(model, user_prompt, load_image_nutrition)

        # with colRight:
        #     # st.write(caption_response)

    st.title("Nutri-Score Prediction")
            
        
    score = st.text_input(label="Enter the score")  # Replace with the desired score
    if score:
        generate_nutri_score_image(score)

#     score = st.text_input(label="Enter the score")  # Replace with the desired score

#     if score:
#         generate_nutri_score_image(score)


# def main():
#     st.title("AnnaGuru")

#     # insert the saved image
#     st.image("src/logo.png")

#     #insert user input text "what is the product name?"
#     product_name = st.text_input("What is the product name?")
#     st.write(f"Product name: {product_name}")

#     # Upload the first image
#     st.subheader("Upload Nutrition facts image")
#     image1 = st.file_uploader("Choose an image", type=["jpg", "jpeg", "png"], key="image1")

#     # Upload the second image
#     st.subheader("Upload Ingredients list image")
#     image2 = st.file_uploader("Choose an image", type=["jpg", "jpeg", "png"], key="image2")

#     if image1 and image2:
#         # Display the uploaded images
#         st.image(image1, caption="Image 1", use_column_width=True)
#         st.image(image2, caption="Image 2", use_column_width=True)

#         # Save the images
#         image1_path = "image1.jpg"
#         image2_path = "image2.jpg"
#         save_image(image1, image1_path)
#         save_image(image2, image2_path)

#         # Generate text based on the images
#         text = generate_text(image1_path, image2_path)

#     # Set up the Streamlit app
#     st.title("Nutri-Score Prediction")

#     score = st.text_input(label="Enter the score")  # Replace with the desired score

#     if score:
#         generate_nutri_score_image(score)

#     # Display the score
#     # st.success(f"Maggie's Nova Score: {maggie_data['Score'].mode()[0]}")
#     # st.success(generate_nutri_score_image(maggie_data['Score'].mode()[0]))


# if __name__ == "__main__":
#     main()