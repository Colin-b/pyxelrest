import flask
import jwt
import datetime
import requests

app = flask.Flask(__name__)

already_asked_for_quick_expiry = [False]


@app.route('/auth_success')
def post_token():
    redirect_uri = flask.request.args.get('redirect_uri')
    expiry_in_1_hour = datetime.datetime.utcnow() + datetime.timedelta(hours=1)
    token = jwt.encode({'exp': expiry_in_1_hour}, 'secret').decode('unicode_escape')
    requests.post(redirect_uri, data={'id_token': token})
    return flask.redirect(redirect_uri)


@app.route('/auth_failure')
def post_without_token():
    redirect_uri = flask.request.args.get('redirect_uri')
    requests.post(redirect_uri, data={})
    return flask.redirect(redirect_uri)


@app.route('/auth_success_quick_expiry')
def post_token_quick_expiry():
    if already_asked_for_quick_expiry[0]:
        expiry_now = datetime.datetime.utcnow() + datetime.timedelta(hours=1)
    else:
        already_asked_for_quick_expiry[0] = True
        expiry_now = datetime.datetime.utcnow() - datetime.timedelta(hours=1)
    redirect_uri = flask.request.args.get('redirect_uri')
    token = jwt.encode({'exp': expiry_now}, 'secret').decode('unicode_escape')
    requests.post(redirect_uri, data={'id_token': token})
    return flask.redirect(redirect_uri)


def start_server(port):
    app.run(port=port)

if __name__ == '__main__':
    start_server(8947)
