from agents import Agent, Runner
from dotenv import load_dotenv

load_dotenv()

spanish_agent = Agent(
    name="Spanish agent",
    instructions="you translate the user's message to Spanish"
)

french_agent = Agent(
    name="French agent",
    instructions="You translate the user's message to French",
)

orchestrator_agent = Agent(
    name="orchestrator_agent",
    instructions=(
        "You are a translation agent. You use the tools given to you to translate."
        "If asked for multiple translations, you call the relevant tools."
    ),
    tools=[
        spanish_agent.as_tool(
            tool_name="translate_to_spanish",
            tool_description="Translate the user's message to Spanish",
        ),
        french_agent.as_tool(
            tool_name="translate_to_french",
            tool_description="Translate the user's message to French",
        ),
    ],
)

result = Runner.run_sync(orchestrator_agent, input="Say 'Hello, how are you?' in Spanish.")
print(result.raw_responses) # to print which agent as a tool running

print(result.final_output) # actual output 
