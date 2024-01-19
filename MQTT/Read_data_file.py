import paho.mqtt.client as mqttClient
import time
from mysqlConnection import connectmysql
from filterData import filter_data
import json

# topic = 'v3/cdtc2@ttn/devices/eui-2cf7f12043307b86/up'
# broker_adrs = "eu1.cloud.thethings.network"
# ur = "cdtc2@ttn"
# passw = "NNSXS.JYBAYF5OBCQCZ4BZ2HK5VDSS7ABR4ZT3YD4KONI.FYBT6V3WS4LVN3OMQNYUFRS7MKRGHQ7IDHO4N4YNCHVKZO5WA2EA"

TOPIC = 'sensors/temperatuur'
Connected = False  # global variable for the state of the connection
broker_address = '127.0.0.1'  # Broker address
port = 1883  # Broker port
user = 'user1'  # Connection username
password = 'password'  # Connection password
client_id = "mqttx_c1b631ab"

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to broker")
        global Connected  # Use global variable
        Connected = True  # Signal connection

    else:
        print("Connection failed")

def on_message(client, userdata, message):

    payload = json.loads(message.payload)
    filterd_data = filter_data(payload)
    if len(filterd_data) > 0:
        connectmysql(filterd_data)

client = mqttClient.Client(client_id)  # create new instance
client.username_pw_set(user, password=password)  # set username and password
client.on_connect = on_connect  # attach function to callback
client.on_message = on_message  # attach function to callback
 
# client.tls_set(tls_version=mqttClient.ssl.PROTOCOL_TLS)
client.connect(broker_address, port=port)  # connect to broker
 
client.loop_start()  # start the loop

while Connected != True:  # Wait for connection
    time.sleep(0.1)
    # print('not connected')
 
client.subscribe(TOPIC)
 
try:
    while True:
        time.sleep(1)
 
except KeyboardInterrupt:
    print("exiting")
    client.disconnect()
    client.loop_stop()