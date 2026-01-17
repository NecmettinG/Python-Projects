from fastapi import FastAPI, UploadFile

app = FastAPI()

@app.post("/upload-chunked/")
async def upload_chunked(file: UploadFile):
  CHUNK_SIZE = 1_024 #size in bytes.
  contents = []
  while chunk := await file.read(CHUNK_SIZE): 
      contents.append(chunk) 
      
  last_element = contents.pop()
  return {"last_chunk_data": last_element}

