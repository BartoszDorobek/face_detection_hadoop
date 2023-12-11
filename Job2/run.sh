#!/bin/bash

# Set your Hadoop home directory
#HADOOP_HOME=/work/hadoop/hadoop
HADOOP_HOME=/work/hadoop/hadoop-3.3.1
HADOOP_BIN=${HADOOP_HOME}/bin/hadoop

# Input and output directories
INPUT_PATH="/home/usermr/examples/input/images_small/"
OUTPUT_PATH="/home/usermr/examples/output/face_count/"

# Upload input data to HDFS
hadoop fs -put $INPUT_PATH/*.csv input

# Run Hadoop Streaming job
hadoop jar ${HADOOP_HOME}/share/hadoop/tools/lib/hadoop-streaming-3.3.1.jar \
    -mapper Mapper.py \
    -reducer Reducer.py \
    -input input \
    -output $OUTPUT_PATH

# Display the output
$HADOOP_BIN fs -cat $OUTPUT_PATH/*