import streamlit as st
import requests
import json

# --- CONFIGURATION ---
st.set_page_config(page_title="Midhilaj's Portfolio", page_icon="🚀")

# --- API SETUP (SECURE) ---
try:
    # 🔑 This pulls the key from Streamlit Cloud Secrets!
    API_KEY = st.secrets["GOOGLE_API_KEY"]
except FileNotFoundError:
    st.error("⚠️ Key not found. Did you add GOOGLE_API_KEY to Streamlit Secrets?")
    st.stop()

URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key={API_KEY}"

# --- SIDEBAR & HEADER ---
st.sidebar.header("Tech Stack")
st.sidebar.markdown(
    """
    ![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
    ![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=flat&logo=Streamlit&logoColor=white)
    ![Gemini AI](https://img.shields.io/badge/Google%20Gemini-8E75B2?style=flat&logo=googlebard&logoColor=white)
    ![Git](https://img.shields.io/badge/Git-F05032?style=flat&logo=git&logoColor=white)
    ![VS Code](https://img.shields.io/badge/VS%20Code-007ACC?style=flat&logo=visualstudiocode&logoColor=white)
    """
)
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
        st.header("🧾")
    with col2:
        st.subheader("AI Invoice Automator (New!)")
        st.write("""
        - **Automated Data Entry:** Extracts Invoice #, Date, and Totals from PDFs using AI.
        - **Tech:** Python, Gemini Flash, Streamlit.
        - **Impact:** Reduces manual work by 90%.
        """)
        st.link_button("View Code", "https://github.com/muhammedmidlaj123/Invoice-Automation-Agent")

with st.container():
    col1, col2 = st.columns([1, 2])
    with col1:
        st.header("🏦")
    with col2:
        st.subheader("Smart Bank System")
        st.write("""
        - A secure banking logic app with Login/Signup & Transaction history.
        - Built using Python OOP and File Handling.
        """)
        st.link_button("View Code", "https://github.com/muhammedmidlaj123/bank-system-python")
st.write("---") # A divider line

with st.container():
    col1, col2 = st.columns([1, 3])
    
    with col1:
        # You can use an emoji or an image here
        st.header("📄") 
        
    with col2:
        st.subheader("The AI Document Expert (RAG)")
        st.write("""
        **The Problem:** Reading long PDF policies or resumes takes too much time.
        **The Solution:** An AI-powered tool that reads the PDF for you.
        - **Tech Stack:** Python, Google Gemini 1.5, PyPDF2, Streamlit.
        - **Key Feature:** Upload any PDF and chat with it like a human.
        """)
        
        # LINK THE BUTTON TO YOUR NEW APP
        st.link_button("🚀 Launch App", "https://pdf-analyser-8dtyzpy6pfya8u9oyocipk.streamlit.app/")

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

st.write("---")

# --- AI CHATBOT SECTION ---
st.header("🤖 Chat with My AI Bot")
st.write("Ask me about my skills, projects, or resume!")

# 1. Initialize Chat History
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hello! I am Zam's AI Assistant. Ask me about his Invoice Project!"}
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
            # Context for the AI (Updated with Invoice Project)
            context_text = """
            You are an enthusiastic AI assistant for Midhilaj EK (Zam).
            Your goal is to promote him to recruiters as a Junior Python Developer.
            
            - Location: Dubai, UAE (Visit Visa).
            - Contact: +971 56 661 4794 | muhammmedmidlaj2021@gmail.com
            
            - TECHNICAL SKILLS:
              Python, Streamlit, Gemini API, JSON Parsing, Automation, Git, VS Code.
            
            - KEY PROJECTS (Sell these!):
              1. **AI Invoice Automator**: A tool that uses Gemini Flash to extract data (Total, Date, Vendor) from PDF invoices automatically. It solves manual data entry problems.
              2. **Smart Bank System**: A Python-based banking logic app with secure login and transaction history.
              3. **AI Portfolio**: This website itself! A RAG-based chatbot built with Streamlit.

            - BACKGROUND:
              He is a Commerce student who self-taught Python and AI in just a few months. He is a VERY fast learner and ready to join immediately as an intern.

            INSTRUCTIONS:
            - If asked about the "Invoice Project", emphasize that it automates boring work and saves time.
            - If asked "Why hire him?", mention his speed in learning and his practical projects.
            - Keep answers short, punchy, and professional.
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
