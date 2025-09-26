import streamlit as st
import requests

st.title("Khaled Chat Online 🤖")

# Hugging Face Inference API URL
API_URL = "https://api-inference.huggingface.co/models/khaledghalwash/khaled_chatkkj"

# Use your Hugging Face token safely
# If your model is public, you can remove HEADERS entirely
HEADERS = {"Authorization": "Bearer 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"}

def query_model(prompt):
    """Send prompt to HF Inference API and return generated text"""
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

# Input from user
user_input = st.text_input("Write your message:")

# Send button
if st.button("Send"):
    reply = query_model(user_input)
    st.write(reply)
