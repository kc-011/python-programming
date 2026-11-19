from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

load_dotenv()
GROQ_API_KEY = os.getenv('GROQ_API_KEY')
llm = ChatOpenAI(model='openai/gpt-oss-120b', api_key=GROQ_API_KEY, base_url='https://api.groq.com/openai/v1')

# Simple Prompting
# prompt = 'Explain ML to a Fresher in 5 lines'
# response = llm.invoke(prompt)
# print(response.content)

# With PromptTemplate (also for Simple Text Generation - just dynamic)
from langchain_core.prompts import PromptTemplate
# prompt_t = PromptTemplate.from_template("""Explain {topic} in simple words
#             with one example""")
# prompt = prompt_t.format(topic='NLP')
# response = llm.invoke(prompt)
# print(response.content)

# With ChatPromptTemplate
from langchain_core.prompts import ChatPromptTemplate
# prompt=ChatPromptTemplate.from_messages([
#     ("system","You are a {profession}"),
#     ("human","explain {topic} is simple words")
# ])
# messages = prompt.format_messages(profession='Python Teacher',
#             topic = 'Decorators')
# response = llm.invoke(messages)
# print(response.content)

# Using JSON parser
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.output_parsers import StrOutputParser
strparser = StrOutputParser()
parser = JsonOutputParser()
prompt = PromptTemplate.from_template("""
Evaluate the following student.

Student: {name}
Marks: {marks}

Return the result in JSON format with:
name, marks, grade, result.

{format_instructions}
""")
formatted_prompt = prompt.format(name='Mossa', marks=60, format_instructions="Return only valid JSON.")
response = llm.invoke(formatted_prompt)
result = parser.parse(response.content)
result2 = strparser.parse(response.content)
print(result)
print(result2)
print(type(result))
print(type(result2))
# uH ok...