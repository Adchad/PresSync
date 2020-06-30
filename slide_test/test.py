
from flask import Flask, Response
import requests 
import os
from flask_socketio import SocketIO
from time import sleep
app = Flask(__name__)
SITE_NAME = 'https://perso.telecom-paristech.fr/dufourd/cours/'
socketio = SocketIO(app)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def proxy(path):

   r = requests.get(f'{SITE_NAME}{path}')
   return Response(r.content, status=r.status_code, content_type=r.headers['content-type'])

if __name__ == '__main__':
  app.run(host="0.0.0.0")
  socketio.run(app, host="0.0.0.0")
