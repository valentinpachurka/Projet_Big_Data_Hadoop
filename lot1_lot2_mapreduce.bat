cd 'C:\Users\lucie\Desktop\DIGINAMIC\14 - Projet Big Data\A tester dans Hadoop'

docker cp lot1_mapper_1.py hadoop-master:/root/
docker cp lot1_reducer_1.py hadoop-master:/root/
docker cp lot1_mapper_2.py hadoop-master:/root/
docker cp lot1_reducer_2.py hadoop-master:/root/
docker cp lot1_mapper_3.py hadoop-master:/root/
docker cp lot1_reducer_3.py hadoop-master:/root/
docker cp lot2_mapper_1.py hadoop-master:/root/
docker cp lot2_reducer_1.py hadoop-master:/root/
docker cp lot2_mapper_2.py hadoop-master:/root/
docker cp lot2_reducer_2.py hadoop-master:/root/

docker cp dataw_fro03.csv hadoop-master:/root/

docker cp lot1_lot2_mapreduce.sh hadoop-master:/root/
docker cp suite.sh hadoop-master:/root/

docker exec hadoop-slave1 /bin/bash -c './service_slv.sh'
docker exec hadoop-slave2 /bin/bash -c './service_slv.sh'
docker exec hadoop-master /bin/bash -c './lot1_lot2_mapreduce.sh'

docker cp '\\wsl.localhost\docker-desktop-data\data\docker\volumes\cge01\_data\data_2_1.csv' hadoop-master:/root/

docker exec hadoop-master /bin/bash -c './suite.sh'