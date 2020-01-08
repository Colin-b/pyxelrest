import flask
import jwt
import datetime
import logging


logger = logging.getLogger(__name__)
app = flask.Flask(__name__)

already_asked_for_quick_expiry = [False]


@app.route('/auth_success')
def post_token():
    expiry_in_1_hour = datetime.datetime.utcnow() + datetime.timedelta(hours=1)
    return submit_a_form_with_a_token(expiry_in_1_hour, 'id_token')


@app.route('/auth_success_with_custom_token')
def post_token_as_my_custom_token():
    expiry_in_1_hour = datetime.datetime.utcnow() + datetime.timedelta(hours=1)
    return submit_a_form_with_a_token(expiry_in_1_hour, 'my_custom_token')


@app.route('/auth_success_without_response_type')
def post_token_as_token():
    expiry_in_1_hour = datetime.datetime.utcnow() + datetime.timedelta(hours=1)
    return submit_a_form_with_a_token(expiry_in_1_hour, 'token')


@app.route('/auth_failure')
def post_without_token():
    return submit_an_empty_form()


@app.route('/auth_success_quick_expiry')
def post_token_quick_expiry():
    response_type = flask.request.args.get('response_type')
    if already_asked_for_quick_expiry[0]:
        expiry_in_1_hour = datetime.datetime.utcnow() + datetime.timedelta(hours=1)
        return submit_a_form_with_a_token(expiry_in_1_hour, response_type)
    else:
        already_asked_for_quick_expiry[0] = True
        expiry_in_1_second = datetime.datetime.utcnow() + datetime.timedelta(seconds=1)
        return submit_a_form_with_a_token(expiry_in_1_second, response_type)


@app.route('/auth_timeout')
def close_page_so_that_client_timeout_waiting_for_token():
    return close_page()


def submit_a_form_with_a_token(token_expiry, response_type):
    redirect_uri = flask.request.args.get('redirect_uri')
    state = flask.request.args.get('state')
    token = jwt.encode({'exp': token_expiry}, 'secret').decode('unicode_escape')
    return f"""
<html>
    <body>
        <form method="POST" name="hiddenform" action="{redirect_uri}">
            <input type="hidden" name="{response_type}" value="{token}" />
            <input type="hidden" name="state" value="{state}" />
            <noscript>
                <p>Script is disabled. Click Submit to continue.</p>
                <input type="submit" value="Submit" />
            </noscript>
        </form>
        <script language="javascript">document.forms[0].submit();</script>
    </body>
</html>
        """


def submit_an_empty_form():
    redirect_uri = flask.request.args.get('redirect_uri')
    return f"""
<html>
    <body>
        <form method="POST" name="hiddenform" action="{redirect_uri}">
            <noscript>
                <p>Script is disabled. Click Submit to continue.</p>
                <input type="submit" value="Submit" />
            </noscript>
        </form>
        <script language="javascript">document.forms[0].submit();</script>
    </body>
</html>
        """


def close_page():
    return """
<html>
    <body onload="window.open('', '_self', ''); window.setTimeout(close, 1)">
    </body>
</html>
        """


def start_server(port):
    logger.info(f'Starting server on localhost:{port}')
    app.run(port=port)


if __name__ == '__main__':
    start_server(8947)
