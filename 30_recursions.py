# Recursion is the process of defining something in terms of itself.

def factorial(n):
    if n==0 or n==1 :
        return 1
    return n*factorial(n-1)

print("factorial of 10 is :" , factorial(10))

# fibonacci sequence -- 0 1 1 2 3 5 8 13...  first two terms 0,1 and rest 2  consecutive terms added. f(n)=f(n-1)+f(n-2).... to calculate a particular term of fibonacci sequence -->

def fibonacci(n):
    if n==0 :
        return 0 
    elif n==1 :
        return 1
    else :
        return fibonacci(n-1)+fibonacci(n-2)
    
print(f'10th term of fibonacci is  {fibonacci(10)}')


    
       


