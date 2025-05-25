# lists are ordered collection of data & MUTABLE. Items separated by , and enclosed within [].

lst1=["Vernnit" , 1 , True ]      #can contain diff data types.
print(lst1)       

# Each item has its own index starts  from 0 and ends at len(lst) represents index n-1. Each item can be accessed by its index.
# listName[start : end : jumpIndex]
# jump index prints the consecutive value skipping values as directed.
lst2=[1,2,3,"vernnit", True]
print(lst2[0])
print(lst2[4])
print(lst2[:])
print(lst2[0:5])
print(lst2[0:5:2])

# negative indexing  -- or just put len(lst) before negative index and convert to positive.
colors = ["Red", "Green", "Blue", "Yellow", "Green"]
#          [-5]    [-4]    [-3]     [-2]      [-1]
print(colors[-1])
print(colors[-3])
print(colors[-5])




#  We can check for a particular item or chars or particular items within the list using in keyword
# applies for strings as well.
lst3=[1,2,3,"vernnit"]
if 1 in lst3:
    print(bool(1))
else :
    print(bool(0))
    
if "ernnit" in "vernnit" :
    print(bool(1))
    
# LIST COMPREHENSION--List comprehensions are used for creating new lists from other iterables like lists, tuples, dictionaries, sets, and even in arrays and strings.


    
# List = [Expression(item) for item in iterable if Condition]

# Expression: It is the item which is being iterated.

# Iterable: It can be list, tuples, dictionaries, sets, and even in arrays and strings.

# Condition: Condition checks if the item should be added to the new list or not.

# not so efficient way
ls1=[]

for c in range(0,101):
    if c%2==0:
        ls1.append(c)
print(ls1)

# list comprehension
ls1=[num*2 for num in range(0,101) if num%2==0]
print(ls1)


          
          
          