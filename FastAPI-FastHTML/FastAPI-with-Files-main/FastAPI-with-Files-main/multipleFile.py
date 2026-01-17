from fastapi import FastAPI, File, UploadFile
from typing import List

app = FastAPI()

@app.post("/uploadfiles/")
async def create_upload_files(files : List[UploadFile]): #We are going to pass a list of files (multiple file upload).
    return {"filenames" : [file.filename for file in files]} #We are going to return the names of files as a list in json format.