# There are four types of arguments that we can provide in a function:

# Default Arguments             already given values which operates if no argument is given. 
# Keyword Arguments             ignores order or sequence by giving key=value recognizing by parameter name.
# Variable length Arguments     for taking multiple values *args and **kwargs
# Required Arguments            like the parameters already defined inside the function.(a,b)

def average(a,b=1):             #a=required b=default 
    avg=((a+b)/2)
    return(avg)                 

a=average(b=6,a=5)              #keyword
print(a)

# PRINT just shows the human user a string representing what is going on inside the computer. The computer cannot make use of that printing. RETURN is how a function gives back a value. This value is often unseen by the human user, but it can be used by the computer in further functions.


def division(*something):
    print(type(something))             #similarly double asterisk gives dictionary **.
    sum=0
    for i in something:
        sum+=i                         #assignment operator.
        division=sum/len(something)
    return(division)

a=division(1,2,3,4,5,6,7,8,9,10)
print(a)
