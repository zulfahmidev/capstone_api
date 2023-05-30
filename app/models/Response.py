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
  option_id = db.Column(db.Integer, db.ForeignKey('options.id', ondelete='CASCADE'))
  created_at = db.Column(db.DateTime, nullable=False)
  
  def __init__(self, user_id: int, option_id: int) :
    self.user_id = user_id
    self.option_id = option_id
    self.created_at = datetime.now()
    self.save()
      
  def destroy(self) :
    db.session.delete(self)
    db.session.commit()
  
  def update(self, user_id: int, option_id: int) :
    self.user_id = user_id
    self.option_id = option_id
    self.save()

  def save(self) :
    db.session.add(self)
    db.session.commit()
  
  def asDict(self) :
    user = User.query.get(self.user_id)
    option = Option.query.get(self.option_id)
    field = Field.query.get(option.field_id)
    form = Form.query.get(field.form_id)
    return {
      "id": self.id,
      "user_id": {
        "id": user.id,
        "name": user.title
      },
      "form_id": {
        "id": form.id,
        "title": form.title
      },
      "field_id": {
        "id": field.id,
        "label": form.label
      },
      "option_id": {
        "id": option.id,
        "value": form.value
      },
      "created_at": self.created_at
    }
  