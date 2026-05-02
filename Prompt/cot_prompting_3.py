from openai import OpenAI
from dotenv import load_dotenv
import json 
load_dotenv() # here it is not used but keeping it for future use if we want to load any environment variable from .env file

client = OpenAI(
    api_key="",
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

response = client.chat.completions.create(

    model="gemini-3-flash-preview",
    response_format={"type":"json_object"},
    messages=[  
        {"role": "system", "content": SYSTEM_PROMPT},#system prompt
        {
            "role": "user",
            "content": "Hey, write a code to add n numbers in js"
            # "content":"help me solve a-b whole square"
        },
        {
            "role":"assistant",
           "content":json.dumps( {"step": "START",  "content": "The user wants a JavaScript function to calculate the sum of an arbitrary amount of numbers ('n' numbers)."} )
        },
         {
            "role":"assistant",
           "content":json.dumps( {"step": "PLAN", "content": "I will define a function that uses the rest parameter syntax (...args) to accept any number of arguments in JavaScript."} )
        },
        {
            "role":"assistant",
           "content":json.dumps( {
    "step": "OUTPUT",
    "content": "To add 'n' numbers in JavaScript, you can use the rest parameter syntax along with the `reduce` method. Here is the code:\n\n```javascript\nfunction addNumbers(...numbers) {\n  return numbers.reduce((accumulator, current) => accumulator + current, 0);\n}\n\n// Example usage:\nconsole.log(addNumbers(1, 2, 3)); // Output: 6\nconsole.log(addNumbers(10, 20, 30, 40, 50)); // Output: 150\n```"
  } )
        }
    ]
)

# this assistant role is added here for history, we can automate to provide this history to this model at once also. here we added it manually one by one after running the file again and again with role as assistant

print(response.choices[0].message.content)

