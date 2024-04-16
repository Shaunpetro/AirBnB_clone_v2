#!/usr/bin/python3
"""
the model instantitiates a obj of stroage depending on tpe
containing the model of all objects
"""
from os import getenv
from models.engine.db_storage import DBStorage
from models.engine.file_storage import FileStorage


if getenv('HBNB_TYPE_STORAGE') == 'db':
    storage = DBStorage()
else:
    storage = FileStorage()

sorage.reload()
