from utils import URL
from extensions import db
from sqlalchemy import Identity
from datetime import datetime
from werkzeug.security import generate_password_hash

class User(db.Model) :
    
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), unique=True, index=True)
    picture = db.Column(db.String(255), nullable=True)
    password = db.Column(db.String(255), nullable=False)
    birth_date = db.Column(db.DateTime, nullable=False)
    phone = db.Column(db.String(255), nullable=False)
    address = db.Column(db.String(255), nullable=False)
    email_verified = db.Column(db.Boolean, nullable=False, default=False)
    created_at = db.Column(db.DateTime, nullable=False)

    def __init__(self, name, email, password, birth_date, phone=None, address=None) :

        y, m, d = birth_date.strip().split('-')

        self.name = name.strip().lower()
        self.email = email.strip().lower()
        self.password = generate_password_hash(password.strip())
        self.birth_date = datetime(int(y), int(m), int(d))
        self.phone = phone.strip()
        self.address = address.strip()
        self.created_at = datetime.now()
        self.save()
        

    def as_dict(self):
        picture = URL.StorageURL("default.jpg")
        if self.picture is not None :
            picture = URL.StorageURL('uploads/'+self.picture)
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "birth_date": self.birth_date,
            "phone": self.phone,
            "address": self.address,
            "picture": picture,
            "created_at": self.created_at,
        }
      
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