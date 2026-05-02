from fastapi import FastAPI, Query
from .queue.worker import process_query
from .client.rq_client import queue
from dotenv import load_dotenv
load_dotenv()


app = FastAPI()

@app.get("/")
def root():
    return {"status":"Server is up and running"}

@app.post("/chat")
def chat(
        query:str = Query(...,description="The chat query of user")
):
   job =  queue.enqueue(process_query,query) # this will return id of the job 
   return {"status":"queued","job_id":job.id} # here we are not returning actual result 

@app.get("/job-status") # this is for getting actual result with id passed once process completed 
def get_result(
        job_id:str = Query(..., description="Job Id")
):
    job = queue.fetch_job(job_id= job_id)
    result = job.return_value()
    return {"result":result}
