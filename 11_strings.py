# string is like an array of characters . used when working with unicode characters. 
# strings can be enclosed in single double quotes. multiline strings are enclosed in triple single or double quotes.

a="hey! there i am vernnit's best friend"
print(a)
b='hello , "i am vernnit"'
print(b)
c=''' hey , 
i 
am vernnit'''
print(c)

# indexing means obtaining elements of a string . starts from 0. using[].
print(a[0])
print(a[3])
print(a[7])

# to obtain every character we can use for loop.

print("using For loop for indexing")

for character in c:
    print(character)