# LCEL - LangChain Expression Language

import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()
GROQ_API_KEY = os.getenv('GROQ_API_KEY')
llm = ChatOpenAI(model='openai/gpt-oss-120b', api_key=GROQ_API_KEY, base_url='https://api.groq.com/openai/v1')

prompt=ChatPromptTemplate.from_messages([
    ("system", "You are an experienced {role}."),
    ("human", "Explain {topic} in a few lines with an example.")
])
parser = StrOutputParser()
chain = prompt | llm | parser
response = chain.invoke({'role':'Python Teacher', 'topic':'decorators'})
print(response)

# Syntax for Gemini
# from langchain_google_genai import ChatGoogleGenerativeAI
# llm = ChatGoogleGenerativeAI(model="gemini-4-hydrogen",temperature=0.7)
# response = llm.invoke("Explain LangChain with a simple example")
# print(response.content[0]['text'])