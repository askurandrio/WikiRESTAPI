"""This module defines DB classes needed for application"""
#split this file?


import sqlalchemy
import sqlalchemy.ext.declarative


BASE = sqlalchemy.ext.declarative.declarative_base()


class Page(BASE):
    """This is the class for Pages in the DB"""
    __tablename__ = 'pages'
    oid = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)

    def __init__(self, oid=None):
        self.oid = oid


class Change(BASE):
    """This is the class for Changes in the DB"""
    __tablename__ = 'changes'
    oid = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    page_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey('pages.oid'),
                                nullable=False)
    title = sqlalchemy.Column(sqlalchemy.String)
    text = sqlalchemy.Column(sqlalchemy.Text)

    def __init__(self, oid=None, page_id=None, title=None, text=None):
        self.oid = oid
        self.page_id = page_id
        self.title = title
        self.text = text
