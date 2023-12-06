#!/usr/bin/env python

import sys
import cv2
import csv

# Load the pre-trained Haar Cascade face detector
cascade_filename = cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
face_cascade = cv2.CascadeClassifier(cascade_filename)

def detect_face(image, scaleFactor, minNeighbors, minSize):
    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(image_gray, scaleFactor=scaleFactor, minNeighbors=minNeighbors, minSize=minSize)
    return faces

def process_image(line):
    # Parse the CSV line
    image_name, x, y, width, height = line.strip().split(',')

    # Convert values to integers
    x, y, width, height = map(int, [x, y, width, height])

    # Return a tuple with image name and face coordinates
    return image_name, (x, y, width, height)

def main():
    scaleFactor = 1.2
    minNeighbors = 1
    minSize = (30, 30)

    for line in sys.stdin:
        # Split the line into image name and face coordinates
        image_name, face_coordinates = process_image(line)

        # Detect faces using Haar Cascade in the image
        image = cv2.imread(image_name)
        if image is not None:
            faces = detect_face(image, scaleFactor, minNeighbors, minSize)

            # Emit each face's image name and coordinates
            for face in faces:
                print(f"{image_name},{','.join(map(str, face))}")

if __name__ == "__main__":
    main()
