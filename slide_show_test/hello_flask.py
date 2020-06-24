
import flask

from flask_socketio import SocketIO, send

APP = flask.Flask(__name__)
socketio = SocketIO(APP)

@APP.route('/')
def index():
    return flask.render_template('index.html')



#@APP.route('/hello/<name>/')
#def hello(name):

 #     return flask.render_template('hello.html', name=name)


   
@socketio.on('message')
def handle_message(message):
        print('message reçu: ' + message )
        send("Voici le message de retour")
        send("change page")


if __name__ == '__main__':
    APP.debug= True
    socketio.run(APP)

