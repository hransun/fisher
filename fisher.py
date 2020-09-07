import json

from flask import Flask, make_response, jsonify

from app import create_app
from app.libs.helper import is_isbn_or_key
from app.spider.yushu_book import YuShuBook
from app.web import book



app = create_app()


# some code from michael so that it actually works
#app.add_url_rule('/hello',view_func=hello)
if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=app.config['DEBUG'],threaded = True)


# copy + paste in the terminal: set FLASK_ENV=development     or      export FLASK_ENV=development