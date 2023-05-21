import os

def baseURL(uri) :
  print(uri)
  return os.getenv('APP_URL') + "/" + uri