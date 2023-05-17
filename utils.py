from flask import jsonify
from flask_jwt_extended import verify_jwt_in_request, get_jwt
from functools import wraps
from extensions import db
from app.models.LoginLog import LoginLog

def login_required(fn) :
  @wraps(fn)
  def wrapper(*args, **kwargs) :
      verify_jwt_in_request()
      log = LoginLog.query.filter_by(token_identifier=get_jwt()['jti']).first()
      if log is not None :
        if log.destroy_at is None :
          return fn(*args, **kwargs)
        return jsonify(
            status=False,
            message="Invalid token."
        ), 401
      return jsonify(
          status=False,
          message="Invalid token."
      ), 401
  return wrapper