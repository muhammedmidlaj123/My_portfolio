import streamlit as st

# --- PAGE SETUP ---
st.set_page_config(page_title="Midhilaj's Portfolio", page_icon="🚀")

# 1. Main Title
st.title("Hi, I am Midhilaj EK! 👋")

# 2. Subtitle
st.subheader("Junior Python Developer & AI Enthusiast based in Dubai")

# 3. Simple Text
st.write("""
I am a passionate developer currently building AI-powered applications.
I have experience with Python, Object-Oriented Programming, and Streamlit.
""")

# 4. Sidebar info
st.sidebar.header("Skills")
st.sidebar.write("🐍 Python")
st.sidebar.write("🤖 Artificial Intelligence")
st.sidebar.write("📊 Data Analysis")
st.sidebar.write("---")
st.sidebar.write("📍 Dubai, UAE")

# 5. Projects Section
st.write("---")
st.header("My Projects")

# Project 1: Smart Bank AI
with st.container():
    col1, col2 = st.columns([1, 2])
    with col1:
        st.header("🏦")
    with col2:
        st.subheader("Smart Bank System")
        st.write("""
        - A secure banking system built with Python.
        - Features: Login/Signup, Loan Calculator, and Transaction History.
        """)
        st.link_button("View Code on GitHub", "https://github.com/muhammedmidlaj123/bank-system-python")

st.write("---")

# 6. Education Section
st.header("Education & Timeline")
edu_col1, edu_col2 = st.columns(2)

with edu_col1:
    st.subheader("🎓 Education")
    st.write("**Bachelor of Computer Applications (BCA)**")
    st.write("IGNOU (UAE Center) | *Current Student*")
    st.write("---")
    st.write("**Commerce Stream (Plus Two)**")
    st.write("Completed with Focus on Business")

with edu_col2:
    st.subheader("🚀 My Journey")
    st.write("""
    - **Sept 2025:** Started learning Python basics.
    - **Nov 2025:** Explored AI & Gen Ai Roadmaps.
    - **Jan 2026:** Built 'Smart Bank' System.
    - **Goal:** To secure an Internship in AI/Gen AI by March 2026.
    """)

st.write("---")
st.header("🤖 AI Chat Bot")
st.info("The AI Bot is currently undergoing maintenance. Check back soon!")
