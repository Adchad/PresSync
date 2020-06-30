import flask 
import requests 
import os
from flask_socketio import SocketIO
from time import sleep
APP = flask.Flask(__name__)
SITE_NAME = 'https://perso.telecom-paristech.fr/dufourd/cours/'
socketio = SocketIO(APP)

@APP.route('/proxy/', defaults={'path': ''})
@APP.route('/proxy/<path:path>')
def proxy(path):

    r = requests.get(f'{SITE_NAME}{path}')
    return flask.Response(r.content, status=r.status_code, content_type=r.headers['content-type'])

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

if __name__ == '__main__':
  #APP.run(host="0.0.0.0")
    APP.debug = True
    socketio.run(APP, host="0.0.0.0")


