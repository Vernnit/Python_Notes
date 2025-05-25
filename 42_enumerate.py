# The enumerate function is a built-in function in Python that allows you to loop over a sequence (such as a list, tuple, or string) and get the index and value of each element in the sequence at the same time.
#you can also specify the start value of index.


fruits = ['apple', 'banana', 'mango']
for index, fruit in enumerate(fruits):
    print(index, fruit ,"\n")
    


fruit=["apple", "banana", "mango"]
for x, i in enumerate(fruit , start=1):
    print(x,i)
    if x==1:
        print("hello")
