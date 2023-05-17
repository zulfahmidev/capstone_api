from flask import request, jsonify, Blueprint, render_template
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity, get_jwt, set_access_cookies, unset_jwt_cookies
from werkzeug.security import check_password_hash, generate_password_hash
from extensions import db, mail
from itsdangerous import URLSafeTimedSerializer
from flask_mail import Message

from app.models.User import User
# from middlewares.checkToken import token_required

from datetime import datetime, timedelta
import os

auth = Blueprint('auth', __name__)


# Register
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
# End Register

# Send Email Verification
def send_email_verify(email) :
    token = generate_verify_token(email)
    msg = Message(
        subject="Verify Email Address",
        recipients=[email],
        sender=os.getenv('MAIL_USERNAME'),
        html=render_template('verify_email.html', token=token)
    )
    mail.send(msg)
# End Send Email Verification

# Verify Email
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
# End Verify Email

# Login
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
        
        access_token = create_access_token(identity=user.id, fresh=True)
        response = jsonify(
            success=True,
            message="Your have succesfully logged in.",
            data= {
                "access_token": access_token
            }
        )
        set_access_cookies(response, access_token)
        return response, 200
    else :
        return jsonify(
            success=False,
            message="Login failed. Please check your credentials and try again.",
        ), 401
# End Login

# Me
@auth.route('/me', methods=['GET'])
@jwt_required()
def me() :
    user = User.query.filter_by(id=get_jwt_identity()).one_or_none()
    return jsonify(
        status=True,
        message="Data loaded successfully.",
        data=user.as_dict()
    )
# End Me

# Logout
@auth.route('/logout', methods=['POST'])
@jwt_required()
def logout() :
    # user = User.query.filter_by(id=get_jwt_identity()).one_or_none()
    response = jsonify(
        status=True,
        message="Successfully Logged Out."
    )
    unset_jwt_cookies(response)
    return response, 20
# End Logout

# Forgot Password
@auth.route('/forgot-password', methods=['POST'])
def forgotPassword() :
    email = request.json.get('email')
    user = User.query.filter_by(email = email).one_or_none()
    if user is not None :
        token = generate_verify_token(email)
        return jsonify(
            status=True,
            message="Token reset has been successfully generated.",
            body= {
                "reset_token": token
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
    try :
        email = verify_token(token)
    except :
        return jsonify(
            status=False,
            message='Token has been expired!.'
        ), 419
    password = request.json.get('password')
    user = User.query.filter_by(email=email).first()
    if user is not None :
        user.password = generate_password_hash(password)
        db.session.add(user)
        db.session.commit()
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
    serializer = URLSafeTimedSerializer(os.getenv('APP_KEY'))
    return serializer.dumps(email, salt=os.getenv('SECURITY_PASSWORD_SALT'))
# End Generate Verify Token

# Check Verify Token
def verify_token(token, expiration=3600) :
    serializer = URLSafeTimedSerializer(os.getenv('APP_KEY'))
    try :
        email = serializer.loads(
            token,
            salt=os.getenv['SECRET_PASSWORD_SALT'],
            max_age=expiration
        )
    except:
        return False
    return email
# End CHeck Verify Token