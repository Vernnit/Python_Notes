# Function caching is a technique for improving the performance of a program by storing the results of a function call so that you can reuse the results instead of recomputing them every time the function is called. This can be particularly useful when a function is computationally expensive, or when the inputs to the function are unlikely to change frequently.

# functools.lru_cache decorator.

# The maxsize parameter is used to specify the maximum number of results to cache. If maxsize is set to None, the cache will have an unlimited size.

from functools import lru_cache
import time
@lru_cache(maxsize=None)
def sq(x):
    time.sleep(5)
    return x*x

print(sq(2))
print(sq(3))
print(sq(4))
print(sq(5))  #Takes 5 seconds each to get printed.


print(sq(2))
print(sq(3))
print(sq(4))
print(sq(5))  #Instantly gets printed.

# Only stores in current running program , every time the programme is run again cache is cleared.