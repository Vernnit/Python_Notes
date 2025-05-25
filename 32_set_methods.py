s1={1,2,3,4,}
s2={3,4,5,6,7}
print(s1.union(s2))    # it joins all the values of s2 and s1 but does not alter any of the two sets.
print(s1,s2)
s1.update(s2)  # it updates s1 with the values of s2 .there is nothing like union_update.
print(s1 , s2) 

print(s1.intersection(s2))   #values which are common
s1.intersection_update(s2)   #updates s1 with intersection values only.
print(s1)    

s3={2,3,4,5}
print(id(s3))
s4={3,4,8}
print(s3.symmetric_difference(s4)), s3.symmetric_difference(s4) #A U B - A ^ B
# s3.symmetric_difference_update(s4)
# print(s3)

print(s3.difference(s4))    #s3-s4
s3.difference_update(s4)
print(s3)
print(id(s3))


