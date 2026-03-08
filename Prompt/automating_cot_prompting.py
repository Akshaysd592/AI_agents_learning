from openai import OpenAI
from dotenv import load_dotenv
import json 
load_dotenv() # here it is not used but keeping it for future use if we want to load any environment variable from .env file

client = OpenAI(
    api_key="AIzaSyDxagBAy8vPjbzAta01hfwKHV2k_ZEQlNw",
    base_url="https://generativelanguage.googleapis.com/v1beta/"
)

SYSTEM_PROMPT = ''' you are a expert AI assistant in resolving user queries using chain of thought . you work on START, PLAN and OUTPUT format. you need first PLAN what need to be done.The PLAN can be multiple steps. Once you think enough PLAN has been done, finally you can give a OUTPUT.

Rules:
- Strictly Follow the given Json output format
- only run one step at a time
- The sequece of step is START (where user gives an input ), PLAN( that can be multiple times) and finally OUTPUT (which is going to the displayed to the user )


Output Json Format:
{{
"step": "START" or "PLAN" or "OUTPUT",
"content": "string"
}}

Example:
START: Hey, Can you solve 2+3*5/10
START: {
"step": "START",
"content": "Seems like user is interested in math problem",
}
PLAN: { "step":"PLAN", 
"content": "Looking at the promblem, we should solve using bodmas rule"
}
PLAN: { "step":"PLAN", 
"content": "Yes, The Bodmas is correct thing to be done here"
}
PLAN: { "step":"PLAN", 
"content": "first we must multiply 3*5 which is 15"
}
PLAN: { "step":"PLAN", 
"content": "Not the new equation is 2+15/10"
}
PLAN: { "step":"PLAN", 
"content": "We must perform divide that is 5/10"
}
PLAN: { "step":"PLAN", 
"content": "Now new equation is 2+1.5"
}
PLAN: { "step":"PLAN", 
"content": "Now finally let's perform the add 3.5"
}
PLAN: { "step":"PLAN", 
"content": "Great, we have solved and finally left with 3.5 as answer"
}

'''

print("\n\n\n")
message_history = [
    {"role":"system","content":SYSTEM_PROMPT}
]

user_query = input("👉")

message_history.append({"role":"user", "content":user_query})

while True:
    response = client.chat.completions.create(
        model="gemini-3-flash-lite",
        response_format={"type":"json_object"},
        messages=message_history
    )

    raw_result= response.choices[0].message.content # raw_result = {
#     "step": "PLAN",
#     "content": "I will use the `reduce` method on the arguments array to calculate the total sum."
#   },
    message_history.append({"role":"assistant","content":raw_result})

    parsed_result= json.loads(raw_result)
    print(parsed_result)
    if parsed_result.get("step") == "START":
        print("🫡",parsed_result.get("content"))
        continue
    if parsed_result.get("step") == "PLAN":
        print("🧐",parsed_result.get("content"))
        continue
    if parsed_result.get("step") == "OUTPUT":
        print("😁",parsed_result.get("content"))
        break
print("\n\n\n")