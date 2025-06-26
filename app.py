import streamlit as st
from langchain_community.chat_models import ChatOpenAI
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
import os

# ✅ Load API key from Streamlit secrets
os.environ["OPENAI_API_KEY"] = st.secrets["OPENAI_API_KEY"]
st.write("Key loaded:", "Yes" if os.getenv("OPENAI_API_KEY") else "No")  # Debugging

# App layout
st.set_page_config(page_title="Chatbot with Memory", layout="centered")
st.title("🧠 Chatbot with Memory")

# Initialize chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# LangChain Conversation
def get_chain():
    memory = ConversationBufferMemory(return_messages=True)
    st.write("Using model: gpt-3.5-turbo")  # Debugging
    return ConversationChain(
        llm=ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.7),
        memory=memory,
        verbose=False
    )

# Setup the chain
if "chain" not in st.session_state:
    st.session_state.chain = get_chain()

# Input box
user_input = st.text_input("Ask something...")

if user_input:
    response = st.session_state.chain.run(user_input)
    st.session_state.chat_history.append((user_input, response))

# Show chat history
for user_msg, ai_msg in st.session_state.chat_history:
    st.markdown(f"**You:** {user_msg}")
    st.markdown(f"**Bot:** {ai_msg}")
