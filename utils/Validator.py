import base64
import imghdr
import io
import re
from flask import jsonify

from extensions import db
from datetime import datetime 

class Validator :
  
  def __init__(self, data, rules) :
    self.json = data.json
    self.files = data.files
    self.rules = rules
    self.errors = []
    
  def getErrors(self) :
    return self.errors
    
  def validate(self) :
    for k in self.rules :
      for rule in self.rules[k] :
        value = self.json.get(k)
        rule = rule.strip().split(':')
        key = rule[0]
        args = []
        if len(rule) > 1 :
          args = rule[1].replace(' ', '').split(',')
          
        if key == 'required' :
          if k not in self.files and value is None :
            self.errors.append(f'The {k} field is required.')
        elif key == 'integer' :
          if value is not None :
            if not isinstance(value, int):
              self.errors.append(f'The {k} is not am integer.')
        elif key == 'numeric' :
          if value is not None :
            if not value.isdigit():
              self.errors.append(f'The {k} does not contain a numeric value.')
        elif key == 'email' :
          if value is not None :
            if not is_valid_email(value):
              self.errors.append(f'The {k} does not contain a valid email address.')
        elif key == 'string' :
          if value is not None :
            if not isinstance(value, str):
              self.errors.append(f'The {k} is not a string.')
        elif key == 'base64' :
          if value is not None :
            try :
              base64.b64decode(value)
            except base64.binascii.Error :
              self.errors.append(f'The {k} is not in Base64 format.')
        elif key == 'boolean' :
          if value is not None :
            if not isinstance(value, bool) :
              self.errors.append(f'The {k} is not a boolean.')
        elif key == 'image' :
          if value is not None :
            if (not isBase64Image(value)) :
              self.errors.append(f'The {k} is not a Base64 Image.')
        elif key == 'date' :
          if value is not None :
            if (not is_valid_date(value, "%Y-%m-%d")) :
              self.errors.append(f'The {k} does not match the expected format YYYY-MM-DD.')
        elif key == 'exists' :
          if value is not None :
            res = exists(value, args[0], args[1])
            if (res is not True) :
              self.errors.append(f'The selected {k} is invalid.')
        elif key == 'lower' :
          if value is not None :
            if not isinstance(value, str):
              self.errors.append(f'The {k} is not a string.')
        else:
          self.errors.append(f'The \'{key}\' field does not exists.')
        
          
    return len(self.errors) == 0

def allowed_file(filename, exts = []) :
  return '.' in filename and \
    filename.rsplit('.', 1)[-1].lower() in exts
    
def isBase64Image(base64_image) :
  try :
    file = base64.b64decode(base64_image)
    img_type = imghdr.what(io.BytesIO(file))
    return img_type is not None
  except base64.binascii.Error :
    return False

def is_valid_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email) is not None
  
def is_valid_date(date_string, format):
    try:
        datetime.strptime(date_string, format)
        return True
    except ValueError:
        return False

def exists(val: str, tbl: str, fld: str) :
  models = {}
  
  for model in db.Model.__subclasses__():
    if isinstance(model, type) and issubclass(model, db.Model):
      models[model.__tablename__] = model
  
  metadata = db.metadata
  if tbl not in metadata.tables.keys() :
    return False
  
  if fld not in metadata.tables[tbl].columns.keys() :
    return False
  
  rec = db.session.query(models[tbl])\
    .filter(getattr(models[tbl], fld) == val)\
    .first()
  
  if rec is None :
    return False
  return True
