# In object-oriented programming, the term "constructor" refers to a special type of method that is automatically executed when an object is created from a class. The purpose of a constructor is to initialize the object's attributes, allowing the object to be fully functional and ready to use.

# However, there are times when you may want to create an object in a different way, or with different initial values, than what is provided by the default constructor. This is where class methods can be used as alternative constructors.

class person:
    def __init__(self , name , age , place ):
        self.name=name
        self.age=age
        self.place=place
    def show(self):
        print(f'{self.name} , {self.age} , {self.place}')    
        
    @classmethod
    def from_string(cls,string):
        name , age , place =string.split('-')
        return cls(name , int(age) , place )
    
a=person.from_string('Vernnit-21-Shimla')
a.show()
