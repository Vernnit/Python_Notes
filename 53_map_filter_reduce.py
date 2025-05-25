# In Python, the map, filter, and reduce functions are built-in functions that allow you to apply a function to a sequence of elements and return a new sequence the sequence can be list , tuple or any kind of iterable object. These functions are known as higher-order functions, as they take other functions as arguments.



# MAP
# The map function applies a function to each element in a sequence and returns a new sequence containing the transformed elements.
# The function argument is a function that is applied to each element in the iterable argument.

function = lambda x: x*x*x    
iterable= [1,2,3,4,5,6]
a=map(function , iterable)
print(a)    #returns a map object for efficiency , you can convert it into list.
b=list(a)
print(b)

# FILTER
# The filter function filters a sequence of elements based on a given predicate (a function that returns a boolean value) and returns a new sequence containing only the elements that meet the predicate. 

predicate=lambda x: x%2==0 
a=list(filter(predicate , iterable))
print(a)

def predicate2(x):
    return x>2
print(list(filter(predicate2 , iterable)))


# REDUCE - 

# The reduce function is a higher-order function that applies a function to a sequence and returns a single value. It is a part of the functools module in Python and has the following syntax:
# The function argument is a function that takes in two arguments and returns a single value.

# The reduce function applies the function to the first two elements in the iterable and then applies the function to the result and the next element, and so on. The reduce function returns the final result.
l=[1,2,3,4,5,6,7,8,9,10]
from functools import reduce
a=reduce(lambda x , y: x+y , l)       #((((1+2)+3)+4)+5....) 
print(a)
b=reduce(lambda x, y: x*y , l)
print(b)
