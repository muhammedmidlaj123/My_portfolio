import streamlit as st
import requests
import json

# --- PAGE CONFIG ---
st.set_page_config(page_title="Midhilaj's Portfolio", page_icon="🚀")

# --- MAIN LAYOUT ---
st.title("Hi, I am Midhilaj EK! 👋")
st.subheader("Junior Python Developer & AI Enthusiast based in Dubai")

st.write("""
I am a passionate developer currently building AI-powered applications.
I have experience with Python, Object-Oriented Programming, and Streamlit.
""")

st.write("---")

# --- SIDEBAR ---
st.sidebar.header("Skills")
st.sidebar.write("🐍 Python")
st.sidebar.write("🤖 Artificial Intelligence")
st.sidebar.write("📊 Data Analysis")
st.sidebar.write("---")
st.sidebar.write("📍 Dubai, UAE")

# --- PROJECTS ---
st.header("My Projects")
with st.container():
    col1, col2 = st.columns([1, 2])
    with col1:
        st.header("🏦")
    with col2:
        st.subheader("Smart Bank System")
        st.write("A secure banking system built with Python (Login, Loans, Transactions).")
        st.link_button("View Code", "https://github.com/muhammedmidlaj123/bank-system-python")

st.write("---")

# --- EDUCATION ---
st.header("Education & Journey")
st.write("**Bachelor of Computer Applications (BCA)** - IGNOU (UAE) | *Current*")
st.write("**Goal:** Internship in AI/Gen AI by March 2026.")

st.write("---")

# --- 🤖 SMART AI CHAT BOT ---
st.header("🤖 Chat with My AI Bot")

api_key = st.text_input("Enter your Google API Key:", type="password")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Ask me about Midhilaj..."):
    st.chat_message("user").markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    if not api_key:
        st.error("Please enter an API Key!")
    else:
        # --- SMART MODEL FINDER ---
        # We try 3 different models. If one fails, we try the next.
        models_to_try = [
            "gemini-1.5-flash",
            "gemini-pro",
            "gemini-1.5-pro-latest"
        ]
        
        success = False
        
        with st.chat_message("assistant"):
            status_box = st.empty()
            status_box.markdown("Thinking...")
            
            for model_name in models_to_try:
                try:
                    url = f"https://generativelanguage.googleapis.com/v1beta/models/{model_name}:generateContent?key={api_key}"
                    headers = {"Content-Type": "application/json"}
                    data = {
                        "contents": [{"parts": [{"text": "You are a helpful assistant for Midhilaj EK. User says: " + prompt}]}]
                    }
                    
                    response = requests.post(url, headers=headers, json=data)
                    
                    if response.status_code == 200:
                        # SUCCESS!
                        result = response.json()
                        ai_text = result['candidates'][0]['content']['parts'][0]['text']
                        status_box.markdown(ai_text)
                        st.session_state.messages.append({"role": "assistant", "content": ai_text})
                        success = True
                        break # Stop trying models, we found one!
                    
                except Exception:
                    continue # Try next model
            
            if not success:
                status_box.error(f"Error: Could not connect to Google AI. Please check your API Key.")
