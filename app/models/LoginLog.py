from extensions import db
from datetime import datetime

class LoginLog(db.Model) :
    
    id = db.Column(db.Integer, primary_key=True)
    token_identifier = db.Column(db.Text, nullable=False)
    destroy_at = db.Column(db.DateTime, nullable=True)
    created_at = db.Column(db.DateTime, nullable=False)

    def __init__(self, token_identifier: str) :
      self.token_identifier = token_identifier
      self.created_at = datetime.now()
      self.save()
    
    def destroy(self) :
        self.destroy_at = datetime.now()
        self.save()

    def save(self) :
      db.session.add(self)
      db.session.commit()