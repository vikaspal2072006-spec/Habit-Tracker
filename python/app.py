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

st.divider()
st.subheader("🗑️ Remove Habit")
if habits:
    selected_habit = st.selectbox(
        "Select a habit to remove",
        habits
    )

    if st.button("Remove Habit"):
        habits.remove(selected_habit)
        st.success("Habit removed successfully")
        st.rerun()

else:
    st.info("No habits available to remove. ")

st.divider()
st.subheader("✅ Daily Habit Tracker")
habit_status = {}
for habit in habits:
    habit_status[habit] = st.checkbox(habit)
    if habit_status[habit]:
        st.success(f"{habit}completed")
    else:
        st.info(f"{habit}pending")

complete_count = sum(habit_status.values())
total_habit=len(habits)
if total_habit>0:
    percentage=(complete_count/total_habit)*100
else:
    percentage=0

st.divider()
st.subheader("📊 Today's Progress")
st.metric("Complete Habit",f"{complete_count}/{total_habit}")
st.progress(percentage/100)
st.write(f"{percentage:.2f}% Completed")
