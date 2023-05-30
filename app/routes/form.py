from flask import Blueprint, jsonify, request

from utils.Validator import Validator

from app.models.Form import Form
from app.models.Field import Field
from app.models.Option import Option
from app.models.Response import Response

form_route = Blueprint('form', __name__)

# Get Form
@form_route.route('/', methods=['GET'])
def index() :
  forms = [v.asDict() for v in Form.query.all()]
  return jsonify(
    status=True,
    message='Data loaded successfully.',
    data=forms
  ), 200
  
# Get One Form
@form_route.route('/<id>', methods=['GET'])
def show(id) :
  form = Form.query.get(id)
  if form :
    return jsonify(
      status=True,
      message='Data loaded successfully.',
      data=form.asDict()
    ), 200
  return jsonify(
    status=False,
    message='Form not found.',
  ), 404

# Create Form
@form_route.route('/', methods=['POST'])
def store() :
  val = Validator(request, {
    'title': ['required', 'string'],
    'description': ['required', 'string'],
  })
  
  if not val.validate() :
    return jsonify(
      status=False,
      message='Invalid field.',
      errors=val.getErrors()
    ), 400
  
  form = Form(
    title=request.json.get('title').lower(),
    description=request.json.get('description'),
  )
  return jsonify(
    status=True,
    message='Form successfully created.',
    data=form.asDict()
  ), 200

# Update Form
@form_route.route('/<id>', methods=['PUT'])
def update(id) :
  val = Validator(request, {
    'title': ['required', 'string'],
    'description': ['required', 'string'],
  })
  
  if not val.validate() :
    return jsonify(
      status=False,
      message='Invalid field.',
      errors=val.getErrors()
    ), 400
  
  form = Form.query.get(id)
  
  if form :
    form.update(
      title=request.json.get('title').lower(),
      description=request.json.get('description'),
    )
    
    return jsonify(
      status=True,
      message='Form successfully updated.',
      data=form.asDict()
    ), 200
    
  return jsonify(
    status=False,
    message='Form not found.',
  ), 404

# Delete Form
@form_route.route('/<id>', methods=['DELETE'])
def destroy(id) :
  
  form = Form.query.get(id)
  
  if form :
    form.destroy()
    
    return jsonify(
      status=True,
      message='Form successfully deleted.',
      data=form.asDict()
    ), 200
    
  return jsonify(
    status=False,
    message='Form not found.',
  ), 404

# Get Field

# Create Field

# Update Field

# Delete Field


# Get Option

# Create Option

# Update Option

# Delete Option


# Get Response

# Create Response