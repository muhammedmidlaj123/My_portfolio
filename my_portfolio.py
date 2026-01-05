
import streamlit as st

# 1. Main Title
st.title("Hi, I am Midhilaj EK! 👋")

# 2. Subtitle
st.subheader("Junior Python Developer & AI Enthusiast based in Dubai")

# 3. Simple Text
st.write("""
I am a passionate developer currently building AI-powered applications.
I have experience with Python, Object-Oriented Programming, and Google Gemini AI.
""")

# 4. Sidebar info
st.sidebar.header("Skills")
st.sidebar.write("🐍 Python")
st.sidebar.write("🤖 Artificial Intelligence")
st.sidebar.write("📊 Data Analysis")
st.write("---")  # This adds a divider line

st.header("My Projects")

# Project 1: Smart Bank AI
with st.container():
    col1, col2 = st.columns([1, 2])  # Split screen into 2 parts

    with col1:
        # We will add a real screenshot later. For now, an icon.
        st.header("🏦")

    with col2:
        st.subheader("Smart Bank System with AI")
        st.write("""
        - A secure banking system built with Python & File Handling.
        - Integrated **Google Gemini AI** to give financial advice.
        - Features: Login/Signup, Loan Calculator, and Transaction History.
        """)
        st.link_button("View Code on GitHub", "https://github.com/muhammedmidlaj123/bank-system-python")
        st.write("---")
        st.header("Education & Timeline")

        col1, col2 = st.columns(2)

        with col1:
            st.subheader("🎓 Education")
            st.write("**Bachelor of Computer Applications (BCA)**")
            st.write("IGNOU (UAE Center) | *Current Student*")
            st.write("---")
            st.write("**Commerce Stream (Plus Two)**")
            st.write("Completed with Focus on Business")

        with col2:
            st.subheader("🚀 My Journey")
            st.write("""
            - **Sept 2025:** Started learning Python basics.
            - **Nov 2025:** Explored AI & Gen Ai Roadmaps.
            - **Jan 2026:** Built 'Smart Bank' with Google Gemini AI.
            - **Goal:** To secure an Internship in AI/Gen AI by March 2026.
            """)