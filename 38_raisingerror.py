# In python, we can raise custom errors by using the raise keyword.

a=int(input("enter the  value btw 5 and 10"))
if not 5<a<10:
    raise ValueError("please enter a valid value")




# In Python, we can define custom exceptions by creating a new class that is derived from the built-in Exception class.

# class CustomError(Exception):
#   # code ...
#   pass

# try:
#   # code ...

# except CustomError:
# #   code...