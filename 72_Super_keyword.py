# The super() keyword in Python is used to refer to the parent class. It is especially useful when a class inherits from multiple parent classes and you want to call a method or a constructor from one of the parent classes.

# The super() keyword is also useful when a class inherits from multiple parent classes. In this case, you can specify the parent class from which you want to call the method.


class parent1:
    def __init__(self ,a , b ,c):
        self.a=a
        self.b=b
        self.c=c
    def samefn(self):
        print('function from parent 1')

class parent2:
    def samefn(self):
        print('function from parent 2')

class child(parent1, parent2):
    def __init__(self , a ,b, c , d):
        
        self.d=d
        
        super().__init__(a, b ,c)
        # parent1.__init__(self , a, b, c)    alternate method to call a constructor from other parent class. 
        
    def samefnchild(self):
        super().samefn()                #prints first parent class   
        
        parent1.samefn(self)            #takes self argument necessary.
        
        parent2.samefn(self)
        
a=child(1,2,3,4)
a.samefnchild()    


#child.samefnchild(a) ----> without self given in function ; you would get  an error as extra argument given as a is given as an argument .