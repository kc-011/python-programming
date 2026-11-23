# Conversation history using Python list
# Before introducing LangChain's history components, let's understand the concept using a normal Python list

from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
from dotenv import load_dotenv
import os
from termcolor import colored, cprint

load_dotenv()
GROQ = os.getenv('GROQ_API_KEY')
llm = ChatOpenAI(model= 'openai/gpt-oss-120b', api_key=GROQ, base_url=os.getenv('GROQ_BASE_URL'))
chat_history = [SystemMessage(content='You are a helpful Python Teacher')]
window = 1
while True:
    user_input = input(colored(text='You: ', color='green'))
    if user_input.lower() == 'exit':
        break
    # Adding user's message to history
    chat_history.append(HumanMessage(content=user_input))
    # Adding AI's reply to history
    response = llm.invoke(chat_history)
    chat_history.append(AIMessage(content=response.content))
    print(colored('AI: ', 'yellow'), response.content)
    if len(chat_history) > (1 + window *2):
        chat_history = [chat_history[0]] + chat_history[-(window*2):]
