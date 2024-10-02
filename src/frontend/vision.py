"""
This module contains the code for the vision interface of the application.
"""
import json
import streamlit as st
from PIL import Image
from pyNutriScore import NutriScore
from src.nutri_code import generate_nutri_score_image


def vision_interface(gemini_model):
    """Vision interface for the Streamlit frontend."""
    st.title("Nutrition Facts Image Captioning")

    image_nutrition_facts = st.file_uploader("Upload nutrition facts image",
                                             type=["jpg", "jpeg", "png"],
                                             key="image_nutrition_facts")

    image_ingredient_list = st.file_uploader("Upload ingredient list image",
                                             type=["jpg", "jpeg", "png"],
                                             key="image_ingredient_list")

    if st.button("Generate Captioning"):
        load_image_nutrition = Image.open(image_nutrition_facts)
        st.image(
            load_image_nutrition.resize((800, 500)),
            caption="Nutrition Facts"
            )

        load_image_ingredients = Image.open(image_ingredient_list)
        st.image(
            load_image_ingredients.resize((800, 500)),
            caption="Ingredients List"
            )

        caption_response = extract_nutrition_facts(image_nutrition_facts,
                                                   image_ingredient_list,
                                                   gemini_model)

        st.header("Health Analysis Report", divider=True)

        st.subheader("Nutrition")
        score = caption_response['nutri_class']
        if score:
            generate_nutri_score_image(score)

        st.metric(label="Nutri-Score", value=caption_response['nutri_score'])

        st.subheader("Nutritional Information", divider=True)
        col1, col2, col3, col4, col5, col6, col7, col8 = st.columns(8)
        with col1:
            st.metric(
                label="Energy",
                value=f"{caption_response['nutrition_facts']['energy']} kcal")
        with col2:
            st.metric(
                label="Sugar",
                value=f"{caption_response['nutrition_facts']['sugar']} g")
        with col3:
            st.metric(
                label="Saturated Fats",
                value=f"{caption_response['nutrition_facts']
                         ['saturated_fats']} g")
        with col4:
            st.metric(
                label="Sodium",
                value=f"{caption_response['nutrition_facts']['sodium']} mg")
        with col5:
            st.metric(
                label="Protein",
                value=f"{caption_response['nutrition_facts']['proteins']} g")
        with col6:
            st.metric(
                label="Dietary Fiber",
                value=f"{caption_response['nutrition_facts']['fibers']} g")
        with col7:
            st.metric(
                label="Fruit Percentage",
                value=f"{caption_response['nutrition_facts']
                         ['fruit_percentage']} %")
        with col8:
            st.metric(
                label="Food Type",
                value=caption_response['nutrition_facts']['food_type'])

        st.subheader("Health Analysis", divider=True)
        if caption_response['nutrition_facts']["health_analysis"]:
            st.json(caption_response["nutrition_facts"]["health_analysis"])

        st.subheader("Additives", divider=True)
        if caption_response['nutrition_facts']["additives"]:
            st.json(caption_response["nutrition_facts"]["additives"])


def extract_nutrition_facts(image_path1, image_path2, gemini_model):
    """Extract nutrition facts from the image using the Gemini model."""
    sample_image_1 = Image.open(image_path1)
    sample_image_2 = Image.open(image_path2)

    prompt = """
    You are a smart AI enabled label reader which extracts nutrition facts 
    from an image.
    Extract the food type from ingredients list and only the following 
    entities from the nutrition facts (for per 100g serving):
    1. Energy
    2. Sugar
    3. Saturated Fats
    4. Sodium
    5. Protein
    6. Dietary Fiber
    7. Fruits‚ vegetables‚ nuts and olive oils percentage 
    (estimate from ingredients list analysis)
    8. Food type ('solid' or 'beverage')
    ##RULES:
    1. Remember to convert all the units to grams except energy and
    fruit_percentage, say from mg to g.
    2. If any corresponding key say `fiber` is not found in the image replace
    it as `0` in its corresponding value
    3. If amount of fruits, vegetables and nuts is not specified on the label,
    estimate from the list of ingredients.
    4. Say if list of ingredients are: sugar, cocoa solids, cocoa butter,
    almonds(8%), raisins(5%), permitted emulsifiers (e322, e476).
    Then the estimated percentage of fruits, vegetables, nuts and olive oils
    is (8+5)% = 13%.
    If no such values are found, then set it as 0.
    5. Provide a health analysis report based on the nutrition content and
    ingredients list as a summary for nutrient types present in
    ["energy", "sugar", "saturated_fats", "sodium", "proteins", "fibers",
    "fruit_percentage"].
    6. A sample health analysis report for just 3 nutrients is as follows:
      "health_analysis": {
        "Fat in high quantity (32.5%)": {
          "FYI": "A high consumption of fat, especially saturated fats, can
          raise cholesterol, which increases the risk of heart diseases.",
          "Recommendation": "Limit the consumption of fat and saturated fat"
        },
        "Sugars in high quantity (38.3%)": {
          "FYI": "A high consumption of sugar can cause weight gain and
          tooth decay. It also augments the risk of type 2 diabetes and
          cardio-vascular diseases.",
          "Recommendation": "Limit the consumption of sugar and sugary drinks
          (no more than 1 glass a day)."
        },
        "Salt in low quantity (0.0825%)": {
          "FYI": "A high consumption of salt (or sodium) can cause raised
          blood pressure, which can increase the risk of heart disease and
          stroke.",
          "Recommendation": "Limit the consumption of salt and salted food"
        }
      },
      "additives": {
        "E322 - Lecithins": "Lecithins are natural compounds commonly used in
        the food industry as emulsifiers and stabilizers. They do not present
        any known health risks."
      }
    where the key is the nutrient and its quantity from nutrition facts and
    the value is the FYI and Recommendation based on the quantity. List down
    the major additives/preservatives present in the food and their description
    along with any health risks involved.
    7. Sample output should have the following keys in json format:
    {
    'energy': 250,
    'sugar': 20,
    'saturated_fats': 4,
    'sodium': 0.45,
    'proteins': 12,
    'fibers': 30,
    'fruit_percentage': 13,  
    'food_type': 'solid',
    'health_analysis': {}
    }
  """

    # Contents to be processed by the model
    contents = [sample_image_1, sample_image_2, prompt]

    # call the model to generate the content
    response = gemini_model.generate_content(contents)  

    # Parse the response text to JSON
    response_json = json.loads(response.text)

    # Calculate Nutri-Score and its class using the pyNutriScore package
    result_score = NutriScore().calculate(response_json,
                                          response_json['food_type'])
    result_class = NutriScore().calculate_class(response_json,
                                                response_json['food_type'])

    # Return the final Nutri-Score and its class
    return {
        "nutri_score": result_score,
        "nutri_class": result_class,
        "nutrition_facts": response_json
        }
