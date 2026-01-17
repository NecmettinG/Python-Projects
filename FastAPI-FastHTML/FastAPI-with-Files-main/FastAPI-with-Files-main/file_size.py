from fastapi import FastAPI, UploadFile
app = FastAPI()
@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile): #file is an instance of UploadFile.
    content = await file.read()  # Read file content. read() is an async method. That's why we use async and await. 
    return {"file_size": len(content)} #It will return the size value which is in bytes.

#in .txt files, a single character is 1 byte. If a .txt file contains the string "hello" and we upload this file, file_size will be 5 in json format. 
