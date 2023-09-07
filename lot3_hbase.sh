stop-hbase.sh
./start-hadoop.sh
start-hbase.sh
hbase-daemon.sh stop rest
hbase-daemon.sh start thrift

cat <<CMDES | hbase shell
disable "dataw_fro03"
drop "dataw_fro03"
disable "Log_dataw_fro03"
drop "Log_dataw_fro03"
exit
CMDES

python3 lot3.py

hbase-daemon.sh stop thrift
hbase-daemon.sh start rest -p 9090