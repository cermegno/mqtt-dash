# mqtt-dash
Python scripts to subscribe to MQTT topic and create a dashboard with the readings. This is part of the Pied Piper training program. 

## MQTT Subscriber
- "mqtt-sub.py" tunes in to a configurable MQTT topic
- writes incoming messages to a configuration Redis database
- every student in the classroom specifies their name as the location
- only the latest values are kept in Redis

## MQTT Dashboard
 - "mqtt-dash" is a web app that you can push to Cloud Foundry. Don't forget to bind a Redis database to it
 - it reads all the values from the database
 - builds a table with all values using Boostrap CSS

## Additional resources
- Sample code for sensors with Raspberry PI and MQTT publisher can be found in the [IoT RPI](https://github.com/cermegno/iot-rpi)
- If the planned architecture uses EdgeXfoundry to filter data and to publish resulting MQTT messages you can find more examples at Jonas Werner [Blog](http://jonamiki.com/2019/03/26/tentacle-tales-from-tokyo/) and EdgeXfoundry related GitHub [repos](https://github.com/jonas-werner?tab=repositories)
