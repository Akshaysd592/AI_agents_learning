#Zero Shot prompting
# Giving direct instruction to the model
from openai import OpenAI
client = OpenAI(
    api_key="",
    base_url="https://generativelanguage.googleapis.com/v1beta/"
)

SYSTEM_PROMPT = "You should only and only ans the coding related questions do not ans anything else. your name is Alexa-ak. if user asks something else that coding then just say sorry "
response = client.chat.completions.create(
    model="gemini-3-flash-preview",
    n=1,
    messages=[  
        {"role": "system", "content": SYSTEM_PROMPT},#system prompt
        {
            "role": "user",
            "content": "can you write a program in C# for hello world printing."
        }
    ]
)

print(response.choices[0].message.content)