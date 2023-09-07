cd 'C:\Users\lucie\Desktop\DIGINAMIC\14 - Projet Big Data\A tester dans Hadoop'

docker cp lot3.py hadoop-master:/root/lot3.py
docker cp dataw_fro03.csv hadoop-master:/root/dataw_fro03.csv 
docker cp lot3_hbase.sh hadoop-master:/root/

docker exec hadoop-master /bin/bash -c './lot3_hbase.sh'
