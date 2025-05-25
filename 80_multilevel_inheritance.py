# Multilevel inheritance is a type of inheritance in object-oriented programming where a derived class inherits from another derived class. This type of inheritance allows you to build a hierarchy of classes where one class builds upon another, leading to a more specialized class.

# multilevel inheritance means you're inheriting from something that is also inherited from something. It can be good to chain inheritance like this so each class is responsible for a different functionality, or to create different branching points of shared functionality


class parent1:
    def __init__(self, a):
        self.a = a

    def show(self):
        print(f'{self.a}')


class child(parent1):
    def __init__(self, a, b):
        self.b = b
        parent1.__init__(self, a)

    def show(self):
        parent1.show(self)
        print(f'{self.b}')


class grandchild(child):
    def __init__(self, a, b, c):
        self.c = c
        super().__init__(a, b)

    def show(self):
        child.show(self)
        print(f'{self.c}')

    def __str__(self):
        return f'{self.a} , {self.b} , {self.c}'


x = grandchild(1, 2, 3)
x.show()

# The key difference between Multiple and Multilevel Inheritance is that Multiple Inheritance is when a class inherits from many base classes while Multilevel Inheritance is when a class inherits from a derived class making that derived class a base class for a new class.
