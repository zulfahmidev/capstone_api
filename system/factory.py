from flask import Flask
import os
from dotenv import load_dotenv

from routes.auth import auth

from system.extensions import jwt, db, mgr, mail

def createApp() :
    load_dotenv()

    # template_dir=os.path.abspath('../templates')
    app = Flask(__name__, template_folder='../templates')

    # JWT Configuration
    app.config['JWT_KEY'] = os.getenv('JWT_KEY')

    # DB Configuration
    db_host = os.getenv('DB_HOST')
    db_name = os.getenv('DB_NAME')
    db_user = os.getenv('DB_USER')
    db_pass = os.getenv('DB_PASS')
    db_port = os.getenv('DB_PORT')
    app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql://{db_user}:{db_pass}@{db_host}:{db_port}/{db_name}'

    # Mail Configuration
    app.config['MAIL_SERVER'] = os.getenv('MAIL_SERVER')
    app.config['MAIL_PORT'] = os.getenv('MAIL_PORT')
    app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME')
    app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD')
    app.config['MAIL_USE_TLS'] = True
    app.config['MAIL_USE_SSL'] = False

    db.init_app(app)
    jwt.init_app(app)
    mgr.init_app(app, db)
    mail.init_app(app)

    app.register_blueprint(auth, url_prefix='/auth')

    return app