from flask import Blueprint, jsonify, request

from utils.Validator import Validator
from utils import Tests

from app.models.Form import Form
from app.models.Field import Field
from app.models.Option import Option
from app.models.Response import Response
from app.models.ResponseAnswer import ResponseAnswer

form_route = Blueprint('form', __name__)

# Get Form
@form_route.route('/', methods=['GET'])
def getAll() :
  forms = [{
    'id': v.id,
    'title': v.title,
    'slug': v.slug,
    'description': v.description, 
  } for v in Form.query.all()]
  return jsonify(
    status=True,
    message='Data loaded successfully.',
    data=forms
  ), 200
  
# Get One Form
# @form_route.route('/<id>', methods=['GET'])
# def get(id) :
#   form = Form.query.get(id)
#   if form :
#     return jsonify(
#       status=True,
#       message='Data loaded successfully.',
#       data=form.asDict()
#     ), 200
#   return jsonify(
#     status=False,
#     message='Form not found.',
#   ), 404
  
# Get One Form By Slug
@form_route.route('/<slug>', methods=['GET'])
def getBySlug(slug) :
  form = Form.query.filter_by(slug=slug).first()
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
# @form_route.route('/', methods=['POST'])
# def store() :
#   val = Validator(request, {
#     'title': ['required', 'string', 'unique:forms,title'],
#     'description': ['required', 'string'],
#   })
  
#   if not val.validate() :
#     return jsonify(
#       status=False,
#       message='Invalid field.',
#       errors=val.getErrors()
#     ), 400
  
#   form = Form(
#     title=request.json.get('title'),
#     description=request.json.get('description'),
#   )
#   return jsonify(
#     status=True,
#     message='Form successfully created.',
#     data=form.asDict()
#   ), 200

# Update Form
# @form_route.route('/<id>', methods=['PUT'])
# def update(id) :
#   val = Validator(request, {
#     'title': ['string', 'unchanged'],
#     'description': ['string'],
#   })
  
#   if not val.validate() :
#     return jsonify(
#       status=False,
#       message='Invalid field.',
#       errors=val.getErrors()
#     ), 400
  
#   form = Form.query.get(id)
  
#   if form :
#     form.update({
#       'title':request.json.get('title').lower().strip() if request.json.get('title') else None,
#       'description':request.json.get('description'),
#     })
    
#     return jsonify(
#       status=True,
#       message='Form successfully updated.',
#       data=form.asDict()
#     ), 200
    
#   return jsonify(
#     status=False,
#     message='Form not found.',
#   ), 404

# Delete Form
# @form_route.route('/<id>', methods=['DELETE'])
# def destroy(id) :
  
#   form = Form.query.get(id)
  
#   if form :
#     form.destroy()
    
#     return jsonify(
#       status=True,
#       message='Form successfully deleted.',
#       data=form.asDict()
#     ), 200
    
#   return jsonify(
#     status=False,
#     message='Form not found.',
#   ), 404

# Get Field
# @form_route.route('/field/<id>', methods=['GET'])
# def getField(id) :
#   field = Field.query.get(id)
#   if field :
#     return jsonify(
#       status=True,
#       message='Data loaded successfully.',
#       data=field.asDict()
#     ), 200
#   return jsonify(
#     status=False,
#     message='Field not found.',
#   ), 404

# Create Field
# @form_route.route('/field', methods=['POST'])
# def storeField() :
#   val = Validator(request, {
#     'label': ['required', 'string'],
#     'form_id': ['required', 'integer', f'exists: forms, id']
#   })
#   if not val.validate():
#     return jsonify(
#       status=False,
#       message='Invalid field.',
#       errors= val.getErrors()
#     ), 400
  
#   field = Field(
#     form_id=request.json.get('form_id'), 
#     label=request.json.get('label')
#   )
  
#   return jsonify(
#     status=True,
#       message='Field successfully created.',
#     data=field.asDict()
#   ), 200

# Update Field
# @form_route.route('/field/<id>', methods=['PUT'])
# def updateField(id) :
#   val = Validator(request, {
#     'label': ['required', 'string']
#   })
#   if not val.validate():
#     return jsonify(
#       status=False,
#       message='Invalid field.',
#       errors= val.getErrors()
#     ), 400
  
#   field = Field.query.get(id)
#   if field :
#     field.update({
#       'label': request.json.get('label').lower().strip() if request.json.get('label') else None
#     })
#     return jsonify(
#       status=True,
#       message='Field successfully updated.',
#       data=field.asDict()
#     ), 200
#   return jsonify(
#     status=False,
#     message='Field not found.',
#   ), 404

