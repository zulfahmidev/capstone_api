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
    title=request.json.get('title'),
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
    'title': ['string'],
    'description': ['string'],
  })
  
  if not val.validate() :
    return jsonify(
      status=False,
      message='Invalid field.',
      errors=val.getErrors()
    ), 400
  
  form = Form.query.get(id)
  
  if form :
    form.update({
      'title':request.json.get('title').lower().strip() if request.json.get('title') else None,
      'description':request.json.get('description'),
    })
    
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
    label=request.json.get('label')
  )
  
  return jsonify(
    status=True,
      message='Field successfully created.',
    data=field.asDict()
  ), 200

# Update Field
@form_route.route('/field/<id>', methods=['PUT'])
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
    field.update({
      'label': request.json.get('label').lower().strip() if request.json.get('label') else None
    })
    return jsonify(
      status=True,
      message='Field successfully updated.',
      data=field.asDict()
    ), 200
  return jsonify(
    status=False,
    message='Field not found.',
  ), 404

# Delete Field
@form_route.route('/field/<id>', methods=['DELETE'])
def destroyField(id) :
  
  field = Field.query.get(id)
  if field :
    field.destroy()
    return jsonify(
      status=True,
      message='Field successfully destroyed.',
      data=field.asDict()
    ), 200
  return jsonify(
    status=False,
    message='Field not found.',
  ), 404


# Get Option
@form_route.route('/field/option/<id>', methods=['GET'])
def getOption(id) :
  option = Option.query.get(id)
  if option :
    return jsonify(
      status=True,
      message='Data loaded successfully.',
      data=option.asDict()
    ), 200
  return jsonify(
    status=False,
    message='Option not found.',
  ), 404
  
# Create Option
@form_route.route('/field/option', methods=['POST'])
def storeOption() :
  val = Validator(request, {
    'value': ['required', 'string'],
    'field_id': ['required', 'integer', 'exists: fields, id']
  })
  if not val.validate():
    return jsonify(
      status=False,
      message='Invalid field.',
      errors= val.getErrors()
    ), 400
  
  option = Option(
    field_id=request.json.get('field_id'), 
    value=request.json.get('value')
  )
  
  return jsonify(
    status=True,
    message='Option successfully created.',
    data=option.asDict()
  ), 200

# Update Option

# Delete Option


# Get Response

# Create Response