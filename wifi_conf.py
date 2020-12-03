import network
from machine import Pin
import sys,time
print('LOAD: wifi_conf.py')



def set_connection():
    p = Pin(2,Pin.OUT)

    try:
        print("Connecting . . . ")
        station = network.WLAN(network.STA_IF)
        station.active(True)
        # station.connect("CGA2121_yNeAyLJ", "VQpSMxzbYQgNjRmWBr")
        station.connect("blase", "AGLL7HKEB9")
        print("Connected")
        for i in range(0,4):
            p.value(1)
            time.sleep(1)
            print("ok")
            p.value(0)
            time.sleep(1)
    except:
        print("Connection failed")

        p.value(1)
        time.sleep(4)
        p.value(0)