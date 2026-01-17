
from fastapi import  FastAPI,Depends
from fastapi.security import OAuth2PasswordRequestForm
app = FastAPI()
@app.post("/token")
async def login(
    form_data: OAuth2PasswordRequestForm = Depends()
#OAuth2PasswordRequestForm is a dependency class to collect the username and password as form data for an OAuth2 password flow.
#The OAuth2 specification dictates that for a password flow the data should be collected using form data (instead of JSON), 
#And that it should have the specific fields username and password.
#There will be form variables on request body like grant_type, username (required), password (required), scope, client_id, client_secret.

):
    return {
        "access_token": form_data.username, #returning username form data.
        "token_type": "bearer"
    }
