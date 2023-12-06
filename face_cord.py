import cv2
import os
import csv

class FaceDetector():
    def __init__(self, faceCascadePath):
        self.faceCascade = cv2.CascadeClassifier(faceCascadePath)

    def detect(self, image, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30)):
        rects = self.faceCascade.detectMultiScale(image, scaleFactor=scaleFactor, minNeighbors=minNeighbors, minSize=minSize)
        return rects

def detect_face(image, scaleFactor, minNeighbors, minSize):
    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(image_gray, scaleFactor=scaleFactor, minNeighbors=minNeighbors, minSize=minSize)

    return faces  # Return the face coordinates

def main():
    image_directory = "input/images_small/"
    scaleFactor = 1.2
    minNeighbors = 1
    minSize = (30, 30)

    coordinates_output_file = "output/face_coordinates.csv"

    with open(coordinates_output_file, 'w', newline='') as coord_file:
        coord_writer = csv.writer(coord_file)

        coord_writer.writerow(["Image_name", "x", "y", "width", "height"])

        for filename in os.listdir(image_directory):
            if filename.endswith(".jpg"):
                image_path = os.path.join(image_directory, filename)

                image = cv2.imread(image_path)
                if image is not None:
                    faces = detect_face(image, scaleFactor, minNeighbors, minSize)

                    # Write face coordinates to the coordinates file
                    for x, y, w, h in faces:
                        coord_writer.writerow([filename, x, y, w, h])

if __name__ == '__main__':
    # Load the pre-trained Haar Cascade face detector
    cascade_filename = cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
    face_cascade = cv2.CascadeClassifier(cascade_filename)

    # Detector object created
    fd = FaceDetector(cascade_filename)

    main()
