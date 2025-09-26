import streamlit as st
import requests

st.title("Khaled Chat Online 🤖")

API_URL = "https://api-inference.huggingface.co/models/khaledghalwash/khaled_chatkkj"

def query_model(prompt):
    response = requests.post(API_URL, json={"inputs": prompt})
    # Some models return a dict with 'generated_text'
    return response.json()[0]['generated_text']

user_input = st.text_input("Write your message:")

if st.button("Send"):
    reply = query_model(user_input)
    st.write(reply)
