from flask import request, jsonify, Blueprint, render_template
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from werkzeug.security import check_password_hash
from system.extensions import db, mail
from itsdangerous import URLSafeTimedSerializer
from flask_mail import Message

from models.User import User
# from middlewares.checkToken import token_required

import jwt
import os

auth = Blueprint('auth', __name__)

@auth.route('/register', methods=['POST'])
def register() :
    name = request.json.get('name').lower()
    email = request.json.get('email').lower()
    phone = request.json.get('phone')
    address = request.json.get('address')
    birth_date = request.json.get('birth_date')
    password = request.json.get('password')

    user = User.query.filter_by(email = email).one_or_none()

    if user is not None :
        return jsonify(
            success=False,
            message='Email is already exists.'
        ), 400
    
    user = User(name, email, password, birth_date, phone, address)
    db.session.add(user)
    db.session.commit()

    send_email_verify(email)

    return jsonify(
        success=True,
        message= 'Registration successful! Please check your mailbox for email verification',
    ), 201

def send_email_verify(email) :
    token = generate_verify_token(email)
    msg = Message(
        subject="Verify Email Address",
        recipients=[email],
        sender=os.getenv('MAIL_USERNAME'),
        html=render_template('verify_email.html', token=token)
    )
    mail.send(msg)


@auth.route('/verify/<token>', methods=['GET'])
def verify_email(token):
    try :
        email = verify_token(token)
    except :
        return jsonify(
            status=False,
            message='Token has been expired!.'
        ), 419
    user = User.query.filter_by(email=email).one_or_none()
    if user.email_verified :
        return jsonify(
            status=False,
            message='Email Verified successfully.'), 400
    else :
        user.email_verified = True
        db.session.add(user)
        db.session.commit()
        return jsonify(
            status=True,
            message='You have successfully verified your email!.'), 200

@auth.route('/login', methods=['POST'])
def login() :
    email = request.json.get('email').lower()
    password = request.json.get('password')

    user = User.query.filter_by(email = email).one_or_none()

    if user is not None and check_password_hash(user.password, str(password)) :
        if not bool(user.email_verified) :
            return jsonify(
                status=False,
                message="Please verify your email before logging in."
            ), 400
        
        access_token = create_access_token(identity=user.id)
        return jsonify(
            success=True,
            message="Your have succesfully logged in.",
            data= {
                "access_token": access_token
            }
        ), 200
    else :
        return jsonify(
            success=False,
            message="Login failed. Please check your credentials and try again.",
        ), 401
    
@auth.route('/me', methods=['GET'])
@jwt_required()
def me() :
    user = User.query.filter_by(id=get_jwt_identity()).one_or_none()
    return jsonify(
        status=True,
        message="Data loaded successfully.",
        data=user.as_dict()
    )

def generate_verify_token(email) :
    serializer = URLSafeTimedSerializer(os.getenv('APP_KEY'))
    return serializer.dumps(email, salt=os.getenv('SECURITY_PASSWORD_SALT'))

def verify_token(token, expiration=3600) :
    serializer = URLSafeTimedSerializer(os.getenv('APP_KEY'))
    try :
        email = serializer.loads(
            token,
            salt=app.config['SECRET_PASSWORD_SALT'],
            max_age=expiration
        )
    except:
        return False
    return email