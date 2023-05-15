from flask import request, jsonify
from functools import wraps

from models.User import User
import os
import jwt

def token_required(f) :
    @wraps(f)
    def decorator(*args, **kwargs) :
        token = None
        if 'Authorization' in request.headers :
            token = request.headers['Authorization'].split(" ")[1]
        if not token:
            return jsonify(
                status=False,
                message='a valid token is missing'
            )
        try :
            data = jwt.decode(token, os.getenv('JWT_KEY'), algorithms=["HS256"])
            current_user = User.query.filter_by(username=data['username']).first()
        except Exception as e:
            print(e)
            return jsonify(
                status=False,
                message='token is invalid'
            )
        return f(current_user, *args, **kwargs)
    return decorator