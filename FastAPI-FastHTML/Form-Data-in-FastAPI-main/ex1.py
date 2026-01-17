from fastapi import FastAPI,  Form #Form handles application/x-www-form-urlencoded data. 
app = FastAPI()

@app.post("/login/")
async def login(username: str = Form(...)): #It is required to pass value to username.
    return {"username": username}
