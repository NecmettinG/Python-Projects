from fastapi import Depends #Depends for using dependency injection.
from fastapi import FastAPI,Form
app = FastAPI()
async def verify_token(token: str = Form(...)): #We will see "token" field in swagger ui request body. not "token_main"!
    return f"{token} is my token."

@app.post("/protected/")
async def protected_route(
    message: str = Form(...),
    token_main: str = Depends(verify_token) #token_main is depended to verify_token function. token_main will hold the return value of verify_token function.
#on request body, we will pass data for token with using verify_token. the parameter called "token" is a form variable, we will send data to it. 
):
    return {"message": message, "token": token_main} 
