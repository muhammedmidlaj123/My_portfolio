import streamlit as st
import requests
import json

# --- PAGE SETUP ---
st.set_page_config(page_title="Midhilaj's Portfolio", page_icon="🚀")

# 1. Main Title
st.title("Hi, I am Midhilaj EK! 👋")

# 2. Subtitle
st.subheader("Junior Python Developer & AI Enthusiast based in Dubai")

# 3. Bio
st.write("""
I am a passionate developer currently building AI-powered applications.
I have experience with Python, Object-Oriented Programming, and Streamlit.
""")

# 4. Sidebar
st.sidebar.header("Skills")
st.sidebar.write("🐍 Python")
st.sidebar.write("🤖 Artificial Intelligence")
st.sidebar.write("📊 Data Analysis")
st.sidebar.write("---")
st.sidebar.write("📍 Dubai, UAE")

# 5. Projects
st.write("---")
st.header("My Projects")

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

# 6. Education
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

# 7. THE "DIRECT LINE" AI CHAT BOT 🤖
st.header("🤖 Chat with My AI Bot")

# Securely ask for the Key
api_key = st.text_input("Enter your Google API Key to Chat:", type="password")

# Initialize Chat History
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display Old Messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat Input
if prompt := st.chat_input("Ask me anything about Midhilaj..."):
    # Show User Message
    st.chat_message("user").markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    if not api_key:
        st.error("Please enter an API Key to chat!")
    else:
        # --- THE FIX: Using 'gemini-pro' instead of 'flash' ---
        try:
            url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key={api_key}"
            headers = {"Content-Type": "application/json"}
            
            system_instruction = "You are an AI assistant for Midhilaj EK's Portfolio. You are professional and helpful."
            
            data = {
                "contents": [{
                    "parts": [{"text": system_instruction + "\nUser said: " + prompt}]
                }]
            }

            response = requests.post(url, headers=headers, json=data)
            
            if response.status_code == 200:
                result = response.json()
                # Check if the response has the expected structure
                if 'candidates' in result and result['candidates']:
                     ai_text = result['candidates'][0]['content']['parts'][0]['text']
                     with st.chat_message("assistant"):
                         st.markdown(ai_text)
                     st.session_state.messages.append({"role": "assistant", "content": ai_text})
                else:
                     st.error("Google AI replied, but blocked the content (Safety Filter). Try a different question.")

            else:
                st.error(f"Google Error: {response.status_code} - {response.text}")

        except Exception as e:
            st.error(f"Connection Error: {e}")
