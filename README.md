# Hadoop face detection system
## Technologies 
- Python
  - PyArrow - Apache Arrow Python
- Hadoop
  - Hadoop streaming
- OpenCV
    - Haar cascade algorithm
## Pipeline
![image](https://github.com/BartoszDorobek/face_detection_hadoop/assets/53353490/7f9483bf-b50d-4790-80eb-a4973ae7f8e1)

## Mapper
![image](https://github.com/BartoszDorobek/face_detection_hadoop/assets/53353490/66e08e68-b34c-44bf-84f1-8bd787939092)

## MapReduce Job Execution Flow
![image](https://github.com/BartoszDorobek/face_detection_hadoop/assets/53353490/e6c507cc-a402-48a0-852f-0ede45a9d764)

## Evaluation
We have used F1-score as metric for evaluation.

The average result on testing dataset was 68,40%

![image](https://github.com/BartoszDorobek/face_detection_hadoop/assets/53353490/536a5974-6f66-430c-91ee-ef163ddb4be2)

For the purpose of increasing accuracy, we may utilize a larger dataset and a more complex face detection algorithm, such as YOLO.
