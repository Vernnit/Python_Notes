# With the while loop we can execute a set of statements as long as a condition is true.
# first initialise the variable #set a condition. #increment the value. 
#WHILE LOOP ENTRY CONTROLLED -- DO WHILE EXIT CONTROLLED TYPE.
i=1
while(i<10):
    print(i)
    i=i+1
print("terminated")                #incremented loop

# i=11
# while(i>10):
#     print(i)                     #infinite loop
#     i=i+1


count=4
while(count>0):
    print(count)
    count=count-1                  #decrementing 
else:
    print("false , else executed.")        # whenever condition inside while loop becomes false else is executed.
    
    
#Do while loop does not exist in python. it executes at least once then checks for condition if true it will execute and false it will terminate. BUT DOESN'T EXIST IN PYTHON.
#  do {
#     loop body;
# } while condition;

# one way to emulate do while loop

a=int(input("enter value of a"))
print(a)
while(a<=10):                                #at a=11 it will terminate
    a=int(input("enter value of a again"))
    print(a)
    
# *******ANOTHER EMULATION OF DO WHILE LOOP*******

i=0
while True:
    print(i)       #executing no matter what is the condition
    i=i+1
    if i%100==0:   # condition when applied breaks the loop #CONDITION IS CHECKED AT LAST SO INITIAL ITERATION ALWAYS RUN
        break