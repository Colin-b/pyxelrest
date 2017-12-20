from flask import Flask
import time

app = Flask(__name__)


@app.route('/swagger.json')
def swagger():
    # Do not respond to this call (simulate service down behind a reverse proxy)
    time.sleep(3600)


def start_server(port):
    app.run(port=port)


if __name__ == '__main__':
    start_server(8950)
