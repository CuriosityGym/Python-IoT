from machine import Pin
import time
light = Pin(2, Pin.OUT, value=1)

while 1:
    light.value(0)
    time.sleep(0.5)
    light.value(1)
    time.sleep(0.5)
