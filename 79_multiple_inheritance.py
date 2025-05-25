# Multiple inheritance is a powerful feature in object-oriented programming that allows a class to inherit attributes and methods from multiple parent classes.

# It's important to note that, in case of multiple inheritance, Python follows a method resolution order (MRO) to resolve conflicts between methods or attributes from different parent classes. The MRO determines the order in which parent classes are searched for attributes and methods.

# multiple inheritance allows you to inherit from more than one class at a time. This is good when you need to insert some additional functionality into your class.

class parent1:
    def __init__(self, a):
        self.a = a

    def show(self):
        print('method of parent1 called')


class parent2:
    def __init__(self, b):
        self.b = b

    def show(self):
        print('method of parent2 is called')


class child(parent2, parent1):
    def __init__(self, a, b, c):
        self.c = c
        parent1.__init__(self, a)
        parent2.__init__(self, b)

    def __str__(self):
        return f'{self.a} ,{self.b} ,{self.c} '


x = child(1, 2, 3)
# method of parent class mentioned first in the arguments of child class is called.
x.show()


print(child.mro())
