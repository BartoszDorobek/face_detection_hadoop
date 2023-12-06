#!/usr/bin/env python

import sys

def main():
    current_image = None
    face_count = 0

    for line in sys.stdin:
        line = line.strip()
        image_name, _ = line.split(',', 1)

        if current_image == image_name:
            face_count += 1
        else:
            if current_image is not None:
                print(f"{current_image},{face_count}")
            current_image = image_name
            face_count = 1

    if current_image is not None:
        print(f"{current_image},{face_count}")

if __name__ == "__main__":
    main()
