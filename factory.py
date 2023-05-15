from flask import Flask
import os
from dotenv import load_dotenv

from routes.auth import auth

from extensions import jwt, db

def createApp() :
    load_dotenv()

    app = Flask(__name__)
    app.config['JWT_KEY'] = os.getenv('JWT_KEY')

    db_host = os.getenv('DB_HOST')
    db_name = os.getenv('DB_NAME')
    db_user = os.getenv('DB_USER')
    db_pass = os.getenv('DB_PASS')
    db_port = os.getenv('DB_PORT')

    # print(f'mysql://{db_user}:{db_pass}@{db_host}:{db_port}/{db_name}')

    app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql://{db_user}:{db_pass}@{db_host}:{db_port}/{db_name}'

    db.init_app(app)
    jwt.init_app(app)

    app.register_blueprint(auth, url_prefix='/auth')

    return app