FROM python:3.7-alpine

WORKDIR /usr/code

RUN set -eux \
  && apk add --no-cache --virtual .build-deps build-base \
  && pip install --upgrade pip setuptools wheel

ADD requirements.txt /usr/code
RUN pip install -r requirements.txt

ADD app /usr/code/

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
