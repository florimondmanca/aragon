# Aragon

Scalable, fault-tolerant rule-based streaming data cleansing application for Apache Kafka, written in Python.

## Installation

This project entirely runs inside [Docker] and [Docker Compose], so make sure to have these installed.

Before starting Docker Compose, create and fill in the following `.env` file:

```bash
DATABASE_USER=...
DATABASE_PASSWORD=...
DATABASE_NAME=...
```

You should also run `chmod -R +x tools`.

## Usage

To start all services, run:

```bash
docker-compose up -d
```

After running this for the first time, run:

```bash
./tools/setup.sh
```

to setup Kafka topics and other resources.

You can interact with the API using any HTTP client, e.g. cURL or [HTTPie](https://httpie.org/):

```bash
http get localhost:8041/rules/
http post localhost:8041/rules/ pattern=batman
http get localhost:8041/rules/1
http delete localhost:8041/rules/1
```

When creating or deleting a rule, an event is sent to the `rules` topic.

To consume the rules topic for debugging purposes, run:

```bash
./tools/consume_rules.sh [--from-beginning]
```

## Reference

### Services

The `docker-compose.yml` file declares the following services:

- `zookeeper`: a Zookeeper instance (cluster metadata).
- `broker`: a Kafka broker.
- `db`: a PostgreSQL database.
- `api`: web API application (available at http://localhost:8041).

## Development

```
python -m venv venv
. venv/bin/activate
pip install -r requirements.txt
pip install -r api/requirements.txt
```

## Resources

_Resources used while building this project._

- [Building a streaming fraud detection system with Kafka and Python](https://blog.florimond.dev/building-a-streaming-fraud-detection-system-with-kafka-and-python)
- [In-Depth Summary of Apache Kafka](https://medium.com/@aozturk/kafka-guide-in-depth-summary-5b3cb6dbc83c)
- [Docker Compose with Named Volumes and Multiple Networks](https://sandro-keil.de/blog/docker-compose-with-named-volumes-and-multiple-networks/)
- [Python Uvicorn Alpine Docker image (Gist)](https://gist.github.com/Midnighter/6f848a1b2264fa453706284305673834)
