import base64
import imghdr
import io

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
        if rule == 'image' :
          if value is not None :
            if (not isBase64Image(value)) :
              self.errors.append(f'The {k} is not a Base64 Image.')
          
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