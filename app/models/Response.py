from extensions import db
from datetime import datetime

from app.models.User import User
from app.models.Form import Form
from app.models.ResponseAnswer import ResponseAnswer

class Response(db.Model) :
  
  __tablename__ = 'responses'
  
  id = db.Column(db.Integer, primary_key=True)
  user_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete='CASCADE'))
  form_id = db.Column(db.Integer, db.ForeignKey('forms.id', ondelete='CASCADE'))
  result = db.Column(db.String(255),  nullable=True)
  created_at = db.Column(db.DateTime, nullable=False)
  
  def __init__(self, user_id: int, form_id: int) :
    self.user_id = user_id
    self.form_id = form_id
    self.created_at = datetime.now()
    self.save()
  
  def setResult(self, result: str) :
    self.result = result
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
    user = User.query.get(self.user_id)
    form = Form.query.get(self.form_id)
    responses = [v.asDict() for v in ResponseAnswer.query.filter_by(response_id=self.id).all()]
    return {
      "id": self.id,
      "user_id": {
        "id": user.id,
        "name": user.name
      },
      "form_id": {
        "id": form.id,
        "title": form.title
      },
      "responses": responses,
      "result": self.result,
      "created_at": self.created_at
    }
  
    
  