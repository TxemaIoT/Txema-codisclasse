import cayenne.client
from random import randint
from time import sleep

def cayenne(valors):
    #nopasa=valors[0]
    sipasa=valors[1]
    #client.virtualwrite(1,nopasa)
    client.virtualwrite(2,sipasa)
   

def distancia():
    binario=randint(0,1)
    return binario


MQTT_USERNAME = "de520690-7c7b-11e9-ace6-4345fcc6b81e"
MQTT_PASSWORD = "7ee42ae57699c9a50dfaf16ae464485897e1237b"
MQTT_CLIENT_ID = "e9429fb0-7c7b-11e9-b4eb-6bf2c2412b24"
client = cayenne.client.CayenneMQTTClient()
client.begin(MQTT_USERNAME, MQTT_PASSWORD, MQTT_CLIENT_ID)


while True:
    client.loop()
    persones=0
    valors=distancia()
    for seconds in range(60):
        #persones=valors[0]
        persones +=1
    print(valors)
    Sleep(1)
    cayenne(valors)
     
