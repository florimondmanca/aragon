FROM python:3.7-alpine

WORKDIR /usr/app

RUN set -eux \
  && apk add --no-cache --virtual .build-deps build-base \
  && pip install --upgrade pip setuptools wheel

ADD requirements.txt /usr/app
RUN pip install -r requirements.txt

ADD app.py /usr/app

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
