from extensions import db
from datetime import datetime

from app.models.User import User
from app.models.Form import Form
from app.models.Field import Field
from app.models.Option import Option

class ResponseAnswer(db.Model) :
  
  __tablename__ = 'response_answers'
  
  id = db.Column(db.Integer, primary_key=True)
  response_id = db.Column(db.Integer, db.ForeignKey('responses.id', ondelete='CASCADE'))
  option_id = db.Column(db.Integer, db.ForeignKey('options.id', ondelete='CASCADE'))
  created_at = db.Column(db.DateTime, nullable=False)
  
  def __init__(self, response_id: int, option_id: int) :
    self.response_id = response_id
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
    return {
      "id": self.id,
      "response_id": self.response_id,
      "option_id": self.option_id,
      "created_at": self.created_at
    }
  
    
  