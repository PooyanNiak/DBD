import string
import PIL.Image
import numpy as np
import cv2
from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin

from image_detector import pose_detector, behaviour_detector


app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route("/")
@cross_origin()
def index():
    return "server started!"


@ app.route("/imageProcess/v1.0/findPose", methods=["POST"])
@cross_origin()
def process_image():
    try:
        img = PIL.Image.open(request.files.get('imagefile', ''))
        img = np.array(img)
        img = cv2.cvtColor(np.array(img), cv2.COLOR_BGR2RGB)
        result = behaviour_detector(pose_detector(img))
        return jsonify({"result": result})
    except Exception as err:
        print(err)
        return jsonify({"error": "no image found"})


if __name__ == "__main__":
    app.run()
