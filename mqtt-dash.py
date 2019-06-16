import redis
import os, json
from flask import Flask, render_template

if 'VCAP_SERVICES' in os.environ:
    VCAP_SERVICES = json.loads(os.environ['VCAP_SERVICES'])
    CREDENTIALS = VCAP_SERVICES["rediscloud"][0]["credentials"]
    r = redis.Redis(host=CREDENTIALS["hostname"], port=CREDENTIALS["port"], password=CREDENTIALS["password"])
else:
    r = redis.Redis(host='127.0.0.1', port='6379')

app = Flask(__name__)

@app.route('/')
def index():
    readings = []
    for each_key in r.keys('*'):
        newreading = {  "loc" : each_key ,
                        "tem" : r.hget(each_key,'temp') ,
                        "hum" : r.hget(each_key,'humidity')}
        readings.append(newreading)

    print readings
    response = render_template("readings.html", readings=readings)
    return response

if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0', port=int(os.getenv('PORT', '5000')), threaded=True)
