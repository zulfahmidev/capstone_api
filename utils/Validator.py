import base64
import imghdr
import io
import re
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
        if rule == 'required' :
          if k not in self.files and value is None :
            self.errors.append(f'The {k} field is required.')
        if rule == 'integer' :
          if value is not None :
            if not isinstance(value, int):
              self.errors.append(f'The {k} is not am integer.')
        if rule == 'numeric' :
          if value is not None :
            if not value.isdigit():
              self.errors.append(f'The {k} does not contain a numeric value.')
        if rule == 'email' :
          if value is not None :
            if not is_valid_email(value):
              self.errors.append(f'The {k} does not contain a valid email address.')
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
        if rule == 'image' :
          if value is not None :
            if (not isBase64Image(value)) :
              self.errors.append(f'The {k} is not a Base64 Image.')
        if rule == 'date' :
          if value is not None :
            if (not is_valid_date(value, "%Y-%m-%d")) :
              self.errors.append(f'The {k} does not match the expected format YYYY-MM-DD.')
          
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