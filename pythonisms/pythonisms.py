
from functools import wraps
from time import sleep

def decorate_null(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return_val = func(*args, **kwargs)
        decorator = f'The LinkedList Representation is : {return_val} + NULL'
        return decorator

    return wrapper

def decorate_length(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return_val = func(*args, **kwargs)
        decorator = f'The length of the items : {return_val}'
        return decorator
    return wrapper

def decorate_index(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return_val = func(*args, **kwargs)
        decorator = f'The index of item is : {return_val}'
        return decorator
    return wrapper

class Node:
    def __init__(self, value, next_ = None):
        self.value = value
        self.next = next_

class LinkedList:

    def __init__(self, collection=None):
        self.head = None
        if collection:
            for item in reversed(collection):
                self.insert(item)

    def __iter__(self):
        def value_generator():
            current = self.head
            while current:
                yield current.value
                current = current.next
        return value_generator()
   
    @decorate_null 
    def __str__(self):
        out = ""
        for value in self:
            out += f"[ {value} ] -> "
        return out + "None"

    @decorate_length
    def __len__(self):
        return len(list(iter(self)))
   
    @decorate_index
    def __getitem__(self, index):
        if index < 0:
            raise IndexError
        for i, item in enumerate(self):
            if i == index:
                return item
        raise IndexError


    def insert(self, value):
        self.head = Node(value, self.head)

    def append(self, value):
        node = Node(value)
        if not self.head:
            self.head = node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = node


if __name__ == "__main__":
   food = LinkedList()
   food.insert("apple")
   food.insert("banana")
   food.insert("orange")
   print(food)
   print(food.__len__())
   print(food[1])
 
   print(food.__iter__())




   