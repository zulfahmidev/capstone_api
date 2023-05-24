from flask import Blueprint, jsonify, request
from app.models.Major import Major
from app.models.MajorCategory import MajorCategory
from extensions import db
from utils.Validator import Validator
from utils import Auth

major_route = Blueprint('major', __name__)

@major_route.route('/', methods=['GET'])
def show() :
  majors = db.session.query(Major).all()
  return jsonify(
    status=True,
    message='Data loaded successfully.',
    data=majors
  ), 200

@major_route.route('/category', methods=['GET'])
def showCategory() :
  categories = db.session.query(MajorCategory).all()
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
  
  category = MajorCategory(request.json.get('name').lower())
  return jsonify(
    status=True,
    message='Category successfully created.',
    data=category.asDict()
  ), 200