import cv2
import mediapipe as mp
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands
mp_pose = mp.solutions.pose
mp_face_mesh = mp.solutions.face_mesh


# For webcam input:
cap = cv2.VideoCapture(0)
# with mp_hands.Hands(
#     model_complexity=0,
#     min_detection_confidence=0.5,
#     min_tracking_confidence=0.5) as hands:
  
pose = mp_pose.Pose(model_complexity=0,
  min_detection_confidence=0.7,
  min_tracking_confidence=0.7, enable_segmentation=False)

  # face_mesh = mp_face_mesh.FaceMesh(
  #   max_num_faces=1,
  #   refine_landmarks=True,
  #   min_detection_confidence=0.5,
  #   min_tracking_confidence=0.5)

while cap.isOpened():
  success, image = cap.read()

    # To improve performance, optionally mark the image as not writeable to
    # pass by reference.
    # image.flags.writeable = False
    # image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    # results = hands.process(image)

    # # # Draw the hand annotations on the image.
    # image.flags.writeable = True
    # image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    # if results.multi_hand_landmarks:
    #   for hand_landmarks in results.multi_hand_landmarks:
    #     mp_drawing.draw_landmarks(
    #         image,
    #         hand_landmarks,
    #         mp_hands.HAND_CONNECTIONS,
    #         mp_drawing_styles.get_default_hand_landmarks_style(),
    #         mp_drawing_styles.get_default_hand_connections_style())
    
  image.flags.writeable = False
  results = pose.process(image)
  image.flags.writeable = True
  mp_drawing.draw_landmarks(
      image,
      results.pose_landmarks,
      mp_pose.POSE_CONNECTIONS,
      landmark_drawing_spec=mp_drawing_styles.get_default_pose_landmarks_style())
    
      
    # image.flags.writeable = False
    # results = face_mesh.process(image)
    # # Draw the face mesh annotations on the image.
    # image.flags.writeable = True
    # # image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    # if results.multi_face_landmarks:
    #   for face_landmarks in results.multi_face_landmarks:
    #     mp_drawing.draw_landmarks(
    #         image=image,
    #         landmark_list=face_landmarks,
    #         connections=mp_face_mesh.FACEMESH_TESSELATION,
    #         landmark_drawing_spec=None,
    #         connection_drawing_spec=mp_drawing_styles
    #         .get_default_face_mesh_tesselation_style())
    #     mp_drawing.draw_landmarks(
    #         image=image,
    #         landmark_list=face_landmarks,
    #         connections=mp_face_mesh.FACEMESH_CONTOURS,
    #         landmark_drawing_spec=None,
    #         connection_drawing_spec=mp_drawing_styles
    #         .get_default_face_mesh_contours_style())
    #     mp_drawing.draw_landmarks(
    #         image=image,
    #         landmark_list=face_landmarks,
    #         connections=mp_face_mesh.FACEMESH_IRISES,
    #         landmark_drawing_spec=None,
    #         connection_drawing_spec=mp_drawing_styles
    #         .get_default_face_mesh_iris_connections_style())
    # Flip the image horizontally for a selfie-view display.
  cv2.imshow('MediaPipe Hands', cv2.flip(image, 1))
  if cv2.waitKey(5) & 0xFF == 27:
    break
cap.release()