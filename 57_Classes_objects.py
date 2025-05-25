# A class is a blueprint or a template for creating objects, providing initial values for state (member variables or attributes), and implementations of behavior (member functions or methods). The user-defined objects are created using the class keyword.

class details:
    name="vernnit"
    age=21
    

# Object is the instance of the class used to access the properties of the class Now lets create an object of the class.
obj1= details()
print(obj1.name , obj1.age)

obj2= details()
obj2.name="TONY"
print(obj2.name, obj2.age)





# SELF PARAMETER
# The self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class.

# It must be provided as the extra parameter inside the method definition.


class person:
    name='Jerry'       #attribute
    age=21
    place='New York'
    occupation='Trash man'
    
    def info(self):   #method
        print(f'{self.name} , {self.age}  , {self.place} , {self.occupation} ')
    
a=person()
a.info()
    
'''In python, everything is an object. And every object has attributes and methods or functions. Attributes are described by data variables for example like name, age, height etc.

Properties are special kind of attributes which have getter, setter and delete methods like __get__, __set__ and __delete__ methods.

A property decorator in Python provides getter/setter access to an attribute. You can define getters, setters, and delete methods with the property function. If you just want the read property, there is also a @property decorator you can add above your method.'''