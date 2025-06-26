# 🧠 Chatbot with Memory (LangChain + OpenAI + Streamlit)

This is a simple conversational chatbot built with [LangChain](https://www.langchain.com/), [OpenAI](https://platform.openai.com/), and [Streamlit](https://streamlit.io/). It uses memory to maintain conversation context.

## 🚀 Features
- Built with `gpt-3.5-turbo` using LangChain's `ChatOpenAI`
- Maintains chat history using `ConversationBufferMemory`
- Clean Streamlit UI
- `.env` support for your OpenAI API key

## 📦 Requirements

Install dependencies:

```bash
pip install -r requirements.txt

## 🚀 Usage

1. Add your OpenAI API key in Streamlit Cloud secrets:
   ```toml
   OPENAI_API_KEY = "sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

