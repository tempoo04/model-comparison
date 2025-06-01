import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.chat_models import ChatAnthropic
from langchain_community.chat_models import ChatCohere

load_dotenv()

my_key_openai = os.getenv("openai_apikey")

def ask_gpt(prompt, temperature, max_tokens):
    llm = ChatOpenAI(api_key=my_key_openai,
                     temperature=temperature,
                     max_tokens=max_tokens,
                     model="gpt-4.1")
    AI_Response = llm.invoke(prompt)

    return AI_Response.text

#################################################

my_key_google = os.getenv("google_apikey")

def ask_gemini(prompt, temperature, max_tokens):
    llm = ChatGoogleGenerativeAI(api_key=my_key_google,
                     temperature=temperature,
                     model="gemini-pro")
    AI_Response = llm.invoke(prompt)

    return AI_Response.text

################################################
my_key_anthropic = os.getenv("anthropic_apikey")

def ask_claude(prompt, temperature, max_tokens):
    llm = ChatAnthropic(api_key=my_key_anthropic,
                     temperature=temperature,
                     max_tokens=max_tokens,
                     model="claude-2.1")
    AI_Response = llm.invoke(prompt)

    return AI_Response.text

################################################

my_key_cohere = os.getenv("cohere_apikey")

def ask_command(prompt, temperature, max_tokens):
    llm = ChatCohere(api_key=my_key_cohere,
                     temperature=temperature,
                     max_tokens=max_tokens,
                     model="command")
    AI_Response = llm.invoke(prompt)

    return AI_Response.text