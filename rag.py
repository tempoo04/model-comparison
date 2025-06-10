import streamlit as st
import raghelper

st.set_page_config(page_title="RAG with LangChain", layout="wide")
st.title("RAG with LangChain: URL")
st.divider()

col_input, col_rag, col_normal = st.columns([1,2,2])

with col_input:
    target_url = st.text_input(label="Enter URL address:")
    st.divider()
    prompt = st.text_input(label="Enter your question:", key="url_prompt")
    st.divider()
    submit_btn = st.button(label="Submit", key="url_button")

    if submit_btn:
        with col_rag:
            with st.spinner("The answer is being loaded..."):
                st.success("ANSWER - RAG activated")
                st.markdown(raghelper.rag_with_url(target_url, prompt))
                st.divider()

        with col_normal:
            with st.spinner("The answer is being loaded..."):
                st.info("ANSWER - RAG deactivated")
                st.markdown(raghelper.ask_gemini(prompt))
                st.divider()


st.title("RAG with LangChain: PDF")
st.divider()

col_input, col_rag, col_normal = st.columns([1,2,2])

with col_input:
    selected_file = st.file_uploader(label="Choose File", type=["pdf"])
    st.divider()
    prompt = st.text_input(label="Enter your question:", key="pdf_prompt")
    st.divider()
    submit_btn = st.button(label="Submit", key="pdf_button")

    if submit_btn:

        with col_rag:
            with st.spinner("The answer is being loaded..."):
                st.success("ANSWER - RAG activated")
                AI_Response, relevant_documents = raghelper.rag_with_pdf(filepath=f"./data/{selected_file.name}", prompt=prompt)
                st.markdown(AI_Response)
                st.divider()
                for doc in relevant_documents:
                    st.caption(doc.page_content)
                    st.markdown(f"Source: {doc.metadata}")
                    st.divider()

        with col_normal:
            with st.spinner("The answer is being loaded..."):
                st.info("ANSWER - RAG deactivated")
                st.markdown(raghelper.ask_gemini(prompt))
                st.divider()





