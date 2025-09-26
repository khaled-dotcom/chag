import streamlit as st
import requests

st.title("Khaled Chat Online 🤖")

API_URL = "https://api-inference.huggingface.co/models/khaledghalwash/khaled_chatkkj"
HEADERS = {"Authorization": f"Bearer {st.secrets['HF_TOKEN']}"}

def query_model(prompt):
    try:
        response = requests.post(API_URL, headers=HEADERS, json={"inputs": prompt})
        response.raise_for_status()
        data = response.json()
        if isinstance(data, list) and "generated_text" in data[0]:
            return data[0]["generated_text"]
        else:
            return str(data)
    except Exception as e:
        return f"Error: {e}"

user_input = st.text_input("Write your message:")

if st.button("Send"):
    reply = query_model(user_input)
    st.write(reply)