# Delete Field
# @form_route.route('/field/<id>', methods=['DELETE'])
# def destroyField(id) :
  
#   field = Field.query.get(id)
#   if field :
#     field.destroy()
#     return jsonify(
#       status=True,
#       message='Field successfully destroyed.',
#       data=field.asDict()
#     ), 200
#   return jsonify(
#     status=False,
#     message='Field not found.',
#   ), 404


# Get Option
# @form_route.route('/field/option/<id>', methods=['GET'])
# def getOption(id) :
#   option = Option.query.get(id)
#   if option :
#     return jsonify(
#       status=True,
#       message='Data loaded successfully.',
#       data=option.asDict()
#     ), 200
#   return jsonify(
#     status=False,
#     message='Option not found.',
#   ), 404
  
# Create Option
# @form_route.route('/field/option', methods=['POST'])
# def storeOption() :
#   val = Validator(request, {
#     'value': ['required', 'string'],
#     'field_id': ['required', 'integer', 'exists: fields, id']
#   })
#   if not val.validate():
#     return jsonify(
#       status=False,
#       message='Invalid field.',
#       errors= val.getErrors()
#     ), 400
  
#   option = Option(
#     field_id=request.json.get('field_id'), 
#     value=request.json.get('value')
#   )
  
#   return jsonify(
#     status=True,
#     message='Option successfully created.',
#     data=option.asDict()
#   ), 200

# Update Option
# @form_route.route('/field/option/<id>', methods=['PUT'])
# def updateOption(id) :
#   val = Validator(request, {
#     'value': ['required', 'string']
#   })
#   if not val.validate():
#     return jsonify(
#       status=False,
#       message='Invalid field.',
#       errors= val.getErrors()
#     ), 400
  
#   option = Option.query.get(id)
#   if option :
#     option.update({
#       'value': request.json.get('value').lower().strip() if request.json.get('value') else None
#     })
#     return jsonify(
#       status=True,
#       message='Option successfully updated.',
#       data=option.asDict()
#     ), 200
#   return jsonify(
#     status=False,
#     message='Option not found.',
#   ), 404

# Delete Option
# @form_route.route('/field/option/<id>', methods=['DELETE'])
# def destroyOption(id) :

#   option = Option.query.get(id)
#   if option :
#     option.destroy()
#     return jsonify(
#       status=True,
#       message='Option successfully destroyed.',
#       data=option.asDict()
#     ), 200
#   return jsonify(
#     status=False,
#     message='Option not found.',
#   ), 404

# Get Response
@form_route.route('/response/<form_id>', methods=['GET'])
def getResponse(form_id) :
  val = Validator(request, {
    'user_id': ['integer', 'exists:users,id']
  })
  if not val.validate():
    return jsonify(
      status=False,
      message='Invalid field.',
      errors= val.getErrors()
    ), 400
  res = Response.query.filter_by(form_id=form_id)
  
  if request.json.get('user_id') :
    res = res.filter_by(user_id=request.json.get('user_id'))
  responses = [v.asDict() for v in res.all()]
  return jsonify(
    status=True,
    message='Data loaded successfully.',
    data=responses
  ), 200
  
@form_route.route('/response', methods=['POST'])
def storeResponse() :
  val = Validator(request, {
    'user_id': ['required', 'integer', 'exists: users, id'],
    'form_id': ['required', 'integer', 'exists: forms, id'],
    'responses': ['required', 'array'],
  })
  if not val.validate():
    return jsonify(
      status=False,
      message='Invalid field.',
      errors= val.getErrors()
    ), 400
  
  response = Response(
    user_id=request.json.get('user_id'),
    form_id=request.json.get('form_id'),
  )
  res = request.json.get('responses')
  weights = []
  for v in res :
    option = Option.query.get(v['option_id'])
    weights.append(option.value)
    ResponseAnswer(
      response_id=response.id,
      option_id=v['option_id']
    )
  
  result = Tests.predictMajor([weights])[0]
  response.setResult(result)
  
  return jsonify(
    status=True,
    message='Response successfully sended.',
    data=response.asDict()
  ), 200
  
@form_route.route('/init/tests', methods=['GET'])
def intiTest() : 
  if Tests.init() :
    return jsonify(
      status=True,
      message='The tests form was successfully initiated.'
    ), 200
  return jsonify(
    status=False,
    message='Tests form failed to initialize.'
  ), 500
  