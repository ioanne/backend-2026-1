from flask import Flask

app = Flask(__name__)


@app.route('/')
def home():
    return 'Hola amigos!' # HTTP 200 OK

@app.route('/ifts')
def ifts():
    return 'Hola alumnos!' # HTTP 200 OK


# Fragmento de python para que no se ejecute el código app.run
# al import app.py desde otro lado.
if __name__ == '__main__':
    app.run(debug=True)
