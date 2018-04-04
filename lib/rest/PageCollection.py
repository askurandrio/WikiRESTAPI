"""This module defines the Page class"""

import flask_restful
from flask import request

from lib.db import get_session, Page, Change


class PageResource(flask_restful.Resource):
    """The REST endpoint for Page"""

    @staticmethod
    def post():
        """Create a new page"""
        session = get_session()
        page = Page()
        session.add(page)
        session.flush()
        change = Change(page_id=page.oid, title=request.args['title'], text=request.args['text'])
        session.add(change)
        session.commit()
        return {'page_id':page.oid}, 201

    @staticmethod
    def put(page_id):
        """Update the page"""
        session = get_session()
        page = session.query(Page).get(page_id)
        if page is None:
            return 'Page not found', 404
        change = Change(page_id=page.oid, title=request.args['title'], text=request.args['text'])
        session.add(change)
        session.flush()
        session.commit()
        return {'change_id':change.oid}, 200

    @staticmethod
    def get(page_id=None):
        """Get the page or pages id"""
        session = get_session()
        if page_id is None:
            page_ids = [page.oid for page in session.query(Page)]
            return {'page_ids': page_ids}

        page = session.query(Page).get(page_id)
        if page is None:
            return 'Page not found', 404

        change = session.query(Page, Change).\
                         filter(Change.page_id == page.oid).\
                         order_by(Change.oid.desc()).\
                         first()[1]
        return {'change_id':change.oid, 'title':change.title, 'text':change.text}
