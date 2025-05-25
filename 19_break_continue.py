# The break statement is used to terminate the loop immediately when it is encountered.

for i in range(10):
    print(i)          #prints till 8 then gets condition i==8 and leaves the loop.
    if i==8:
        break
    
for i in range(10):
    if i==8:
        break
    print(i)          #prints till 7 then gets condition i==8 and leaves the loop.
    
    
i=1
while(i<5):           #prints till 3 then breaks[2 printed -> not eq 3 2+1 =3 ->prints eq eq 3 so breaks]
    print(i)
    if i==3:
        break
    i=i+1
    
i=1
while(i<5):           #prints till 2 then breaks [ 2 -> not eq 3 -> prints ->2+1 =3 ==3 so breaks not printed]
    print(i)
    i=i+1
    if i==3:
        break
    
#  *** The continue statement is used to skip the current iteration of the loop and the control flow of the program goes to the next iteration.*** #

for x in range(12):
    if x==10:
        print("skips the iteration")
        continue
        
    print(x)
   
for x in range(12):       
    print(x)
    if x==10:
        print("does not skips the iteration")
        continue
    
i=1
while(i<=8):
    i=i+1
    if i==6:                    #skips 6
        continue
    print(i)
    
i=1
while(i<=8):
    if i==6:
        continue                # executes only till 5
    print(i)
    i=i+1
   
   