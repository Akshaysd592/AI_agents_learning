from openai import OpenAI
client = OpenAI(
    api_key="AIzaSyDxagBAy8vPjbzAta01hfwKHV2k_ZEQlNw",
    base_url="https://generativelanguage.googleapis.com/v1beta/"
)


response = client.chat.completions.create(
    model="gemini-3-flash-preview",
    n=1,
    messages=[  
        {"role": "system", "content": "you are a expert in mathematics and only and onl answer maths related questions. if the query is not related to maths. just say sorry and don not answer that"},#system prompt
        {
            "role": "user",
            # "content": "hey, can you code a python program that can print hello"
            "content": "help me solve (a+b)^2"
        }
    ]
)

print(response.choices[0].message.content)