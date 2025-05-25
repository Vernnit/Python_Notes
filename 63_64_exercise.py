# Library Management System

class Library:
    def __init__(self ,Number,Books=None ):
        
        self.n=Number
        if Books==None:
            self.b=[]
        else:
            self.b=Books
        
    def check(self):
        if self.Number==len(self.Books):
            print('All books verified')
        else:
            print('Something is Wrong !')
            
        