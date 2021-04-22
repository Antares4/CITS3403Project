from flask import Flask
from config import Config

def initapp():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    from app.index import bp as index_bp
    app.register_blueprint(index_bp)

    return app