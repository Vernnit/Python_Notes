# There are three main types of errors in Python: syntax errors, runtime errors, and logical errors1.

# Syntax errors occur when the code does not follow the rules of the Python language. For example, forgetting a colon at the end of a statement or using incorrect indentation. Syntax errors are detected by the interpreter before the program runs.

# Runtime errors occur when the code is syntactically correct, but fails to execute due to some unexpected condition. For example, dividing by zero, accessing an invalid index of a list, or importing a module that does not exist. Runtime errors are also called exceptions, and can be handled using the try-except-finally statements.

# Logical errors occur when the code runs without any runtime errors, but produces incorrect or unexpected results. For example, using the wrong operator, variable, or algorithm in a calculation. Logical errors are often caused by human mistakes or faulty logic, and can be difficult to debug.


# try:
#      #statements which could generate
#      #exception
# except:
#      #Solution of generated exception

try:
    a = int(input("enter the number"))
    for i in range(1, 11):
        print(f'multiplication of {a} and {i} is given by {a*i}')
except Exception as e:
    print(e)

try:
    a = int(input("enter the number"))
    for i in range(1, 11):
        print(f'multiplication of {a} and {i} is given by {a*i}')
except ValueError:
    print("invalid value given")


# An except clause may name multiple exceptions as a parenthesized tuple, for example:

# ... except (RuntimeError, TypeError, NameError):
# ...     pass
