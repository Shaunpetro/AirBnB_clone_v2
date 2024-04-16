#!/usr/bin/python3
"""Defines the FileStorage class for hbnb clone."""
import json


class FileStorage:
    """Class manages storage for hbnb models in JSON Format"""
    __file_path = 'file.json'
    __object = {}

    def all(self, cls=None):
        """Returns a dictionary of models to curent storeage"""
        filtered_by_class = {}
        if cls:
            for key, value in FileStorage.__objects.items():
                if value.__class__ == cls:
                    filtered_by_class[key] = value
            return filtered_by_class
        return FileStorage.__objects

    def new(self, obj):
        """Adss a new obj to storage dictionary"""
        self.all().update({obj.to_dict()['__class__'] + '.' + obj.id: obj})

    def save(self):
        """Save storage dict to file"""
        with open(FileStorage.__file_path, 'w') as f:
            temp = {}
            temp.update(FileStorage.__objects)
            for key, val in temp.items():
                temp[key] = val.to_dict()
            json.dump(temp, f)

    def reload(self):
        """loads the storage dict from file"""
        from models.base_model import BaseModel
        from models.amenity import Amenity
        from models.city import City
        from models.place import Place
        from models.review import Review
        from models.state import State
        from models.user import User

        classes = {
            'BaseModel': Basemode, 'User': User, 'Place': Place,
            'State': State, 'City': City, 'Amenity': Amenity,
            'Review': Review
        }
        try:
            temp = {}
            with open(FileStorage.__file_path, 'r') as f:
                temp = json.load(f)
                for key, val in temp.items():
                    self.all()[key] = classes[val['__class__']](**val)
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """del obj from __obj if its inside"""
        if obj:
            key = '{}.{}'.format(type(obj).__name__, obj.id)
            del FileStorage.__objects[key]

    def close(self):
        """deserialize json file to obj before leaving"""
        self.reload()
