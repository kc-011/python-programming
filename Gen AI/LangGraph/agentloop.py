from langchain_openai import ChatOpenAI
from langchain.tools import tool
from langchain.agents import create_agent
from dotenv import load_dotenv
import os

# Tool 1: Calculator
@tool
def calc(a:float, b:float, op:str) -> float:
    """Perform addition, subtraction, multiplication or division."""
    print('Calculator Tool was used')

    if op == "add":
        return a + b
    elif op == "subtract":
        return a - b
    elif op == "multiply":
        return a * b
    elif op == "divide":
        return a / b if b != 0 else "Cannot divide by zero"
    else:
        return "Invalid operation"

# Tool 2: Employee Database
employees = [
    {"id": 1, "name": "Rahul", "salary": 50000},
    {"id": 2, "name": "Priya", "salary": 60000},
    {"id": 3, "name": "Amit", "salary": 45000}
]

@tool
def get_emp(name: str) -> str:
    """Find employee details using their name."""
    print('Employee Tool was used') 

    for emp in employees:
        if emp["name"].lower() == name.lower():
            return str(emp)

    return "Employee not found"

# Tool 3: Weather
@tool
def get_weather(city: str) -> str:
    """Get current weather information for a city."""
    print('Weather Tool was used')

    # Simulated weather response
    return f"The weather in {city} is sunny with 28°C."


load_dotenv()
GROQ = os.getenv('GROQ_API_KEY')
llm = ChatOpenAI(model= 'openai/gpt-oss-120b', api_key=GROQ, base_url=os.getenv('GROQ_BASE_URL'), temperature=0)
agent = create_agent(model=llm,
                     tools=[calc, get_emp, get_weather],
                     system_prompt="""
                    You are a helpful AI assistant.
                    Use the available tools whenever required.
                    If a tool is not required, answer normally.
                    Explain the results clearly.
                     """)

print('AI Agent Chatbot')
while True:
    query = input('\nYou: ')
    if query.lower() == 'exit':
        break
    response = agent.invoke({'messages':[{
        'role':'user', 'content':query}]})
    print('\nAI: ', response['messages'][-1].content)

