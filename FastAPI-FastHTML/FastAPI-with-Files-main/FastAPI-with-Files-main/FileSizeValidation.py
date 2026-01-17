from fastapi import HTTPException
from fastapi import FastAPI,  UploadFile
app = FastAPI()
@app.post("/fileSize/")
async def validate_file_size(file: UploadFile, max_size: int): #max_size is a query. it will represent max byte size.
    content = await file.read() #content will include the content of the file.
    if len(content) > max_size: #if the size of the content (bytes) is greater than query value, we will get exception.
        raise HTTPException(400, "File too large")
    return content #we will return the contents of the file. If it is a text file, we will return the string data.
