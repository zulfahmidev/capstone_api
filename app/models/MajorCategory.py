from extensions import db
from datetime import datetime

class MajorCategory(db.Model) :
    
    __tablename__ = 'major_categories'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)

    def __init__(self, name: str) :
      self.name = name
      self.created_at = datetime.now()
      self.save()
    
    def destroy(self) :
      db.session.delete(self)
      db.session.commit()

    def save(self) :
      db.session.add(self)
      db.session.commit()
    
    def asDict(self) :
      return {
        "id": self.id,
        "name": self.name,
        "created_at": self.created_at,
      }