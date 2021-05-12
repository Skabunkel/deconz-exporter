from prometheus_client import Gauge
import json

_gauges = {
  "battery": Gauge("deconz_sensor_battery", "Battery level of sensor in percent", ["manufacturer", "model", "name"]),
  "humidity": Gauge("deconz_sensor_humidity", "Humidity of sensor in percent", ["manufacturer", "model", "name", "type", "uid"]),
  "pressure": Gauge("deconz_sensor_pressure", "Air pressure in hectopascal (hPa)", ["manufacturer", "model", "name", "type", "uid"]),
  "temperature": Gauge("deconz_sensor_temperature", "Temperature of sensor in Celsius", ["manufacturer", "model", "name", "type", "uid"]),
};

def _extract_metric(metric, metricName, devider):
    value = float(metric['state'][metricName])/devider;

    _gauges[metricName].labels(
      manufacturer = metric['manufacturername'], 
      model=metric['modelid'], 
      name=metric['name'], 
      type=metric['type'],
      uid=metric['uniqueid'],
    ).set(value);
    

def extract_metrics(logger, request_content):
  metric_result = {};
  data = json.loads(request_content.decode('utf-8'));
  _extract_battery(data);

  for key in data:
    metric = data[key];

    if metric['type'] == 'ZHAHumidity':
      _extract_metric(metric, 'humidity', 100);
    elif metric['type'] == 'ZHATemperature':
      _extract_metric(metric, 'temperature', 100);
    elif metric['type'] == 'ZHAPressure':
      _extract_metric(metric, 'pressure', 1);



def _extract_battery(data):
  processed = set();

  for key in data:
    value = 0;
    metric = data[key];

    if metric['name'] in processed:
      continue;
    
    processed.add(metric['name']);
    config = metric['config'];

    if 'battery' in config:
      value = int(config['battery']);
    
    _gauges['battery'].labels(manufacturer = metric['manufacturername'], model=metric['modelid'], name=metric['name']).set(value);


