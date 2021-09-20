from pythonisms import __version__

import pytest

from pythonisms.pythonisms import LinkedList

def test_version():
    assert __version__ == '0.1.0'



def test_next():
    food = LinkedList()
    food.insert("apple")
    food.insert("banana")
    food.insert("orange")
    iterator = iter(food)
    assert next(iterator) == "orange"
    assert next(iterator) == "banana"
    assert next(iterator) == "apple"



def test_str():
   food = LinkedList()
   food.insert("apple")
   food.insert("banana")
   food.insert("orange")
   assert str(food) == "The LinkedList Representation is : [ orange ] -> [ banana ] -> [ apple ] -> None + NULL"


def test_get_item():
   food = LinkedList()
   food.insert("apple")
   food.insert("banana")
   food.insert("orange")
   assert str(food[0]) == "The index of item is : orange"


def test_lenght_item():
   food = LinkedList()
   food.insert("apple")
   food.insert("banana")
   food.insert("orange")  
   assert food.__len__() == "The length of the items : 3"

