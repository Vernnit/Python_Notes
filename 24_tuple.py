# tuples are also ordered collection of data , BUT IMMUTABLE. cannot be changed directly.

tup=(1,81,"vernnit","verma",32,23)
print(tup)
print(type(tup))

# tup[0]=12     immutable so throws an error. 

# indexing same as in lists--
print(tup[0])
print(tup[:])
print(tup[-3])
print(tup[0:4:2])         # Tuple[start : end : jumpIndex]
print(tup[0:6:2])
print(tup[::2])

# check for an item 
if "vernnit" in tup:
     print(bool(1))
else:
     print(bool(0))

     
    
