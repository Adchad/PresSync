import flask #Serveur flask
import requests #Library de requêtes HTTP, pour obtenir nos pages HTML
from flask_socketio import SocketIO, send, emit, join_room #Toutes nos fonctions de sockets
import json #Pour le formattage des données

###########################
#Initialisation du serveur#
###########################
APP = flask.Flask(__name__)
socketio = SocketIO(APP)

#Données relatives à chaque room : adresse absolue, relative, et titre
site_list=[]
html_list=[]
title_list=["","","","","","","","","","","","","","","","",""]

#Fonction de slicing, pour récupérer les chemins relatifs des fichiers statics, au chargement d'une iframe#
#*********************************************************************************************************#
def prev_fold(url):
    L=url.split("/")
    L.pop()
    return "/".join(L)

def prev_pop(url):
    L=url.split("/")
    a = L.pop()
    return "/".join(L), a

#Fonctions de routage : grâce à l'application web APP de flask, on aiguille les pages distribuées par le serveur#
#***************************************************************************************************************#


#Page d'accueil
@APP.route('/')
def index():
    return flask.render_template('index.html')

#Page d'accueil des professeurs, de laquelle ils peuvent créer une room de présentation
@APP.route('/accueil_profs')
def profs():
    return flask.render_template('page_accueil_prof.html')

#Page d'accueil des élèves : ils voient les présentations en cours, et peuvent les rejoindre en cliquant
@APP.route('/accueil_eleves')
def eleves():
    return flask.render_template('page_accueil_eleves.html')


@APP.route('/student')
def student():
    return flask.render_template('student.html')


@APP.route('/room/<id>/')
def room1(id):

     return flask.render_template('room1.html',id=id,html_link=html_list[int(id)-1])

@APP.route('/room/student/<id>/')
def room1student(id):

     return flask.render_template('room1_student.html',id=id,html_link=html_list[int(id)-1])


#Routing de proxy
@APP.route('/proxy/<int:id>/<int:id2>/', defaults={'path': ''})
@APP.route('/proxy/<int:id>/<int:id2>/<path:path>')
def proxy(id,id2,path):
    site = site_list[id-1] + "/"
    r = requests.get(f'{site}{path}')
    print(site + path)
    return flask.Response(r.content, status=r.status_code, content_type=r.headers['content-type'])


@APP.route('/proxy/<int:id>/', defaults={'path': ''})
@APP.route('/proxy/<int:id>/<path:path>')
def proxy_root(id,path):
    site = prev_fold(site_list[id-1]) + "/"
    r = requests.get(f'{site}{path}')
    return flask.Response(r.content, status=r.status_code, content_type=r.headers['content-type'])


def change_page(page):
    send("change_page "+ page, broadcast= True)


#Fonctions de gestion des sockets : on décrit le comportement du serveur selon le nom de la socket reçue#
#*******************************************************************************************************#

##Gestion de l'event générique 'message' / utilisé pour le debug
@socketio.on('message')
def handle_message(message):
        print('message reçu: ' + message )
        send("Voici le message de retour")
        send("change page")

##Gestion de l'event perso 'my event' / utilisé pour le debug
@socketio.on('my event')
def handle_my_custom_event(json):
    emit('my response', json, callback=ack)

##Exemple d'event perso / pour la science
def ack():
    print('message was received!')




#Gestion de l'event perso 'slidechanged' (émis par le professeur) => Renvoie à toute la room le numéro de la nouvelle slide
@socketio.on('slidechanged')
def handle_slidechanged(data):
    index = data['index']
    room = data['room']
    print("yes, la slide est maintenant la slide numero : " + str(index))

    emit('update slide', index, room=room)

#Gestion de l'évent perso 'sliderequest' (émis par un élève) => Envoie à la room de sliderequest, pour atteindre le prof
@socketio.on('sliderequest')
def handle_sliderequest(room):
    print('loop')
    emit('sliderequest', room=room)

#Test de join de room, pour le debug
@socketio.on('join')
def on_join(room):
    join_room(room)
    print("room " + room + " entered")
    emit('messagetest', "room 1 gang !", room="1")
    emit('messagetest', "room 2 gang !", room="2")

#Gestion de la création d'une nouvelle room par un prof
@socketio.on('newroom')
def handle_newroom(url):
    site,html = prev_pop(url)
    site_list.append(site)
    html_list.append(html)
    print("room number : " + str(len(site_list)) + "room url : " + url )
    emit('newroomnumber' , str(len(site_list)))

@socketio.on('request_available_rooms')
def handle_request_available_rooms():
    emit('available_rooms',json.dumps(html_list))

#Le prof a appuyé sur 'quitter la room' : on renvoie "closed_room" à toute la room, ce qui les ramène à la page d'accueil
#on efface l'url de la room, ce qui permet de ne plus l'afficher aux élèves : elle n'est plus accessible
@socketio.on('quit_room')
def handle_quit_room(room):
    html_list[int(room)-1]="none"
    print("on travaille dans la room "+ room)
    emit("closed_room", room=room)

#Gestion de l'udpate du titre
@socketio.on('new_title')
def handle_new_title(data):
    title_list[int(data['room'])-1] = data['title']
    print(data['title'] + data['room'])
    emit("update_title", ( title_list[int(data['room'])-1], data['room']), broadcast=True)

#Lors de la connexion d'un élève, il demande le titre de sa présentation au serveur
@socketio.on('title_request')
def handle_title_request(room):
     emit("room_title", title_list[int(room)-1]  ,room=room)
     emit("update_title", ( title_list[int(room)-1], room), broadcast=True)




######################
#Lancement du serveur#
######################
if __name__ == '__main__':
    APP.debug= True
    socketio.run(APP)
