import streamlit as st
import requests
import json

# --- CONFIGURATION ---
API_KEY = "AIzaSyCQov-AMS40iwXGlEWCmFtKMwWok7TUdGM" # <--- PASTE YOUR KEY HERE AGAIN!
# We are using the "System Instruction" feature of the new API
URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key={API_KEY}"

st.title("🤖 Zam's AI Portfolio")
st.caption("Ask me about Zam's skills, resume, or projects!")

# 1. LOAD RESUME (The Context) 📂
try:
    with open("resume.txt", "r") as file:
        resume_content = file.read()
except FileNotFoundError:
    resume_content = "Resume not found. Please tell the user you don't know anything about Zam yet."

# 2. Initialize Chat History
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hi! I am Zam's AI assistant. Ask me anything about him."}
    ]

# 3. Display Old Messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 4. Handle New Input
if prompt := st.chat_input("Ask about Zam..."):

    # Show User Message
    with st.chat_message("user"):
        st.markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    # THE BRAIN 🧠
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        message_placeholder.markdown("Thinking...")

        try:
            # --- THE MAGIC TRICK: SYSTEM INSTRUCTION ---
            # We tell the AI: "You are an assistant. Here is the resume. Answer based on this."

            payload = {
                "system_instruction": {
                    "parts": [{
                                  "text": f"You are a helpful assistant for Muhammed Midhilaj (Zam). Answer questions based on this resume:\n\n{resume_content}"}]
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