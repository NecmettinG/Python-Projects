from fastapi import FastAPI,File,Form, UploadFile
app = FastAPI()
@app.post("/upload/")
async def upload_file(
    file: UploadFile = File(...), #We have special form type for uploading files. with File(...), we are uploading file as form data. 
    description: str = Form(...)
):
    return {
        "filename": file.filename, #we will return the uploaded file name into json format.
        "description": description #description comes from form input.
    }


