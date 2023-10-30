import streamlit as st
import pandas as pd
import requests
import pydeck as pdk

# !/usr/bin/python


st.set_page_config(layout="centered")
# header

def Home():
    with st.container():

    # Add the title and description within the container

        logo_image = "https://i.imgur.com/QtiDzrN.png"  # Replace with the actual path to your logo image
        st.image(logo_image, width=200)
        st.markdown("<h1 style='text-align: center; color: white;'>Home To All The Recipes You Will Ever Need</h1>", unsafe_allow_html=True)

    # Load and display your logo image with container width

# what i do

    with (st.container()):
        with open("styles.css") as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

        st.write("---")

        st.header("About Us")
        st.write("At Arocha Meals, we've distilled the essence of culinary artistry into three core pillars: All Types of Recipes, Make Your Own Recipe, and Ingredients. With a relentless dedication to these essentials, we aim to be your premier destination for culinary exploration.")
        st.header("Our Culinary Foundations:")
        st.write("Our commitment revolves around three fundamental facets of the culinary world, each meticulously curated for your culinary journey:")

        st.header("All Types of Recipes: 🌮🥗")
        st.write("Delve into a world of flavors with our extensive collection of recipes. From timeless classics to contemporary innovations, we offer an array of recipes to satiate your gastronomic curiosity.")

        st.header("Make Your Own Recipe: 🍳👨‍🍳")
        st.write("We believe that creativity knows no bounds in the kitchen. Our Make Your Own Recipe section empowers you to become a culinary virtuoso. Design your own dishes, experiment with ingredients, and share your unique culinary creations with our global community.")
        st.header("Ingredients: 🌶️🍋")
        st.write("Explore the intricate universe of culinary ingredients in our Ingredients section. Our guides provide in-depth insights into a wide array of cooking elements, from kitchen staples to exotic finds. Delve deeper into the art of cuisine by understanding the components that make it remarkable.")




def Recipes():
    with st.container():
        # Add the title and description within the container
        logo_image = "https://i.imgur.com/QtiDzrN.png"  # Replace with the actual path to your logo image
        st.image(logo_image, width=100)

    user_query = st.text_input("Enter an Ingredient")

    # Button to trigger the API request
    submit_button = st.button("Search Recipes")

    # Define your Spoonacular API key (replace with your actual key)
    apiKey = "71648f5810894c3d905128dc3a497553"

    # Define the API endpoint URL
    api_url = "https://api.spoonacular.com/recipes/complexSearch"

    # Function to make the API request
    def get_recipes(query):
        params = {
            "apiKey": apiKey,
            "query": query
        }
        response = requests.get(api_url, params=params)
        return response

    if submit_button:
        if not user_query:
            st.error("Please enter a query.")
        else:
            response = get_recipes(user_query)
            if response.status_code == 200:
                recipes = response.json()
                st.title("Recipes for '" + user_query + "'")
                for recipe in recipes["results"]:
                    st.subheader(recipe["title"])  # Display recipe name
                    st.image(recipe["image"])  # Display recipe image
            else:
                st.error(f"API request failed. Status code: {response.status_code}")




st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ("Home", "Recipes", "MYOM", "Ingredients"))




if page == "Home":
    Home()
elif page == "Recipes":
    Recipes()
elif page == "MYOM":
    MYOM()



