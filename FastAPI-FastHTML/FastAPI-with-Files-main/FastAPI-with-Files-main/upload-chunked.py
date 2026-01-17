from fastapi import FastAPI, UploadFile

app = FastAPI()
# Chunked reading for large files
@app.post("/upload-chunked/")
async def upload_chunked(file: UploadFile):
  CHUNK_SIZE = 1024  # 1KB chunk size, we can also type 1_024 with underscore for better readability.
  contents = []
  while chunk := await file.read(CHUNK_SIZE): # chunk will hold maximum 1024 bytes data in each iteration and will be appended to contents list.
      contents.append(chunk) #If we upload 1MB text file, 1048576 bytes, there will be 1024 elements-chunks inside of contents list.
      print(chunk)
  return {"chunks_received": len(contents)}

# ":=" is walrus operator!"
#If we upload a .txt file with 1_048_577 bytes, there will be 1025 elements-chunks inside of contents list. that 1 byte is also considered a chunk.
#In this code, a chunk may have the size between 1-1024 bytes. In 1048577 bytes, portioning will be 1024-1024-1024-...-1024-1.
#It will portion the bytes as chunks until bytes are depleted.
#If you want to work with chunks, just write the byte size of a single chunk inside of await file.read(). (await file.read(size))