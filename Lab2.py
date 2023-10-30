import streamlit as st
import requests
import re

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
            st.error("Please enter an ingredient.")
        else:
            response = get_recipes(user_query)
            if response.status_code == 200:
                recipes = response.json()
                st.title("Recipes for '" + user_query + "'")
                for recipe in recipes["results"]:
                    st.subheader(recipe["title"])  # Display recipe name
                    st.image(recipe["image"])  # Display recipe image
                    st.write("Meal ID:", recipe["id"])  # Display meal ID
            else:
                st.error(f"API request failed. Status code: {response.status_code}")




def strip_html_tags(text):
    # Use regular expressions to remove HTML tags and entities
    clean_text = re.sub(r'<.*?>', '', text)
    return clean_text

def Ingredients():
    with st.container():
        # Add the title and description within the container
        logo_image = "https://i.imgur.com/QtiDzrN.png"  # Replace with the actual path to your logo image
        st.image(logo_image, width=100)

    user_query = st.text_input("Enter Meal ID")

    # Button to trigger the API request
    submit_button = st.button("Search")

    # Define your Spoonacular API key (replace with your actual key)
    apiKey = "71648f5810894c3d905128dc3a497553"

    # Define the API endpoint URL
    api_url = "https://api.spoonacular.com/recipes/{id}/information"

    # Function to make the API request
    def get_recipe_information(recipe_id):
        params = {
            "apiKey": apiKey,
        }
        response = requests.get(api_url.format(id=recipe_id), params=params)
        return response

    if submit_button:
        if not user_query:
            st.error("Please enter a Meal ID.")
        else:
            response = get_recipe_information(user_query)
            if response.status_code == 200:
                recipe_info = response.json()
                st.title("Recipe Information for Meal ID " + user_query)
                st.write("Title:", recipe_info["title"])

                # Display ingredients
                ingredients = recipe_info["extendedIngredients"]
                st.markdown("Ingredients:")
                for ingredient in ingredients:
                    st.write("- " + ingredient["name"])

                # Parse and display summary and instructions as plain text
                st.markdown("Summary:")
                summary_html = recipe_info["summary"]
                summary_text = strip_html_tags(summary_html)
                st.write(summary_text)

                st.markdown("Instructions:")
                instructions_html = recipe_info["instructions"]
                instructions_text = strip_html_tags(instructions_html)
                st.write(instructions_text)
            else:
                st.error(f"API request failed. Status code: {response.status_code}")

def Review():
    with st.container():
        st.title("Rate My Website")

        # Create an empty list to store ratings
        def save_ratings(ratings):
            with open("ratings.txt", "a") as file:
                for rating in ratings:
                    file.write(f"{rating}\n")



        # Create an empty list to store ratings
        ratings = []

        # Ask users to rate the website
        user_rating = st.slider("Rate our website from 1 (worst) to 10 (best)", 1, 10)

        # Display the user's rating
        st.write(f"You rated our website as: {user_rating}")

        # Add the user's rating to the list of ratings
        ratings.append(user_rating)

        # Save the ratings to a file
        save_ratings(ratings)

        # Calculate and display the average rating
        if len(ratings) > 0:
            average_rating = sum(ratings) / len(ratings)
            st.write(f"Average Rating: {average_rating:.2f}")

            def save_feedback(feedback):
                with open("feedback.txt", "a") as file:
                    file.write(f"{feedback}\n")

            # Function to retrieve and display feedback
            def display_feedback():
                with open("feedback.txt", "r") as file:
                    feedback_data = file.readlines()
                    st.subheader("User Feedback")
                    for feedback in feedback_data:
                        st.markdown(f"> {feedback.strip()}", unsafe_allow_html=True)
                        st.markdown("---")

            st.title("Feedback Section")

            # Text area for users to leave feedback
            user_feedback = st.text_area("Leave your feedback here:", max_chars=200)

            # Button to submit feedback
            submit_feedback = st.button("Submit Feedback")

            if submit_feedback and user_feedback:
                # Save the user's feedback to a file
                save_feedback(user_feedback)
                st.success("Thank you for your feedback! It has been submitted.")

            # Display existing feedback
            display_feedback()


st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ("Home", "Recipes", "Ingredients", "Review"))
if page == "Home":
    Home()
elif page == "Recipes":
    Recipes()
elif page == "Ingredients":
    Ingredients()
elif page == "Review":
    Review()




