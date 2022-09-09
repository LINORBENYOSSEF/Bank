from typing import Type, TypeVar, Optional
from pymongo import MongoClient

from .data import Adapter
from model.base import Column


T = TypeVar('T')


class Database(object):

    def __init__(self):
        self._client = MongoClient()
        self._db = self._client.get_database('bank')
        self._adapter = Adapter()

    def add(self, value: T):
        collection = self._db.get_collection(value.__class__.__name__)
        collection.insert_one(self._adapter.obj_to_dict(value))

    def get_all(self, data_type: Type[T]):
        collection = self._db.get_collection(data_type.__name__)
        results = collection.find()
        return self._adapter.dict_list_to_obj(list(results), data_type)

    def find_one(self, data_type: Type[T], column: str, value) -> Optional[T]:
        collection = self._db.get_collection(data_type.__name__)
        result = collection.find_one({column: value})
        if result is None:
            return None
        return self._adapter.dict_to_obj(result, data_type)
