# python3.6

import random
import json
from paho.mqtt import client as mqtt_client
import threading
import time

broker = 'broker.emqx.io'
port = 1883
topic = "python/mmthesis"
# generate client ID with pub prefix randomly
client_id = f'python-mqtt-{random.randint(0, 100)}'
username = 'emqx'
password = 'public'
buffer = []

def connect_mqtt() -> mqtt_client:
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(client_id)
    client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client

def consumer():
    while (True):
        if (len(buffer)>0):
            print(buffer[-1])
            buffer.pop()
        time.sleep(3)

def subscribe(client: mqtt_client):
    # detectors objects
    def on_message(client, userdata, msg):
        global buffer
        msg = json.loads(msg.payload.decode())
        timestamp = msg["timestamp"]
        value = msg["value"]
        msg = {"timestamp":timestamp, "value":float(value)}
        buffer.append(msg)
        # runner(msg)

        
        #print (f"Anomaly Score : {anomalyScore}")
        # print (f"timestamp {timestamp}")
        # print (f"value {value}")

        #TODO call detector algorithm here

    client.subscribe(topic)
    client.on_message = on_message


def run():
    client = connect_mqtt()
    subscribe(client)
    client.loop_forever()


if __name__ == '__main__':
    buffer_processor = threading.Thread(target=run)
    buffer_processor.start()

    buffer_consumer = threading.Thread(target=consumer)
    buffer_consumer.start()
    buffer_consumer.join()
    