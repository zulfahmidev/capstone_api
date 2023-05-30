from flask import Flask
import os
from dotenv import load_dotenv
from app.routes.auth import auth
from app.routes.user import user_route
from app.routes.storage import storage_route
from app.routes.major import major_route
from app.routes.form import form_route
from config import InitConfig
from extensions import db, mail, jwt, mgr

import collections
collections.Iterable = collections.abc.Iterable

app = Flask(__name__)
# app.static_folder = 'static'

load_dotenv('.env')
InitConfig(app)

jwt.init_app(app)
db.init_app(app)
mail.init_app(app)
mgr.init_app(app, db)

app.register_blueprint(auth, url_prefix='/auth')
app.register_blueprint(storage_route, url_prefix='/storage')
app.register_blueprint(user_route, url_prefix='/user')
app.register_blueprint(major_route, url_prefix='/major')
app.register_blueprint(form_route, url_prefix='/form')