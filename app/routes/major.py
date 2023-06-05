from flask import Blueprint, jsonify, request
from app.models.Major import Major
from extensions import db
from utils.Validator import Validator
from utils import Auth

major_route = Blueprint('major', __name__)

@major_route.route('/', methods=['GET'])
def showAll() :
  val = Validator(request, {
    'search': ['string']
  })
  if not val.validate() :
    return jsonify(
      status=False,
      message='Invalid field.',
      errors=val.getErrors()
    ), 400
    
  majors = db.session.query(Major)
  search = request.json.get('search')
  if search is not None :
    majors = majors.filter(Major.name.like(f'%{search}%'))
  majors = [v.asDict() for v in majors.all()]
  return jsonify(
    status=True,
    message='Data loaded successfully.',
    data=majors
  ), 200
  
@major_route.route('/<id>', methods=['GET'])
def show(id) :    
  major = Major.query.get(id)
  if (major) :
    return jsonify(
      status=True,
      message='Data loaded successfully.',
      data=major.asDict()
    ), 200
  return jsonify(
    status=True,
    message='Major not found.',
  ), 404
  
# @major_route.route('/', methods=['POST'])
# def store() :
#   val = Validator(request, {
#     'name': ['required', 'string'],
#     'description': ['required', 'string'],
#   })
  
#   if not val.validate() :
#     return jsonify(
#       status=False,
#       message='Invalid field.',
#       errors=val.getErrors()
#     ), 400
  
#   major = Major(
#     name=request.json.get('name'),
#     description=request.json.get('description'),
#   )
  
#   return jsonify(
#     status=True,
#     message='Major successfully created.',
#     data=major.asDict()
#   ), 200
  
# @major_route.route('/<id>', methods=['PUT'])
# def update(id) :
#   val = Validator(request, {
#     'name': ['string'],
#     'description': ['string'],
#   })
  
#   if not val.validate() :
#     return jsonify(
#       status=False,
#       message='Invalid field.',
#       errors=val.getErrors()
#     ), 400
  
#   major = Major.query.get(id)
  
#   if major :
#     major.update({
#       'name':request.json.get('name').lower().strip() if request.json.get('name') else None,
#       'description':request.json.get('description'),
#     })
#     return jsonify(
#       status=True,
#       message='Major successfully updated.',
#       data=major.asDict()
#     ), 200
  
#   return jsonify(
#     status=False,
#     message='Major not found.',
#   ), 404
  
# @major_route.route('/<id>', methods=['DELETE'])
# def destroy(id) :
  
#   major = Major.query.get(id)
  
#   if major :
#     major.destroy()
#     return jsonify(
#       status=True,
#       message='Major successfully destroyed.',
#       data=major.asDict()
#     ), 200
  
#   return jsonify(
#     status=False,
#     message='Major not found.',
#   ), 404