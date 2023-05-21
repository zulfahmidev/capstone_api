import base64

from flask import Blueprint, jsonify, request

from app.models.User import User
from utils import Auth
from utils.Validator import Validator

user_route = Blueprint('user', __name__)

@user_route.route('/<id>', methods=['GET'])
@Auth.login_required
def show(id) :
    user = User.query.get(id)
    if user is not None :
        return jsonify(
            status=True,
            message='Data loaded successfully.'
        ), 200
    return jsonify(
        status=False,
        message='User not found.',
        data=user.as_dict()
    ), 404

@user_route.route('/<id>', methods=['PUT'])
@Auth.login_required
def update(id) :
    val = Validator(request.json, {
        'name': ['string'],
        'birth_date': ['string'],
        'phone': ['string', 'numeric'],
        'address': ['string'],
        'picture': ['string', 'base64'],
    })
    
    if val.validate() :
        user = User.query.get(id)
        
        if user is not None :
            keys = [
                'name', 'birth_date', 'phone', 'address', 'picture'
            ]
            for k in keys :
                if request.json.get(k) is not None :
                    setattr(user, k, request.json.get(k))
            user.save()
            return jsonify(
                status=True,
                message='Data succesfully updated.'
            ), 200
        return jsonify(
            status=False,
            message='User not found.'
        ), 404
    return jsonify(
        status=False,
        message='Invalid field.',
        errors=val.getErrors()
    ), 400
    