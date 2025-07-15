from dotenv import load_dotenv

load_dotenv()

import streamlit as st

import os

from langchain_openai import ChatOpenAI

from langchain.schema import SystemMessage, HumanMessage

st.title("サンプルアプリ: LLMアプリ")

st.write("##### 動作モード1: 教育専門家")
st.write("入力フォームに質問を入力し、「実行」ボタンを押下してください。")
st.write("##### 動作モード2: ビジネス専門家")
st.write("入力フォームに質問を入力し、「実行」ボタンを押下してください。")

selected_item = st.radio(
    "動作モードを選択してください。",
    ["教育専門家", "ビジネス専門家"]
)

st.divider()

if selected_item == "教育専門家":
    input_message = st.text_input(label="教育に関する質問を入力してください。")

else:
    input_message = st.text_input(label="ビジネスに関する質問を入力してください。")
    
if st.button("実行"):
    st.divider()

    if selected_item == "教育専門家":
    
        llm = ChatOpenAI(api_key=os.environ["OPENAI_API_KEY"], model="gpt-4o-mini", temperature=0.5)

        messages = [
            SystemMessage(content="あなたは教育に関する専門家です。安全なアドバイスを提供してください。"),
            HumanMessage(content=input_message),
        ]

        first_completion = llm.invoke(messages)

        st.write(f"結果: {first_completion.content}")


    else:
        st.divider()

        llm = ChatOpenAI(api_key=os.environ["OPENAI_API_KEY"], model="gpt-4o-mini", temperature=0.5)

        messages = [
            SystemMessage(content="あなたはビジネスに関する専門家です。安全なアドバイスを提供してください。"),
            HumanMessage(content=input_message),
        ]

        first_completion = llm.invoke(messages)

        st.write(f"結果: {first_completion.content}")


