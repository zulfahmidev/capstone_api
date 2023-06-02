from flask import Blueprint, jsonify, request
from app.models.Major import Major
from app.models.MajorCategory import MajorCategory
from extensions import db
from utils.Validator import Validator
from utils import Auth

major_route = Blueprint('major', __name__)

@major_route.route('/', methods=['GET'])
def show() :
  majors = [v.asDict() for v in db.session.query(Major).all()]
  return jsonify(
    status=True,
    message='Data loaded successfully.',
    data=majors
  ), 200
  
@major_route.route('/', methods=['POST'])
def store() :
  val = Validator(request, {
    'name': ['required', 'string'],
    'description': ['required', 'string'],
    'id_category': ['required', 'integer', 'exists:major_categories,id'],
  })
  
  if not val.validate() :
    return jsonify(
      status=False,
      message='Invalid field.',
      errors=val.getErrors()
    ), 400
  
  major = Major(
    name=request.json.get('name'),
    description=request.json.get('description'),
    id_category=request.json.get('id_category'),
  )
  
  return jsonify(
    status=True,
    message='Major successfully created.',
    data=major.asDict()
  ), 200
  
@major_route.route('/<id>', methods=['PUT'])
def update(id) :
  val = Validator(request, {
    'name': ['string'],
    'description': ['string'],
    'id_category': ['integer', 'exists:major_categories,id'],
  })
  
  if not val.validate() :
    return jsonify(
      status=False,
      message='Invalid field.',
      errors=val.getErrors()
    ), 400
  
  major = Major.query.get(id)
  
  if major :
    major.update({
      'name':request.json.get('name').lower().strip() if request.json.get('name') else None,
      'description':request.json.get('description'),
      'id_category':request.json.get('id_category'),
    })
    return jsonify(
      status=True,
      message='Major successfully updated.',
      data=major.asDict()
    ), 200
  
  return jsonify(
    status=False,
    message='Major not found.',
  ), 404
  
@major_route.route('/<id>', methods=['DELETE'])
def destroy(id) :
  
  major = Major.query.get(id)
  
  if major :
    major.destroy()
    return jsonify(
      status=True,
      message='Major successfully destroyed.',
      data=major.asDict()
    ), 200
  
  return jsonify(
    status=False,
    message='Major not found.',
  ), 404

@major_route.route('/category', methods=['GET'])
def showCategory() :
  categories = [v.asDict() for v in db.session.query(MajorCategory).all()]
  return jsonify(
    status=True,
    message='Data loaded successfully.',
    data=categories
  ), 200

@major_route.route('/category', methods=['POST'])
def storeCategory() :
  val = Validator(request, {
    'name': ['required', 'string']
  })
  
  if not val.validate() :
    return jsonify(
      status=False,
      message='Invalid field.',
      errors=val.getErrors()
    ), 400
  
  category = MajorCategory(request.json.get('name'))
  return jsonify(
    status=True,
    message='Category successfully created.',
    data=category.asDict()
  ), 200

@major_route.route('/category/<id>', methods=['DELETE'])
def destroyCategory(id) :    
  category = MajorCategory.query.get(id)
  if category :
    category.destroy()
    return jsonify(
      status=True,
      message='Category successfully destroyed.',
      data=category.asDict()
    ), 200
  return jsonify(
    status=False,
    message='Category not found.',
  ), 404

@major_route.route('/category/<id>', methods=['PUT'])
def updateCategory(id) :
  val = Validator(request, {
    'name': ['string']
  })
  
  if not val.validate() :
    return jsonify(
      status=False,
      message='Invalid field.',
      errors=val.getErrors()
    ), 400
  
  category = MajorCategory.query.get(id)
  if category :
    category.update({
      'name':request.json.get('name').lower().strip() if request.json.get('name') else None
    })
    return jsonify(
      status=True,
      message='Category successfully updated.'
    ), 200
  return jsonify(
    status=False,
    message='Category not found.',
  ), 404