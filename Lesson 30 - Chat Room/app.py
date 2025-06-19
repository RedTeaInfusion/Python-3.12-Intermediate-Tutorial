from flask import Flask, render_template
from flask_socketio import SocketIO, send
from dotenv import load_dotenv
import os

load_dotenv()
app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('FLASK_SECRET_KEY')
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('chat.html')

@socketio.on('message')
def handle_message(msg):
    print(f'Message: {msg}')
    send(msg, broadcast=True)

def main():
    host = os.getenv('FLASK_HOST')
    port = int(os.getenv('FLASK_PORT'))
    socketio.run(app, host, port)

if __name__ == '__main__':
    main()