from fastapi import FastAPI, UploadFile

app = FastAPI()

@app.post("/upload-chunked/")
async def upload_chunked(file: UploadFile):
  CHUNK_SIZE = 512 #size in bytes.
  contents = []
  while chunk := await file.read(CHUNK_SIZE): 
      contents.append(chunk)
      print(chunk) 
      
  return {"chunks_received": len(contents)}

