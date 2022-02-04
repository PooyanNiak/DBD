import os

import cv2
import mediapipe as mp
import numpy as np
import pandas as pd
from tqdm import tqdm

mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_pose = mp.solutions.pose

pose = mp_pose.Pose(static_image_mode=True, model_complexity=1)
# image = cv2.imread(r'Images\c0\img_34.jpg')
# # while True:
# #     cv2.imshow('image', image)
# #     if cv2.waitKey(5) & 0xFF == 27:
# #       break
# image.flags.writeable = False
# results = pose.process(image)
# image.flags.writeable = True
# landmarks = results.pose_landmarks.landmark
# df = pd.DataFrame([], columns=['landmarks', 'class', 'filename'])

# res = []
# temp = {}
# tmp = {}
# for i in range(0, len(results.pose_landmarks.landmark)):
#     temp['x'] = landmarks[i].x
#     temp['y'] = landmarks[i].y
#     temp['z'] = landmarks[i].z
#     temp['presence'] = landmarks[i].presence
#     temp['visibility'] = landmarks[i].visibility
#     tmp[f"{i}"] = temp
#     temp = {}
    
# row = {'landmarks': tmp, 'class': 'c0', 'filename': 'image_name'}

# df = df.append(row, ignore_index=True)
# print(df.head())
# df.to_csv('landmarks.csv')
# print(res)
# mp_drawing.draw_landmarks(
#     image,
#     results.pose_landmarks,
#     mp_pose.POSE_CONNECTIONS,
#     landmark_drawing_spec=mp_drawing_styles.get_default_pose_landmarks_style())
# # save image
# cv2.imwrite('test_pose.jpg', image)
# exit()

# loop over all images in different classes which are placed in different folders
# in the images folder and save the pose landmarks in a csv file
df = pd.DataFrame(columns=['landmarks', 'class', 'filename'])
folders = ['c0', 'c1', 'c2', 'c3', 'c4', 'c5', 'c6', 'c7', 'c8', 'c9']
with mp_pose.Pose(static_image_mode=True, 
                    model_complexity=1,
                    min_detection_confidence=0.7,
                    min_tracking_confidence=0.7, enable_segmentation=False) as pose:
    for folder in os.listdir(r'Images'):
        fail = 0
        success = 0
        for image_name in tqdm(os.listdir('Images/' + folder)):
            address = 'Images\\' + folder + '\\' + image_name
            image = cv2.imread(address)
            image.flags.writeable = False
            results = pose.process(image)
            image.flags.writeable = True
            try:
                landmarks = results.pose_landmarks.landmark
                res = []
                temp = {}
                tmp = {}
                for i in range(0, len(results.pose_landmarks.landmark)):
                    temp['x'] = landmarks[i].x
                    temp['y'] = landmarks[i].y
                    temp['z'] = landmarks[i].z
                    temp['presence'] = landmarks[i].presence
                    temp['visibility'] = landmarks[i].visibility
                    tmp[f"{i}"] = temp
                    temp = {}
                row = {'landmarks': tmp, 'class': folder, 'filename': image_name}

                
                df = df.append(row, ignore_index=True)
                success += 1

            except:
                fail += 1
                
        print(f"{folder}: No pose found {fail/len(os.listdir('Images/' + folder)):.2f}")
        print(f"{folder}: {success}/{len(os.listdir('Images/' + folder))}")
            
    df.to_csv('pose_landmarks.csv', index=False)
