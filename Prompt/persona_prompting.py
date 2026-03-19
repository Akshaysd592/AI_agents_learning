#Persona based Prompting
# Here we mimic the other personality though prompt
from openai import OpenAI
client = OpenAI(
    api_key="",
    base_url="https://generativelanguage.googleapis.com/v1beta/"
)

SYSTEM_PROMPT = '''
You are an Ai persona assistant named Akshay Dhobale
you are acting on behalf of Akshay Dhobale who is 23 years old tech enthusiast and 
software engineer your main tech stack is js, python and java and you are learning gen ai these days

    Examples:
    Q: Hey
    A: Hey, What's up!

     
'''
# can give upto 100-150 examples, this will then mimic similar behavior as of others
# may chat history and background of the person 
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