# Multithreading is a technique in programming that allows multiple threads of execution to run concurrently within a single process. In Python, we can use the threading module to implement multithreading.

# To create a thread, we need to create a Thread object and then call its start() method. The start() method runs the thread and then to stop the execution, we use the join() method.

# The following are some of the most commonly used functions in the threading module:

# threading.Thread(target, args): This function creates a new thread that runs the target function with the specified arguments.

# threading.Lock(): This function creates a lock that can be used to synchronize access to shared resources between threads.


import threading
import time
def func(x):
    print(f'stopping for {x} seconds')
    time.sleep(x)
    return x

tm1=time.perf_counter()
#Normal Code 
# func(4)
# func(3)
# func(1)
# tm2=time.perf_counter()
# print(tm2-tm1)

t1=threading.Thread(target=func, args=[4])
t2=threading.Thread(target=func, args=[3])
t3=threading.Thread(target=func, args=[1])

t1.start()             #starts the function and runs in bg.
t2.start()
t3.start()

# To wait for the function to complete.
t1.join()
t2.join()
t3.join()

tm2=time.perf_counter()
print(tm2-tm1)


from concurrent.futures import ThreadPoolExecutor

def Threadpool_demo():
    with ThreadPoolExecutor() as executor:
        l=[9,8,7,6,5,4,3,2,1]
        results=executor.map(func , l)
        for result in results:
            print(result)
        
Threadpool_demo()






'''
Using a lock to synchronize access to shared resources -

When working with multithreading in python, locks can be used to synchronize access to shared resources among multiple threads. A lock is an object that acts as a semaphore, allowing only one thread at a time to execute a critical section of code. The lock is released when the thread finishes executing the critical section.'''

# import threading
# def increment(counter, lock):
#     for i in range(10000):
#         lock.acquire()
#         counter += 1
#         lock.release()
# if __name__ == '__main__':
#     counter = 0
#     lock = threading.Lock()
#     threads = []
#     for i in range(2):
#         thread = threading.Thread(target=increment, args=(counter, lock))
#         threads.append(thread)
#         thread.start()
#     for thread in threads:
#         thread.join()
#     print("Counter value:", counter)