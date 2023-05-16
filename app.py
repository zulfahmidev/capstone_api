import os
import secrets
from system.factory import createApp

app = createApp()

if __name__ == '__main__' :
    app.config['SECRET_KEY'] = os.getenv("APP_KEY")
    app.config['SECURITY_PASSWORD_SALT'] = secrets.SystemRandom().getrandbits(128)
    app.run(
        host='0.0.0.0',
        debug=os.getenv('APP_DEBUG'),
    )