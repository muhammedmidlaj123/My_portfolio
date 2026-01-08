import streamlit as st
import google.generativeai as genai

# 1. Page Configuration
st.set_page_config(page_title="Zam's AI Portfolio", page_icon="🚀")

# 2. Side Bar: Personal Info
with st.sidebar:
    st.header("About Me")
    st.image("https://cdn-icons-png.flaticon.com/512/4712/4712109.png", width=100) # Placeholder image
    st.write("**Name:** Muhammed Midhilaj EK (Zam)")
    st.write("**Role:** Python & AI Enthusiast")
    st.write("**Location:** Dubai, UAE")
    st.write("I am building AI tools and learning Python!")
    
    st.divider()
    
    # Check for API Key
    if "GOOGLE_API_KEY" in st.secrets:
        st.success("API Key Loaded! 🟢")
        genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
    else:
        st.error("Missing API Key in Streamlit Secrets!")
        st.stop()

# 3. Main Content: Introduction
st.title("🤖 Zam's AI Portfolio")
st.write("Welcome to my interactive portfolio! You can chat with my AI assistant below.")

st.divider()

# 4. The Chatbot Logic (Updated Model)
st.subheader("💬 Chat with my AI")

# Initialize Chat History if it doesn't exist
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# React to User Input
if prompt := st.chat_input("Ask me anything..."):
    # Display user message
    with st.chat_message("user"):
        st.markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Generate AI Response
    try:
        # --- THE FIX IS HERE: Using gemini-1.5-flash ---
        model = genai.GenerativeModel('gemini-1.5-flash') 
        response = model.generate_content(prompt)
        
        # Display AI message
        with st.chat_message("assistant"):
            st.markdown(response.text)
        st.session_state.messages.append({"role": "assistant", "content": response.text})
        
    except Exception as e:
        st.error(f"An error occurred: {e}")
