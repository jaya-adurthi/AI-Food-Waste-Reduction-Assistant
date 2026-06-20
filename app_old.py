
import streamlit as st

# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(
    page_title="AI Food Waste Reduction Assistant",
    page_icon="🌱",
    layout="wide"
)

# -----------------------------
# SESSION STATE
# -----------------------------
if "meals_saved" not in st.session_state:
    st.session_state.meals_saved = 0

if "money_saved" not in st.session_state:
    st.session_state.money_saved = 0

if "waste_reduced" not in st.session_state:
    st.session_state.waste_reduced = 0

if "co2_saved" not in st.session_state:
    st.session_state.co2_saved = 0

# -----------------------------
# CSS
# -----------------------------
st.markdown("""
<style>

.stApp{
background:#0b1220;
}

.hero{
background:linear-gradient(135deg,#00c853,#64dd17);
padding:40px;
border-radius:20px;
text-align:center;
color:white;
margin-bottom:20px;
}

.card{
background:#1e293b;
padding:20px;
border-radius:15px;
text-align:center;
color:white;
}

</style>
""", unsafe_allow_html=True)

# -----------------------------
# HERO
# -----------------------------
st.markdown("""
<div class="hero">
<h1>🌱 AI Food Waste Reduction Assistant</h1>
<h3>Reduce Food Waste • Save Money • Protect Environment</h3>
</div>
""", unsafe_allow_html=True)

# -----------------------------
# DASHBOARD
# -----------------------------
st.markdown("## 📊 Impact Dashboard")

c1,c2,c3,c4 = st.columns(4)

c1.metric("🍽 Meals Saved", st.session_state.meals_saved)
c2.metric("💰 Money Saved", f"₹{st.session_state.money_saved}")
c3.metric("♻ Waste Reduced", f"{st.session_state.waste_reduced} kg")
c4.metric("🌍 CO₂ Saved", f"{st.session_state.co2_saved} kg")

st.markdown("---")

# -----------------------------
# ABOUT
# -----------------------------
st.header("🌍 About Project")

st.write("""
This application helps users reduce food waste through smart recipe suggestions,
storage recommendations and waste reduction guidance.

Supports SDG 12 - Responsible Consumption and Production.
""")

# -----------------------------
# FEATURE CARDS
# -----------------------------
col1,col2,col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="card">
    <h3>🍳 Recipe Suggestions</h3>
    <p>Generate recipes from available ingredients.</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="card">
    <h3>🥦 Storage Tips</h3>
    <p>Learn proper storage methods.</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="card">
    <h3>♻ Waste Reduction</h3>
    <p>Reduce food wastage smartly.</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# -----------------------------
# SERVICE SELECTOR
# -----------------------------
service = st.selectbox(
    "Choose Service",
    [
        "🍳 Recipe Suggestions",
        "🥦 Storage Tips",
        "♻ Waste Reduction"
    ]
)

ingredients = st.text_area(
    "Enter Ingredients",
    placeholder="Rice, Egg, Onion"
)

# -----------------------------
# DATA
# -----------------------------
recipes = {
    ("rice","egg"): "🍳 Egg Fried Rice",
    ("bread","egg"): "🍞 Bread Omelette",
    ("tomato","onion"): "🍅 Tomato Onion Curry",
    ("potato","onion"): "🥔 Potato Fry",
    ("rice","tomato"): "🍛 Tomato Rice",
    ("egg","onion"): "🍳 Onion Omelette",
    ("egg","tomato"): "🍳 Tomato Omelette",
    ("bread","tomato"): "🥪 Tomato Sandwich"
}

storage = {
    "rice":"Store in airtight container.",
    "egg":"Keep refrigerated.",
    "onion":"Store in cool dry place.",
    "tomato":"Store at room temperature.",
    "potato":"Store in dark cool place.",
    "bread":"Store in sealed packet."
}

waste = {
    "rice":"Use leftover rice for fried rice.",
    "egg":"Use egg shells for compost.",
    "onion":"Use onion peels in vegetable stock.",
    "tomato":"Make soup using extra tomatoes.",
    "potato":"Use leftover potatoes in curry.",
    "bread":"Convert stale bread into breadcrumbs."
}

# -----------------------------
# ANALYZE
# -----------------------------
if st.button("🔍 Analyze"):

    if ingredients.strip() == "":
        st.warning("Please enter ingredients.")

    else:

        st.balloons()

        ing = [x.strip().lower() for x in ingredients.split(",")]

        # Dashboard Update
        count = len(ing)

        st.session_state.meals_saved += 1
        st.session_state.money_saved += count * 40
        st.session_state.waste_reduced += count
        st.session_state.co2_saved += round(count * 0.5)

        if service == "🍳 Recipe Suggestions":

            recipe_found = "🥗 Mixed Vegetable Meal"

            for combo, recipe in recipes.items():
                if all(item in ing for item in combo):
                    recipe_found = recipe
                    break

            st.subheader("🍳 Suggested Recipe")
            st.success(recipe_found)

        elif service == "🥦 Storage Tips":

            st.subheader("🥦 Storage Recommendations")

            found = False

            for item in ing:
                if item in storage:
                    st.info(f"{item.title()} → {storage[item]}")
                    found = True

            if not found:
                st.warning("Storage information not available.")

        elif service == "♻ Waste Reduction":

            st.subheader("♻ Waste Reduction Suggestions")

            found = False

            for item in ing:
                if item in waste:
                    st.success(waste[item])
                    found = True

            if not found:
                st.warning("Waste reduction tips not available.")

st.markdown("---")

st.caption("🌱 AI Food Waste Reduction Assistant | SDG 12 Sustainability Project")