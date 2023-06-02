import io

from flask import Blueprint, send_file, jsonify
from utils import Storage, Auth

storage_route = Blueprint('storage', __name__)

@storage_route.route('/<path:filepath>', methods=['GET'])
def view(filepath) :
  blob = Storage.getFile(filepath)
  if blob.exists() :
    content_type = blob.content_type
    image_data = blob.download_as_bytes()
    filename = filepath.split('/')[-1]
    return send_file(io.BytesIO(image_data), mimetype=content_type, as_attachment=False, download_name=filename)
  return jsonify(
    status=False,
    message='File not found.'
  )