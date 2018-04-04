"""This module defines engine and session"""

import sqlalchemy

from ..config import DBPATH
from .classes import BASE


SESSIONMAKER = None


def get_session():
    """Get a DB session"""
    global SESSIONMAKER #pylint: disable=W0603
    if SESSIONMAKER is None:
        SESSIONMAKER = make_sessionmaker(DBPATH)
    return SESSIONMAKER()


def make_sessionmaker(dbpath):
    """Make a session"""
    engine = sqlalchemy.create_engine(dbpath)
    BASE.metadata.create_all(engine)
    return sqlalchemy.orm.sessionmaker(bind=engine)
