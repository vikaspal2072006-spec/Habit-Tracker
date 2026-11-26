import streamlit as st

st.title("🎯 Welcome to LifeOS")
st.subheader("Build better habits, build a better life.")

st.divider()
st.header("👤 User Profile")
name = st.text_input("Enter your name :- ")
if name:
    st.success(f"Welcome,{name}!!!")
st.divider()
st.header("🎯 My Daily Habits")
habits=[
    "Wake Up Early",
    "Exercise",
    "Create Project",
    "Study Python",
    "Practice English",
    "Read Books",
    "Drink Enough Water"
]
for index,habit in enumerate(habits,start=1):
    st.write(index,habit)
st.divider()
st.subheader("➕ Add New Habit")
new_habit=st.text_input("Enter new habit")
if st.button("ADD HABIT"):
    if new_habit.strip():
        habits.append(new_habit.strip())
        st.success("New habit added successfully")
    else:
        st.warning("Enter Habit ")

