# A class method is a type of method that is bound to the class and not the instance of the class. In other words, it operates on the class as a whole, rather than on a specific instance of the class.


# Class methods are defined using the "@classmethod" decorator, followed by a function definition. The first argument of the function is always "cls," which represents the class itself.

# They are useful for creating factory methods, alternative constructors, and other types of methods that operate at the class level.

class Company:
    Name = 'Apple'

    def __init__(self):
        print(f'{self.Name}')

    @classmethod  # Remember to put this first.
    def change(cls, newname):
        cls.Name = newname


# a = Company()
# a.change('Microsoft')   #Changes for whole class.
# b=Company()

# accessed directly by class name without instantiating an object
Company.change('Nokia')
Company()
