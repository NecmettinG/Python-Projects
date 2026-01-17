from fastapi import BackgroundTasks, FastAPI, Form
from typing import Optional
import time
import uvicorn

app = FastAPI()

def process_form(data: str): #Form data is sent to this function as a parameter.
  # Simulate some time-consuming process
  time.sleep(5)  # Simulates a 5-second processing task
  with open("processed_data.txt", "a") as f: #"a" means append mode, we will append data to end of the processed_data.txt file.
      f.write(f"Processed: {data}\n") #we will append data to the file.
      #If there is no processed_data.txt file, it will be created!

@app.post("/submit/")
async def submit_form(
  background_tasks: BackgroundTasks, #BackgroundTasks is collection of background tasks that will be called after a response has been sent to the client.
  data: str = Form(...)
):
  background_tasks.add_task(process_form, data) #process_form function will be executed and data will be sent to process_form after the response.
  return {"message": f"Processing data: {data}"} # process_form will be executed after this.

# Add a root endpoint for testing
@app.get("/")
async def root():
  return {"message": "Welcome to the API"}

if __name__ == "__main__":
  uvicorn.run(app, host="127.0.0.1", port=8000)