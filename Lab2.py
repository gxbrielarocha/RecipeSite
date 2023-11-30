import streamlit as st
import requests
import plotly as px
import pandas as pd
import numpy as np


st.set_page_config(layout="centered")
# header
with open("Styles.css", "r") as f:
    Styles_css = f.read()

# Apply the custom CSS using st.markdown
st.markdown(f'<style>{Styles_css}</style>', unsafe_allow_html=True)


# Read the custom CSS file
with open("header.css", "r") as f:
    custom_css = f.read()

# Apply the custom CSS using st.markdown
st.markdown(f'<style>{custom_css}</style>', unsafe_allow_html=True)

# Create your Streamlit content




# Create your Streamlit content


# Create your Streamlit content


def Home():
    with st.container():

    # Add the title and description within the container

        logo_image = "https://i.imgur.com/QtiDzrN.png"  # Replace with the actual path to your logo image
        st.image(logo_image, width=200)
        st.markdown("<h1 style='text-align: center; color: light blue;'>Home To All The Recipes You Will Ever Need</h1>", unsafe_allow_html=True)

    # Load and display your logo image with container width

    def create_map():
        # Coordinates of the Roman Colosseum
        colosseum_location = pd.DataFrame({
            'latitude': [41.8902],
            'longitude': [12.4924],
        })

        # Create a Streamlit map centered at the Roman Colosseum
        st.map(colosseum_location, zoom=15, use_container_width=True)

        # Add a marker for the Roman Colosseum and label it as "Our Headquarters"
        st.text("Our Headquarters")


    # Call the function to create the map
    create_map()
# what i do

    with (st.container()):


        st.write("---")

        st.header("About Us")
        st.write("At Arocha Meals, we've distilled the essence of culinary artistry into three core pillars: All Types of Recipes, Make Your Own Recipe, and Ingredients. With a relentless dedication to these essentials, we aim to be your premier destination for culinary exploration.")
        st.header("Our Culinary Foundations:")
        st.write("Our commitment revolves around three fundamental facets of the culinary world, each meticulously curated for your culinary journey:")

        st.header("All Types of Recipes: 🌮🥗")
        st.write("Delve into a world of flavors with our extensive collection of recipes. From timeless classics to contemporary innovations, we offer an array of recipes to satiate your gastronomic curiosity.")
        main_ingredients = ["Chicken", "Beef", "Pasta", "Fish", "Vegetarian", "Dessert", "Soup", "Salad", "Seafood",
                            "Pork",
                            "Lamb", "Pizza", "Mexican", "Italian", "Asian", "Indian", "Grilled", "BBQ", "Breakfast",
                            "Smoothie",
                            "Casserole", "Vegan", "Gluten-Free", "Mediterranean", "Appetizer", "Side Dish", "Bread",
                            "Dairy-Free",
                            "Crockpot", "Stir Fry", "Sushi", "Sandwich", "Greek", "French", "Spanish", "American",
                            "Cajun", "Keto",
                            "Low-Carb", "High-Protein", "Low-Fat", "Low-Calorie", "Paleo", "Whole30", "Soup", "Curry",
                            "Roasted",
                            "Baked", "Fried", "Gravy", "Sauce", "Marinated", "Skewers", "Gratin", "Stuffed", "Steamed",
                            "Pan-Fried",
                            "Slow Cooker", "Instant Pot", "Teriyaki", "Mango", "Pineapple", "Avocado", "Quinoa",
                            "Risotto", "Tacos",
                            "Shrimp", "Turkey", "Ham", "Eggplant", "Zucchini", "Sweet Potato", "Cabbage", "Chili",
                            "Stew", "Lasagna",
                            "Quesadilla", "Frittata", "Pesto", "Ratatouille", "Ceviche", "Gnocchi", "Paella", "Pumpkin",
                            "Egg Roll",
                            "Spring Roll", "Chow Mein", "Sushi Roll", "Hot Pot", "Fajitas", "Enchiladas", "Pad Thai",
                            "Bolognese",
                            "Goulash", "Calzone", "Burrito", "Empanadas", "Samosa", "Sorbet", "Tiramisu", "Panna Cotta",
                            "Crepes",
                            "Cheesecake", "Baklava", "Cannoli", "Macarons", "Churros", "Scones", "Muffins"]

        recipe_types = [f"{ingredient} Recipe" for ingredient in np.random.choice(main_ingredients, 200)]
        recipe_counts = np.random.randint(1, 1000, 200)

        data = pd.DataFrame({'Recipe Type': recipe_types, 'Count': recipe_counts})

        # Streamlit app


        # Create bar chart
        fig = px.bar(data, x='Recipe Type', y='Count', title='Recipe Types Distribution by Main Ingredient')
        fig.update_layout(xaxis=dict(title='Recipe Types'), yaxis=dict(title='Count'))

        # Display the chart
        st.plotly_chart(fig)
        st.header("Make Your Own Recipe: 🍳👨‍🍳")
        st.write("We believe that creativity knows no bounds in the kitchen. Our Make Your Own Recipe section empowers you to become a culinary virtuoso. Design your own dishes, experiment with ingredients, and share your unique culinary creations with our global community.")
        st.header("Ingredients: 🌶️🍋")
        st.write("Explore the intricate universe of culinary ingredients in our Ingredients section. Our guides provide in-depth insights into a wide array of cooking elements, from kitchen staples to exotic finds. Delve deeper into the art of cuisine by understanding the components that make it remarkable.")

    years = list(range(1980, 2023, 5))  # Start from 1980
    customers_helped = np.cumsum(np.random.randint(20000, 80000, size=len(years)))

    data = pd.DataFrame({'Year': years, 'Customers Helped': customers_helped})

    # Streamlit app
    st.title("Customers Helped")

    # Create line chart
    fig = px.line(data, x='Year', y='Customers Helped', markers=True, title='Customers Helped Over Time')
    fig.update_layout(yaxis=dict(title='Customers Helped'))

    # Display the chart
    st.plotly_chart(fig)
