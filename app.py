import streamlit as st
import openai

# Judul dan deskripsi
st.set_page_config(page_title="AI Penulis Konten", layout="centered")
st.title("✍ AI Penulis Konten Otomatis")
st.markdown("Buat konten secara instan dengan bantuan AI. Masukkan topik, dan dapatkan hasil tulisan secara otomatis.")

# API Key dari secrets
OPENAI_API_KEY = "sk-xxxxxxxxxxxxxxxxxxxxxxxx"

# Input dari user
prompt = st.text_input("📝 Masukkan topik konten:")

# Proses saat ada input
if prompt:
    with st.spinner("Sedang menulis..."):
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Kamu adalah penulis konten profesional."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=300
        )
        hasil = response["choices"][0]["message"]["content"]
        st.text_area("📄 Hasil Konten", value=hasil, height=250)
        st.download_button("⬇ Download Hasil", data=hasil, file_name="konten.txt", mime="text/plain")
else:
    st.info("Masukkan topik terlebih dahulu.")
