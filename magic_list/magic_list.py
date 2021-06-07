from dataclasses import dataclass
from collections.abc import MutableSequence


@dataclass
class Person:
    age: int = 1


class MagicList(MutableSequence):
    def __init__(self, cls_type=None):
        self._store = []
        self.cls_type = cls_type

    def __getattr__(self, item):
        print("__getattr__", item)

    def __setattr__(self, key, value):
        if key in ['_store', 'cls_type']:
            return super(MagicList, self).__setattr__(key, value)
        if not self.cls_type:
            raise ValueError("cls_type is missing!")
        self._store.append(self.cls_type(value))

    def __repr__(self):
        return str(self._store)

    def __len__(self):
        return super(MagicList, self).__len__()

    def __delitem__(self, index):
        self._store.__delitem__(index)

    def insert(self, index, value):
        self._store.insert(index, value)

    def __setitem__(self, index, value):
        if index > len(self._store):
            raise IndexError("list index out of range")
        self._store.append(value)

    def __getitem__(self, index):
        if index > len(self._store):
            raise IndexError("list index out of range")
        if index == len(self._store):
            return self
        return self._store[index]

















