from dotenv import load_dotenv
from agents import Agent,Runner,WebSearchTool,function_tool
import requests



load_dotenv()

@function_tool
def get_weather(city: str): # for function tools using openai sdk
    """
    Fetch the weather for given location 

    Args:
        city: The city name to fetch the weather for 
    """
    url = f"https://wttr.in/{city.lower()}?format=%C+%t"
    response = requests.get(url)

    if response.status_code == 200:
        return f"The weather in {city} is {response.text}"
    return f"Something went wrong"

# now since we are using openai sdk most of the implementation is done by openai(abstracted)
hello_agent = Agent(
    name="Hello World Agent",
    instructions="You are an agent which greets the users and helps them answer using emojis and in a funny way",
    tools=[
        WebSearchTool(), #now it can use web for the response like today's weather we can ask  as we are providing it as a tool 
        get_weather # don't have to call it this is reference here as this is a function tool 
    ]
)


result = Runner.run_sync(hello_agent,"Hey there, My name is Akshay");

print(result.final_output)