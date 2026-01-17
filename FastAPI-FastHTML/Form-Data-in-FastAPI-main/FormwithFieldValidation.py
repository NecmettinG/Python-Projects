from pydantic import EmailStr # EmailStr is a special string type for emails. We have to pass a string data in the format of "user@example.com"
from fastapi import FastAPI,Form
app = FastAPI()
@app.post("/register/")
async def register(
    email: EmailStr = Form(...),
    password: str = Form(..., min_length=8), #min_length=8 means we have to pass a string data with min length 8.
    age: int = Form(..., gt=0, lt=120) #gt means greater than, lt means less than. We have to pass int data to age that is in the interval of [1, 119]
    #ge means greater than or equal to, le means less than or equal to. 
):
    return {"message": "Registration successful"}
