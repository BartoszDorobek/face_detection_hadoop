hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-*.jar \
    -mapper Mapper.py \
    -reducer Reducer.py \
    -input input_directory/*.csv \
    -output output_directory
