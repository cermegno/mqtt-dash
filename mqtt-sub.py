import paho.mqtt.client as mqtt
import time
import redis
import json

# Choose the right Redis database
r = redis.Redis(host='127.0.0.1', port='6379')
#r = redis.Redis(host='myredis.in.pws.cloud', port='12345', password='secret')

# Select the right MQTT broker
#broker_address="127.0.0.1"
#broker_address="test.mosquitto.org"
broker_address="broker.hivemq.com"
# We will tune in to this MQTT topic
topic = "albpiper123"

# This tells where the readings are from
location = "Alberto"
print "Collecting data for location: " + location

def on_message(client, userdata, message):
    m = str(message.payload.decode("utf-8"))
    #print("- New message received: " + m)

    # Create a dictionary and extract the current values
    obj = json.loads(m)
    humidity = obj["readings"][0]["value"]
    temp = obj["readings"][1]["value"]

    # Write the received data to a database
    print "Temp: " + str(temp) + " - Humidity: " + str(humidity)
    r.hmset(location,{'temp':temp, 'humidity': humidity})
    # You can also use other Redis structures, ex: 
    #r.set('RPIvalue',m)

   # These are other things you can extract from the message
   #print("message topic=",message.topic)
   #print("message qos=",message.qos)
   #print("message retain flag=",message.retain)

print("Creating new instance ...")
client = mqtt.Client("sub1") #create new instance
client.on_message=on_message #attach function to callback
print("Connecting to broker ...")
client.connect(broker_address) #connect to broker

client.loop_start() #start the loop

while True:
    client.subscribe(topic) ### USE YOUR OWN TOPIC NAME
    time.sleep(1) # wait

client.loop_stop() #stop the loop

