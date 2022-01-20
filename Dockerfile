FROM python:3.10-slim

COPY src /opt/src

WORKDIR /opt/src
RUN pip3 install -r requirements.txt


ENTRYPOINT ["/opt/src/main.py"]
