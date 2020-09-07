from flask import flash, url_for, render_template
from flask_login import login_required
from werkzeug.utils import redirect
from flask_login import login_required, current_user
from app.models.base import  db
from app.models.gift import Gift
from app.models.wish import Wish
from app.libs.email import send_email

from app.spider.yushu_book import YuShuBook
from app.view_models.wish import MyWishes
from . import web

__author__ = '七月'


@web.route('/my/wish')
def my_wish():
    uid = current_user.id
    wishes_of_mine = Wish.get_user_wishes(uid)
    isbn_list = [wish.isbn for wish in wishes_of_mine]
    gift_count_list = Wish.get_gift_counts(isbn_list)
    view_model = MyWishes(wishes_of_mine, gift_count_list)
    return render_template('my_wish.html', wishes=view_model.gifts)


@web.route('/wish/book/<isbn>')
@login_required
def save_to_wish(isbn):
    yushu_book = YuShuBook()
    yushu_book.search_by_isbn(isbn)
    if current_user.can_save_to_list(isbn):
        with db.auto_commit():
            wish = Wish()
            wish.uid = current_user.id
            wish.isbn = isbn
            db.session.add(wish)
    else:
        flash('这本书已添加至你的赠送清单或已存在于你的心愿清单，请不要重复添加')
    return redirect(url_for('web.book_detail', isbn=isbn))

@login_required
@web.route('/satisfy/wish/<int:wid>')
def satisfy_wish(wid):
    wish = Wish.query.get_or_404(wid)
    gift = Gift.query.filter_by(uid = current_user.id, isbn = Wish.isbn).first()
    if not gift :
        flash('not added, please add')
    else:
        send_email(wish.user.email,
                  '有人像送你一本书','email/satisify_wish', wish = wish, gift = gift)
        flash('email sent and you will got a drift. ')
    return redirect(url_for('web.book_detail',isbn = wish.isbn))

@login_required
@web.route('/wish/book/<isbn>/redraw')
def redraw_from_wish(isbn):
    wish = Wish.query.filter_by(isbn = isbn, launched = False).first_or_404()
    with db.auto_commit():
        wish.delete()
    return redirect(url_for('web.my_wish'))
