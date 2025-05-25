# In Python, a lambda function is a small anonymous function without a name. It is defined using the lambda keyword and has the following syntax:

# lambda arguments: expression

# can be anonymous without a name , used as arguments in other higher functions,




multiplication =lambda x, y: print(f'Multiplication of {x} and {y} is {x*y}')
# def multiplication(a,b):
#      print(f'multiplication  of {a} and {b} is {a*b}')    
multiplication (2,3)
double= lambda x,y : print(f'double of {x} and {y}  is {2*x} and {2*y}')
cube=lambda x : print(f"cube of {x} is {x**3} ")


def operators(x,y):
    multiplication(x,y)
    double(x,y)
    cube(x)
    
x = int(input("enter no. 1  "))
y = int(input("enter no. 2  "))  

operators(x,y)

x=int(input('enter x: '))
def function(fx,x):
    print(f"{fx} +5")
    print(f'value of {fx}+5 is {fx(x)+5}' )

function(lambda x:x*x*x ,x)

#small function is required for a short period of time. They are commonly used as arguments to higher-order functions, such as map, filter, and reduce.

f=lambda *a:print(len(a) , type(a))                  #sublist parameters are not allowed in lambda and def both but * operator unpacks tuple and provide as a argument for lambda or def.
f(1,2,3,4)                         
