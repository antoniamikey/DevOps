from flask import Flask
from redis import Redis
import socket

app = Flask(__name__)
redis = Redis(host='redis', port=6379)

@app.route("/")
def hello_world():
    hostname = socket.gethostname()
    count = redis.incr('hits')
    return 'Hello World from {} ! I have been seen {} times.\n'.format(hostname, count)


if __name__ == '__main__':
      app.run(host='0.0.0.0', port=8080)