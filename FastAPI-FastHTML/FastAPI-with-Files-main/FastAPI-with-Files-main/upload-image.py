from fastapi import HTTPException
from fastapi import FastAPI, UploadFile
app = FastAPI()
@app.post("/upload-image/")
async def upload_image(file: UploadFile):
    if not file.content_type.startswith('image/'): #the content type of the images starts with "image/".
        raise HTTPException(400, "File is not an image")
    return {"filename": file.filename}
