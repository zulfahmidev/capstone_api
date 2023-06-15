from flask import request, jsonify, Blueprint, render_template

home = Blueprint('home', __name__)
@home.route('/', methods=['GET'])
def home() :
  return jsonify(
    status=True,
    message="Welcome to Arahku backend service!"
  )