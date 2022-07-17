FROM python:3.8-slim-buster

WORKDIR /python-docker

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

ENV FLASK_IP=0.0.0.0
ENV FLASK_PORT=5000
ENV FLASK_APP=flaskPython.py

COPY . .

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
