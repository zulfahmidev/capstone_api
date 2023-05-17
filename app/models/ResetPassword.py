from extensions import db
from datetime import datetime

class ResetPassword(db.Model) :
    
    id = db.Column(db.Integer, primary_key=True)
    reset_token = db.Column(db.Text, nullable=False)
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