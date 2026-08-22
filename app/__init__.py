from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os

load_dotenv()

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    os.makedirs(app.instance_path, exist_ok=True)

    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'sistema_estoque')
    
    caminho_banco = os.path.join(app.instance_path, 'estoque.db')
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{caminho_banco}'
    
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    from app.routes import bp
    app.register_blueprint(bp)

    from app import models

    with app.app_context():
        db.create_all()

    return app