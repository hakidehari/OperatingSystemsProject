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
        user = json['user_name']
        w0t = mlfq.incrementMsgCount(user)
        if 'True' in w0t:
            socketio.emit('my response', json, callback=messageReceived)
        if 'False' in w0t:
            json['message'] = "You have reached your message limit.  This chat will now self destruct in 5 seconds."
            socketio.emit('my response', json, callback=messageReceived)
        if 'loweredPriority' in w0t:
            if mlfq.priority[user] == 4:
                json['message'] = "Your priority level is 4. These messages will now self destruct in 5 seconds."
                socketio.emit('my response', json, callback=messageReceived)
                json['message'] = "CLOSE"
                socketio.emit('my response', json, callback=messageReceived)
            else:
                json['message'] = "You have been lowered to priority level " + str(mlfq.priority[user]) + ".  Be careful or your messages will self destruct!"
                socketio.emit('my response', json, callback=messageReceived)




if __name__ == '__main__':
    socketio.run(app, debug=True)

