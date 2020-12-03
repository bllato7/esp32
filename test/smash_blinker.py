print('LOAD: blinker.py')
import sys,time
from machine import Pin
def blink(pin=2):
    p = Pin(pin,Pin.OUT)
    try:
          while 1:
            p.value(1)
            time.sleep(1)
            p.value(0)
            time.sleep(1)
    except:
        p.value(0)
        Pin(pin,Pin.IN)
