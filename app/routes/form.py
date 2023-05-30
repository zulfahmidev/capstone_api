from flask import Blueprint, jsonify, request

from utils.Validator import Validator

from app.models.Form import Form
from app.models.Field import Field
from app.models.Option import Option
from app.models.Response import Response

form_route = Blueprint('form', __name__)

# Get Form
@form_route.route('/', methods=['GET'])
def getAll() :
  forms = [{
    'id': v.id,
    'title': v.title,
    'description': v.description, 
  } for v in Form.query.all()]
  return jsonify(
    status=True,
    message='Data loaded successfully.',
    data=forms
  ), 200
  
# Get One Form
@form_route.route('/<id>', methods=['GET'])
def get(id) :
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
@form_route.route('/field/<id>', methods=['GET'])
def getField(id) :
  field = Field.query.get(id)
  if field :
    return jsonify(
      status=True,
      message='Data loaded successfully.',
      data=field.asDict()
    ), 200
  return jsonify(
    status=False,
    message='Field not found.',
  ), 404

# Create Field
@form_route.route('/field', methods=['POST'])
def storeField() :
  val = Validator(request, {
    'label': ['required', 'string'],
    'form_id': ['required', 'integer', f'exists: forms, id']
  })
  if not val.validate():
    return jsonify(
      status=False,
      message='Invalid field.',
      errors= val.getErrors()
    ), 400
  
  field = Field(
    form_id=request.json.get('form_id'), 
    label=request.json.get('label').strip()
  )
  
  return jsonify(
    status=True,
      message='Field successfully created.',
    data=field.asDict()
  ), 200

# Update Field
@form_route.route('/field/<id>', methods=['POST'])
def updateField(id) :
  val = Validator(request, {
    'label': ['required', 'string']
  })
  if not val.validate():
    return jsonify(
      status=False,
      message='Invalid field.',
      errors= val.getErrors()
    ), 400
  
  field = Field.query.get(id)
  if field :
    return jsonify(
      status=True,
      message='Data loaded successfully.',
      data=field.asDict()
    ), 200
  return jsonify(
    status=False,
    message='Field not found.',
  ), 404

# Delete Field


# Get Option

# Create Option

# Update Option

# Delete Option


# Get Response

# Create Response