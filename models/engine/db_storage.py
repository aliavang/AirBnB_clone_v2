#!/usr/bin/python3
"""This is the database storage"""
from sqlalchemy import create_engine


class DBStorage():
    """This is the class for DBStorage
    """
    __engine = None
    __session = None

    def __init__(self):
        """Instantiation of DBStorage class
        """
        self.__engine = create_engine('mysql+mysqldb://HBNB_MY
