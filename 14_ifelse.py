a=int(input("enter your age:"))
print("your age is :", a)

# conditional operators -
# <less than , greater than >, less than equal to <=, greater than eq to>=, equal to ==,not equal to!= 

if (a>=18):
    print("you can drive")
else:
    print("you can not drive")   
    
# indentations necessary to keep it a part of if or else
# elif used to further create conditions in between 

num=int(input("enter the value of number :"))

#first checks first condition if not true moves to another until it gets a true condition and after that it doesn't checks another.
if (num<0): 
    print("number is negative")
elif(num==0):
    print("number is neutral")
elif(num==1221):
    print("number is special")
else:
    print("number is positive")
    
# nested if else means if else statements inside if else statements.

num2=int(input("enter the value of num for nested ifelse"))

if(num2<0):
    if(num2==-12):
        print("num is exact value")
    else:
        print("num is negative")
        
elif(num2>0):
    if(num2==21):
        print("good number ")
    elif(num2>=12 and num2<=21):
        print("number is between 12-21")
    else:
        print("number is positive")
else:
    print("number is zero")
