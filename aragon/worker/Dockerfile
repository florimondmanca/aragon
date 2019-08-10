FROM python:3.7-alpine

WORKDIR /usr/code

ADD requirements.txt /usr/code/
RUN pip install -r requirements.txt
ADD aragon/ /usr/code/aragon/

CMD ["faust", "-A", "aragon.worker.app", "worker", "-l", "info", "--without-web"]
