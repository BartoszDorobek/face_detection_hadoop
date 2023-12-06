#!/usr/bin/env python
def reduce_faces(face_data_list):
    count_output = []
    coord_output = []

    for face_data in face_data_list:
        if face_data:
            image_path = face_data["image_path"]
            faces = face_data["faces"]

            # Count faces
            face_count = len(faces)
            count_output.append((image_path, face_count))

            # Emit face coordinates
            for x, y, w, h in faces:
                coord_output.append((image_path, x, y, w, h))

    return count_output, coord_output

