from flask import Flask, request
from pymongo import MongoClient
from socket import gethostname
import time

mongo = MongoClient('mongodb://mongo:27017/')
db = mongo.k8sdb
app = Flask(__name__)

current_time_millis = lambda: int(round(time.time() * 1000))

@app.route("/")
def main():
    hostname = gethostname()
    time = current_time_millis()
    db.datasets.insert_one({"hostname" : hostname, "timestamp" : time})
    json = '{"message" : "This is a k8s get started app. hostname: %s"}' % gethostname()
    return json, 200, {"Content-Type" : "application/json"}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, threaded=True)
