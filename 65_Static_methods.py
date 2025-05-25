# Self is  not required as an argument. 

# Static method does not automatically take class(cls) or instance(self) as an argument. 

# Static methods are often used to create utility functions that don't need access to instance data or class data .


# Syntax of @staticmethod is:

# @staticmethod
# def func(args, ...)



class shop:
    def __init__(self ,p1, p2 ):
      self.p1=p1
      self.p2=p2 
    def additem(self,p3):
        print(self.p1+self.p2+p3)  #accessing instance data.
        
    @staticmethod                    
    def add(a,b):     
        print(a+b)                 #no reference to the class instance .  
        
a=shop(200,300)

a.additem(100)

shop(500,500).additem(500)

a.add(2,3)

shop.add(500,500)

