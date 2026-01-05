import streamlit as st
import google.generativeai as genai

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
            st.write("---")
            st.header("🤖 Chat with My AI Bot")

            # 1. Ask for API Key (Securely)
            api_key = st.text_input("Enter your Google API Key to Chat:", type="password")

            if api_key:
                # 2. Configure the AI
                genai.configure(api_key=api_key)
                model = genai.GenerativeModel('gemini-1.5-flash')

                # 3. Initialize Chat History (This keeps messages on screen)
                if "messages" not in st.session_state:
                    st.session_state.messages = []

                # 4. Display Old Messages
                for message in st.session_state.messages:
                    with st.chat_message(message["role"]):
                        st.markdown(message["content"])

                # 5. The Chat Input Box
                if prompt := st.chat_input("Ask me anything about Midhilaj..."):
                    # Show User Message
                    st.chat_message("user").markdown(prompt)
                    # Save to history
                    st.session_state.messages.append({"role": "user", "content": prompt})

                    # Generate AI Response
                    try:
                        # We give the AI a "Persona" so it knows who it is
                        context = """
                        You are an AI assistant for Midhilaj EK's Portfolio.
                        Answer questions as if you are his digital representative.

                        Midhilaj's Info:
                        - Skills: Python, AI, Streamlit, Banking Systems.
                        - Education: BCA Student at IGNOU, Commerce Background.
                        - Current Goal: Internship in AI/Robotics.
                        - Projects: Smart Bank System (Python), Portfolio Website (Streamlit).
                        - Contact: midhilaj@example.com

                        Keep answers short and professional.
                        """

                        full_prompt = context + f"\nUser: {prompt}\nAI:"
                        response = model.generate_content(full_prompt)

                        # Show AI Message
                        with st.chat_message("assistant"):
                            st.markdown(response.text)

                        # Save AI message to history
                        st.session_state.messages.append({"role": "assistant", "content": response.text})

                    except Exception as e:
                        st.error(f"Error: {e}")