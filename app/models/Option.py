from extensions import db
from datetime import datetime

class Option(db.Model) :
  
  __tablename__ = 'options'
  
  id = db.Column(db.Integer, primary_key=True)
  field_id = db.Column(db.Integer, db.ForeignKey('fields.id', ondelete='CASCADE'))
  value = db.Column(db.String(255), nullable=False)
  weight = db.Column(db.Integer, nullable=False)
  created_at = db.Column(db.DateTime, nullable=False)
  
  def __init__(self, field_id: int, value: str, weight: int) :
    self.field_id = field_id
    self.value = value
    self.weight = weight
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
      "value": self.value,
      "weight": self.weight,
      # "field_id": self.field_id
    }
  