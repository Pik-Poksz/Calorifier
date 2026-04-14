import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

# 💖 NEW THEME (replace your old CSS block with this)
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

/* Input boxes */
.stTextInput input {
    border-radius: 10px;
    border: 2px solid #f8c8dc;
}

/* Number input */
.stNumberInput input {
    border-radius: 10px;
    border: 2px solid #e0aaff;
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


# 👇 REST OF YOUR CODE SAME
st.title("Calorie Tracker")

if "data" not in st.session_state:
    st.session_state.data = pd.DataFrame(columns=["Food", "Calories"])

food = st.text_input("Enter food item")
calories = st.number_input("Enter calories", min_value=0)

if st.button("Add"):
    new_entry = pd.DataFrame([[food, calories]], columns=["Food", "Calories"])
    st.session_state.data = pd.concat([st.session_state.data, new_entry], ignore_index=True)

st.subheader("Today's Intake")
st.dataframe(st.session_state.data)

total = st.session_state.data["Calories"].sum()

# ---- DAILY GOAL ----
goal = st.number_input("Daily Calorie Goal", value=2000)
remaining = goal - total

# ---- DASHBOARD CARDS ----
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

st.subheader(f"Total Calories: {total}")
