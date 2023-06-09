from extensions import db
from datetime import datetime

class Major(db.Model) :
  
  __tablename__ = 'majors'
  
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(255), nullable=False)
  description = db.Column(db.Text, nullable=False)
  created_at = db.Column(db.DateTime, nullable=False)
  
  def __init__(self, name: str, description: str) :
    self.name = name.lower().strip()
    self.description = description
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
      "name": self.name,
      "description": self.description,
      "created_at": self.created_at,
    }