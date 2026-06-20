import streamlit as st

st.set_page_config(
    page_title="Waste Reduction Assistant",
    page_icon="♻",
    layout="wide"
)

st.title("♻ Smart Food Waste Reduction Assistant")

st.write(
    "Enter one or multiple ingredients to get food waste reduction tips."
)

ingredients = st.text_area(
    "Enter Ingredients",
    placeholder="Rice, Bread, Tomato"
)

waste_tips = {

    "rice":"🍚 Convert leftover rice into fried rice, lemon rice or rice balls.",

    "bread":"🍞 Turn stale bread into breadcrumbs, croutons or bread pudding.",

    "tomato":"🍅 Use extra tomatoes for soup, chutney, sauce or juice.",

    "onion":"🧅 Use onion peels for vegetable stock preparation.",

    "potato":"🥔 Reuse leftover potatoes in curry, sandwiches or cutlets.",

    "egg":"🥚 Use eggs before expiry and compost the shells.",

    "banana":"🍌 Overripe bananas can be used in milkshakes or banana bread.",

    "milk":"🥛 Use excess milk to make curd, paneer or desserts.",

    "chicken":"🍗 Use leftovers in wraps, sandwiches or fried rice.",

    "paneer":"🧀 Add leftover paneer to curries or sandwiches.",

    "apple":"🍎 Use extra apples in juice, smoothies or fruit salad.",

    "carrot":"🥕 Use carrot peels in soups or vegetable stock."
}

if st.button("♻ Generate Waste Reduction Tips"):

    if ingredients.strip() == "":
        st.warning("Please enter ingredients.")

    else:

        items = [x.strip().lower() for x in ingredients.split(",")]

        st.success("Waste Reduction Tips Generated")

        for item in items:

            st.subheader(f"🔹 {item.title()}")

            if item in waste_tips:
                st.info(waste_tips[item])

            else:
                st.warning(
                    "Waste reduction tip currently unavailable."
                )

        st.divider()

        st.success(
            """
🌱 Benefits

✅ Reduces food wastage

✅ Saves household expenses

✅ Promotes sustainable consumption

✅ Supports SDG 12 goals
"""
        )