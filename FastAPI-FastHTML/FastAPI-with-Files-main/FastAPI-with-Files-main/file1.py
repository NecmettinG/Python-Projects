from fastapi import FastAPI, File, UploadFile
app = FastAPI()
@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile):
    content= await file.read() #We are able to access the contents, as bytes, of the uploaded file with await file.read().
    print(content  ) #We will print the content inside of the uploaded file. (like a text inside of a .txt file.)
    return {
        "filename": file.filename,
        "content_type": file.content_type
        
        }
#await is for prioritizing the proccess. (in this code, reading is prioritized. It is an asynchronus operation.)