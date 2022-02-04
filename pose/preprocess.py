# remove landmarks noise
def remove_noise(pose_landmarks):
    for i in range(0, len(pose_landmarks.landmark)):
        if pose_landmarks.landmark[i].presence == 0:
            pose_landmarks.landmark[i].x = 0
            pose_landmarks.landmark[i].y = 0
            pose_landmarks.landmark[i].z = 0
            pose_landmarks.landmark[i].presence = 0
            pose_landmarks.landmark[i].visibility = 0
    return pose_landmarks

    # TODO: remove noise

# replace landmarks with average of same landmarks
def replace_landmarks(pose_landmarks):
    # TODO: replace landmarks (code is AI generated)
    for i in range(0, len(pose_landmarks.landmark)):
        if pose_landmarks.landmark[i].presence == 0:
            x = 0
            y = 0
            z = 0
            count = 0
            for j in range(0, len(pose_landmarks.landmark)):
                if pose_landmarks.landmark[j].presence == 1:
                    if pose_landmarks.landmark[i].name == pose_landmarks.landmark[j].name:
                        x += pose_landmarks.landmark[j].x
                        y += pose_landmarks.landmark[j].y
                        z += pose_landmarks.landmark[j].z
                        count += 1
            if count > 0:
                pose_landmarks.landmark[i].x = x / count
                pose_landmarks.landmark[i].y = y / count
                pose_landmarks.landmark[i].z = z / count
                pose_landmarks.landmark[i].presence = 1
                pose_landmarks.landmark[i].visibility = 1
    return pose_landmarks