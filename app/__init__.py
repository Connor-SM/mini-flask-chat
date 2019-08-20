from flask import Flask
from flask_socketio import SocketIO
from config import Config
from flask_cors import CORS


app = Flask(__name__)
app.config.from_object(Config)

socketio = SocketIO(app)
CORS(app)

from app import routes
