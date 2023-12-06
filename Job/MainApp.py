import cv2
import os
import csv
from Mapper import map_faces
from Reducer import reduce_faces

class FaceDetector():
    def __init__(self, faceCascadePath):
        self.faceCascade = cv2.CascadeClassifier(faceCascadePath)

    def detect(self, image, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30)):
        rects = self.faceCascade.detectMultiScale(image, scaleFactor=scaleFactor, minNeighbors=minNeighbors, minSize=minSize)
        return rects

def main():
    image_directory = "../input/images_small/"
    scaleFactor = 1.2
    minNeighbors = 1
    minSize = (30, 30)

    count_output_file = "../output/face_counts.csv"
    coordinates_output_file = "../output/face_coordinates.csv"

    # Initialize outputs
    count_output = []
    coord_output = []

    for filename in os.listdir(image_directory):
        if filename.endswith(".jpg"):
            image_path = os.path.join(image_directory, filename)

            # Use the map_faces function from Mapper.py
            face_data = map_faces(image_path)

            if face_data:
                count_output.append(face_data)
                coord_output.append(face_data)

    # Use the reduce_faces function from Reducer.py
    count_result, coord_result = reduce_faces(count_output)

    # Write counted faces to the count file
    with open(count_output_file, 'w', newline='') as count_file:
        count_writer = csv.writer(count_file)
        count_writer.writerow(["Image_name", "Counted_faces"])
        for image_path, face_count in count_result:
            count_writer.writerow([image_path, face_count])

    # Write face coordinates to the coordinates file
    with open(coordinates_output_file, 'w', newline='') as coord_file:
        coord_writer = csv.writer(coord_file)
        coord_writer.writerow(["Image_name", "x", "y", "width", "height"])
        for image_path, x, y, w, h in coord_result:
            coord_writer.writerow([image_path, x, y, w, h])

if __name__ == '__main__':
    # Load the pre-trained Haar Cascade face detector
    cascade_filename = cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
    face_cascade = cv2.CascadeClassifier(cascade_filename)

    # Detector object created
    fd = FaceDetector(cascade_filename)

    main()
