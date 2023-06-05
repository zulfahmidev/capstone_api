from extensions import db
from datetime import datetime
from slugify import slugify

from app.models.Field import Field

class Form(db.Model) :
  
  __tablename__ = 'forms'
  
  id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.String(255), nullable=False, unique=True)
  slug = db.Column(db.String(255), nullable=False, unique=True)
  description = db.Column(db.Text, nullable=True)
  created_at = db.Column(db.DateTime, nullable=False)
  
  def __init__(self, title: str, description: str) :
    self.title = title.lower().strip()
    self.slug = slugify(self.title)
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
    fields = [v.asDict() for v in Field.query.filter_by(form_id=self.id).all()]
    return {
      "id": self.id,
      "title": self.title,
      "slug": self.slug,
      "description": self.description,
      "fields": fields,
      "created_at": self.created_at
    }
  