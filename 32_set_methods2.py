s1={1,2,3,4}
s2={3,4,5,6}
print(s1.isdisjoint(s2))  #no common values in both the sets-- prints True.

# The issuperset() method checks if all the items of a particular set are present in the original set. It returns True if all the items are present, else it returns False.

print(s1.issuperset(s2))  
print(s1.issubset(s2))   #checks if a set is present in the original set.

s1.add(1221)              #adds a particular assigned value.
print(s1)

print(s1.discard(2))      #does not raise a error 
print(s1.remove(1))            #raises an error 

print(s1.pop())                   #pops out random value      
print(s1)

s3={1,2}
print(s3)
del s3       #deletes the set . It is a keyword.
# print(s3)

s4={00,11,22}
print(s4.clear())     #clears the elements of set an gives an empty set.
print(s4) 

# checking item in a set
s5={"vernnit", 1 , 3}
if "vernnit" in s5:
    print(bool(1))
else:
    print(bool(0))



