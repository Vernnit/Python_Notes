# Python access modifiers are used to modify the default scope of a variable. There are three types of access modifiers in Python and they are – Public, Private, and Protected. In Python, we use underscores “_” symbol to specify the access modifier for specific data members and member functions in the class.


# PUBLIC-

# In the case of the Public access modifier in Python, all the members in the Python class are public by default. Any member declared as public can be accessed from outside the class through an object.Also values can be modified.


# PRIVATE -

# A double underscore “__” makes the variable private as well as secure and the members of the class which is declared private are accessible within the class. Also, it is not possible to access them outside the class because it will throw an error.

# So, to access the private members of a class we have name mangling of private variables. Every member with a double underscore will be changed to ” object._class__variable “ and then it can be accessed from outside the class.


# PROTECTED-

# The data member of the class is declared protected by adding a single underscore “_” and this prevents it from being access. The protected members of the class can be accessed by other members within the class also it can be accessible to the class derived from it.
# We can access the protected members from the outside class with the help of an object.

# Protected access specifiers are designed so that responsible programmer would identify by their name convention and do the required operation only on that protected class members or class methods


class employee:
    def __init__(self):
        self.name = 'vernnit'
        self._name = 'harry'
        self.__name = 'john'

    def info(self):
        print(f'name1 is accessible {self.name} , name2 {
              self._name} and name3 {self.__name}')


a = employee()
print(a.name)
print(a._name)  # accessible within the class and outside the class.
# print(a.__name)  #accessible within the class but not outside the class.
a.info()


# SUBCLASS / INHERITED CLASS
class manager(employee):
    def info2(self):
        print(f'name1 is accessible {self.name} , name2 {
              self._name} and name3 {{self.__name}} NOT ACCESSIBLE WITHIN SUBCLASS')


b = manager()
b.info2()
print(b.name)
print(b._name)


# OTHER CLASS
class Hr:
    n = a._name
    # m=a.__name

    def info3(self):
        print(f'name1 is accessible {a.name} , name2 {
              a._name} and name3 {{a.__name}} NOT ACCESSIBLE   ')


c = Hr()
c.info3()
print(c.n)
# print(c.m)


'''#__  is known as a "weak internal use indicator" and it is a convention only     '''

# Name mangling in Python is a technique used to protect class-private and superclass-private attributes from being accidentally overwritten by subclasses. Names of class-private and superclass-private attributes are transformed by the addition of a single leading underscore and a double leading underscore respectively.'''
