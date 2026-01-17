from fastapi import FastAPI,  Form
app = FastAPI()
@app.post("/user/")
async def create_user( #We can define multiple Form fields. All of them are required to pass data.
    username: str = Form(...),
    password: str = Form(...),
    email: str = Form(...),
    full_name: str = Form(...)
):
    return {
        "username": username,
        "email": email,
        "full_name": full_name
    }
