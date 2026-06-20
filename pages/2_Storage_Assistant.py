import streamlit as st

st.set_page_config(
    page_title="Storage Assistant",
    page_icon="🥦",
    layout="wide"
)

st.title("🥦 Smart Food Storage Assistant")

st.write("Enter one or multiple ingredients separated by commas.")

ingredients = st.text_area(
    "Enter Ingredients",
    placeholder="Tomato, Egg, Milk"
)

storage_data = {

    "tomato":"🍅 Store at room temperature away from direct sunlight.",

    "onion":"🧅 Store in a cool, dry and ventilated place.",

    "potato":"🥔 Store in a cool, dark place. Avoid refrigeration.",

    "egg":"🥚 Keep refrigerated at 4°C or below.",

    "rice":"🍚 Store in an airtight container in a dry place.",

    "bread":"🍞 Store in a sealed packet or bread box.",

    "milk":"🥛 Keep refrigerated and consume before expiry date.",

    "banana":"🍌 Store at room temperature until ripe.",

    "chicken":"🍗 Refrigerate immediately and use within 1-2 days.",

    "paneer":"🧀 Keep refrigerated and consume within 2-3 days.",

    "carrot":"🥕 Store in refrigerator vegetable drawer.",

    "cabbage":"🥬 Refrigerate in a plastic bag.",

    "apple":"🍎 Refrigerate for longer shelf life."
}

if st.button("📦 Check Storage Recommendations"):

    if ingredients.strip() == "":
        st.warning("Please enter ingredients.")
    else:

        items = [x.strip().lower() for x in ingredients.split(",")]

        st.success("Storage Recommendations Generated")

        for item in items:

            st.subheader(f"🔹 {item.title()}")

            if item in storage_data:
                st.info(storage_data[item])
            else:
                st.warning(
                    "Storage information currently unavailable."
                )

        st.divider()

        st.success(
            """
✅ Proper storage increases shelf life

✅ Reduces food spoilage

✅ Minimizes food waste

✅ Saves money and resources
"""
        )