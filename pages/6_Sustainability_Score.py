import streamlit as st

st.set_page_config(
    page_title="Sustainability Score",
    page_icon="🏆",
    layout="wide"
)

if "meals_saved" not in st.session_state:
    st.session_state.meals_saved = 0

if "waste_reduced" not in st.session_state:
    st.session_state.waste_reduced = 0

st.title("🏆 Sustainability Score")

score = min(
    100,
    int(
        st.session_state.get("meals_saved", 0) * 10 +
        st.session_state.get("waste_reduced", 0) * 5
    )
)

st.progress(score / 100)

st.success(f"Current Sustainability Score: {score}/100")

if score >= 80:
    st.balloons()
    st.success("Excellent Sustainable Practices!")

elif score >= 60:
    st.info("Good Progress. Keep reducing food waste.")

else:
    st.warning("You can improve your sustainability habits.")

st.markdown("---")

st.write("""
### How is this score calculated?

✅ Food Waste Reduction

✅ Smart Ingredient Usage

✅ Recipe Utilization

✅ Sustainable Consumption Practices
""")