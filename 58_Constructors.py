''' IT CANNOT RETURN A VALUE OTHER THAN NONE .

    def __init__(self, *args, **kwargs): --> none'''
    

# A constructor is a special method in a class used to create and initialize an object of a class. There are different types of constructors. Constructor is invoked automatically when an object of a class is created.

# A constructor is a unique function that gets called automatically when an object is created of a class. The main purpose of a constructor is to initialize or assign values to the data members of that class.

# def __init__(self):
	# initializations
 
 
 
 
# class person:
#     def __init__(self):
#         print('hey , i am a person')
        
# a=person()     #every time  an object is made of this class init is evoked.

# Self is necessary while creating a method but not necessary to mention while calling , it is automatically given as an argument.



class person:
    def __init__(self ,n , a , p , o):
        self.n=n       # n as a argument is a value and self.n is an attribute which can be altered to change a value.
        self.a=a
        self.p=p
        self.o=o
        
    def info(self):
        print(f'Name is {self.n} , age is {self.a}')
        
a=person("vernnit" , 21 , "shimla" , "student")
a.info()    #person.info(a) without self


'''Parameterized Constructor in Python
When the constructor accepts arguments along with self, it is known as parameterized constructor.

These arguments can be used inside the class to assign the values to the data members.'''



# When the constructor doesn't accept any arguments from the object and has only one argument, self, in the constructor, it is known as a Default constructor.