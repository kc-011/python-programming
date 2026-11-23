from langchain_openai import ChatOpenAI
from langchain.agents import create_agent
from langgraph.checkpoint.memory import InMemorySaver
from dotenv import load_dotenv
import os

load_dotenv()
GROQ = os.getenv('GROQ_API_KEY')
llm = ChatOpenAI(model= 'openai/gpt-oss-120b', api_key=GROQ, base_url=os.getenv('GROQ_BASE_URL'))

checkpointer = InMemorySaver()
agent = create_agent(model=llm, tools=[], system_prompt=(
    """
        You are a helpful AI assistant.
        Remember previous messages in the conversation.
        Answer questions using conversation context.

"""), checkpointer=checkpointer)

session_id = 'user_1'
config = {
    'configurable':{
        'thread_id':session_id
    }
}

print("LANGCHAIN CONVERSATIONAL CHATBOT")
print("Type 'exit' to stop")
while True:
    user_input = input("\nYou: ")
    if user_input.lower() == "exit":
        print("Chatbot session ended.")
        break
    try:
        response = agent.invoke({'messages':[{
            'role':'user',
            'content':user_input}]},
            config=config
            )
        ai_response = response['messages'][-1].content
        print('\nAI: ', ai_response)
    except Exception as e:
        print('\nError: ', e)