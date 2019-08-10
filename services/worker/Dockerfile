FROM python:3.7-alpine

WORKDIR /usr/code

ADD requirements.txt /usr/code

RUN set -eux && \
  apk add --no-cache postgresql-libs && \
  apk add --no-cache --virtual .build-deps build-base postgresql-dev && \
  pip install --upgrade pip setuptools wheel && \
  pip install -r requirements.txt --no-cache-dir && \
  apk --purge del .build-deps

ADD app /usr/code/

CMD ["faust", "-A", "app", "-L", "uvloop", "worker", "-l", "info", "--with-web", "-p", "8000"]
