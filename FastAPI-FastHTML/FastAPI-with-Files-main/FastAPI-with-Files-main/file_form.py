from fastapi import FastAPI, File, UploadFile, Form
app = FastAPI()
@app.post("/upload-with-data/")
async def create_upload_with_data(
    file: UploadFile,
    description: str = Form(...), #with Form(...), we are passing string data that is not inside of json payload. THEY ARE NOT QUERRIES BTW! 
    category: str = Form(...) #We write strings inside of white areas.
):
    return {
        "filename": file.filename,
        "description": description,
        "category": category
    } #we will return the name of the file and form strings inside of json.
