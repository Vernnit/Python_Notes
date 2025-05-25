l=[21,31,3,1,21,52,4]
print(l)

l.append(69)          #adds 69 at the end of the list  l .
l.append("vernnit")
l.append("verma")
print(l)

l=[45,54,1,4,0,21]
l.sort()               #ascending order
l.sort(reverse=True)   #descending order
print(l)

l=[1,2,3,4,5,6,1]
l.reverse()            #reverses the order of the list.
print(l)
print(l.index(1))      #prints index of the FIRST occurrence of 1.
print(l.count(1))      # counts occurrence of 1. 

m=l.copy()             #creates a copy of l and a new list m and can be changed without affecting the original list.
m[0]=999
print(m)

# l1=[1,2,3]            
# m1=l1               A reference is created l1 is a reference of m1 now so if m1 is changed l1 also changes.
# m1[0]=21
# print(m1)
# print(l1)  

l3=[21,12,31,13]
l3.insert(4,213)      # inserts the item at the given index.
l3.insert(0,212)
print(l3)

# To concatenate two lists 
l=[1,2,3]
m=[4,5,6]
k=l+m                 #gives same result as below fn gives. 
print(k)

l.extend(m)           #open up m and put in or extend l .
print(l)