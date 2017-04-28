import flask
import jwt
import datetime
import requests

app = flask.Flask(__name__)


@app.route('/auth_success')
def post_token():
    redirect_uri = flask.request.args.get('redirect_uri')
    expiry_in_1_hour = datetime.datetime.utcnow() + datetime.timedelta(hours=1)
    token = jwt.encode({'exp': expiry_in_1_hour}, 'secret').decode('unicode_escape')
    requests.post(redirect_uri, data={'id_token': token})
    return ''


@app.route('/auth_failure')
def post_without_token():
    redirect_uri = flask.request.args.get('redirect_uri')
    requests.post(redirect_uri, data={})
    return ''


def start_server(port):
    app.run(port=port)

if __name__ == '__main__':
    start_server(8947)
