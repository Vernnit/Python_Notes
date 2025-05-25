x=int(input("enter the number to be matched :"))

match x:                       # matches the value with case and does not need a break  like c.
    case 0:
        print("case zero")    
    case 1:
        print("case one")
    case 2:
        print("case two ")
    case _:
        print ("default case ")  #just like else statement .
        
        
# We can also use the if statements inside 

y=int(input("enter the value of y:"))

match y:
    case 0:
        print(y, "is the value ") 
      
    # case 4 if y%2==0 :                          previously written code and gives value only when input was 4.
    #     print(y," is the even value ")
    
    
    case _ if y%2==0 :                           #use this when to match with a condition
        print(y," is the even value ")
        
    case _ if y>10 and y<20 :
        print("special case ")
        
    case _ if y>=20:
        print(y , "big number ")