from flask import Flask, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)


@app.route('/', methods=['GET'], strict_slashes=False)
def main():
    return "Server Running with Kubernetes Ingress Test"


@app.route('/2', methods=['GET'], strict_slashes=False)
def main2():
    try:
        x = requests.get('http://192.168.49.2/server2/')
    except Exception as e:
        return jsonify({"error": str(e)})
    return jsonify({"no_error": str(x.text)})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)