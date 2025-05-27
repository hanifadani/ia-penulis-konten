import streamlit as st
import openai

# GANTI dengan API key kamu
openai.api_key = "sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxx"

st.title("AI Penulis Konten Otomatis")

topik = st.text_input("Topik Konten:")
gaya = st.selectbox("Gaya Bahasa:", ["Santai", "Formal", "Lucu", "Motivasi", "Untuk Iklan"])

if st.button("Generate"):
    if topik:
        prompt = f"Tuliskan konten singkat tentang '{topik}' dengan gaya '{gaya}' dalam 2-3 kalimat."
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=100
        )
        hasil = response.choices[0].text.strip()
        st.text_area("Hasil Konten:", value=hasil, height=150)
    else:
        st.warning("Masukkan topik dulu ya!")