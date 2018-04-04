"""Unit tests of database modules"""

import unittest

from lib.db import Page, Change, make_sessionmaker


class TestPage(unittest.TestCase):
    """Test Page"""

    def test_add(self):
        """The page creation test"""
        session = make_sessionmaker('sqlite://')()
        session.add(Page())
        session.commit()
        self.assertNotEqual(session.query(Page).get(1), None)
        self.assertEqual(session.query(Page).get(2), None)
