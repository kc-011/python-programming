from openai import OpenAI
from dotenv import load_dotenv
import os

# from transformers import pipeline

# chatbot = pipeline('text-generation', model='gpt2')
# messages = [{'role':'system', 'content':'You are a helpful AI assistant'}]
# while True:
#     user_input = input('You: ')
#     if user_input.lower() == 'exit':
#         print('k bye')
#         break
#     messages.append({'role':'user', 'content':user_input})
#     result = chatbot(messages, max_length = 100, num_return_sequence=1)[0]['generated-text'][-1]['content']
#     print('Chatbot:', result)
#     print()

import json

load_dotenv()
api_key=os.getenv('OPENROUTER_API_KEY')
client=OpenAI(api_key=api_key, base_url=os.getenv("OPENROUTER_BASE_URL"))
print('Chatbot')
print("Type 'exit' to end conversation")
try:
    with open('Gen AI/memory.json', 'r') as fp:
        messages = json.load(fp)
except FileNotFoundError:
    messages = [{'role':'system', 'content':'You are a helpful AI assistant'}]

while True:
    user_input = input('You: ')
    print()
    if user_input.lower() == 'exit':
        print('--End--')
        break
    messages.append({'role':'user', 'content': user_input})
    response = client.chat.completions.create(model="baidu/ernie-5.5-flash-preview:free",
    messages=messages , temperature=0.7, max_tokens=200)
    answer = response.choices[0].message.content  
    messages.append({'role':'assistant', 'content':answer})
    with open('Gen AI/memory.json', 'w') as fp:
        json.dump(messages, fp, indent=4)
    print('Chatbot:', answer)
    print()

