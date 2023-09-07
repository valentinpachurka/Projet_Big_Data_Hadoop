./start-hadoop.sh
start-hbase.sh
hbase-daemon.sh start thrift

hdfs dfs -put data_2_1.csv input

hadoop jar hadoop-streaming-2.7.2.jar -file lot2_mapper_2.py -mapper "python3 lot2_mapper_2.py" -file lot2_reducer_2.py -reducer "python3 lot2_reducer_2.py" -input input/data_2_1.csv -output output/output_lot2_2 

exit