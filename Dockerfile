FROM python:3.7.8-slim

ENV PYTHONPATH /app

COPY cv_project/requirements.txt requirements/requirements.txt
RUN pip install -U pip && pip install -r requirements/requirements.txt

COPY src /app/src
COPY wsgi.py /app/wsgi.py
COPY bin /app/bin
COPY cv.json /app/cv.json
COPY app.py /app/app.py
COPY config.py /app/config.py
COPY commands.py /app/commands.py

WORKDIR /app

RUN useradd demo
USER demo

EXPOSE 8080

ENTRYPOINT ["bash", "/app/bin/run.sh"]
