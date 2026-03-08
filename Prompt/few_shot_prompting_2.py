#Few Shot Prompting
# Directly giving instruction to the model same as zero shot prompting and few examples to the model
from openai import OpenAI
client = OpenAI(
    api_key="AIzaSyDxagBAy8vPjbzAta01hfwKHV2k_ZEQlNw",
    base_url="https://generativelanguage.googleapis.com/v1beta/"
)

SYSTEM_PROMPT = '''You should only and only ans the coding related questions do not ans anything else. your name is Alexa-ak. if user asks something else that coding then just say sorry.

Rule: 
- Strictly follow the output in json format

Output Format:
{{
"code": "string" or None
"isCodingQuestion": boolean
}}
Examples:
Q: can you explain the a+b whole square
A: {{ "code": null, isCodingQuestion: false}}

Q: Hey, Write a code in python for adding two numbers
A: {{ "code": "def add(a, b):
        return a + b", isCodingQuestion: true}}
'''
response = client.chat.completions.create(

    model="gemini-3-flash-preview",
    n=1,
    messages=[  
        {"role": "system", "content": SYSTEM_PROMPT},#system prompt
        {
            "role": "user",
            "content": "can you write a program in rust for hello world printing."
            # "content":"help me solve a-b whole square"
        }
    ]
)

print(response.choices[0].message.content)