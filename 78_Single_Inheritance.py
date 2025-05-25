# Single inheritance is a type of inheritance where a class inherits properties and behaviors from a single parent class. This is the simplest and most common form of inheritance.

class animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def make_sound(self):  # over ridden method
        print('sound made by the animal')


class dog(animal):
    def __init__(self, name, color):
        self.color = color
        # if we miss any argument of the indicated class it gives missing argument error.
        animal.__init__(self, name, species='Dog')

    def make_sound(self):
        print('bark')


a = dog('dog', "black")
a.make_sound()
