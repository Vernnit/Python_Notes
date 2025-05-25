dic={"name":"vernnit", "age":20, "weight": "unknown" , "Bad boy":True}
print(dic)

# Values in a dictionary can be accessed using keys. We can access dictionary values by mentioning keys either in square brackets or by using get method.
print(dic["name"])      #throws an error if not present. 
print(dic.get("name"))  #gives none if not present. get method. x.get()

#multiple
print(dic.keys())
print(dic.values())
print(dic.items())

for keys in dic.keys():
    print(keys)
    
for values in dic.values():
    print(values)

for keys , values in dic.items():
    print(f"the value of {keys} is given by {values}")
    print(f"the value of {keys} is given by {dic[keys]}")
    

# DICTIONARY COMPREHENSION


