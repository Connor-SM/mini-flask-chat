from app import app, socketio
from flask import render_template, redirect, url_for


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


def messageReceived(methods=['GET', 'POST']):
    print('message was received!!!')


@socketio.on('my event')
def handle_my_custom_event(json, methods=['GET', 'POST']):
    print('received my event: ' + str(json))
    socketio.emit('my response', json, callback=messageReceived)
