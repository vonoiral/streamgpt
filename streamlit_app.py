
import streamlit as st
import openai

openai.api_key = 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

st.title("ChatGPT Interactive Website")

question = st.text_input("Ask me anything:")

if question:
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=question,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    ).choices[0].text

    st.write("ChatGPT says:", response)
