from flask import current_app


from app.spider.yushu_book import YuShuBook
from sqlalchemy import Column, String, Integer, ForeignKey, Boolean, desc,func
from sqlalchemy.orm import relationship
from app.models.base import Base,db


class Gift(Base):
    __tablename__ = 'gift'

    id = Column(Integer, primary_key=True)
    uid = Column(Integer, ForeignKey('user.id'), nullable=False)
    user = relationship('User')
    isbn = Column(String(15),nullable=False)
    launched = Column(Boolean, default=False)



    @classmethod
    def get_user_gifts(cls,uid):
        gifts = Gift.query.filter_by(uid=uid,launched=False).order_by(
            desc(Gift.create_time)).all()

        return gifts

    @classmethod
    def get_wish_counts(cls,isbn_list):
        count_list =db.session.query(func.count(Wish.id),Wish.isbn).filter(Wish.launched == False, Wish.isbn.in_(isbn_list),
                                      Wish.status ==1).group_by(
            Wish.isbn).all()

        count_list =[{'count':w[0],'isbn':w[1]} for w in count_list]
        return count_list




    @property
    def book(self):
        yushu_book = YuShuBook()
        yushu_book.search_by_isbn(self.isbn)
        return yushu_book.first

    @classmethod
    #@cache.memoize(timeout=600)
    def recent(cls):
        recent_gift = Gift.query.filter_by(launched=False).order_by(
            desc(Gift.create_time)).group_by(Gift.isbn).limit(
            current_app.config['RECENT_BOOK_PER_PAGE']).distinct().all()
        #view_model = GiftsViewModel.recent(gift_list)
        return recent_gift

    def is_yourself_gift(self, uid):
        if self.uid == uid:
            return True

    @property
    def book(self):
        yushu_book = YuShuBook()
        yushu_book.search_by_isbn(self.isbn)
        return yushu_book.first
'''
        # @classmethod
        # @cache.memoize(timeout=600)
        # def recent(cls):
        #     gift_list = cls.query.filter_by(launched=False).order_by(
        #         desc(Gift.create_time)).group_by(Gift.book_id).limit(
        #         current_app.config['RECENT_BOOK_PER_PAGE']).all()
        #     view_model = GiftsViewModel.recent(gift_list)
        #     return view_model
        
        '''

from app.models.wish import Wish
