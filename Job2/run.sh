#!/bin/bash

# Set your Hadoop home directory
#HADOOP_HOME=/path/to/your/hadoop
HADOOP_BIN=${HADOOP_HOME}/bin/hadoop

# Input and output directories
INPUT_PATH="/home/usermr/examples/input/images_small/"
OUTPUT_PATH="/home/usermr/examples/output/face_count/"

# Upload input data to HDFS
hadoop fs -put $INPUT_DIR/*.csv input

# Run Hadoop Streaming job
hadoop jar $HADOOP_BIN/share/hadoop/tools/lib/hadoop-streaming-*.jar \
    -mapper Mapper.py \
    -reducer Reducer.py \
    -input input \
    -output $OUTPUT_DIR

# Display the output
hadoop fs -cat $OUTPUT_DIR/*
