import streamlit as st
import google.generativeai as genai

st.title("My AI App")

GOOGLE_API_KEY = "AIzaSyClqufiEjImdlm_iU6avdStm7GdXu0_yL4"
genai.configure(api_key=GOOGLE_API_KEY)

user_input = st.text_input("Ask me anything:")

if st.button("Send"):
    model = genai.GenerativeModel('gemini-2.5-flash')
    response = model.generate_content(user_input)
    st.write(response.text)
