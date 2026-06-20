import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Dashboard",
    page_icon="📊",
    layout="wide"
)

# Session State Defaults
if "meals_saved" not in st.session_state:
    st.session_state.meals_saved = 0

if "money_saved" not in st.session_state:
    st.session_state.money_saved = 0

if "waste_reduced" not in st.session_state:
    st.session_state.waste_reduced = 0

if "co2_saved" not in st.session_state:
    st.session_state.co2_saved = 0

st.title("📊 Sustainability Dashboard")

st.write("Track your sustainability impact in real time.")

# Metrics
c1, c2, c3, c4 = st.columns(4)

with c1:
    st.metric(
        "🍽 Meals Saved",
        st.session_state.meals_saved
    )

with c2:
    st.metric(
        "💰 Money Saved",
        f"₹{st.session_state.money_saved}"
    )

with c3:
    st.metric(
        "♻ Waste Reduced",
        f"{st.session_state.waste_reduced} kg"
    )

with c4:
    st.metric(
        "🌍 CO₂ Saved",
        f"{st.session_state.co2_saved} kg"
    )

st.divider()

# Sustainability Score
score = min(
    100,
    int(
        st.session_state.meals_saved * 10
        + st.session_state.waste_reduced * 5
    )
)

st.subheader("🏆 Sustainability Score")

st.progress(score / 100)

st.success(f"Current Sustainability Score: {score}/100")

# Chart
data = pd.DataFrame({
    "Category": [
        "Meals Saved",
        "Money Saved",
        "Waste Reduced",
        "CO₂ Saved"
    ],
    "Value": [
        st.session_state.meals_saved,
        st.session_state.money_saved,
        st.session_state.waste_reduced,
        st.session_state.co2_saved
    ]
})

st.subheader("📈 Impact Overview")

st.bar_chart(
    data.set_index("Category")
)

st.divider()

# Summary
st.info(
    f"""
Meals Saved: {st.session_state.meals_saved}

Money Saved: ₹{st.session_state.money_saved}

Waste Reduced: {st.session_state.waste_reduced} kg

CO₂ Saved: {st.session_state.co2_saved} kg
"""
)

if score >= 80:
    st.success("🌟 Excellent Sustainability Performance")

elif score >= 50:
    st.info("👍 Good Progress. Keep Going")

else:
    st.warning("🚀 Start using the Recipe Assistant to improve your score")