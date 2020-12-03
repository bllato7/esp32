
# blink the given pin at 1Hz 50% duty cycle
# use ctrl-c to end

# notify
print('LOAD: blinker.py')

import sys,time
from machine import Pin

def blink(pin=13):
    
    p = Pin(pin,Pin.OUT)

    try:

          while 1:
            p.value(1)
            print('pin',pin,'ON')
            time.sleep(0.5)
            p.value(0)
            print('pin',pin,'OFF')
            time.sleep(0.5)

    except:
        p.value(0)
        Pin(pin,Pin.IN)
        
