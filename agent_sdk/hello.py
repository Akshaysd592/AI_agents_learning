from dotenv import load_dotenv
from agents import Agent,Runner


load_dotenv()

# now since we are using openai sdk most of the implementation is done by openai(abstracted)
hello_agent = Agent(
    name="Hello World Agent",
    instructions="You are an agent which greets the users and helps them answer using emojis and in a funny way"
)


result = Runner.run_sync(hello_agent,"Hey there, My name is Akshay");

print(result.final_output)