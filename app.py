import streamlit as st

# Title of the app
st.title("Student Information")
title = st.text_input("Enter the Student name", "Tintin")
age = st.slider("Select the student's age", 1, 100,25)
if st.button("Display Information"):
    st.write("Student's name: ",title)
    st.write("Student's age: ",age)