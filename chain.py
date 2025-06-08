# OpenAI Function Runnable CHain
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.pydantic_v1 import BaseModel, Field
from typing import Optional
from langchain.chains.openai_functions import create_openai_fn_runnable
from dotenv import load_dotenv
import os

load_dotenv()
my_key_openai = os.getenv("openai_apikey")

class Human(BaseModel):
    """Identifying information of people"""

    name: str = Field(..., description="Name of person")
    age: int = Field(..., description="Age")
    job: Optional[str] = Field(..., description="Job")


class Town(BaseModel):
    """Identifying information of town"""

    name: str = Field(..., description="Name of town")
    plate_no: int = Field(..., description="Plate number")
    climate: Optional[str] = Field(..., description="Climate of city")

llm = ChatOpenAI(model="gpt-4-0125-preview", api_key=my_key_openai)

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are the most successful algorithm of the world by saving the entities"),
        ("human", f"Do the callbacks for the required functions to save the entities I inputted: {input}"),
        ("human", "Hint: Make sure you answer them in a right format")
    ]
)

chain_2 = create_openai_fn_runnable([Human, Town], llm, prompt)

print(chain_2.invoke({"input": "Leon was 34 years old and a successful computer engineer"}))
print(chain_2.invoke({"input": "The weather in Leon is always hot and in vehicles with 09 plate number the air conditioner is always on for this reason"}))



# Stuff Document Chain
# from langchain_openai import ChatOpenAI
# from langchain_core.documents import Document
# from langchain_core.prompts import ChatPromptTemplate
# from langchain.chains.combine_documents import create_stuff_documents_chain
# import os
# from dotenv import load_dotenv
#
# load_dotenv()
#
# my_key_openai = os.getenv("openai_apikey")
#
# llm = ChatOpenAI(
#     model = "gpt-4-0125-preview",
#     api_key = my_key_openai,
# )
#
# prompt = ChatPromptTemplate.from_messages(
#     [("system", "Write the favorite colors of the people here:\n\n{context}")]
# )
#
# docs = [
#     Document(page_content="Guelfo likes red but not green"),
#     Document(page_content="Ghibellino  likes green but not blue"),
#     Document(page_content="Muro says, he does not have favorite but he likes orange apparently"),
# ]
#
# chain_1 = create_stuff_documents_chain(llm, prompt)
# print(chain_1.invoke({"context": docs}))
