from time import sleep
from umqtt.simple import MQTTClient
import ujson
from machine import I2C, Pin, RTC
import mpu6050
import timestart



SERVER = '192.168.1.103'  # MQTT Server Address (Change to the IP address of your Pi)
PORT = 1883
CLIENT_ID = 'MPU'
TOPIC = b'test'
USER = 'admin'
PASSWORD = 'admin'

client = MQTTClient(CLIENT_ID, SERVER, user=USER, password=PASSWORD)
client.connect()   # Connect to MQTT broker

i2c = I2C(scl=Pin(22), sda=Pin(21))
acc = mpu6050.accel(i2c, "5432")
rtc = RTC()



def send(tim):

    while True:
        try:
    # Confirm sensor results are numeric
            vals = acc.get_values()
            print(vals)
            # vals["sensor_id"] = 5432
            # vals["timestamp"] = str(rtc.datetime())
            # msg = bytearray(str(vals),"utf8")
            # msg = ujson.loads(vals)
            
            client.publish(TOPIC, vals)  # Publish sensor data to MQTT topic


        except OSError:
            print('Failed to read sensor.')
        sleep(tim)