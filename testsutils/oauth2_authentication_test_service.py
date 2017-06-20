import flask
import jwt
import datetime


app = flask.Flask(__name__)

already_asked_for_quick_expiry = [False]


@app.route('/auth_success')
def post_token():
    expiry_in_1_hour = datetime.datetime.utcnow() + datetime.timedelta(hours=1)
    return submit_token(expiry_in_1_hour)


@app.route('/auth_success_with_custom_response_type')
def post_token_with_custom_response_type():
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
        expiry_in_1_second = datetime.datetime.utcnow() + datetime.timedelta(seconds=1)
        return submit_token(expiry_in_1_second)


@app.route('/auth_timeout')
def post_token_after_client_timeout():
    return close_page()


def submit_token(expiry):
    redirect_uri = flask.request.args.get('redirect_uri')
    response_type = flask.request.args.get('response_type')
    token = jwt.encode({'exp': expiry}, 'secret').decode('unicode_escape')
    return """
<html>
    <body>
        <form method="POST" name="hiddenform" action="{0}">
            <input type="hidden" name="{1}" value="{2}" />
            <noscript>
                <p>Script is disabled. Click Submit to continue.</p>
                <input type="submit" value="Submit" />
            </noscript>
        </form>
        <script language="javascript">document.forms[0].submit();</script>
    </body>
</html>
        """.format(redirect_uri, response_type, token)


def submit_no_token():
    redirect_uri = flask.request.args.get('redirect_uri')
    return """
<html>
    <body>
        <form method="POST" name="hiddenform" action="{0}">
            <noscript>
                <p>Script is disabled. Click Submit to continue.</p>
                <input type="submit" value="Submit" />
            </noscript>
        </form>
        <script language="javascript">document.forms[0].submit();</script>
    </body>
</html>
        """.format(redirect_uri)


def close_page():
    return """
<html>
    <body onload="window.open('', '_self', ''); window.setTimeout(close, 1)">
    </body>
</html>
        """


def start_server(port):
    app.run(port=port)

if __name__ == '__main__':
    start_server(8947)
