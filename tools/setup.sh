set -x

exec docker-compose exec broker kafka-topics \
  --zookeeper zookeeper:2181 \
  --create \
  --replication-factor 1 \
  --partitions 1 \
  --topic rules \
  --config "cleanup.policy=compact"
