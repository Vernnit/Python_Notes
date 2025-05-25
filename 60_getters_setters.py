# Getters in Python are methods that are used to access the values of an object's properties. They are used to return the value of a specific property, and are typically defined using the   @property decorator   .

# It is important to note that the getters do not take any parameters and we cannot set the value through getter method.For that we need setter method which can be added by decorating method with @property_name.setter.

# In conclusion, getters are a convenient way to access the values of an object's attribute, while keeping the internal representation of the attribute hidden. This can be useful for encapsulation and data validation.

# There is a property_name.deleter too.

class person:
    def __init__(self, name, place, age):
        self.n = name  # name , age , place is just like values. like without __init__ name="vernnit".and here name is like self.n.s
        self.p = place
        self.a = age

    @property
    def age(self):
        return self.a

    @age.setter
    def age(self, newvalue):
        self.a = newvalue

    def info(self):
        # {self.name} there is no attribute name.
        print(f'My name is {self.n} age {self.a} and I live in {self.p} ')


x = person('vernnit', 'shimla', 21)
x.a = 30
print(x.age)  # this is absurd if we dont apply a getter.

# this is absurd if we dont apply a setter after a getter for this        property_name.
x.age = 40
x.info()


'''When you define a class in object-oriented programming (OOP), you’ll likely end up with some instance and class attributes. These attributes are just variables that you can access through the instance, the class, or both.

Attributes hold the internal state of objects. In many cases, you’ll need to access and mutate this state, which involves accessing and mutating the attributes. Typically, you’ll have at least two ways to access and mutate attributes. You can either:

Access and mutate the attribute directly
Use methods to access and mutate the attribute
If you expose the attributes of a class to your users, then those attributes automatically become part of the class’s public API. They’ll be public attributes, which means that your users will directly access and mutate the attributes in their code.

Having an attribute that’s part of a class’s API will become a problem if you need to change the internal implementation of the attribute itself. A clear example of this issue is when you want to turn a stored attribute into a computed one. A stored attribute will immediately respond to access and mutation operations by just retrieving and storing data, while a computed attribute will run computations before such operations.

The problem with regular attributes is that they can’t have an internal implementation because they’re just variables. So, changing an attribute’s internal implementation will require converting the attribute into a method, which will probably break your users’ code. Why? Because they’ll have to change attribute access and mutation operations into method calls throughout their codebase if they want the code to continue working.'''
