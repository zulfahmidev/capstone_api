import os
import base64
import string
import random
import time

from google.cloud import storage

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = 'credentials.json'

storage = storage.Client()
bucket = storage.bucket(os.getenv('BUCKET_NAME'))

def getFile(filename) :
  return bucket.blob(filename)

def fileExists(filename) :
  return bucket.blob(filename).exists()

def uploadFile(file_base64) :
  
  # Konversi data base64 menjadi bytes
  file_bytes = base64.b64decode(file_base64)
  
  # Simpan file ke cloud
  blob = bucket.blob(generateFilename())
  try :
    blob.upload_from_string(file_bytes)
    return blob
  except :
    return None
  
def generateFilename() :
  timestamp = str(int(time.time()))
  random_chars = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
  return timestamp + '_' + random_chars