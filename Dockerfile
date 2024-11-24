FROM python:3.13

ENV CONTAINER_HOME=/var/www

WORKDIR $CONTAINER_HOME

COPY requirements.txt $CONTAINER_HOME/requirements.txt

RUN pip install -r $CONTAINER_HOME/requirements.txt

COPY . .
