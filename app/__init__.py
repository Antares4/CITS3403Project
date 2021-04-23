from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
db = SQLAlchemy()
migrate = Migrate()

def initapp():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    migrate.init_app(app, db)
    with app.app_context():
        db.create_all()
    from app.index import bp as index_bp
    app.register_blueprint(index_bp)

    from app.auth import bp as auth_bp
    app.register_blueprint(auth_bp)

    return app

from app import model
