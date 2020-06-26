
import flask

from flask_socketio import SocketIO, send, emit

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

##Gestion de l'event générique 'message
@socketio.on('message')
def handle_message(message):
        print('message reçu: ' + message )
        send("Voici le message de retour")
        send("change page")

##Exemple d'event perso
def ack():
    print('message was received!')


@socketio.on('my event')
def handle_my_custom_event(json):
    emit('my response', json, callback=ack)

##Gestion de l'event perso 'slidechanged' (émis par le professeur)
@socketio.on('slidechanged')
def handle_slidechanged(index):
    print("yes, la slide est maintenant la slide numero : " + str(index))
    emit('update slide', index, broadcast=True)

##Gestion de l'évent perso 'sliderequest' (émis par un élève)
@socketio.on('sliderequest')
def handle_sliderequest():
    emit('sliderequest', broadcast=True)

##Lancement du serv
if __name__ == '__main__':
    APP.debug= True
    socketio.run(APP)



