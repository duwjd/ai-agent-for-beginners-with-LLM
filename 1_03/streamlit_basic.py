import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from openai import OpenAI
from config.const import OPENAI_API_KEY
from config.log_config import logger
import streamlit as st


client = OpenAI(api_key= OPENAI_API_KEY)

with st.sidebar:
    openai_api_key = os.getenv("OPENAI_API_KEY")

    if not openai_api_key:
        openai_api_key = st.text_input("OPENAI_API_KEY", type="password")
        os.environ["OPENAI_API_KEY"] = openai_api_key

st.title("Streamlit Basic : 챗봇 만들기")

if("messages" not in st.session_state):
    st.session_state["messages"] = [{"role" : "assistant", "content" : "How can I help you?"}]


for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input():
    if not openai_api_key:
        st.warning("OPENAI_API_KEY 환경변수를 설정해주세요")
        st.stop()
    
    client = OpenAI(api_key= openai_api_key)
    st.session_state.messages.append({"role" : "user", "content" : prompt})
    st.chat_message("user").write(prompt)
    response = client.chat.completions.create(
        model="gpt-4o",
        temperature=0.9,
        messages = st.session_state.messages
    )
    msg = response.choices[0].message.content
    st.session_state.messages.append({"role" : "assistant", "content" : msg})
    st.chat_message("assistant").write(msg)