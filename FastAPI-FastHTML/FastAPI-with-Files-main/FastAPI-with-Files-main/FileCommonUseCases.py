from fastapi import FastAPI, UploadFile
from fastapi import HTTPException
app = FastAPI()

# Example 1: Reading text file
@app.post("/upload-text/")
async def upload_text(file: UploadFile):
  content = await file.read()
  text_content = content.decode('utf-8')  # Convert bytes to string. It only works on .txt and similar files like asm etc.
  return {"text": text_content}

# Example 2: Reading image file
@app.post("/upload-image/")
async def upload_image(file: UploadFile):
  content = await file.read() #We can also read files and return its byte size.
  # Process image bytes
  return {"file_size": len(content)}

# Example 3: Reading with size limit
@app.post("/upload-limited/")
async def upload_limited(file: UploadFile):
  content = await file.read()
  if len(content) > 1_048_576:  # 1MB limit. 1_024 Byte is 1 KB, 1_048_576 Byte is 1 MB. (we can also type 1048576 or 1024 without underscore.)
      raise HTTPException(status_code=400, detail="File too large") #We will get http exception if we upload a file with the size more than 1MB.
  return {"file_size": len(content)} #If we don't exceed the file size, we will get the size value in json.