from extensions import db

class MyModel(db.Model) :
  
  def update(self, fields: dict) :
    for key in fields :
      setattr(self, key, fields[key])
    return self.save()
      
  def destroy(self) :
    db.session.delete(self)
    return db.session.commit()

  def save(self) :
    db.session.add(self)
    return db.session.commit()