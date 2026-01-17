
from datetime import date
from enum import Enum #For using enumeration.
from fastapi import FastAPI,Form
app = FastAPI()
class UserType(str, Enum): #This class is created for using enumeration.
    ADMIN = "adminn"
    USER = "user"

@app.post("/create-event/")
async def create_event(
    event_date: date = Form(...), #date is a class for time stamps.
    user_type: UserType = Form(...), #on request body, we will able to pass only two string data, "admin" and "user". It is required to pass data btw. 
    description: str = Form(...)
):
    return {"event": "created", "user_type": user_type} # on user_type, we will return "admin" or "user", depend on the enum data we pass.

