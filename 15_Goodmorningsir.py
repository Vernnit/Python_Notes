import time
current_time1=time.strftime('%H:%M:%S')
print(current_time1)
current_time=int(time.strftime("%H"))


if(current_time>=5 and current_time<12):
    print("Good morning sir ")
elif(current_time>=12 and current_time<17):
    print("Good after noon sir")
    
elif(current_time>=1 and current_time<5):
    a=input("Are you going to sleep? Yes/No ")
    if(a=="Yes"):
        print("Good night sir")        
    elif(a=="No"):
        print("sleep")
    else:
        print("please answer Yes/No only")
else:
    print("Good Evening sir")
    
