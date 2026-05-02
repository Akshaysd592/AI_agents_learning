from typing import Annotated

from langgraph.graph import StateGraph, START,END
from typing_extensions import TypedDict
from langgraph.graph.message import add_messages
from langchain.chat_models import init_chat_model
from dotenv import load_dotenv
load_dotenv()

llm = init_chat_model(
    model="gpt-4.1-mini",
    model_provider="openai"
)


#State
class State(TypedDict):
    messages: Annotated[list,add_messages] #this is appending new message with earlier message list


#Nodes
def chatbot(state: State): #This is node created 
    response = llm.invoke(state.get("messages"))
    return {"message":[response]}
    # return {"messages":["Hi, This is a messsage from ChatBot Node"]}

def sampleNode(state: State): #This is node created 
    return {"messages":["This is a sample node "]}

graph_builder = StateGraph(State)
graph_builder.add_node("chatbot",chatbot)


# connect node with edge
graph_builder.add_edge(START,"chatbot")
graph_builder.add_edge("chatbot","sampleNode")
graph_builder.add_edge("sampleNode",END)
# START-> chatbot -> sampleNode -> END

graph = graph_builder.compile()


#Running Graph which will update state for each node
update_state = graph.invoke(State({"messages":"Hi, My name is Akshay"}))
print("updated state",update_state)
