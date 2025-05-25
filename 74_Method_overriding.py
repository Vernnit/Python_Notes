#  When a method in a subclass has the same name, same parameters or signature and same return type(or sub-type) as a method in its super-class, then the method in the subclass is said to override the method in the super-class.

# The version of a method that is executed will be determined by the object that is used to invoke it.

# If an object of a parent class is used to invoke the method, then the version in the parent class will be executed, but if an object of the subclass is used to invoke the method, then the version in the child class will be executed.


''' Another way to customize the behavior of a class is to call the base class method from the derived class method. To do this, you can use the super function. The super function allows you to call the base class method from the derived class method, and can be useful when you want to extend the behavior of the base class method, rather than replace it.'''


class shape:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def area(self):
        return self.x*self.y


class circle(shape):
    def __init__(self, radius):
        self.radius = radius

    # def area(self):
        # return 3.14*self.radius*self.radius
        super().__init__(radius, radius)
        # without it  , it will give an error that circle has no attribute x so if we define another init.

    def area(self):
        return 3.14*super().area()  # this is called  method overriding.
# rec=shape(3,5)
# print(rec.area())


c = circle(5)
print(c.area())
