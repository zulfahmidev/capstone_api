from extensions import db
from datetime import datetime

from app.models.User import User
from app.models.Form import Form
from app.models.Field import Field
from app.models.Option import Option

class Response(db.Model) :
  
  __tablename__ = 'responses'
  
  id = db.Column(db.Integer, primary_key=True)
  user_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete='CASCADE'))
  form_id = db.Column(db.Integer, db.ForeignKey('forms.id', ondelete='CASCADE'))
  field_id = db.Column(db.Integer, db.ForeignKey('fields.id', ondelete='CASCADE'))
  option_id = db.Column(db.Integer, db.ForeignKey('options.id', ondelete='CASCADE'))
  created_at = db.Column(db.DateTime, nullable=False)
  
  def __init__(self, user_id: int, form_id: int, field_id: int, option_id: int) :
    self.user_id = user_id
    self.form_id = form_id
    self.field_id = field_id
    self.option_id = option_id
    self.created_at = datetime.now()
    self.save()
      
  def destroy(self) :
    db.session.delete(self)
    db.session.commit()
  
  def update(self, fields: dict = {}) :
    for field in fields :
      if fields[field] :
        setattr(self, field, fields[field])
    self.save()

  def save(self) :
    db.session.add(self)
    db.session.commit()
  
  def asDict(self) :
    user = User.query.get(self.user_id)
    option = Option.query.get(self.option_id)
    field = Field.query.get(self.field_id)
    form = Form.query.get(self.form_id)
    return {
      "id": self.id,
      "user_id": {
        "id": user.id,
        "name": user.name
      },
      "form_id": {
        "id": form.id,
        "title": form.title
      },
      "field_id": {
        "id": field.id,
        "label": field.label
      },
      "option_id": {
        "id": option.id,
        "value": option.value
      },
      "created_at": self.created_at
    }
  
    
  