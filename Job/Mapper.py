import cv2
import numpy as np
import sys

def map_faces(image_path):
    cascade_filename = cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
    face_cascade = cv2.CascadeClassifier(cascade_filename)

    image = cv2.imread(image_path)
    if image is not None:
        image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(image_gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

        face_data = {
            "image_path": image_path,
            "faces": [(x, y, w, h) for x, y, w, h in faces]
        }

        return face_data
    else:
        return None
