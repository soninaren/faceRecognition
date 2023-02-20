import face_recognition
import shutil
from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/takePicture")
def takePicture():
    filePath = request.args.get("filePath")
    image = face_recognition.load_image_file(filePath)
    face_locations = face_recognition.face_locations(image)
    if len(face_locations) > 0:  
      return "true"
    else:
       return "false"
