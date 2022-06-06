from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/', methods=['GET'], strict_slashes=False)
def main3():
    return 'Server Running 2'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)