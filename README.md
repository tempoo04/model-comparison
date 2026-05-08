# Model Comparison

This repository contains a set of small LangChain experiments built around model comparison and retrieval-augmented generation.

The main pieces are:

- a Streamlit app that compares responses from GPT, Gemini, Claude, and Cohere
- a Streamlit RAG app for URL and PDF inputs
- a small OpenAI function-calling demo
- helper modules for model access, loading data, and RAG retrieval

## Project Layout

```text
.
├── chain.py
├── data/
│   ├── ai_course.xlsx
│   ├── digital.pdf
│   ├── gelecek.pdf
│   └── timeline.pdf
├── loaders.py
├── model.py
├── modelhelper.py
├── rag.py
├── raghelper.py
├── requirements.txt
├── URL_Content.txt
└── README.md
```

## Features

- Compare answers across multiple LLMs in a single UI
- Adjust temperature and token limits from the Streamlit sidebar
- Run RAG against a web page or PDF
- Test OpenAI function calling with Pydantic schema targets
- Load and process local documents from `data/`

## Requirements

- Python 3.10 or newer
- API keys for the providers you want to use

## Environment Variables

Create a `.env` file in the repository root with the keys used by the scripts:

```env
openai_apikey=your_openai_api_key
google_apikey=your_google_api_key
anthropic_apikey=your_anthropic_api_key
cohere_apikey=your_cohere_api_key
hugging_access_token=your_huggingface_token
```

Not every script needs every key, but the comparison app and RAG helpers expect the relevant provider keys to be available.

## Install

Create a virtual environment and install dependencies:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

## Run

Run the model comparison app:

```powershell
streamlit run model.py
```

Run the RAG app:

```powershell
streamlit run rag.py
```

Run the OpenAI function-calling demo:

```powershell
python chain.py
```

## What Each Script Does

- `model.py` presents a Streamlit interface that sends the same prompt to GPT, Gemini, Claude, and Cohere and shows timing for each response.
- `modelhelper.py` contains the provider-specific helper functions used by `model.py`.
- `rag.py` provides two RAG workflows, one for a URL and one for PDF upload.
- `raghelper.py` handles web loading, PDF loading, text splitting, embeddings, and retrieval.
- `chain.py` demonstrates `create_openai_fn_runnable` using `Human` and `Town` schemas.
- `loaders.py` contains document-loading experiments and an Excel-to-HTML extraction example.

## Notes

- `loaders.py` currently writes `excel.html` from `data/ai_course.xlsx` when run.
- `rag.py` expects uploaded PDFs to be available in `./data/` when the file path is built from the uploaded filename.
- Some modules are exploratory and may need cleanup before production use.
