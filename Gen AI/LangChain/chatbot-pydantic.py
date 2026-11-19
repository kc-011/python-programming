from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

load_dotenv()
GROQ_API_KEY = os.getenv('GROQ_API_KEY')
llm = ChatOpenAI(model='openai/gpt-oss-120b', api_key=GROQ_API_KEY, base_url='https://api.groq.com/openai/v1')

# What if you want to enforce a particular output structure?For example, you want:
# - name to be a string. - marks to be an integer. - grade to be a string. - result to be a string.
# We can use Pydantic with LangChain.Pydantic parsing validates the output structure and data types,
# but it does not guarantee that the LLM's evaluation or generated values are factually correct.

from pydantic import BaseModel, Field
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser

class StudentEval(BaseModel):
    name: str = Field(description='Student Name')
    marks: int = Field(description='Marks Obtained (out of 100)')
    grade: str = Field(description='Student Grade')
    result: str = Field(description='Pass or Fail')

parser = PydanticOutputParser(pydantic_object=StudentEval)
prompt = PromptTemplate(template="""
    Evaluate this student.

    Name: {name}
    Marks: {marks}

    {format_instructions}
    """,
    input_variables=["name", "marks"],
    partial_variables={
        "format_instructions": parser.get_format_instructions()
    }
)
formatted_prompt = prompt.format(name='Possa', marks=90)
response = llm.invoke(formatted_prompt)
result = parser.parse(response.content)
print(result)
print(result.name)
print(result.marks)
print(type(result))
