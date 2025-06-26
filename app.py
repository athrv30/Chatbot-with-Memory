
import streamlit as st
from langchain_community.chat_models import ChatOpenAI
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
from langchain.schema import AIMessage, HumanMessage
from dotenv import load_dotenv
import os

# Load .env variables
load_dotenv()

# Set page title
st.set_page_config(page_title="Chatbot with Memory", layout="centered")
st.title("🧠 Chatbot with Memory")

# Initialize session state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Initialize OpenAI Chat Model with memory
def get_chain():
    memory = ConversationBufferMemory(return_messages=True)
    return ConversationChain(
        llm=ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.7),
        memory=memory,
        verbose=False
    )

# Load or create chain
if "chain" not in st.session_state:
    st.session_state.chain = get_chain()

# User input
user_input = st.text_input("Ask something...", key="user_input")

# Handle input
if user_input:
    response = st.session_state.chain.run(user_input)
    st.session_state.chat_history.append((user_input, response))

# Display conversation
for i, (user_msg, ai_msg) in enumerate(st.session_state.chat_history):
    st.markdown(f"**You:** {user_msg}")
    st.markdown(f"**Bot:** {ai_msg}")
