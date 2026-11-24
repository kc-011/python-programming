import gradio as gr
import uuid
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.agents import create_agent
from langgraph.checkpoint.memory import InMemorySaver
import os

load_dotenv()
GROQ = os.getenv('GROQ_API_KEY')
llm = ChatOpenAI(model= 'openai/gpt-oss-120b', api_key=GROQ, base_url=os.getenv('GROQ_BASE_URL'))

checkpointer = InMemorySaver()
agent = create_agent(model=llm, tools=[], system_prompt="""
    You are a helpful AI teaching assistant.

    Answer questions clearly and explain concepts
    with examples wherever necessary.

    Remember previous messages in the conversation.
    """, checkpointer=checkpointer)

def chatbot_response(user_input, chat_history, session_id):
    if not user_input.strip():
        return "", chat_history
    try:
        config = {
            'configurable':{
                'thread_id':session_id
            }
        }
        response = agent.invoke({'messages':[{
            'role':'user', 'content':user_input}]},
            config=config)
        answer = response['messages'][-1].content
        chat_history.append({'role':'user', 'content':user_input})
        chat_history.append({'role':'assistant', 'content':answer})
        return "", chat_history
    except Exception as e:
        print('Error:', e)
        chat_history = chat_history or []
        chat_history.append({'role':'assistant', 'content':f"Error:{e}"})
        return "", chat_history

def new_chat():
    new_session_id = str(uuid.uuid4())
    print('New Session Created:', new_session_id)
    return [], new_session_id

with gr.Blocks(title='LangChain Conversational Chatbot') as demo:
    gr.Markdown("# LangChain Conversational Chatbot")
    gr.Markdown("Chat with an AI assistant that remembers "
                "your previous messages.")

    session_id = gr.State(value=lambda: str(uuid.uuid4()))
    chatbot = gr.Chatbot(height=450, label='AI Assistant')
    user_input = gr.Textbox(placeholder='Ask me anything...', label='Your Message')
    with gr.Row():
        send_btn = gr.Button('Send', variant='primary')
        new_chat_btn = gr.Button('New Chat')

    send_btn.click(fn=chatbot_response, inputs=[user_input, chatbot, session_id],
                   outputs=[user_input, chatbot])
    user_input.submit(fn=chatbot_response, inputs=[user_input, chatbot, session_id],
                   outputs=[user_input, chatbot])
    new_chat_btn.click(fn=new_chat, inputs=[], outputs=[chatbot, session_id])

if __name__ == '__main__':
    demo.launch()