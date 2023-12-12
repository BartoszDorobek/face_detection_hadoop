#!/bin/bash
#!/usr/bin/python3


#   running example from the book:
#   command to run in terminal:
#   [$]: cat sample1.txt | python3 mapper.py | sort | python3 reducer.py
#   
#   script to run it on hadoop via Hadoop Streaming:
#   docs: https://hadoop.apache.org/docs/r1.2.1/streaming.html

#   checking the contents of hadoop directories:
#   [$]: hadoop fs -ls /user/usermr/input

#   sending input files: sample1.txt to hadoop:
#   [$]: hadoop fs -put sample1.txt /user/usermr/input

#   removing directories:
#   [$]: hadoop fs -rm -f -r /user/usermr/output/output_tekst_python

HADOOP_STREAM="/work/hadoop/hadoop-3.3.1/share/hadoop/tools/lib/hadoop-streaming-3.3.1.jar"

INPUT="/user/usermr/input/sample1.txt"
OUTPUT="/user/usermr/output/final"
MAPPER="mapper.py"
REDUCER="reducer.py"
FILES="-file ./mapper.py -file ./reducer.py"
HADOP_PATH="${HADOOP_HOME}/bin/hadoop"

#   delete previous output
echo -e "\nRemoving previous output..."
CMD="hadoop fs -rm -f -r ${OUTPUT}"
echo -e "\n${CMD}"
${CMD}


#   IMPORTANT NOTE:
#   (https://stackoverflow.com/questions/42084411/python-how-to-resolve-the-error-java-lang-runtimeexception-pipemapred-waitoutp)


#   bash problems, this command copied and pasted to terminal works just fine:
hadoop jar ${HADOOP_STREAM} -file ${MAPPER} -mapper "python3 ${MAPPER}" -file ${REDUCER} -reducer "python3 ${REDUCER}" -input ${INPUT} -output ${OUTPUT}

echo -e "\nShowing results:"
CMD="hadoop fs -cat ${OUTPUT}/part-00000"
${CMD}