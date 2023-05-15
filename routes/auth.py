from flask import request, jsonify, Blueprint
from flask_jwt_extended import create_access_token
from werkzeug.security import generate_password_hash, check_password_hash
from extensions import db

from models.User import User
from middlewares.checkToken import token_required

import jwt
import os

auth = Blueprint('auth', __name__)

@auth.route('/register', methods=['POST'])
def register() :
    username = request.json.get('username').lower()
    password = request.json.get('password')

    print(password)

    user = User.query.filter_by(username = username).one_or_none()
    

    if user is not None :
        return jsonify(
            success=False,
            message='Username is exists'
        ), 403
    
    hash_password = generate_password_hash(password)
    user = User(username=username, password=hash_password)
    db.session.add(user)
    db.session.commit()

    return jsonify(
        success=True,
        message='User created',
    ), 201

@auth.route('/login', methods=['POST'])
def login() :
    username = request.json.get('username').lower()
    password = request.json.get('password')

    user = User.query.filter_by(username = username).one_or_none()

    if user is not None and check_password_hash(user.password, str(password)) :
        access_token = jwt.encode(
            {"username": user.username},
            os.getenv("JWT_KEY"),
            algorithm="HS256")

        return jsonify(
            success=True,
            message='User created',
            data=access_token
        ), 200
    else :
        return jsonify(
            success=False,
            message='Login failed',   
        ), 401
    
@auth.route('/me', methods=['GET'])
@token_required
def me(current_user) :
    return jsonify(
        status=True,
        message='',
        data=current_user.username
    )