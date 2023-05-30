from extensions import db
from datetime import datetime

from app.models.Option import Option

class Field(db.Model) :
  
  __tablename__ = 'fields'
  
  id = db.Column(db.Integer, primary_key=True)
  form_id = db.Column(db.Integer, db.ForeignKey('forms.id', ondelete='CASCADE'))
  label = db.Column(db.String(255), nullable=False)
  created_at = db.Column(db.DateTime, nullable=False)
  
  def __init__(self, form_id: int, label: str) :
    self.form_id = form_id
    self.label = label
    self.created_at = datetime.now()
    self.save()
      
  def destroy(self) :
    db.session.delete(self)
    db.session.commit()
  
  def update(self, form_id: int, label: str) :
    self.form_id = form_id
    self.label = label
    self.save()

  def save(self) :
    db.session.add(self)
    db.session.commit()
  
  def asDict(self) :
    options = [v.asDict() for v in Option.query.filter_by(field_id=self.id).all()]
    return {
      "id": self.id,
      "label": self.label,
      "form_id": self.form_id,
      "options": options
    }
  