import streamlit as st
import openai

openai.api_key = st.secrets["OPENAI_API_KEY"]

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",  # atau "gpt-4" jika kamu punya akses
    messages=[
        {"role": "system", "content": "Kamu adalah penulis konten profesional."},
        {"role": "user", "content": prompt}
    ],
    max_tokens=100
)

generated_text = response['choices'][0]['message']['content']
        st.text_area("Hasil Konten:", value=hasil, height=150)
    else:
        st.warning("Masukkan topik dulu ya!")
