import streamlit as st
from transformers import AutoModelForCausalLM, AutoTokenizer

st.title("Khaled Chat Online 🤖")


@st.cache_resource
def load_model():
    tokenizer = AutoTokenizer.from_pretrained(
        "khaledghalwash/khaled_chatkkj",
        use_auth_token=HUGGINGFACE_TOKEN
    )
    model = AutoModelForCausalLM.from_pretrained(
        "khaledghalwash/khaled_chatkkj",
        use_auth_token=HUGGINGFACE_TOKEN
    )
    return tokenizer, model

tokenizer, model = load_model()

def chat(user_input):
    inputs = tokenizer(user_input, return_tensors="pt")
    outputs = model.generate(**inputs, max_length=100)
    return tokenizer.decode(outputs[0], skip_special_tokens=True)

user_input = st.text_input("Your message:")

if st.button("Send"):
    st.write(chat(user_input))
