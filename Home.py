import streamlit as st

st.set_page_config(
    page_title="AI Food Waste Reduction Assistant",
    page_icon="🌱",
    layout="wide"
)

# SESSION STATE
if "meals_saved" not in st.session_state:
    st.session_state.meals_saved = 0

if "money_saved" not in st.session_state:
    st.session_state.money_saved = 0

if "waste_reduced" not in st.session_state:
    st.session_state.waste_reduced = 0

if "co2_saved" not in st.session_state:
    st.session_state.co2_saved = 0

# CSS
st.markdown("""
<style>

.stApp{
    background: linear-gradient(
        135deg,
        #0b1120,
        #102a43,
        #14532d
    );
}

.hero{
    background: linear-gradient(
        135deg,
        #16a34a,
        #22c55e
    );
    padding:40px;
    border-radius:20px;
    text-align:center;
    color:white;
    box-shadow:0px 8px 25px rgba(0,0,0,0.3);
}

.card{
    background:#1e293b;
    padding:25px;
    border-radius:18px;
    text-align:center;
    color:white;
    border:1px solid #334155;
    box-shadow:0px 4px 15px rgba(0,0,0,0.25);
}

.card:hover{
    border:1px solid #22c55e;
}

[data-testid="metric-container"]{
    background:#111827;
    border-radius:15px;
    padding:15px;
    border-left:5px solid #22c55e;
}

h1,h2,h3,h4,h5,h6{
    color:white !important;
}

p,li,div,label{
    color:white !important;
}

.footer{
    text-align:center;
    color:#cbd5e1;
    padding:10px;
}

</style>
""", unsafe_allow_html=True)

# HERO
st.markdown("""
<div class="hero">
<h1>🌱 AI Food Waste Reduction Assistant</h1>
<h3>Reduce Food Waste • Save Money • Protect the Environment</h3>
<p>Smart Sustainable Food Management System</p>
</div>
""", unsafe_allow_html=True)

st.write("")

# DASHBOARD
st.header("📊 Live Impact Dashboard")

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.metric("🍽 Meals Saved", st.session_state.meals_saved)

with c2:
    st.metric("💰 Money Saved", f"₹{st.session_state.money_saved}")

with c3:
    st.metric("♻ Waste Reduced", f"{st.session_state.waste_reduced} kg")

with c4:
    st.metric("🌍 CO₂ Saved", f"{st.session_state.co2_saved} kg")

st.divider()

# ABOUT
st.header("🌍 About The Project")

st.write("""
This AI-powered platform helps users:

✅ Generate recipes from available ingredients

✅ Learn smart food storage techniques

✅ Reduce food wastage

✅ Promote sustainable consumption

✅ Track environmental impact

### SDG Goal Supported

SDG 12 – Responsible Consumption and Production
""")

st.divider()

# IMAGES
st.header("🌱 Food Waste Awareness")

col1, col2 = st.columns(2)

with col1:
    st.image(
        "https://images.unsplash.com/photo-1532996122724-e3c354a0b15b",
        caption="Food Waste Management",
        use_container_width=True
    )

with col2:
    st.image(
        "https://images.unsplash.com/photo-1542601906990-b4d3fb778b09",
        caption="Composting & Sustainability",
        use_container_width=True
    )

st.info("""
🍽 Every year millions of tons of food are wasted globally.

♻ Composting and proper food management reduce environmental impact.

🌱 Small actions can create a sustainable future.
""")

st.divider()

# FEATURES
st.header("🚀 Key Features")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="card">
        <h2>🍳 Recipe Assistant</h2>
        <p>Generate recipes using available ingredients.</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="card">
        <h2>🥦 Storage Assistant</h2>
        <p>Get smart food storage recommendations.</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="card">
        <h2>♻ Waste Reduction</h2>
        <p>Reduce food wastage with sustainable tips.</p>
    </div>
    """, unsafe_allow_html=True)

st.divider()

# FACTS
st.header("🌎 Global Food Waste Facts")

c1, c2, c3 = st.columns(3)

with c1:
    st.metric("🍽 Food Wasted", "1.3 Billion Tons")

with c2:
    st.metric("💰 Economic Loss", "$940 Billion")

with c3:
    st.metric("🌍 CO₂ Impact", "8%")

st.info("""
Nearly one-third of all food produced globally is wasted.

Reducing food waste saves money, conserves resources,
and protects the environment.
""")

st.divider()

# BENEFITS
st.header("📈 Sustainability Benefits")

c1, c2, c3 = st.columns(3)

with c1:
    st.success("💵 Save Household Expenses")

with c2:
    st.info("🌎 Reduce Carbon Footprint")

with c3:
    st.warning("🍽 Minimize Food Wastage")

st.divider()

st.markdown("""
<div class="footer">
🌱 Developed using Streamlit | AI Food Waste Reduction Assistant | 1M1B Internship Project
</div>
""", unsafe_allow_html=True)