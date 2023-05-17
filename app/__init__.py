from flask import Flask
import os
from dotenv import load_dotenv
from app.routes.auth import auth
from config import InitConfig
from extensions import db, mail, jwt, mgr

app = Flask(__name__, 
            template_folder='../templates',
            static_folder='app/static')

load_dotenv('.env')
InitConfig(app)

jwt.init_app(app)
db.init_app(app)
mail.init_app(app)
mgr.init_app(app, db)

app.register_blueprint(auth, url_prefix='/auth')