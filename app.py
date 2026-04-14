import streamlit as st
import pandas as pd

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
st.subheader(f"Total Calories: {total}")
