# Else can be used with for and while loops. it executes when the loop ends successfully not if the loop is broken. 
 
for i in range(6):
    print(i)
else :
    print("No i available ")
    
for i in range(20):
    print(i)
    if i==6:
        break
else:
    print("no i")       #does not execute.
    
    
i=0
while i<10:
    print(i)
    i=i+1
else:
    print("loop over , else executed")
    
    
    
for x in range(6):
    print(f"iteration no. {x+1} in for loop")
else:
    print("loop ended successfully")
print("out of loop")