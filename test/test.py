from flask import Flask, current_app

app = Flask(__name__)
#ctx = app.app_context()
#ctx.push()
with app.app_context():
    a = current_app
    d = current_app.config['DEBUG']
    print(d)
