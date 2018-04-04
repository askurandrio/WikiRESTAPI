"""Test for all application"""
#TODO: Rework this

import os
import unittest

import requests

from lib.db import make_sessionmaker


URI = 'http://127.0.0.1:80'
DB_PATH = 'sqlite:////opt/wikirestapi/db/sql.db'


class TestEndtoEnd(unittest.TestCase):
    """Test all application"""

    def setUp(self):
        if os.path.exists(DB_PATH):
            os.remove(DB_PATH)
        make_sessionmaker(DB_PATH) #TODO: Wrong creation of DB

    def test_add_page(self):
        """The page creation test"""
        params = {'title':'TITLE', 'text':'TEXT'}
        post_req = requests.post('{}/page'.format(URI), params=params)
        post_req.raise_for_status()
        page_id = post_req.json()['page_id']

        get_req = requests.get('{}/page/{}'.format(URI, page_id))
        get_req.raise_for_status()
        get_answ = get_req.json()
        self.assertEqual(get_answ['text'], params['text'])

        with self.assertRaises(Exception):
            requests.get('{}/page/{}'.format(URI, 10)).raise_for_status()

        req_get_all = requests.get('{}/page'.format(URI))
        req_get_all.raise_for_status()
        self.assertCountEqual([page_id], req_get_all.json()['page_ids'])


    def test_upd_page(self):
        """The page update test"""
        post_req = requests.post('{}/page'.format(URI),
                                 params={'title':'TITLE', 'text':'TEXT'})
        post_req.raise_for_status()
        page_id = post_req.json()['page_id']

        upd_params = {'title':'TITLE2', 'text':'TEXT2'}
        requests.put('{}/page/{}'.format(URI, page_id), params=upd_params).raise_for_status()

        get_req = requests.get('{}/page/{}'.format(URI, page_id))
        get_req.raise_for_status()
        self.assertEqual(get_req.json()['text'], upd_params['text'])

    @classmethod
    def tearDownClass(cls):
        if os.path.exists(DB_PATH):
            os.remove(DB_PATH)
        make_sessionmaker(DB_PATH)
