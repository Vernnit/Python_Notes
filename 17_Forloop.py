# to execute a group of statements a certain number of times we use loops.
# for loop is used to iterate ( repeat ) over a sequence of objects i.e. strings , list , tuple , dictionary etc.

name="Vernnit Verma"
for i in name:
    print(i)

list=name.split()
print(list)

for x in list:              #nested loop.
    print(x)           
    for char in x:    
        print(char)        
        
# To loop through a set of code a specified number of times

for k in range(5):       # starts from 0 and ends at n-1.
    print(k , "\n" )
for k in range(1,12):
    print(k, "\n")       # you can specify a start value and ending value (n-1)
    print(k+1)
  
  
# third parameter  specifies the difference between the numbers. i.e. a step value(increment value )    
for x in range(1,12,3):       
    print(x)