from flask import Flask, jsonify, redirect, request
import jwt
import datetime
import requests

app = Flask(__name__)

@app.route('/auth')
def get_token():
    redirect_uri = request.args.get('redirect_uri')
    token = jwt.encode({'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)}, 'secret').decode('unicode_escape')
    requests.post(redirect_uri, data={'id_token':token})
    return ''



def start_server(port):
    app.run(port=port)

if __name__ == '__main__':
    start_server(8947)