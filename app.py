import streamlit as st
from openai import OpenAI
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Page config
st.set_page_config(page_title="Agri Chatbot", page_icon="🌱")
st.title("🌱 Agriculture Chatbot")
st.caption("Conversation-aware | Cost optimized")

# Initialize memory
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "system",
            "content": "You are an expert agriculture advisor for Indian farming."
        }
    ]

# User input
query = st.text_input("Ask about crops, pests, fertilizers, weather")

if query:
    # Add user message to memory
    st.session_state.messages.append(
        {"role": "user", "content": query}
    )

    with st.spinner("Thinking..."):
        try:
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=st.session_state.messages,
                max_tokens=200
            )

            reply = response.choices[0].message.content

            # Add assistant reply to memory
            st.session_state.messages.append(
                {"role": "assistant", "content": reply}
            )

            st.success(reply)

        except Exception as e:
            st.error("Something went wrong. Please try again.")

# Optional: clear chat
if st.button("Clear Chat"):
    st.session_state.messages = [
        {
            "role": "system",
            "content": "You are an expert agriculture advisor for Indian farming."
        }
    ]
