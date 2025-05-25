# A local variable is a variable that is defined within a function and is only accessible within that function. It is created when the function is called and is destroyed when the function returns.

# On the other hand, a global variable is a variable that is defined outside of a function and is accessible from within any function in your code.


x = 10 # global variable

def my_function():
  global x
  x = 5 # this will change the value of the global variable x
  y = 5 # local variable
  print(x)

my_function()
print(x) # prints 5
# print(y) # this will cause an error because y is a local variable and is not accessible outside of the function

# if we dont use global keyword x would print 10 outside the function


# It's important to note that it's generally considered good practice to avoid modifying global variables from within functions, as it can lead to unexpected behavior and make your code harder to debug.

 