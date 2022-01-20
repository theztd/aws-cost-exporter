FROM python:3.10-slim

COPY src /opt/src

WORKDIR /opt/src
CMD pip3 install -r /opt/src/requirements.txt


ENTRYPOINT ["/opt/src/main.py"]
