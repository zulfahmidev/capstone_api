import json
from app.models.Form import Form
from app.models.Field import Field
from app.models.Option import Option
from app.models.Major import Major

from extensions import db

import joblib
classifer = joblib.load("ml/major_classification/Model/model.pkl")

def init() :
  file_path = 'data/tests_form.json'
  metadata = db.metadata
  for tbl in ['forms', 'fields', 'options', 'majors'] :
    if tbl not in metadata.tables.keys() :
      return False
  with open(file_path, 'r') as file:
    tests = json.load(file)
    for test in tests :
      form = Form.query.filter_by(slug=test['slug']).first()
      if form is not None:
        form.destroy()
      form = Form(
        title=test['title'],
        description=test['description'],
      )
      for question in test['questions'] :
        field = Field(
          form_id=form.id,
          label=question['question']
        )
        # print(question['options'][1])
        for opt in question['options'] :
          # print(opt)
          option = Option(
            field_id=field.id,
            value=opt['value'],
            weight=opt['weight'],
          )  
      initMajors()
  return True

def predictMajor(data) :
  y_pred = classifer.predict(data)
  return y_pred

def initMajors() :
  file_path = 'data/majors.json'
  with open(file_path, 'r') as file:
    majors = json.load(file)['majors']
    for major in majors :
      m = Major.query.filter(Major.name.like(f'%{major}%')).first()
      if m is None:
        Major(
          name=major,
          description="-"
        )