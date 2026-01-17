from fastapi import FastAPI, File, UploadFile
app = FastAPI()
@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile): #file is the uploaded file that is passed with fastapi swagger ui.
    return {
        "filename": file.filename,
        "content_type": file.content_type
    }
#file is an instance of UploadFile class.