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

  print("Setting up the registry")
  registry = CollectorRegistry(namespace="environ_sensor")

  print("Setting up the Gauges")
  metric_humidity = Gauge("humidity", "Humidity (Relative)", registry=registry)
  metric_pressure = Gauge("pressure", "Barometric Pressure (Pascals)", registry=registry)
  metric_temperature = Gauge("temperature", "Temperature (Celsius)", registry=registry)

  print("Setting up the router")
  router = Router()
  router.register("GET", "/metrics", registry.handler)

  sensor = PiicoDev_BME280()

  print("Getting ready")
  while not ready:
    time.sleep(0.5)
    ready = wlan.active()

  print("Starting the server")
  while True:
    while not server:
      print("No server yet")
      server = start_http_server(8080, address=wlan.ifconfig()[0])
    print("Server ready")

    print("Getting the values")
    temperature, pressure, humidity = sensor.values() 

    print("Setting the Gauges")
    metric_humidity.set(humidity)
    metric_pressure.set(pressure)
    metric_temperature.set(temperature)

    print("Trying to accept a connection")
    try:
      server.accept(router)
      print("Accepted a connection")
    except OSError as err:
      print("Error accepting request: {}".format(err))
    except ValueError as err:
      print("Error parsing request: {}".format(err))

main()