st.markdown(
    """
    <style>
        body {
            background-color: #1E1E1E;  /* Charcoal black background */
            color: #FFFFFF;  /* White text color */
        }
        .stApp {
            background-color: #8a8583;  /* Charcoal black background for the app container */
        }
        .stButton, .stTextInput, .stSelectbox, .stSlider {
            color: #FFFFFF !important;  /* White text color for interactive elements */
            background-color: #8a8583 !important;  /* Dark gray background for interactive elements */
        }
        .stMarkdown {
            color: #FFFFFF;  /* White text color for markdown */
        }
    </style>
    """,
    unsafe_allow_html=True
)
def Recipes():
    with st.container():
        # Add the title and description within the container
        logo_image = "https://i.imgur.com/QtiDzrN.png"  # Replace with the actual path to your logo image
        st.image(logo_image, width=100)
        st.title("Recipes")  # Change title to white
        st.markdown("Enter An Ingredient | Please Copy the Meal ID If You Would Like To View Ingredients")  # Change description to white

    user_query = st.text_input("", key="user_query", value="", help="Your help text here", type="default")  # Change text input to white

    # Button to trigger the API request
    submit_button = st.button("Search Recipes", key="submit_button", help="Your help text here")  # Change button to white

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
                recipes = response.json()["results"]
                if not recipes:
                    st.error(f"No recipes found for '{user_query}'. Please try a different ingredient.")
                else:
                    st.success("Recipes successfully loaded!")
                    st.title("Recipes for '" + user_query + "'")
                    for recipe in recipes:
                        st.subheader(recipe["title"])  # Display recipe name
                        st.image(recipe["image"])  # Display recipe image
                        st.write("Meal ID:", recipe["id"])  # Display meal ID
            else:
                st.error(f"API request failed. Status code: {response.status_code}")
        # Sample data (replace this with your recipe data)
    



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
                st.success("Successfully retrieved information for Meal ID " + user_query)
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
        user_rating = st.slider("", 1, 10)

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

        def main():
            st.title("Website Feedback")

            # Create a multiselect widget with options for user feedback
            feedback_options = ["User Interface", "Content", "Navigation", "Performance", "Overall Experience"]
            selected_feedback = st.multiselect("Select what you liked about the website:", feedback_options)

            if selected_feedback:
                st.success("Thank you for providing feedback on the following aspects:")
                for feedback in selected_feedback:
                    st.write(f"- {feedback}")
            else:
                st.warning("Please select at least one option to provide feedback.")

        if __name__ == "__main__":
            main()


def MiniGame():
    with st.container():
            def initialize_board(size=5):
                ingredients = ['Flour', 'Sugar', 'Eggs', 'Milk', 'Butter', 'Chocolate', 'Vanilla', 'Baking Powder', 'Salt']
                board = pd.DataFrame(np.random.choice(ingredients, size=(size, size)), columns=[f"Col{i+1}" for i in range(size)])
                return board

# Function to display the game board
            def display_board(board):
                st.dataframe(board)

# Main Streamlit app
            def main():
                st.title("Recipe Discovery Game")

    # Initialize game board
                board_size = 5
                recipe_board = initialize_board(size=board_size)

    # Display initial board
                st.write("Game Board:")
                display_board(recipe_board)

    # Player selects ingredient to find
                st.write("Player's Goal:")
                ingredient_to_find = st.selectbox("Match Ingredient Below With Top Left Cell | Changes Every Time:", ['Flour', 'Sugar', 'Eggs', 'Milk', 'Butter', 'Chocolate', 'Vanilla', 'Baking Powder', 'Salt'])

    # Check if the selected ingredient matches the first cell in the board
                if ingredient_to_find == recipe_board.iloc[0, 0]:
                    st.success("Congratulations! You've found the correct ingredient. You win!")
                else:
                    st.warning("Oops! That's not the correct ingredient. Keep trying!")

# Run the app
            if __name__ == "__main__":
                main()


st.markdown(
    """
    <style>
        .radio-group > div {
            flex-direction: row;
        }
        .radio-group > div > label {
            color: white;
            margin-right: 20px;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Navigation buttons
white_text_style = """
    <style>
        .radio-text label {
            color: white !important;
        }
    </style>
"""

# Apply the white text color style
st.markdown(white_text_style, unsafe_allow_html=True)

st.title("Navigation")

page = st.radio("Go to", ("Home", "Recipes", "Ingredients", "Review", "MiniGame"))

if page == "Home":
    Home()
elif page == "Recipes":
    Recipes()
elif page == "Ingredients":
    Ingredients()
elif page == "Review":
    Review()
elif page == "MiniGame":
    MiniGame()





