import flask
from flask_socketio import SocketIO

# Create the application.
APP = flask.Flask(__name__)

socketio = SocketIO(APP)


@APP.route('/')
def index():
    """ Displays the index page accessible at '/'
    """
    return flask.render_template('PageMaître.html')


if __name__ == '__main__':
    APP.debug=True
    #APP.run()
    socketio.run(APP)






