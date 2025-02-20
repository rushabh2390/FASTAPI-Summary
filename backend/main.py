from logging import error
from fastapi import FastAPI, File, UploadFile
from fastapi import FastAPI, HTTPException, responses
from fastapi.middleware.cors import CORSMiddleware
import shutil
import os
import docx
from pdfminer.high_level import extract_text
from summarygenerator import generate_metadata_summary
from filetextextracter import extract_text_from_file
app = FastAPI()
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/uploadfile")
async def create_upload_file(file: UploadFile = File(...)):
    if not os.path.exists("tmp"):
        os.makedirs("tmp")
    file_location = "tmp/"+file.filename
    with open(file_location, "wb+") as file_object:
        shutil.copyfileobj(file.file, file_object)
    ext = file.filename.split(".")[-1]
    error = None
    try:
        text = extract_text_from_file(file_location, ext)
        probable_metadata, probable_summary = generate_metadata_summary(text)
    except IOError:
        error = "Could not open/read file: " + file.filename+" "+file_location
    finally:
        os.remove(file_location)
    if error is not None:
        return {"error": error}
    return {"probable metadata": str(probable_metadata), "probable summary": str(probable_summary)}
