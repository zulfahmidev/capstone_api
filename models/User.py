from system.extensions import db
from sqlalchemy import Identity
from datetime import datetime
from werkzeug.security import generate_password_hash

class User(db.Model) :
    
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), unique=True, index=True)
    password = db.Column(db.String(255), nullable=False)
    birth_date = db.Column(db.DateTime, nullable=False)
    phone = db.Column(db.String(255), nullable=False)
    address = db.Column(db.String(255), nullable=False)
    email_verified = db.Column(db.Boolean, nullable=False, default=False)
    created_at = db.Column(db.DateTime, nullable=False)

    def __init__(self, name, email, password, birth_date, phone=None, address=None) :

        y, m, d = birth_date.split('-')

        self.name = name
        self.email = email
        self.password = generate_password_hash(password)
        self.birth_date = datetime(int(y), int(m), int(d))
        self.phone = phone
        self.address = address
        self.created_at = datetime.now()
