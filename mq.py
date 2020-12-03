from time import sleep
from umqtt.simple import MQTTClient
import random

SERVER = '192.168.0.15'  # MQTT Server Address (Change to the IP address of your Pi)
PORT = 1883
CLIENT_ID = 'MPU'
TOPIC = b'Tutorial'
USER = 'admin'
PASSWORD = 'admin'

client = MQTTClient(CLIENT_ID, SERVER, user=USER, password=PASSWORD)
client.connect()   # Connect to MQTT broker

def send():

    while True:
        try:
    # Confirm sensor results are numeric
            msg = (b'{}'.format(random.randint(1,9)))
            client.publish(TOPIC, msg)  # Publish sensor data to MQTT topic
            print(msg)

        except OSError:
            print('Failed to read sensor.')
        sleep(4)