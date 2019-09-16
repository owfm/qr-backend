import sys
import pyqrcode
from flask import Flask, request, json
from flask_cors import CORS
from flask import jsonify
import logging
logging.getLogger().setLevel(logging.INFO)


app = Flask(
    __name__, static_url_path='https://qr-backend-stylus.herokuapp.com/static')
CORS(app)


@app.route('/test')
def test():
    return json_response('hello')


@app.route('/qr', methods=["POST"])
def generateQR():
    urls = generateQRcodes(request.json.get('data'))
    return json_response(urls)


def generateQRcodes(data):
    for datum in data:
        qr = pyqrcode.create(datum)
        qr.svg("static/{}.svg".format(datum), scale=6)
    return ["static/{}.svg".format(datum) for datum in data]


def json_response(payload, status=200):
    return (json.dumps(payload), status, {'content-type': 'application/json'})


if __name__ == '__main__':
    app.run(debug=True)
