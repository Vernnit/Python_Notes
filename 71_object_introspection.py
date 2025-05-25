# dir()-method , __dict__ - attribute  , help() -method --->  there are three built-in functions that are commonly used to get information about objects.


# METHOD dir()-

#  The dir() function returns a list of all the attributes and methods (including dunder methods) available for an object. It is a useful tool for discovering what you can do with an object

A=[1,2,3,4,5]
print(dir(A))
print(A.__len__)


# ATTRIBUTE __dict__ - The __dict__ attribute returns a dictionary representation of an object's attributes. It is a useful tool for introspection
class  B:
    def __init__(self ,a , b , c):
        self.a=a 
        self.b=b
        self.c=c
        self.d=123
x=B(1,2,3)     
print(x.__dict__)


# Help() METHOD:

# The help() function is used to get help documentation for an object, including a description of its attributes and methods.used to mine doc strings.
#  used to get the documentation of specified module, class, function, variables etc

print(help(x))
print(help(B))