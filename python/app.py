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
if "habits" not in st.session_state:
    st.session_state.habits=[
    "Wake Up Early",
    "Exercise",
    "Create Project",
    "Study Python",
    "Practice English",
    "Read Books",
    "Drink Enough Water"
]
habits = st.session_state.habits
for index,habit in enumerate(habits,start=1):
    st.write(index,habit)
st.divider()
st.subheader("➕ Add New Habit")
new_habit=st.text_input("Enter new habit")
if st.button("Add Habit"):

    new_habit = new_habit.strip()

    if not new_habit:
        st.warning("Please enter a habit name.")

    elif new_habit.lower() in [habit.lower() for habit in habits]:
        st.warning("Habit already exists!")

    else:
        habits.append(new_habit)
        st.success("Habit added successfully!!!!")
        st.rerun()