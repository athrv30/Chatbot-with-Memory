import streamlit as st
from langchain_community.chat_models import ChatOpenAI
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
from langchain.schema import AIMessage, HumanMessage
import os

# ✅ Set OpenAI key from Streamlit Secrets
os.environ["OPENAI_API_KEY"] = st.secrets["OPENAI_API_KEY"]

# 🎯 Streamlit page setup
st.set_page_config(page_title="Chatbot with Memory", layout="centered")
st.title("🧠 Chatbot with Memory")

# ✅ Initialize session state for chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# ✅ Function to create the LangChain conversation chain
def get_chain():
    memory = ConversationBufferMemory(return_messages=True)
    return ConversationChain(
        llm=ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.7),
        memory=memory,
        verbose=False
    )

# ✅ Initialize the chain if not already in session
if "chain" not in st.session_state:
    st.session_state.chain = get_chain()

# 📥 Input box
user_input = st.text_input("Ask something...", key="user_input")

# 💬 Handle input and response
if user_input:
    response = st.session_state.chain.run(user_input)
    st.session_state.chat_history.append((user_input, response))

# 🧾 Display chat history
for i, (user_msg, ai_msg) in enumerate(st.session_state.chat_history):
    st.markdown(f"**You:** {user_msg}")
    st.markdown(f"**Bot:** {ai_msg}")
