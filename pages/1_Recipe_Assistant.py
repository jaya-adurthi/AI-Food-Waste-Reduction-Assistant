import streamlit as st

st.set_page_config(
    page_title="Recipe Assistant",
    page_icon="🍳",
    layout="wide"
)

# Session State
if "meals_saved" not in st.session_state:
    st.session_state.meals_saved = 0

if "money_saved" not in st.session_state:
    st.session_state.money_saved = 0

if "waste_reduced" not in st.session_state:
    st.session_state.waste_reduced = 0

if "co2_saved" not in st.session_state:
    st.session_state.co2_saved = 0

st.title("🍳 AI Recipe Assistant")

st.write("Enter ingredients and generate recipes.")

ingredients = st.text_area(
    "Enter Ingredients",
    placeholder="Rice, Egg, Onion"
)

recipes = {

    ("rice","egg"):
    {
        "name":"Egg Fried Rice",
        "time":"15 mins",
        "difficulty":"Easy",
        "score":92
    },

    ("bread","egg"):
    {
        "name":"Bread Omelette",
        "time":"10 mins",
        "difficulty":"Easy",
        "score":88
    },

    ("tomato","onion"):
    {
        "name":"Tomato Onion Curry",
        "time":"20 mins",
        "difficulty":"Medium",
        "score":85
    },

    ("potato","onion"):
    {
        "name":"Potato Fry",
        "time":"25 mins",
        "difficulty":"Easy",
        "score":84
    },

    ("milk","banana"):
    {
        "name":"Banana Milkshake",
        "time":"5 mins",
        "difficulty":"Easy",
        "score":90
    },

    ("chicken","rice"):
    {
        "name":"Chicken Fried Rice",
        "time":"30 mins",
        "difficulty":"Medium",
        "score":95
    },

    ("paneer","tomato"):
    {
        "name":"Paneer Curry",
        "time":"25 mins",
        "difficulty":"Medium",
        "score":89
    },

    ("bread","milk"):
    {
        "name":"Bread Pudding",
        "time":"15 mins",
        "difficulty":"Easy",
        "score":86
    }
}

if st.button("🍳 Generate Recipe"):

    if ingredients.strip() == "":
        st.warning("Please enter ingredients")

    else:

        ing = [x.strip().lower() for x in ingredients.split(",")]

        recipe_found = {
            "name":"Mixed Vegetable Meal",
            "time":"20 mins",
            "difficulty":"Easy",
            "score":80
        }

        for combo, details in recipes.items():

            if all(item in ing for item in combo):
                recipe_found = details
                break

        # Dashboard Update
        st.session_state.meals_saved += 1
        st.session_state.money_saved += 50
        st.session_state.waste_reduced += 0.5
        st.session_state.co2_saved += 0.3

        st.success("Recipe Generated Successfully")

        c1,c2,c3,c4 = st.columns(4)

        with c1:
            st.metric(
                "🍳 Recipe",
                recipe_found["name"]
            )

        with c2:
            st.metric(
                "⏱ Time",
                recipe_found["time"]
            )

        with c3:
            st.metric(
                "⭐ Difficulty",
                recipe_found["difficulty"]
            )

        with c4:
            st.metric(
                "🌱 Score",
                f"{recipe_found['score']}/100"
            )

        st.progress(recipe_found["score"]/100)

        st.subheader("🥘 Suggested Recipe")

        st.success(recipe_found["name"])
        

        st.info(
            f"""
Ingredients Used:
{ingredients}

Preparation Time:
{recipe_found['time']}

Difficulty:
{recipe_found['difficulty']}
"""
        )

        st.subheader("🌱 Sustainability Impact")

        st.success(
            f"""
✔ Meal Saved: +1

✔ Money Saved: +₹50

✔ Waste Reduced: +0.5 kg

✔ CO₂ Saved: +0.3 kg
"""
        )