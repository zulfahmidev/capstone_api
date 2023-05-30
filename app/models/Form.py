from extensions import db
from datetime import datetime

from app.models.Field import Field

class Form(db.Model) :
  
  __tablename__ = 'forms'
  
  id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.String(255), nullable=False, unique=True)
  description = db.Column(db.Text, nullable=True)
  created_at = db.Column(db.DateTime, nullable=False)
  
  def __init__(self, title: str, description: str) :
    self.title = title
    self.description = description
    self.created_at = datetime.now()
    self.save()
      
  def destroy(self) :
    db.session.delete(self)
    db.session.commit()
  
  def update(self, title: str, description: str) :
    self.title = title
    self.description = description
    self.save()

  def save(self) :
    db.session.add(self)
    db.session.commit()
  
  def asDict(self) :
    fields = [v.asDict() for v in Field.query.filter_by(form_id=self.id).all()]
    return {
      "id": self.id,
      "title": self.title,
      "description": self.description,
      "fields": fields
    }
  