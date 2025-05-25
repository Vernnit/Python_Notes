# These are special methods that you can define in your classes, and when invoked, they give you a powerful way to manipulate objects and their behavior.

# used to emulate built in functions in python and prevent operator overloading.

#ALWAYS USE ' RETURN '.

class Employee:
    def __init__(self , name , salary):
        self.name=name
        self.salary=salary
    def __add__(self , other):
        return self.salary + other.salary
    
    def __repr__(self):
        return f'Employee({self.name} , {self.salary})'  #something which recreates the object on copy pasting.
                                                         #acts as a fallback if the str is not provided .
    
    
    def __str__(self):
        return f'{self.name} - {self.salary}'  #anything arbitrary.
    
   
   
    
emp1=Employee('vernnit' , 100000)
emp2=Employee('Diwi' , 100000)
print(emp1+emp2)             # unsupported operand type(s) for +: 'Employee' and 'Employee' if dunder add is not defined.

print(emp1)                  # <__main__.Employee object at 0x000001F4DAA95960> this is  printed if do not use __repr__ or __str__

#  __repr__() provides the official string representation of an object, aimed at the programmer.
 
#  __str__() provides the informal string representation of an object, aimed at the user.
