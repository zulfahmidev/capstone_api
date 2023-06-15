from flask import jsonify, Blueprint

home_route = Blueprint('home', __name__)
@home_route.route('/', methods=['GET'])
def home() :
  return jsonify(
    status=True,
    message="Welcome to Arahku backend service!"
  )