from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from tempfile import NamedTemporaryFile
from roboflow import Roboflow
import os

app = FastAPI()

rf = Roboflow(api_key="4Q1ltu8TwBleQSDc8m08")
project = rf.workspace().project("new-drzrt")
model = project.version(1).model

# Enable CORS for all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

async def process_image(file: UploadFile):
    try:
        # Save the uploaded file to a temporary location
        with NamedTemporaryFile(delete=False, suffix=".jpg") as temp_file:
            temp_file.write(file.file.read())
            temp_file_path = temp_file.name

        # Perform YOLO predictions
        results =model.predict(temp_file_path, confidence=40, overlap=30).json()

        # Process the results and format them as needed
        # For example, you might want to return the detected objects and their bounding boxes
        return {"Number of Apples": len(results['predictions'])}

    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)
    finally:
        # Delete the temporary file after processing
        if temp_file_path:
            os.remove(temp_file_path)

@app.post("/predict")
async def predict_image(file: UploadFile = File(...)):
    return await process_image(file)