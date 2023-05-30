import os
from app import app, db, mgr

if __name__ == '__main__' :
    with app.app_context():
        # Migrate the database
        if not os.path.exists('migrations') :
            os.system('flask db init')
        os.system('flask db migrate')
        os.system('flask db upgrade')

    app.run(debug=os.getenv('APP_DEBUG'), host=os.getenv('APP_HOST'))
