from dotenv import  load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI()
response = client.chat.completing.create(
    model="gpt-4.1-mini", #model should be image compatible 
    message=[
        {"role":"user",
         "content":[
             {
              "type":"text",
              "text":"generate a caption for the image in about 50 words"
             },{
                "type":"image_url",
                "image_url":{"https://images.pexels.com/photos/879109"}
             }
         ]}
    ]
)


print("response",response.choices[0].message.content)