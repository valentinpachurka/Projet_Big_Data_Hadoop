cp /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.7.2.jar .
./start-hadoop.sh
start-hbase.sh
hbase-daemon.sh start thrift

hdfs dfs -rm -r output
hdfs dfs -mkdir -p output

hdfs dfs -rm -r input
hdfs dfs -mkdir -p input
hdfs dfs -put dataw_fro03.csv input

hadoop jar hadoop-streaming-2.7.2.jar -file lot1_mapper_1.py -mapper "python3 lot1_mapper_1.py" -file lot1_reducer_1.py -reducer "python3 lot1_reducer_1.py" -input input/dataw_fro03.csv -output output/output_lot1_1

hadoop jar hadoop-streaming-2.7.2.jar -file lot1_mapper_2.py -mapper "python3 lot1_mapper_2.py" -file lot1_reducer_2.py -reducer "python3 lot1_reducer_2.py" -input input/dataw_fro03.csv -output output/output_lot1_2 

hadoop jar hadoop-streaming-2.7.2.jar -file lot1_mapper_3.py -mapper "python3 lot1_mapper_3.py" -file lot1_reducer_3.py -reducer "python3 lot1_reducer_3.py" -input input/dataw_fro03.csv -output output/output_lot1_3 

hadoop jar hadoop-streaming-2.7.2.jar -file lot2_mapper_1.py -mapper "python3 lot2_mapper_1.py" -file lot2_reducer_1.py -reducer "python3 lot2_reducer_1.py" -input input/dataw_fro03.csv -output output/output_lot2_1