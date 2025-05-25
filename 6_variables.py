#variable holds the data 
#data type tells type of data a variable holds
a = 1
b = True
c = "Harry"
d = None

# these are 4 type of data types numeric , boolean , strings , none.
print( type(a), type(b) , type(c) , type(d))

e = "1"
print(type(e)) #this is a string.

# built in data types 
#  numeric- int float complex
#  string - text
#  boolean - true False
#  sequenced data - list [] , tuple () , mapped data i.e. dictionary {key: value}

f= complex(8,2)
print("type of f is:" , type(f),f)


list1 = [8, 2.3, [-4, 5], ["apple", "banana"]]
print(list1)

tuple1 = (("parrot", "sparrow"), ("Lion", "Tiger"))
print(tuple1)

dict1 = {"name":"Sakshi", "age":20, "canVote":True}
print(dict1)