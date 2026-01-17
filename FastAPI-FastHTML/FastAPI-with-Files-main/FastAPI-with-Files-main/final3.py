from fastapi import FastAPI, UploadFile, Form

app = FastAPI()

@app.post("/upload-chunked/")
async def upload_chunked(file: UploadFile, chunk_size: int = Form(...)):
  CHUNK_SIZE =  chunk_size*2
  contents = []
  while chunk := await file.read(CHUNK_SIZE): 
      contents.append(chunk) 
      
  return {"chunks_received": len(contents), "chunk_size": CHUNK_SIZE}

