import streamlit as st
import openai

openai.api_key = st.secrets["OPENAI_API_KEY"]

prompt = st.text_input("Masukkan topik:")

if prompt:
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Kamu adalah penulis konten profesional."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=100
    )

    hasil1 = response['choices'][0]['message']['content']

    st.text_area("Hasil Konten:", value=hasil1, height=150)
else:
    st.warning("Masukkan topik dulu ya!")
