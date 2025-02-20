# # This file runs the Flask app
#
# from app import create_app
#
# app = create_app()
#
# if __name__ == '__main__':
#     app.run()



# run.py

from app import create_app, db

app = create_app()

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run()