import streamlit as st
import random
import datetime

# =============================
# PAGE CONFIG
# =============================
st.set_page_config(
    page_title="Semangat Captain Err 🤍",
    page_icon="🤍",
    layout="centered"
)

# =============================
# HEADER
# =============================
st.title("Semangat Captain Err 🤍")
st.subheader("Untuk Abang-Abang UNPAD Favoritku ✨")

st.markdown(
    """
    <audio autoplay loop>
        <source src="lagu.mp3" type="audio/mp3">
    </audio>
    """,
    unsafe_allow_html=True
)

# =============================
# QUOTES
# =============================
quotes = [
    "Sayangg, aku bangga banget sama kamu 🤍",
    "Selamat telah melewati hari ini dan temu kangen bersama bro dosenmuu 😆",
    "Maafff, hari ini kita belum bisa ketemu yaa, semoga dirimu tidak marah 🤍",
    "Ohhiya, aku mau bilang kalooo… aku selalu bangga sama kamu.",
    "Skripsi nggak akan lebih kuat dari kamu.",
    "Kalau cape, istirahat yaa, jangan dipendem sendiri.",
    "Aku nemenin kamu di sini, selaluu 🎓"
]

# =============================
# BUTTON PESAN RANDOM
# =============================
import time

if st.button("💌 Pesan Spesial"):
    st.balloons()
    for q in quotes:
        st.success(q)
        time.sleep(1)

# =============================
# PESAN HARI INI OTOMATIS
# =============================
st.markdown("---")
today = datetime.date.today()
index = today.day % len(quotes)

st.write("🌷 Pesan Hari Ini:")
st.info(quotes[index])

# =============================
# CEK CAPEK LEVEL
# =============================
st.markdown("---")
mood = st.select_slider(
    "Seberapa capek Captain hari ini?",
    options=["😌 Santai", "🙂 Lumayan", "😔 Capek", "😭 Sangat Capek"]
)

if mood == "😔 Capek":
    st.info("Aku tau kamu capek. Tapi kamu nggak sendirian 🤍")
elif mood == "😭 Sangat Capek":
    st.warning("Sini cerita dulu… Captain juga boleh lelah.")
elif mood == "🙂 Lumayan":
    st.success("Good progress! Sedikit demi sedikit yaa 🤍")
elif mood == "😌 Santai":
    st.success("Wahh lancar nih bimbingannya 😆")

# =============================
# FOOTER
# =============================
st.markdown("---")
st.caption("Dibuat khusus dengan penuh sayang 🤍✨")