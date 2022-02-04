import os
import cv2
import mediapipe as mp
import numpy as np
import pickle
from utils import _normalized_to_pixel_coordinates

labels_dict = {
    "c0": "safe driving",
    "c1": "texting - right",
    "c2": "talking on the phone - right",
    "c3": "texting - left",
    "c4": "talking on the phone - left",
    "c5": "operating the radio",
    "c6": "drinking",
    "c7": "reaching behind",
    "c8": "hair and makeup",
    "c9": "talking to passenger",
}


def pose_detector(image):
    # mp_drawing = mp.solutions.drawing_utils
    # mp_drawing_styles = mp.solutions.drawing_styles
    mp_pose = mp.solutions.pose
    pose = mp_pose.Pose(static_image_mode=True, model_complexity=2,
                        enable_segmentation=False, min_detection_confidence=0.1)

    image.flags.writeable = False
    results = pose.process(image)
    image.flags.writeable = True
    try:
        landmarks = results.pose_landmarks.landmark
        res = []
        temp = []
        tmp = {}
        for i in range(0, len(results.pose_landmarks.landmark)):
            temp.append([landmarks[i].x, landmarks[i].y])
        # print(temp)
        return temp
    except:
        print("Couldn't detect pose!!")
        return
# Test image
# image = cv2.imread("../sample_images/test_pose.jpg")
# image_pose = pose_detector(image)


def behaviour_detector(image_pose):
    filename = "model.sav"
    model = pickle.load(open("../model/" + filename, 'rb'))
    if (image_pose):
        image_pose = np.array(image_pose)
        max_x, min_x = max(image_pose.T[0]), min(image_pose.T[0])
        max_y, min_y = max(image_pose.T[1]), min(image_pose.T[1])
        result = model.predict(np.array(image_pose).reshape((1, 33*2)))
        result_class = labels_dict[result[0]]
        # result class
        # print(result_class)
        # Coords for drawing box
        scaled_min_x, scaled_min_y = _normalized_to_pixel_coordinates(
            min_x, min_y, image_pose.shape[0], image_pose.shape[1])
        scaled_max_x, scaled_max_y = _normalized_to_pixel_coordinates(
            max_x, max_y, image_pose.shape[0], image_pose.shape[1])
        coords = [scaled_min_x, scaled_min_y, scaled_max_x, scaled_max_y]
        # print(coords)
        return {"result": result_class, "coords": coords}
