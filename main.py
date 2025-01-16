import time
from prometheus_express.metric import Gauge
from prometheus_express.registry import CollectorRegistry
from prometheus_express.router import Router
from prometheus_express.server import start_http_server
from PiicoDev_BME280 import PiicoDev_BME280

print("--- Main ---")

def main():
  ready = False
  server = False

  registry = CollectorRegistry(namespace='environ_sensor')

  metric_humidity = Gauge('humidity', 'Humidity (Relative)', registry=registry)
  metric_pressure = Gauge('pressure', 'Barometric Pressure (Pascals)', registry=registry)
  metric_temperature = Gauge('temperature', 'Temperature (Celsius)', registry=registry)

  router = Router()
  router.register('GET', '/metrics', registry.handler)

  sensor = PiicoDev_BME280()

  while not ready:
    time.sleep(0.5)
    ready = wlan.active()

  while True:
    while not server:
      server = start_http_server(8080, address=wlan.ifconfig()[0])

    temperature, pressure, humidity = sensor.values() 

    metric_humidity.set(humidity)
    metric_pressure.set(pressure)
    metric_temperature.set(temperature)

    try:
      server.accept(router)
    except OSError as err:
      print('Error accepting request: {}'.format(err))
    except ValueError as err:
      print('Error parsing request: {}'.format(err))

main()