import streamlit as st
import modelhelper
import time

st.set_page_config(page_title="LangChain: Model Comparison", layout = "wide")
st.title("LangChain: Model Comparison")
st.divider()

col_prompt, col_settings = st.columns({2,3})

with col_prompt:
    prompt = st.text_input("Enter a question")
    st.divider()
    submit_btn = st.button("Ask")

with col_settings:
    temprature = st.slider(label="Temperature",min_value=0.0,max_value=1.0,value=0.7)
    max_tokens = st.slider(label="Maximum number of tokens",min_value=100,max_value=500, value=200, step=100)

st.divider()

col_gpt, col_gemini, col_claude, col_command = st.columns(4)

with col_gpt:
    if submit_btn:
        with st.spinner("GPT is answering..."):
            st.success("GPT")
            start_time = time.perf_counter()
            st.write(modelhelper.ask_gpt(prompt = prompt, temperature = temprature, max_tokens = max_tokens))
            end_time = time.perf_counter()
            elapsed_time = end_time - start_time
            st.caption(f" :hourglass: {round(elapsed_time)} seconds")


with col_gemini:
    if submit_btn:
        with st.spinner("Gemini is answering..."):
            st.info("Gemini Pro")
            start_time = time.perf_counter()
            st.write(modelhelper.ask_gemini(prompt = prompt, temperature = temprature))
            end_time = time.perf_counter()
            elapsed_time = end_time - start_time
            st.caption(f" :hourglass: {round(elapsed_time)} seconds")


with col_claude:
    if submit_btn:
        with st.spinner("Claude is answering..."):
            st.error("Claude 2.1")
            start_time = time.perf_counter()
            st.write(modelhelper.ask_claude(prompt = prompt, temperature = temprature, max_tokens = max_tokens))
            end_time = time.perf_counter()
            elapsed_time = end_time - start_time
            st.caption(f" :hourglass: {round(elapsed_time)} seconds")

with col_command:
    if submit_btn:
        with st.spinner("Command is answering..."):
            st.warning("Command")
            start_time = time.perf_counter()
            st.write(modelhelper.ask_command(prompt = prompt, temperature = temprature, max_tokens = max_tokens))
            end_time = time.perf_counter()
            elapsed_time = end_time - start_time
            st.caption(f" :hourglass: {round(elapsed_time)} seconds")



