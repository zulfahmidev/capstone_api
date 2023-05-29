from extensions import db
from datetime import datetime
from app.models.MajorCategory import MajorCategory

class Major(db.Model) :
  
    __tablename__ = 'majors'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=False)
    id_category = db.Column(db.Integer, db.ForeignKey('major_categories.id'), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)
    
    def __init__(self, name: str, description: str, id_category: int) :
      self.name = name
      self.description = description
      self.id_category = id_category
      self.created_at = datetime.now()
      self.save()
      
    def destroy(self) :
      db.session.delete(self)
      db.session.commit()
    
    def update(self, name: str, description: str, id_category: int) :
      self.name = name
      self.description = description
      self.id_category = id_category
      self.save()

    def save(self) :
      db.session.add(self)
      db.session.commit()
      
    def getCategory(self) -> MajorCategory :
      return MajorCategory.query.get(self.id_category)
    
    def asDict(self) :
      return {
        "id": self.id,
        "name": self.name,
        "description": self.description,
        "category": self.getCategory().asDict(),
        "created_at": self.created_at,
      }