from fastapi import FastAPI, UploadFile, HTTPException

app = FastAPI()

@app.post("/upload/")
async def upload_file(file: UploadFile):
  try:
      content = await file.read() #reading the uploaded file.
      print(type(content)) #<class 'bytes'> is the output in terminal.
      
      # Size validation
      if len(content) > 5_242_880:  # 5MB limit
          raise HTTPException(status_code=400, detail="File too large") #If we upload a file with a size more than 5MB, we will get exception.
          
      # Process the content
      file_location = f"{file.filename}" #file_location will equal to the name of the uploaded file with its extension (like .txt).
      with open(file_location, "wb") as f: #we will create a file that has same name and extension with uploaded file in "write binary" mode. 
          f.write(content) #writing the content of the uploaded file in binary mode. This is useful on .png, .xlsx, .docx etc.
          
      return {
          "filename": file.filename,
          "size": len(content),
          "content_type": file.content_type,
          "location": file_location
      } #"filename" and "location" will be the same.
      
  except Exception as e: #If we get an error in try block:
      raise HTTPException(status_code=500, detail=str(e))
  
  finally: #After the execution, close the file for avoiding memory usage.
      await file.close()