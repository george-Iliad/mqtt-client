import paho.mqtt.client as mqtt
import socket
import re
import time

broker = "mqtt.eclipseprojects.io"
port = 1883
topic = "upatras/AdvancedProgrammingTechniques/Ex3"


def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to MQTT Broker!")
    else:
        print("Failed to connect, return code %d\n", rc)

def on_message(client, userdata, msg):
    print(msg.topic + " " + str(msg.payload))


def catch_post_request():
    s = socket.socket()
    port = 12345
    post_request = ""
    s.bind(('127.0.0.1',port))
    print("Socket binded to",port)
    s.listen(5)
    print("Awaiting POST Request...")
    while True:
        c, addr = s.accept()
        print("Successfuly connected to", addr)
        post_request = c.recv(1024).decode()
        print("POST request received...")
        c.send(("POST received").encode())
        c.close()
        break
    return post_request

def extract_msg(post_request):
    return re.search("msg=(.+)",post_request).group(1)

msg = catch_post_request()

client = mqtt.Client("Client1")
client.connect(broker, port,60)
client.on_connect = on_connect
client.on_message = on_message

client.loop_start()
client.subscribe(topic)
print("Subscribed topic:", topic)
client.publish(topic, extract_msg(msg))
time.sleep(5)
client.loop_stop()
