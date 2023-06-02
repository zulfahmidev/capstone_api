import os

def baseURL(uri) :
  return os.getenv('APP_URL') + "/" + uri

def StorageURL(filename) :
  return baseURL('storage/' + filename)