# deconz-exporter

A super simple and dirty prometheus exporter for deconz.

"""
Enviroment variables used to configure the exporter.
HOST_PORT       Sets port to run the prometheus http server, default to 80  
DECONZ_PORT     Sets deconz port, if its not set it will, default to 80
DECONZ_URL      Sets deconz url, default is 'localhost'
DECONZ_TOKEN    Sets deconz token, default is ''
UPDATE_INTERVAL Sets interval between updates in seconds, default is 10.0 seconds
"""