from fastapi import FastAPI,Form
app = FastAPI()
@app.post("/profile/")
async def update_profile(
    username: str = Form(...),
    bio: str = Form(None), #If we type Form(None) for defining a Form variable, it's not required to pass data to that Form variable.
    website: str = Form(None), #We can send empty values to optional form variables.
    age: int = Form(None)
):
    return {
        "username": username,
        "bio": bio,
        "website": website,
        "age": age
    }
