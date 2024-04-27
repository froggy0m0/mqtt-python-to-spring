# app/mqtt_client.py
import paho.mqtt.client as mqtt
from config.settings import MQTT_BROKER_URL, MQTT_PORT

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

def on_publish(client, userdata, mid):
    print("Message Published.")

def setup_mqtt_client():
    # callback_api_version 인자를 제거하세요.
    client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION1)
    client.on_connect = on_connect
    client.on_publish = on_publish
    client.connect(MQTT_BROKER_URL, MQTT_PORT, 60)
    client.loop_start()  # 네트워크 루프를 시작합니다.
    return client

def publish_message(client, topic, message):
    client.publish(topic, message)
