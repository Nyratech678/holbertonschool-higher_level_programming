Understanding Python Mutable and Immutable Objects

Introduction
In this post, I share what I have learned about one of the fundamental concepts in Python: mutable and immutable objects. Understanding the difference is crucial for writing efficient, bug-free programs and knowing how Python handles data internally.

id and type
Python assigns a unique identifier to each object, accessible via the built-in id() function. This id remains constant for the object's lifetime. The type of an object (type()) determines its behavior and mutability. For example:

python
a = [1, 2, 3]
print(id(a))    # Unique identifier of list object
print(type(a))  # <class 'list'>
Mutable objects
Mutable objects can be changed in place after creation. This means you can modify their content without changing their identity (id). Lists, dictionaries, and sets are common examples.

python
a = [1, 2, 3]
print(id(a))  # e.g. 139926795932424

a[0] = 100
print(a)      # [100, 2, 3]
print(id(a))  # Same id: still 139926795932424
Immutable objects
Immutable objects cannot be changed once created. Any modification creates a new object with a new id. Common immutable types include strings, numbers, and tuples.

python
s = "hello"
print(id(s))  # Some id

s = s + " world"
print(s)      # "hello world"
print(id(s))  # Different id, new object created
Why does it matter and how differently does Python treat mutable and immutable objects
The difference affects how Python manages memory and variable assignments. Mutables allow you to change data without generating new objects, which is efficient but can lead to unintended side effects if multiple references point to the same object.

Immutable objects promote safety and predictability since the data cannot be altered after creation, avoiding side effects at the cost of some overhead when changes require creating new objects.

How arguments are passed to functions and implications
In Python, arguments are passed by object reference. For mutable objects, changes inside a function affect the original object:

python
def add_element(lst):
    lst.append(4)

my_list = [1, 2, 3]
add_element(my_list)
print(my_list)  # [1, 2, 3, 4]
For immutable objects, changes inside a function create new objects without affecting the original:

python
def increment(n):
    n += 1
    return n

x = 5
y = increment(x)
print(x)  # 5
print(y)  # 6