import flask
import jwt
import datetime
import requests

app = flask.Flask(__name__)

already_asked_for_quick_expiry = [False]


@app.route('/auth_success')
def post_token():
    expiry_in_1_hour = datetime.datetime.utcnow() + datetime.timedelta(hours=1)
    return submit_token(expiry_in_1_hour)


@app.route('/auth_failure')
def post_without_token():
    return submit_no_token()


@app.route('/auth_success_quick_expiry')
def post_token_quick_expiry():
    if already_asked_for_quick_expiry[0]:
        expiry_in_1_hour = datetime.datetime.utcnow() + datetime.timedelta(hours=1)
        return submit_token(expiry_in_1_hour)
    else:
        already_asked_for_quick_expiry[0] = True
        expiry_in_5_seconds = datetime.datetime.utcnow() + datetime.timedelta(seconds=5)
        return submit_token(expiry_in_5_seconds)


def submit_token(expiry):
    redirect_uri = flask.request.args.get('redirect_uri')
    token = jwt.encode({'exp': expiry}, 'secret').decode('unicode_escape')
    return """
        <body onload="document.querySelector('#token_form').submit();">
            <form action="{0}" method="post" id="token_form">
                <input type="hidden" name="id_token" value="{1}" />
            </form>
        </body>
        """.format(redirect_uri, token)


def submit_no_token():
    redirect_uri = flask.request.args.get('redirect_uri')
    return """
        <body onload="document.querySelector('#token_form').submit();">
            <form action="{0}" method="post" id="token_form" />
        </body>
        """.format(redirect_uri)


def start_server(port):
    app.run(port=port)

if __name__ == '__main__':
    start_server(8947)
