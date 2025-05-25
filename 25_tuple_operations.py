# to modify a tuple convert it into a temporary list , make changes and convert back to tuple INDIRECTLY. 

tup=(1,2,3,"INDIA",True)
print(id(tup))      #different id

temp=list(tup)
print(type(temp))
temp.append("hello")
temp.pop(2)             #removes an item.
temp[0]=51
tup=tuple(temp)


print(tup)
print(id(tup))     #different id so we cant really change the tuple


# WE CAN DIRECTLY CONCATENATE TWO TUPLES AS IT FORMS A NEW TUPLE.
a=(1,2,3)
b=(4,5,6)
# a.extend(b)     throws an error as the already existing tuple cant be changed 
c=a+b
print(type(c),c)

print(c.count(2))
print(c.index(3))
print(c.index(2,1,6)) #slicing afterwards value to be found.


# All the methods of list can be applied once tuple is converted to a list.
