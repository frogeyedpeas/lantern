from flask import Flask

app = Flask(__name__)


@app.route("/<int(signed=True):argument>")
def process(argument):
    return str(argument+1)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
