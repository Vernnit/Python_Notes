# Unordered collection of data. MUTABLE but items immutable as items are unordered. Does not allow duplicate items.
s1={1,2,"vernnit", "verma","vernnit",2 , True}
print(s1 , type(s1))

# TO create an empty set --  set()... s={} will give empty dictionary.

s={}
print(type(s))
ss=set()
print(type(ss))

# Accessing values of set -- Can't be accessed by indexing as data is unordered. 
# by for loop 
for i in s1:
    print(i)
    
# SET COMPREHENSION