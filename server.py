import os
import json
from flask import Flask, request

app = Flask(__name__)


@app.get('/')
def hello():
    return json.dumps({
        "hello": "world",
        "remote_addr": request.remote_addr,
        "remote_addr_request_env": request.environ.get('REMOTE_ADDR', '<nothing>'),
        "http_x_real_ip": request.environ.get('HTTP_X_REAL_IP', '<nothing>'),
        "bottom text": os.environ.get("BOTTOM_TEXT", "nothing"),
    }, indent=4), 200


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
