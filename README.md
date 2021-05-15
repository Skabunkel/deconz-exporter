# deconz-exporter

A super simple and dirty prometheus exporter for deconz.

Currently only exports battery and Zigbee humidity, temperature and pressure.

```
Enviroment variables used to configure the exporter.
HOST_PORT       Sets port to expose the prometheus metrics on. default to 80  
DECONZ_PORT     Sets the port deconz is available on. default to 80  
DECONZ_URL      Sets the url deconz can be reached by. default is 'localhost'
DECONZ_TOKEN    Sets the token used in the deconz api. default is ''
UPDATE_INTERVAL Sets interval between updates in seconds, default is 10.0 seconds
```
