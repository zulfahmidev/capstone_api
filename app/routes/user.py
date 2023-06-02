import base64

from flask import Blueprint, jsonify, request

from app.models.User import User
from utils import Auth
from utils.Validator import Validator
from utils import Storage

user_route = Blueprint('user', __name__)

@user_route.route('/<id>', methods=['GET'])
@Auth.login_required
def show(id) :
    user = User.query.get(id)
    if user is not None :
        return jsonify(
            status=True,
            message='Data loaded successfully.',
            data=user.as_dict()
        ), 200
    return jsonify(
        status=False,
        message='User not found.'
    ), 404

@user_route.route('/<id>', methods=['PUT'])
@Auth.login_required
def update(id) :
    val = Validator(request, {
        'name': ['string'],
        'birth_date': ['string', 'date'],
        'phone': ['string', 'numeric'],
        'address': ['string'],
        'picture': ['string', 'base64', 'image'],
    })
    
    if val.validate() :
        user = User.query.get(id)
        
        if user is not None :
            if user.picture is not None :
                Storage.deleteFile(user.picture)
            file = Storage.uploadFile(request.json.get('picture'), 'uploads')
            user.update({
                'picture': file.name,
                'name': request.json.get('name').lower().strip() if request.json.get('name') else None,
                'birth_date': request.json.get('birth_date'),
                'phone': request.json.get('phone'), 
                'address': request.json.get('address')   
            })
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
    