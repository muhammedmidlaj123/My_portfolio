import streamlit as st
import google.generativeai as genai

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Midhilaj's Portfolio",
    page_icon="🚀",
    layout="centered"
)

# ---------------- HEADER ----------------
st.title("Hi, I am Midhilaj EK! 👋")
st.subheader("Junior Python Developer & AI Enthusiast based in Dubai")

st.write("""
I am a passionate developer currently building AI-powered applications.
I have experience with Python, Object-Oriented Programming, and Streamlit.
""")

# ---------------- SIDEBAR ----------------
st.sidebar.header("Skills")
st.sidebar.write("🐍 Python")
st.sidebar.write("🤖 Artificial Intelligence")
st.sidebar.write("📊 Data Analysis")
st.sidebar.markdown("---")
st.sidebar.write("📍 Dubai, UAE")

# ---------------- PROJECTS ----------------
st.markdown("---")
st.header("My Projects")

col1, col2 = st.columns([1, 2])
with col1:
    st.markdown("## 🏦")
with col2:
    st.subheader("Smart Bank System")
    st.write("""
    • Secure banking system built with Python  
    • Login / Signup  
    • Loan Calculator  
    • Transaction History  
    """)
    st.lin

