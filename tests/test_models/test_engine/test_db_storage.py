#!/usr/bin/python3
"""test for db storage"""
from models.state import State
from models.engine.db_storage import DBStorage
import unittest
import MySQLdb
import pep8
import os


class TestDBStorage(unittest.TestCase):
    '''test the FileStorage'''

    @classmethod
    def setUp(self):
        """set up for test"""
        self.db = MySQLdb.connect(host="localhost",
                                  port=3306,
                                  user='hbnb_test',
                                  passwd='hbnb_test_pwd',
                                  db='hbnb_test_db',
                                  charset='utf8')
        self.cur = self.db.cursor()
        self.storage = DBStorage()
        self.storage.reload()

    @classmethod
    def tearDown(self):
        """at the end of the test this will tear it down"""
        self.cur.close()
        self.db.close()

    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') != 'db', 'db')
    def test_pep8_DBStorage(self):
        """Tests pep8 style"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/engine/db_storage.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

if __name__ == "__main__":
    unittest.main()
