import streamlit as st
import requests

st.set_page_config(page_title="Debugger", page_icon="🔧")
st.title("🔧 AI DEBUGGER MODE")

api_key = st.text_input("Enter API Key:", type="password")

if st.button("Test Connection"):
    if not api_key:
        st.error("No Key!")
    else:
        st.info("Testing connection...")
        try:
            # 1. Try a simple "Requests" call
            url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key={api_key}"
            data = {"contents": [{"parts": [{"text": "Hello"}]}]}
            
            response = requests.post(url, json=data)
            
            # 2. SHOW THE EXACT RESULT
            st.write(f"Status Code: {response.status_code}")
            st.json(response.json())
            
        except Exception as e:
            st.error(f"CRASH: {e}")
