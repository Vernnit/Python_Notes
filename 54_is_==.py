# The is operator compares the identity of two objects, while the == operator compares the values of the objects. 

# This means that is will only return True if the objects being compared are the exact same object in memory, while == will return True if the objects have the same value.


a=3          #constants can't be changed , so Python creates only one constant in memory keeping identity same.
             #same for tuples and strings and any other immutable same values.
b=3
print(a is b)
print(a==b)

a=[1,3]      #Lists can be changed , so two different memories are allocated to it.
b=[1,3]
print(a is b )
print(a == b )
 