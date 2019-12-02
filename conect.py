import paho.mqtt.client as mqtt
from pyKey import press, pressKey, releaseKey
from time import sleep

BROKER_URL = 'localhost'
BROKER_PORT = 1883
TOPIC = 'jamtoday/vara'
CMD = {
    'l': 'LEFT',
    'r': 'RIGHT',
    'v': 'z'
}


# Funcion que se ejecuta al conectarse al broker MQTT
def conectado_al_broker(client, userdata, flags, rc):
    print('Conectado con resultado {}'.format(str(rc)))
    # Suscribirse al topic
    client.subscribe(TOPIC)


# Funcion que se ejecuta cuando se recibe un mensaje nuevo
def leer_mensaje_nuevo(client, userdata, msg):
    mensaje = msg.payload.decode('UTF-8')
    # print(msg.topic + " " + str(msg.payload))
    print(msg.topic + " " + mensaje)
    comando = CMD.get(mensaje, 'nanai de la china')
    print('tecla -> {}'.format(comando))
    # Pulsacion de teclado
    #press(comando, 1)
    pressKey(comando)
    sleep(0.125)
    releaseKey(comando)


client = mqtt.Client()  # crea el cliente
client.on_connect = conectado_al_broker  # setup cuando se inicia la conexion
client.on_message = leer_mensaje_nuevo  # callback para cuando lee el topic

client.connect(BROKER_URL, BROKER_PORT, 60)
# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()
