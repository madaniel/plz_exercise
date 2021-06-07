import pytest
from magic_list.magic_list import MagicList, Person


def test_magic_list_init():
    MagicList()


def test_magic_list_assign_number():
    a = MagicList()
    a[0] = 5
    assert a[0] == 5


def test_magic_list_assign_number_negative():
    with pytest.raises(IndexError):
        a = MagicList()
        a[1] = 5


def test_magic_list_assign_class():
    a = MagicList(cls_type=Person)
    a[0].age = 5
    assert a[0] == Person(age=5)


def test_magic_list_assign_number_class_negative():
    with pytest.raises(IndexError):
        a = MagicList(cls_type=Person)
        a[1].age = 5


