from fastapi import FastAPI,Body
from ollama import Client

# for this we need ollama docke container  and open webUI docker container running in docker 
client = Client(
    host="http://localhost:11434"
)

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello":"World"}

@app.post("/chat")
def chat(
    message: str = Body(..., description ="The Message")
):
    response = client.chat(model="gemma:2b",message=[
        {"role":"user", "content":message}
    ])
    return {"response": response.message.content}