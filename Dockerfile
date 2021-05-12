FROM python:3-alpine

RUN pip3 install prometheus-client

WORKDIR /srv/deconz-exporter

ADD deconz.py .
ADD main.py .

ENV HOST_PORT 80
ENV DECONZ_PORT 80
ENV DECONZ_URL localhost
#ENV DECONZ_TOKEN
ENV UPDATE_INTERVAL 10.0

ENTRYPOINT [ "python3", "main.py" ]