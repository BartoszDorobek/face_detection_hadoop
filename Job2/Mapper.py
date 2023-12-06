#!/usr/bin/env python

import cv2
import os
import csv
import sys


class FaceDetector():
    def __init__(self, faceCascadePath):
        self.faceCascade = cv2.CascadeClassifier(faceCascadePath)

    def detect(self, image, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30)):
        rects = self.faceCascade.detectMultiScale(image, scaleFactor=scaleFactor, minNeighbors=minNeighbors, minSize=minSize)
        return rects


def detect_face(image, face_cascade, scaleFactor, minNeighbors, minSize):
    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(image_gray, scaleFactor=scaleFactor, minNeighbors=minNeighbors, minSize=minSize)

    return faces  # Return the face coordinates


def process_image(image_path, face_cascade, scaleFactor, minNeighbors, minSize):
    image = cv2.imread(image_path)
    if image is not None:
        faces = detect_face(image, face_cascade, scaleFactor, minNeighbors, minSize)

        # Write face coordinates to standard output
        for x, y, w, h in faces:
            print(f"{os.path.basename(image_path)},{x},{y},{w},{h}")


if __name__ == "__main__":
    # Load the pre-trained Haar Cascade face detector
    cascade_filename = cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
    face_cascade = cv2.CascadeClassifier(cascade_filename)

    # Detector object created
    fd = FaceDetector(cascade_filename)

    # Define detection parameters
    scaleFactor = 1.2
    minNeighbors = 1
    minSize = (30, 30)

    # Read image paths from input
    for line in sys.stdin:
        image_path = line.strip()
        process_image(image_path, face_cascade, scaleFactor, minNeighbors, minSize)
