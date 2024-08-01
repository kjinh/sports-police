from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import JSONResponse
import shutil, requests
from typing import List

app = FastAPI()

# Azure Machine Learning Endpoint URL
AML_ENDPOINT = "testing-url"


@app.get("/")
async def read_root():
    return {"message": "Welcome to the Video Rating API"}


@app.post("/api/upload")
async def upload_video(file: UploadFile = File(...)):
    if not file.content_type.startswith(f"videos/{file.filename}"):
        raise HTTPException(status_code=400, detail="File type not supported")
    
    # 파일 저장 경로 설정
    file_location = f"videos/{file.filename}"
    with open(file_location, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # AML 엔트포인트로 파일 전송
    with open(file_location, "rb") as f:
        files = {'file': f}
        #response = requests.post(AML_ENDPOINT, files=files)
        #result = response.json()
        result = 0.85 # temporary result

    return JSONResponse(content=result)


@app.get("api/details")
async def get_details(score: float, reference_image_url: str):
    details = f"Good" # temporary details
    
    return JSONResponse(content={"score": score, "reference_image_url": reference_image_url, "details": details})
