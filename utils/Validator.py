from flask_inputs import Inputs
from flask_inputs.validators import JsonSchema
import base64

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
        if rule == 'required' :
          if k not in self.files and value is None :
            self.errors.append(f'The {k} field is required.')
        if rule == 'numeric' :
          if value is not None :
            if not value.isdigit():
              self.errors.append(f'The {k} does not contain a numeric value.')
        if rule == 'string' :
          if value is not None :
            if not isinstance(value, str):
              self.errors.append(f'The {k} is not a string.')
        if rule == 'base64' :
          if value is not None :
            try :
              base64.b64decode(value)
            except base64.binascii.Error :
              self.errors.append(f'The {k} is not in Base64 format.')
        if rule == 'boolean' :
          if value is not None :
            if not isinstance(value, bool) :
              self.errors.append(f'The {k} is not a boolean.')
        
        # Masih bermasalah
        # if k not in self.files :
        #   file = self.files[k]
        #   if rule == 'image' :
        #     if file is not None :
        #       if not allowed_file(file.filename, [
        #         'png', 'jpg', 'jpeg', 'gif'
        #       ]) :
        #         self.errors.append(f'The {k} field is not an image.')
          
    return len(self.errors) == 0

def allowed_file(filename, exts = []) :
  return '.' in filename and \
    filename.rsplit('.', 1)[-1].lower() in exts