from sys import path
from typing import List
from fastapi import BackgroundTasks, FastAPI
from fastapi.datastructures import UploadFile
from fastapi.params import File
import utils
import ocr
import time
app = FastAPI()

# def write_notification(email: str, message=""):
#     with open("log.txt", mode="w") as email_file:
#         # breakpoint()
#         content = f"notification for {email}: {message}"
#         email_file.write(content)

# @app.post("/send-notification/{email}")
# def send_notification(email: str, background_tasks: BackgroundTasks):
#     background_tasks.add_task(write_notification, email, message="some notification")
#     return {"message": "Notification sent in the background"}


# @app.post("/register/{email}/{password}")
# def register_user(email: str, passsword: str):
#     return {"message": "User registered successfully"}


@app.get("/")
def home():
    return {"message": "Visit the endpoint: /api/v1/extract_text to perform OCR."}


@app.post("/api/v1/extract_text")
async def extract_text(Images: List[UploadFile] = File(...)):
    response = {}
    s = time.time()
    for img in Images:
        print("Images uploaded: ", img.filename)
        temp_file = utils._save_file_to_server(img, path="./", save_as=img.filename)
        text = await ocr.read_image(temp_file)
        response[img.filename] = text
    response["Time Taken"] = round((time.time() - s), 2)


    return response

