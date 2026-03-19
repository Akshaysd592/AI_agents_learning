import os

from openai import OpenAI
from dotenv import load_dotenv
import json 
from pydantic import BaseModel, Field
from typing import Optional
import requests
# This code will work for OpenAI model (here for gemini need some adjustments)
load_dotenv() # here it is not used but keeping it for future use if we want to load any environment variable from .env file

client = OpenAI(
    api_key="",
    base_url="https://generativelanguage.googleapis.com/v1beta/"
)
#for making vibe coding agent
def run_command(cmd: str):
    result = os.system(cmd)
    return result

#for making agent that makes actual api call and return response

def get_weather(city: str):
    url = f"https://wttr.in/{city.lower()}?format=%C+%t"
    response = requests.get(url)

    if response.status_code == 200:
        return f"The weather in {city} is {response.text}"
    return f"Something went wrong"

avaialble_tool = {
    "get_weather" : get_weather,
    "run_command" : run_command
}
SYSTEM_PROMPT = ''' you are a expert AI assistant in resolving user queries using chain of thought . you work on START, PLAN and OUTPUT format. you need first PLAN what need to be done.The PLAN can be multiple steps. Once you think enough PLAN has been done, finally you can give a OUTPUT. You can also call a tool if required from the list of available tools. For every tool call wait for the OBSERVE step which is the output from the called tool

Rules:
- Strictly Follow the given Json output format
- only run one step at a time
- The sequece of step is START (where user gives an input ), PLAN( that can be multiple times) and finally 

OUTPUT (which is going to the displayed to the user )


Output Json Format:
{{
"step": "START" or "PLAN" or "TOOL" or "OUTPUT",
"content": "string",
"tool":"string",
"input":"string"

}}

Available Tools:
- get_weather: Takes city name as an input and returns the weather info about the city
- run_command: This will run system command in terminal

Example 1:
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

Example 2:
START: What is the weather of Delhi
START: {
"step": "START",
"content": "Seems like user is interested in getting weather in india",
}
PLAN: { "step":"PLAN", 
"content": "Let's see if we are having any available tool from the list of tools"
}
PLAN: { "step":"PLAN", 
"content": "Great, we are having get_weather tool available for this query"
}
PLAN: { "step":"PLAN", 
"content": "I need to call get_weather tool with delhi as a input for city"
}
PLAN: { "step":"TOOL", 
"tool":"get_weather",
"content": "delhi"
}
PLAN: { "step":"OBSERVE", 
"content": "The tempreture of delhi is cloudy with 20 C"
}
PLAN: { "step":"PLAN", 
"content": "Great, I got the weather report about Delhi"
}
PLAN: { "step":"OUTPUT", 
"content": "The current weather in delhi is 20 C with some cloudy sky"
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
    if parsed_result.get("step") == "TOOL":
        tool_to_call = parsed_result.get("tool")
        tool_input = parsed_result.get("input")
        print("$:{tool_to_call}({tool_input})")
        tool_response = avaialble_tool[tool_to_call](tool_input)
        print("$:{tool_reponse}")
        message_history.append({"role":"developer","content":json.dump(
            {"step":"OBSERVE","tool":tool_to_call,"input":tool_input,"output":tool_response}
        )})
        continue
    if parsed_result.get("step") == "PLAN":
        print("🧐",parsed_result.get("content"))
        continue
    if parsed_result.get("step") == "OUTPUT":
        print("😁",parsed_result.get("content"))
        break
print("\n\n\n")