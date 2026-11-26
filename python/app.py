import streamlit as st

st.title("🎯 Welcome to LifeOS")
st.subheader("Build better habits, build a better life.")

name = st.text_input("ENTER YOUR NAME :- ")
if name:
    st.success("welcome,{name}!!!")

st.divider()
st.header("👤 User Profile")
name = st.text_input("Enter your name :- ")
if name:
    st.success(f"Welcome,{name}!!!")
    