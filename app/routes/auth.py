import os
import secrets

from flask import request, jsonify, Blueprint, render_template
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity, get_jti, get_jwt
from werkzeug.security import check_password_hash, generate_password_hash
from itsdangerous import URLSafeTimedSerializer
from flask_mail import Message
from datetime import datetime, timedelta

from extensions import db, mail
from app.models.User import User
from app.models.LoginLog import LoginLog
from app.models.ResetPassword import ResetPassword
from utils import Auth

from utils.Validator import Validator
from sqlalchemy.orm.exc import NoResultFound, MultipleResultsFound

auth = Blueprint('auth', __name__)

# Register
@auth.route('/register', methods=['POST'])
def register() :
    val = Validator(request, {
        'name': ['required', 'string'],
        'email': ['required', 'email'],
        'phone': ['required', 'numeric'],
        'address': ['required', 'string'],
        'birth_date': ['required', 'date'],
        'password': ['required', 'string'],
    })
    
    if not val.validate() :
        return jsonify(
        status=False,
        message='Invalid field.',
        errors=val.getErrors()
        ), 400
    
    name = request.json.get('name')
    email = request.json.get('email')
    phone = request.json.get('phone')
    address = request.json.get('address')
    birth_date = request.json.get('birth_date')
    password = request.json.get('password')

    user = User.query.filter_by(email = email).first()

    if user is not None :
        return jsonify(
            success=False,
            message='Email is already exists.'
        ), 400
    
    user = User(name, email, password, birth_date, phone, address)

    send_email_verify(user)

    return jsonify(
        success=True,
        message= 'Registration successful! Please check your mailbox for email verification',
    ), 201
# End Register

# Send Email Verification
def send_email_verify(user) :
    token = generate_verify_token(user.email)
    msg = Message(
        subject="Verify Email Address",
        recipients=[user.email],
        sender=os.getenv('MAIL_USERNAME'),
        html=render_template('verify_email.html', token=token, name=user.name)
    )
    mail.send(msg)
# End Send Email Verification

# Verify Email
@auth.route('/verify/<token>', methods=['GET'])
def verify_email(token):
    email = None
    try :
        email = verify_token(token)
        user = db.session.query(User).filter_by(email=email).one()
        if user.email_verified :
            return jsonify(
                status=False,
                message='Email Verified successfully.'), 400
        else :
            user.email_verified = True
            user.save()
            return jsonify(
                status=True,
                message='You have successfully verified your email!.'), 200
    except MultipleResultsFound:
        return jsonify(
            status=False,
            message='Something went wrong!.'
        ), 500
    except :
        return jsonify(
            status=False,
            message='Token has been expired!.'
        ), 419
# End Verify Email

# Login
@auth.route('/login', methods=['POST'])
def login() :
    val = Validator(request, {
        'email': ['required', 'email'],
        'password': ['required', 'string'],
    })
    
    if not val.validate() :
        return jsonify(
        status=False,
        message='Invalid field.',
        errors=val.getErrors()
        ), 400
        
    email = request.json.get('email').lower()
    password = request.json.get('password')

    user = User.query.filter_by(email = email).first()

    if user is not None and check_password_hash(user.password, str(password)) :
        if not bool(user.email_verified) :
            return jsonify(
                status=False,
                message="Please verify your email before logging in."
            ), 400
        
        access_token = create_access_token(identity=user.id, fresh=True)

        # Create Login Log
        LoginLog(get_jti(access_token))
        
        response = jsonify(
            success=True,
            message="Your have succesfully logged in.",
            data= {
                "access_token": access_token
            }
        )
        return response, 200
    else :
        return jsonify(
            success=False,
            message="Login failed. Please check your credentials and try again.",
        ), 401
# End Login

# Me
@auth.route('/me', methods=['GET'])
@Auth.login_required
def me() :
    user = User.query.filter_by(id=get_jwt_identity()).first()
    return jsonify(
        status=True,
        message="Data loaded successfully.",
        data=user.as_dict()
    )
# End Me

# Logout
@auth.route('/logout', methods=['POST'])
@Auth.login_required
def logout() :
    log = LoginLog.query.filter_by(token_identifier=get_jwt()['jti']).first()
    log.destroy()
    return jsonify(
        status=True,
        message="Successfully Logged Out."
    ), 20
# End Logout

# Forgot Password
@auth.route('/forgot-password', methods=['POST'])
def forgotPassword() :
    val = Validator(request, {
        'email': ['required', 'email'],
    })
    
    if not val.validate() :
        return jsonify(
        status=False,
        message='Invalid field.',
        errors=val.getErrors()
        ), 400
        
    email = request.json.get('email')
    user = User.query.filter_by(email=email).first()
    if user is not None :
        reset_token = secrets.token_hex(16)
        ResetPassword(email, reset_token)
        return jsonify(
            status=True,
            message="Token reset has been successfully generated.",
            data= {
                "reset_token": reset_token,
            }
        ), 200
    return jsonify(
        status=False,
        message="Account not found for the provided email."
    ), 400
# End Forgot Password

# Reset Password
@auth.route('/reset-password/<token>', methods=['POST'])
def resetPassword(token) :
    val = Validator(request, {
        'password': ['required', 'string'],
    })
    
    if not val.validate() :
        return jsonify(
        status=False,
        message='Invalid field.',
        errors=val.getErrors()
        ), 400
        
    rp = ResetPassword.query.filter_by(reset_token=token).first()
    if rp is not None :
        password = request.json.get('password')
        user = User.query.filter_by(email=rp.email).first()
        if user is not None :
            user.update({
                "password": generate_password_hash(password.strip())
            })
            rp.destroy()
            return jsonify(
                status=True,
                message='Password successfully changed.'
            ), 200
    return jsonify(
        status=True,
        message='Token is invalid.'
    ), 400
# End Reset Password

# Generate Verify Token
def generate_verify_token(email) :
    serializer = URLSafeTimedSerializer('secret_key')
    return serializer.dumps(email, salt='salt_key')
# End Generate Verify Token

# Check Verify Token
def verify_token(token, expiration=3600) :
    serializer = URLSafeTimedSerializer('secret_key')
    try :
        email = serializer.loads(
            token,
            salt='salt_key',
            max_age=expiration
        )
    except:
        return False
    return email
# End CHeck Verify Token
