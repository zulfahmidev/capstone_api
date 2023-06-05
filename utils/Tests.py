import json
from app.models.Form import Form
from app.models.Field import Field
from app.models.Option import Option

def init() :
  file_path = 'data/tests_form.json'
  with open(file_path, 'r') as file:
    tests = json.load(file)
    for test in tests :
      form = Form.query.filter_by(slug=test['slug']).first()
      if form is not None:
        continue
      form = Form(
        title=test['title'],
        description=test['description'],
      )
      for question in test['questions'] :
        field = Field(
          form_id=form.id,
          label=question['question']
        )
        for weight in question['weight'] :
          option = Option(
            field_id=field.id,
            value=weight
          ) 
      print('Tests Form berhasil di inisiasi')