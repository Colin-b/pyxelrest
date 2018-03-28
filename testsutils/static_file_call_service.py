from flask import Flask

app = Flask(__name__)


@app.route('/sub/static/file/call', methods=['GET'])
def get_static_file_call():
    return 'success'


def start_server(port):
    app.run(port=port)


if __name__ == '__main__':
    start_server(8954)
