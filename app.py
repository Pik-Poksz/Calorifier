import streamlit as st
import pandas as pd

# ---- PAGE SETUP ----
st.set_page_config(layout="wide")

# ---- PINK + PURPLE THEME ----
st.markdown("""
<style>

/* Background */
[data-testid="stAppViewContainer"] {
    background: linear-gradient(135deg, #ffe4ec, #f3e5ff);
}

/* Title */
h1 {
    color: #d63384;
}

/* Inputs */
.stTextInput input, .stNumberInput input {
    border-radius: 10px;
    border: 2px solid #f8c8dc;
}

/* Button */
.stButton button {
    background: linear-gradient(90deg, #ff85a2, #c77dff);
    color: white;
    border-radius: 12px;
    border: none;
    padding: 10px 20px;
}

/* Cards */
.stMetric {
    background: linear-gradient(135deg, #ffd6e0, #e5ccff);
    padding: 15px;
    border-radius: 15px;
    text-align: center;
    color: #5a0f3b;
}

/* Table */
[data-testid="stDataFrame"] {
    background-color: #ffffff;
    border-radius: 10px;
}

</style>
""", unsafe_allow_html=True)

# ---- TITLE ----
st.title("💖 Calorie Tracker")

# ---- SESSION STATE ----
if "data" not in st.session_state:
    st.session_state.data = pd.DataFrame(columns=["Food", "Calories"])

# ---- INPUT SECTION ----
st.subheader("🍽️ Add Food")

food = st.text_input("Enter food item")
calories = st.number_input("Enter calories", min_value=0)

if st.button("Add"):
    new_entry = pd.DataFrame([[food, calories]], columns=["Food", "Calories"])
    st.session_state.data = pd.concat([st.session_state.data, new_entry], ignore_index=True)

# ---- CAMERA SECTION ----
st.subheader("📸 Capture your meal")

image = st.camera_input("Take a picture of your food")

if image:
    st.image(image, caption="Your Meal", use_column_width=True)
    st.write("🔍 Analyzing food...")

    # Dummy AI result (for now)
    food_name = "Rice + Curry"
    calories_est = 450

    st.success(f"Detected: {food_name}")
    st.info(f"Estimated Calories: {calories_est}")

# ---- DATA DISPLAY ----
st.subheader("📊 Today's Intake")
st.dataframe(st.session_state.data)

# ---- CALCULATIONS ----
total = st.session_state.data["Calories"].sum()

goal = st.number_input("🎯 Daily Calorie Goal", value=2000)
remaining = goal - total

# ---- DASHBOARD ----
col1, col2 = st.columns(2)

with col1:
    st.markdown("### 🔥 Calories")
    st.metric("Food", total)
    st.metric("Remaining", remaining)

with col2:
    st.markdown("### 🥗 Macros")
    st.write("Carbs: --")
    st.write("Protein: --")
    st.write("Fat: --")

# ---- PROGRESS BAR ----
progress = total / goal if goal > 0 else 0
st.progress(min(progress, 1.0))

# ---- TOTAL ----
st.subheader(f"Total Calories: {total}")
