FROM python:3-alpine

RUN pip3 install prometheus-client

RUN adduser -u 2517 --no-create-home -D -s /sbin/nologin export-user

WORKDIR /srv/deconz-exporter

ADD deconz.py .
ADD main.py .

RUN chmod 750 -R /srv/deconz-exporter
RUN chown 2517:2517 -R /srv/deconz-exporter

ENV HOST_PORT 80
ENV DECONZ_PORT 80
ENV DECONZ_URL localhost
#ENV DECONZ_TOKEN
ENV UPDATE_INTERVAL 10.0

USER 2517:2517
ENTRYPOINT [ "python3", "main.py" ]