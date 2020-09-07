from flask import current_app, flash, url_for, render_template
from werkzeug.utils import redirect

from app.models.gift import Gift
from app.view_models.gift import MyGifts
from . import web
from flask_login import login_required, current_user
from app.models.base import  db
__author__ = '七月'


@web.route('/my/gifts')
@login_required
def my_gifts():
    uid = current_user.id
    gifts_of_mine = Gift.get_user_gifts(uid)
    isbn_list = [gift.isbn for gift in gifts_of_mine]
    wish_count_list = Gift.get_wish_counts(isbn_list)
    view_model = MyGifts(gifts_of_mine,wish_count_list)
    return render_template('my_gifts.html',gifts=view_model.gifts)


@web.route('/gifts/book/<isbn>')
def save_to_gifts(isbn):
    if current_user.can_save_to_list(isbn):
        with db.auto_commit():

            gift = Gift()
            gift.isbn = isbn
            gift.uid = current_user.id
            current_user.beans +=current_app.config['BEANS_UPLOAD_ONE_BOOK']
            db.session.add(gift)

    else:
        flash('this book already in the list , do not add it again')
    return redirect(url_for('web.book_detail', isbn=isbn))



@web.route('/gifts/<gid>/redraw')
def redraw_from_gifts(gid):
    pass



