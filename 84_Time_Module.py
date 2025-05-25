# The time module in Python provides a set of functions to work with time-related operations, such as timekeeping, formatting, and time conversions


# The time.time() function returns the current time as a floating-point number, representing the number of seconds since the epoch (the point in time when the time module was initialized.(1st january , 1970)

def usingFor():
    for i in range(5000):
        i+=1
        print(i)
        
def usingWhile():
    i=0
    while i<5000:
        i+=1
        print(i)
import time    
t=time.time()
usingFor()
t1=time.time()-t

t0=time.time()
usingWhile()    
print(time.time()-t0)
print(t1)

# The time.sleep() function suspends the execution of the current thread for a specified number of seconds.

# The time.strftime() function formats a time value as a string, based on a specified format. This function is particularly useful for formatting dates and times in a human-readable format, such as for display in a GUI, a log file, or a report

import time
t=time.localtime()
formatted_time=time.strftime('%Y-%m-%d %H:%M:%S' ,t)
print(formatted_time)
