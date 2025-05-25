# The finally code block is also a part of exception handling. When we handle exception using the try and except block, we can include a finally block at the end. The finally block is always executed, so it is generally used for doing the concluding tasks like closing file resources or closing database connection or may be ending the program execution with a delightful message.

# CLEAN UP ACTION

def fun():
    try:
        l = [1, 2, 3, 5]
        i = int(input("enter the index:"))
        print(l[i])
        return 1
    except IndexError:
        print("not a valid index ")
        return 0
    except ValueError:
        print("Please enter a valid number")
        return 0
    finally:
        print("It will execute always")
    # print("Why need finally when we can do this")            #didn't execute when the value was returned , but finally executes no matter what happens.


xz = fun()
print(xz)
