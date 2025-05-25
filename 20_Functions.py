# A function is a block of code that performs a specific task whenever it is called.
# built in and user defined functions -
# def function_name(parameters):
#   pass                                     
#    Code and Statements

def geomean(a,b):
    mean=(a*b)/(a+b)
    print(mean)
    
def isgreater(a,b):
    if(a>b):
        print("first number is greater ")
    else:
        print("second number is greater or equal to first")
    
def islesser(a,b):    #to complete code afterwards but at the moments it does nothing and passes on to further code.
    pass    

e=5
f=12
isgreater(e,f)        # call function just like any built in function with arguments and parameters. 
geomean(e,f) 
