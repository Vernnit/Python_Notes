dic1={1:2 , 2:3 , 3:4 , 4:5}
dic2={"vernnit":12 , 5:6 }

dic1.update(dic2)
print(dic1)
dic2.clear()
print(dic2)

print(dic1.pop(2))
print(dic1)

# dic1.popitem()   pops out the last item.

# del dic1         #deletes the whole dictionary
# print(dic1)

del dic1[1]        #if given some value to delete .
print(dic1)


# dictionary comprehension