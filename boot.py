import network
import time
import rp2
import os

print("--- Boot ---")

rp2.country("AU")
network.country("AU")
network.hostname("MicroPython")

wlan = network.WLAN(network.STA_IF)
if not wlan.active():
    wlan.active(True)
wlan.connect("Darude LANstorm", key="Noodlez95@")

while not wlan.isconnected() and wlan.status() >= 0:
    print('.', end='')
    time.sleep(0.5)
print('')

print("Connected to WiFi")
print("IP: %s", wlan.ifconfig()[0])
