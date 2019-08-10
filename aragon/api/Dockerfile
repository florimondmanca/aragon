FROM python:3.7-alpine

WORKDIR /usr/code

ADD requirements.txt /usr/code/
ADD aragon/api/requirements.txt /usr/code/aragon/api/
RUN set -eux && \
  apk add --no-cache postgresql-libs && \
  apk add --no-cache --virtual .build-deps build-base postgresql-dev && \
  pip install --upgrade pip setuptools wheel && \
  pip install -r requirements.txt -r aragon/api/requirements.txt --no-cache-dir && \
  apk --purge del .build-deps
ADD aragon/ /usr/code/aragon/

CMD ["faust", "-A", "aragon.api.app", "worker", "-l", "info", "-p", "8000"]
