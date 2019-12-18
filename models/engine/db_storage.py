#!/usr/bin/python3
"""This is the database storage"""
from sqlalchemy import create_engine
import os

class DBStorage():
    """This is the class for DBStorage
    """
    __engine = None
    __session = None

    def __init__(self):
        """Instantiation of DBStorage class
        """
        MySQL_user = os.environ['HBNB_MYSQL_USER']
        MySQL_pwd = os.environ['HBNB_MYSQL_PWD']
        MySQL_host = os.environ['HBNB_MYSQL_HOST']
        MySQL_db = os.environ['HBNB_MYSQL_DB']
        MySQL_env = os.environ['HBNB_ENV']
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
            MySQL_user, MySQL_pwd, MySQL_host, MySQL_db), pool_pre_ping=True)
        Base.metadata.create_all(engine)
        if My_SQL_env == "test":
            MySQL_user.__table__.drop(engine)

    def all(self, cls=None):
        """Show all class objects in DBStorage or specified class if given
        """
        if cls:
            for key, value in
        else:
            return self.__objects
