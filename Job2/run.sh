#!/bin/bash

# Set your Hadoop home directory
HADOOP_HOME=/path/to/your/hadoop

# Input and output directories
INPUT_DIR=input_directory
OUTPUT_DIR=output_directory

# Upload input data to HDFS
hadoop fs -put $INPUT_DIR/*.csv input

# Run Hadoop Streaming job
hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-*.jar \
    -mapper Mapper.py \
    -reducer Reducer.py \
    -input input \
    -output $OUTPUT_DIR

# Display the output
hadoop fs -cat $OUTPUT_DIR/*
