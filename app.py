import os
from factory import createApp

app = createApp()

if __name__ == '__main__' :
    app.config['SECRET_KEY'] = os.getenv("APP_KEY")
    app.run(
        host='0.0.0.0',
        debug=os.getenv('APP_DEBUG')
    )