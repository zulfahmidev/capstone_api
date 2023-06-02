from extensions import db
from datetime import datetime

class ResetPassword(db.Model) :
    
    __tablename__ = 'reset_passwords'
    
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), db.ForeignKey('users.email'), nullable=False)
    reset_token = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)

    def __init__(self, email: str, reset_token: str) :
      self.email = email
      self.reset_token = reset_token
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