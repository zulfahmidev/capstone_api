import os
import base64
import string
import random
import time
import magic

from google.cloud import storage

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = 'credentials.json'

storage = storage.Client()
bucket = storage.bucket(os.getenv('BUCKET_NAME'))

def getFile(filepath) :
  return bucket.blob(filepath)

def deleteFile(filepath) :
  try :
    blob = bucket.blob(filepath)
    blob.delete()
  except :
    return False

def fileExists(filepath) :
  return bucket.blob(filepath).exists()

def uploadFile(file_base64, dir = '') :
  
  # Konversi data base64 menjadi bytes
  file_bytes = base64.b64decode(file_base64)
  
  ext = get_file_extension(file_bytes) 
  filename = generateFilename() + '.' + ext
  
  # Simpan file ke cloud
  blob = bucket.blob(f'{dir}/{filename}')
  try :
    blob.upload_from_string(file_bytes)
    return blob
  except :
    return None
  
def get_file_extension(file_data):
  file_signature = magic.from_buffer(file_data, mime=True)
  return file_signature.split('/')[1]
  
def generateFilename() :
  timestamp = str(int(time.time()))
  random_chars = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
  return timestamp + '_' + random_chars