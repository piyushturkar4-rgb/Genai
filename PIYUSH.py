import os
import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_ollama import OllamaLLM


prompt=ChatPromptTemplate.from_messages(
    [
("system", "You are a helpful assistant. Please respond to the question asked"),
("user", "Question:{question}")
    ]
)
st.title("My GPT")
input_text=st.text_input("Ask Me Question?")
llm = OllamaLLM(model="gemma2:2b")
output_parser=StrOutputParser()
chain=prompt|llm|output_parser
st.write(chain.invoke({"question":input_text}))