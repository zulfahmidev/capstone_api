import io

from flask import Blueprint, send_file
from utils import Storage, Auth

storage_route = Blueprint('storage', __name__)

@storage_route.route('/<filename>/view', methods=['GET'])
def view(filename) :
  blob = Storage.getFile(filename)
  if blob.exists() :
    content_type = blob.content_type
    image_data = blob.download_as_bytes()
    return send_file(io.BytesIO(image_data), mimetype=content_type, as_attachment=False, download_name=filename)