FROM python:3.7-alpine

COPY src /opt/src

WORKDIR /opt/src
CMD pip3 install -r requirements.txt


ENTRYPOINT ["/opt/src/main.py"]
