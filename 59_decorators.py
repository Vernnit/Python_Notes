'''Python decorators are a powerful and versatile tool that allow you to modify the behavior of functions and methods. They are a way to extend the functionality of a function or method without modifying its source code.

A decorator is a function that takes another function as an argument and returns a new function that modifies the behavior of the original function. The new function is often referred to as a "decorated" function. The basic syntax for using a decorator is the following:'''

    
def decorate(func):
    def modified_func():
        print("Print this before execution of real func. ")
        
        func()

        print('print this after the execution of real func.')

    return modified_func

@decorate   
def func1():
    print('This is the real function.')
    
# decorate(func1)()

func1()


def decorate1(a):
     def mdf(*args , **kwargs):
         print("before function")
         
         a(*args, **kwargs) 
         
         print('after function')
         
     return mdf  
@decorate1 
def func1(a,b):
    print(a+b)
func1(2,3)
    








'''They are a great tool for separating concerns, reducing code duplication, and making your code more readable and maintainable.They are used for a variety of purposes, such as logging, memoization, access control, and more'''