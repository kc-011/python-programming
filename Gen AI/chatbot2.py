from openai import OpenAI
from dotenv import load_dotenv
import os
import json

load_dotenv()
openrouter = OpenAI(api_key=os.getenv('OPENROUTER_API_KEY'), base_url=os.getenv('OPENROUTER_BASE_URL'))
gemini = OpenAI(api_key=os.getenv('GEMINI_API_KEY'), base_url=os.getenv('GEMINI_BASE_URL'))
groq = OpenAI(api_key=os.getenv('GROQ_API_KEY'), base_url=os.getenv('GROQ_BASE_URL'))
deepseek = OpenAI(api_key=os.getenv('DEEPSEEK_API_KEY'), base_url=os.getenv('DEEPSEEK_BASE_URL'))
print('Fetched ✅')

question = "If you could erase all memories of someone you loved to completely cure your grief, should you do it? Answer briefly and keep it short."
messages = [{'role':'user', 'content':question}]

competitors = []
ans = []

def record(model_name, answer):
    competitors.append(model_name)
    ans.append(answer)

#OpenRouter
response = openrouter.chat.completions.create(model = 'dots-studio/dots-3-note-preview:free', messages=messages)
open_ans = response.choices[0].message.content
record('OpenRouter', open_ans)
print('OpenRouter ✅')

# Gemini
# response = gemini.chat.completions.create(model = 'gemini-3.8-flash', messages=messages)
# gem_ans = response.choices[0].message.content
# record('Gemini', gem_ans)
# print('Gemini ✅') 
# JUST SLOW

# ERNIE via OpenRouter
response = openrouter.chat.completions.create(model='baidu/ernie-5.5-flash-preview:free', messages=messages)
ernie_ans = response.choices[0].message.content
record('ERNIE', ernie_ans)
print("ERNIE ✅")

#Groq
response = groq.chat.completions.create(model = 'openai/gpt-oss-120b', messages=messages)
groq_ans = response.choices[0].message.content
record('Groq', groq_ans)
print('Groq ✅')

answers = ""
for index, a in enumerate(ans):
    answers += f'Competitor {index+1}:\n'
    answers += a+'\n\n'

print(answers)

judge = f"""You are judging a competition between {len(competitors)} competitors.
Each model has been given this question:

{question}

Your job is to evaluate each response for clarity and strength of argument, and rank them in order of best to worst.
Here's your marking scheme:
• 1 to 3 points: Generic fence-sitting ("It depends on the person") with cliché advice.
• 4 to 7 points: Clearly weighs happiness against personal identity and picks a reasoned side.
• 8 to 10 points: Makes a compelling, original argument (e.g., framing memory as constitutive of the self) without sounding preachy.

Give points to each answer based on the scheme given above.

Respond with JSON, and only JSON, with the following format (Descending Order of Competitor Number in accordance with their points):
{{"results": ["best competitor number", "second best competitor number", "third best competitor number", ...]}}

Here are the responses from each competitor:

{answers}

Now respond with the JSON with the ranked order of the competitors, nothing else. Do not include markdown formatting or code blocks."""

#Deepseek - Judge
# prompt = [{'role':'system', 'content':judge}]
# response = deepseek.chat.completions.create(model='deepseek-flash', messages=prompt)
# deep_ans = response.choices[0].message.content
# Sadly Paid

# Nvidia via OpenRouter
print('Nvidia is judging....\n ')
prompt = [{'role':'system', 'content':judge}]
response = openrouter.chat.completions.create(model='nvidia/nemotron-3-ultra-550b-a55b:free', messages=prompt)
nvidia_ans = response.choices[0].message.content

print('The Results are in!')

results = json.loads(nvidia_ans)
rank = results['results']
for i, r in enumerate(rank):
    print(f'Rank {i+1}: {competitors[int(r)-1]} (Competitor {int(r)})')
