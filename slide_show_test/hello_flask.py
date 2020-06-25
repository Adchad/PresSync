
import flask

from flask_socketio import SocketIO, send

APP = flask.Flask(__name__)
socketio = SocketIO(APP)

@APP.route('/')
def index():
    return flask.render_template('index.html')


@APP.route('/student')
def student():
    return flask.render_template('student.html')

#@APP.route('/hello/<name>/')
#def hello(name):

 #     return flask.render_template('hello.html', name=name)

def change_page(page):
    send("change_page "+ page, broadcast= True)

   
@socketio.on('message')
def handle_message(message):
        print('message reçu: ' + message )
        if(message[0:4] == "page"):
            change_page(message[5])

if __name__ == '__main__':
    APP.debug= True
    socketio.run(APP)
        


