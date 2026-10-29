
import streamlit as st
import pandas as pd
import pickle

# ==================================================
# STEP 1: Configure the web application
# ==================================================
st.set_page_config(
    page_title="Food Delivery Time Predictor",
    page_icon="🍔",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# ==================================================
# STEP 2: Custom CSS - UI ONLY
# ==================================================
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

.stApp {
    background: linear-gradient(180deg, #fff5e9 0%, #ffffff 55%, #fff4e8 100%);
    font-family: 'Inter', sans-serif;
}

.block-container {
    max-width: 950px;
    padding-top: 1.5rem;
    padding-bottom: 2rem;
}

#MainMenu, footer, header {
    visibility: hidden;
}

/* Hero banner */
.hero {
    background: linear-gradient(135deg, #ff7a36 0%, #f04423 100%);
    padding: 30px 24px;
    border-radius: 24px;
    color: white;
    text-align: center;
    box-shadow: 0 12px 28px rgba(240, 68, 34, 0.18);
    margin-bottom: 24px;
}

.hero-tag {
    display: inline-block;
    background: rgba(255,255,255,0.22);
    padding: 7px 13px;
    border-radius: 30px;
    font-size: 10px;
    font-weight: 700;
    letter-spacing: 1.3px;
}

.hero h1 {
    color: white !important;
    font-size: 34px;
    line-height: 1.2;
    font-weight: 800;
    margin: 15px 0 10px;
}

.hero p {
    color: #fff3eb;
    font-size: 14px;
    line-height: 1.7;
    margin-bottom: 18px;
}

.hero-note {
    background: rgba(255,255,255,0.88);
    color: #795548;
    border-radius: 30px;
    padding: 11px 14px;
    font-size: 12px;
}

/* Section headings */
.section-title {
    color: #292524;
    font-size: 22px;
    font-weight: 800;
    margin: 20px 0 4px;
}

.section-subtitle {
    color: #78716c;
    font-size: 13px;
    margin-bottom: 16px;
}

/* Food cards */
div[data-testid="stVerticalBlockBorderWrapper"] {
    background: rgba(255,255,255,0.96);
    border: 1px solid #f2e5d9;
    border-radius: 16px;
    box-shadow: 0 5px 18px rgba(60,35,20,0.045);
}

div[data-testid="stImage"] img {
    border-radius: 12px;
}

.food-name {
    font-size: 14px;
    color: #292524;
    font-weight: 700;
    margin-top: 8px;
}

.food-category {
    font-size: 12px;
    color: #a16242;
    margin-top: 3px;
}

/* Form labels and inputs */
label {
    color: #44403c !important;
    font-weight: 600 !important;
}

div[data-testid="stNumberInput"] input {
    border-radius: 10px;
}

div[data-baseweb="select"] > div {
    border-radius: 10px;
}

/* Primary prediction button */
div.stButton > button {
    width: 100%;
    min-height: 52px;
    border: none;
    border-radius: 12px;
    background: linear-gradient(90deg, #ff7535, #f04423);
    color: white;
    font-weight: 800;
    font-size: 15px;
    transition: all 0.2s ease;
    box-shadow: 0 5px 14px rgba(240,68,34,0.16);
}

div.stButton > button:hover {
    background: #df3c1d;
    color: white;
    border: none;
    box-shadow: 0 7px 18px rgba(240,68,34,0.25);
}

/* Prediction tip */
.tip {
    background: #fff7ef;
    border: 1px solid #ffdfc9;
    padding: 14px;
    border-radius: 12px;
    color: #8b451f;
    font-size: 12px;
    line-height: 1.6;
    margin-top: 12px;
}

/* Prediction result */
.result-card {
    background: linear-gradient(135deg, #effaf1, #f8fff8);
    border: 1px solid #c8e6cc;
    border-radius: 18px;
    padding: 25px 15px;
    text-align: center;
    margin-top: 20px;
    margin-bottom: 10px;
}

.result-label {
    color: #32634b;
    font-size: 12px;
    font-weight: 800;
    letter-spacing: 1.5px;
}

.result-number {
    color: #087443;
    font-size: 48px;
    font-weight: 800;
    line-height: 1.35;
}

.result-subtitle {
    color: #365b49;
    font-size: 14px;
}

.footer-note {
    text-align: center;
    color: #92877f;
    font-size: 11px;
    padding: 20px 0 5px;
}

@media (max-width: 600px) {
    .block-container {
        padding-left: 0.8rem;
        padding-right: 0.8rem;
    }

    .hero {
        padding: 24px 16px;
    }

    .hero h1 {
        font-size: 27px;
    }

    .result-number {
        font-size: 40px;
    }
}
</style>
""", unsafe_allow_html=True)


# ==================================================
# STEP 3: Load the trained model - unchanged
# ==================================================
@st.cache_resource
def load_model():
    with open("delivery_model.pkl", "rb") as file:
        package = pickle.load(file)
    return package["model"], package["features"]


model, features = load_model()


# ==================================================
# STEP 4: Hero banner
# ==================================================
st.html("""
<div class="hero">
    <div class="hero-tag">🍴 SMART DELIVERY ANALYTICS</div>

    <h1>🍔 Food Delivery<br>Time Predictor</h1>

    <p>
        Craving something delicious?
        Estimate your food delivery time using machine learning.
    </p>

    <div class="hero-note">
        🛵 Enter your order details and discover your estimated delivery time.
    </div>
</div>
""")


# ==================================================
# STEP 5: Food showcase - decorative UI only
# ==================================================
st.markdown("""
<div class="section-title">🍽️ Explore Popular Foods</div>
<div class="section-subtitle">
    A few delicious favourites to make your delivery dashboard feel alive.
</div>
""", unsafe_allow_html=True)

food_items = [
    {
        "name": "Paneer Curry",
        "category": "🇮🇳 North Indian",
        "image": (
            "https://images.unsplash.com/"
            "photo-1631452180519-c014fe946bc7"
            "?auto=format&fit=crop&w=600&q=85"
        ),
    },
    {
        "name": "Cheese Pizza",
        "category": "🇮🇹 Italian",
        "image": (
            "https://images.unsplash.com/"
            "photo-1513104890138-7c749659a591"
            "?auto=format&fit=crop&w=600&q=85"
        ),
    },
    {
        "name": "Classic Burger",
        "category": "🍔 Fast Food",
        "image": (
            "https://images.unsplash.com/"
            "photo-1568901346375-23c9450c58cd"
            "?auto=format&fit=crop&w=600&q=85"
        ),
    },
]

food_cols = st.columns(3, gap="small")

for col, food in zip(food_cols, food_items):
    with col:
        with st.container(border=True):
            st.image(
                food["image"],
                use_container_width=True,
            )
            st.markdown(
                f'<div class="food-name">{food["name"]}</div>'
                f'<div class="food-category">{food["category"]}</div>',
                unsafe_allow_html=True,
            )


# ==================================================
# STEP 6: Delivery information form - unchanged inputs
# ==================================================
st.markdown("""
<div class="section-title">📦 Enter Delivery Details</div>
<div class="section-subtitle">
    Provide the details of your food delivery.
</div>
""", unsafe_allow_html=True)

with st.container(border=True):

    input_left, input_right = st.columns(2, gap="medium")

    with input_left:
        distance_km = st.number_input(
            "🛵 Delivery distance (km)",
            min_value=0.1,
            max_value=50.0,
            value=5.0,
            step=0.5,
        )

        preparation_time_min = st.number_input(
            "🍳 Food preparation time (minutes)",
            min_value=1,
            max_value=120,
            value=15,
        )

        rider_experience_years = st.number_input(
            "🧑 Rider experience (years)",
            min_value=0,
            max_value=50,
            value=3,
        )

    with input_right:
        traffic_level = st.selectbox(
            "🚦 Traffic level",
            options=[1, 2, 3, 4],
            format_func=lambda x: {
                1: "1 - Low",
                2: "2 - Moderate",
                3: "3 - High",
                4: "4 - Severe",
            }[x],
        )

        weather_severity = st.selectbox(
            "🌦️ Weather severity",
            options=[0, 1, 2, 3],
            format_func=lambda x: {
                0: "0 - Clear",
                1: "1 - Light adverse weather",
                2: "2 - Bad weather",
                3: "3 - Severe weather",
            }[x],
        )

        st.markdown("""
        <div class="tip">
            <b>💡 Delivery prediction tip</b><br><br>
            Distance, preparation time, traffic and weather
            can all influence estimated delivery duration.
        </div>
        """, unsafe_allow_html=True)


# ==================================================
# STEP 7: Prediction - original functionality unchanged
# ==================================================
st.write("")

if st.button("🚀 Predict Delivery Time", type="primary"):

    # Prepare the new input - original feature order
    new_delivery = pd.DataFrame(
        [
            [
                distance_km,
                preparation_time_min,
                traffic_level,
                weather_severity,
                rider_experience_years,
            ]
        ],
        columns=features,
    )

    # Make the prediction
    prediction = model.predict(new_delivery)[0]

    # Prevent a negative displayed duration
    prediction = max(0, prediction)

    # Display the result
    st.markdown(
        f"""
        <div class="result-card">
            <div class="result-label">
                ⏱ ESTIMATED DELIVERY TIME
            </div>
            <div class="result-number">{prediction:.1f}</div>
            <div class="result-subtitle">
                minutes to deliver your order
            </div>
            <p style="color:#557866;font-size:12px;margin-bottom:0;">
                ℹ️ This is a model estimate, not a guaranteed arrival time.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )


# ==================================================
# STEP 8: Footer
# ==================================================
st.divider()

st.markdown("""
<div class="footer-note">
    Made with ❤️ using Python · Pandas · Scikit-learn · Pickle · Streamlit
    <br><br>
    FOOD DELIVERY TIME PREDICTOR | EDUCATIONAL PROJECT
</div>
""", unsafe_allow_html=True)
