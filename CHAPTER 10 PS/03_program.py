# Create a class with a class attribute a; create an object from it and set ‘a’ directly using ‘object.a = 0’. Does this change the class attribute?

class Demo:
    a = 10

o = Demo()
print(o.a)  # prints class attribute

o.a = 0     # instance attribute is set
print(o.a)  # prints instance attribute because it is present
print(Demo.a)   # prints the class attribute