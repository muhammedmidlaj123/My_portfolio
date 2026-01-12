import streamlit as st
import requests
import json

# --- CONFIGURATION ---
st.set_page_config(page_title="Midhilaj's Portfolio", page_icon="🚀")

# 🔑 PASTE YOUR REAL API KEY HERE
API_KEY = "YOUR_API_KEY_HERE" 
URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key={API_KEY}"

# --- SIDEBAR & HEADER ---
st.sidebar.header("Skills")
st.sidebar.write("🐍 Python")
st.sidebar.write("🤖 Artificial Intelligence")
st.sidebar.write("📊 Data Analysis")
st.sidebar.write("🌐 Streamlit & APIs")

st.title("Hi, I am Midhilaj EK! 👋")
st.subheader("Junior Python Developer & AI Enthusiast based in Dubai")

st.write("""
I am a passionate developer currently building AI-powered applications.
I have experience with Python, Object-Oriented Programming, and Google Gemini AI.
""")

st.write("---")

# --- PROJECTS SECTION ---
st.header("My Projects")
with st.container():
    col1, col2 = st.columns([1, 2])
    with col1:
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

# --- EDUCATION SECTION ---
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
    - **Jan 2026:** Built 'Smart Bank' with Google Gemini AI.
    - **Goal:** To secure an Internship in AI/Gen AI by March 2026.
    """)

st.write("---")

# --- AI CHATBOT SECTION ---
st.header("🤖 Chat with My AI Bot")
st.write("Ask me about my skills, projects, or resume!")

# 1. Initialize Chat History
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hello! I am Zam's AI Assistant. Ask me anything about his work!"}
    ]

# 2. Display Old Messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 3. Handle New Input
if prompt := st.chat_input("Ask something..."):
    
    # Show User Message
    with st.chat_message("user"):
        st.markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # THE BRAIN 🧠
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        message_placeholder.markdown("Thinking...")

        try:
            # Context for the AI
            context_text = """
            You are an AI assistant for Midhilaj EK (Zam).
            - Location: Dubai, UAE (Visit Visa).
            - Education: BCA Student at IGNOU, Commerce Background.
            - Skills: Python, Streamlit, API Integration, JSON, Requests.
            - Projects: Smart Bank System (Python), Portfolio Website.
            - Goal: Seeking Internship in AI/Robotics.
            Keep answers professional and concise.
            """
            
            payload = {
                "system_instruction": {
                    "parts": [{"text": context_text}]
                },
                "contents": [{"parts": [{"text": prompt}]}]
            }
            
            headers = {'Content-Type': 'application/json'}
            response = requests.post(URL, headers=headers, data=json.dumps(payload))
            
            if response.status_code == 200:
                data = response.json()
                ai_response = data["candidates"][0]["content"]["parts"][0]["text"]
            else:
                ai_response = f"Error: {response.status_code} - {response.text}"

        except Exception as e:
            ai_response = f"Connection Failed: {e}"

        message_placeholder.markdown(ai_response)
    
    st.session_state.messages.append({"role": "assistant", "content": ai_response})
