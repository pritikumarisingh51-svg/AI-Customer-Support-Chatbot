import streamlit as st
import random

# Page settings
st.set_page_config(page_title="AI Chatbot", page_icon="🤖")

# Title
st.title("🤖 AI Customer Support Chatbot")

st.write("Welcome! Ask me anything about services, support, or products.")

# User input
user_input = st.text_input("You:")

# Responses
responses = {
    "hello": ["Hello! How can I help you today? 😊"],
    "hi": ["Hi there! 👋"],
    "how are you": ["I'm doing great! Thanks for asking."],
    "services": ["We provide AI, ML, and software solutions."],
    "price": ["Our pricing depends on the selected service."],
    "contact": ["You can contact us at support@example.com"],
    "bye": ["Goodbye! Have a wonderful day 👋"],
    "help": ["Sure! Tell me your issue."],
    "thanks": ["You're welcome 😊"],
}

# Chatbot logic
if user_input:

    user_input = user_input.lower()

    found = False

    for key in responses:
        if key in user_input:
            st.success(random.choice(responses[key]))
            found = True
            break

    if not found:
        st.warning("Sorry, I don't understand that yet.")