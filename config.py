import os
from datetime import timedelta
import secrets
from dotenv import set_key

class InitConfig() :

    def __init__(self, app) :
        # Set ENV
        # set_key('.env', 'APP_KEY', secrets.token_hex(16))
        # set_key('.env', 'JWT_KEY', secrets.token_hex(16))
        # set_key('.env', 'SECURITY_PASSWORD_SALT', secrets.token_hex(16))

        # Database Configuration
        db_config = {
            'host': os.getenv('DB_HOST'),
            'name': os.getenv('DB_NAME'),
            'user': os.getenv('DB_USER'),
            'pass': os.getenv('DB_PASS'),
            'port': os.getenv('DB_PORT'),
        }
        app.config['SQLALCHEMY_DATABASE_URI'] =\
            f'mysql://{db_config["user"]}:{db_config["pass"]}@{db_config["host"]}:{db_config["port"]}/{db_config["name"]}'
        
        # JWT Configuration
        app.config['JWT_KEY'] = os.getenv('JWT_KEY')
        app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(days=7)

        # Mail Configuration
        app.config['MAIL_SERVER'] = os.getenv('MAIL_SERVER')
        app.config['MAIL_PORT'] = os.getenv('MAIL_PORT')
        app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME')
        app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD')
        app.config['MAIL_USE_TLS'] = True
        app.config['MAIL_USE_SSL'] = False

        # Key Configuration
        app.config['SECRET_KEY'] = os.getenv("APP_KEY")
        app.config['SECURITY_PASSWORD_SALT'] = os.getenv('SECURITY_PASSWORD_SALT')