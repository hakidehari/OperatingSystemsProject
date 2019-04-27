from flask import Flask, render_template
from flask_socketio import SocketIO
from MLFQ import MLFQ

app = Flask(__name__)
app.config['SECRET_KEY'] = 'vnkdjnfjknfl1232#'
socketio = SocketIO(app)
mlfq = MLFQ()

@app.route('/')
def sessions():
    return render_template('session.html')

def messageReceived(methods=['GET', 'POST']):
    print('message was received!!!')

@socketio.on('my event')
def handle_my_custom_event(json, methods=['GET', 'POST']):
    print('received my event: ' + str(json))
    if 'user_name' in json:
        print(json['user_name'])
    socketio.emit('my response', json, callback=messageReceived)

if __name__ == '__main__':
    socketio.run(app, debug=True)

