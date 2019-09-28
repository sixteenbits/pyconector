import paho.mqtt.client as mqtt
from pyKey import pressKey, releaseKey, press, sendSequence, showKeys

BROKER_URL = '172.26.27.102'
BROKER_PORT = 1883
TOPIC = 'jamtoday/vara'
CMD = {
    'l': izquierda,
    'r': derecha,
    'v': varazo
}


def izquierda():
    print('Izquierda')


def derecha():
    print('derecha')


def varazo():
    print('varazo')


# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe(TOPIC)


# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic + " " + str(msg.payload))
    CMD[msg]()
    '''
    if(msg == 'l'):
        print(msg)
    elif(msg):
        print(msg)
    else:
        print(msg)
    '''


client = mqtt.Client()  # crea el cliente
client.on_connect = on_connect  # setup cuando se inicia la conexion
client.on_message = on_message  # callback para cuando lee el topic

client.connect(BROKER_URL, BROKER_PORT, 60)
# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()
