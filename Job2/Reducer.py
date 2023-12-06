#!/usr/bin/env python

import sys

def main():
    current_image = None
    face_count = 0

    for line in sys.stdin:
        # Split the line into image name and face coordinates
        image_name, _ = line.strip().split(',', 1)

        # If it's a new image, print the face count for the previous image
        if current_image and current_image != image_name:
            print(f"{current_image},{face_count}")
            face_count = 0

        # Update current image and increment face count
        current_image = image_name
        face_count += 1

    # Print the last image's face count
    if current_image:
        print(f"{current_image},{face_count}")

if __name__ == "__main__":
    main()
