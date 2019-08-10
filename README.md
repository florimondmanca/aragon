# Aragon

Rule-based streaming data cleansing application written in Python. Runs on Apache Kafka _via_ [Faust](https://faust.readthedocs.io).

## Overview

Current features:

- Modern, type-annotated Python (3.7).
- Fully asynchronous execution.
- Docker-based execution.
- Database of rules.
- Scalable manager/worker architecture _via_ event sourcing.

Planned features:

- Efficient application of word-based and regex-based rules.
- Read from and output to Kafka topics.

## Installation

This project entirely runs inside [Docker](https://docs.docker.com/install/) and [Docker Compose](https://docs.docker.com/compose/), so make sure to have these installed.

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

You can interact with the `api` using any HTTP client, e.g. [HTTPie](https://httpie.org/):

```bash
http get localhost:8041/rules/
http post localhost:8041/rules/ pattern=batman
http get localhost:8041/rules/1
http delete localhost:8041/rules/1
```

Workers are notified of additions and removals of rules.
When creating or deleting a rule, an event is sent to the `rules` topic, which the `worker` consumes:

```bash
$ docker-compose logs -f worker
...
worker_1     | [2019-08-10 21:53:20,351: WARNING]: ADD @b'2': Rule(id=2, pattern='superman', is_regex=False)
worker_1     | [2019-08-10 21:53:41,595: WARNING]: REMOVE @b'2'
```

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
- `worker`: stream processing worker.

## Development

```
python -m venv venv
. venv/bin/activate
pip install -r requirements.txt
pip install -r aragon/api/requirements.txt
```
