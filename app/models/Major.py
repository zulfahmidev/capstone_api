from extensions import db
from datetime import datetime

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