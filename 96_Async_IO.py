# Asynchronous is a non-blocking architecture, so the execution of one task isn't dependent on another. Tasks can run simultaneously. 

# Synchronous is a blocking architecture, so the execution of each operation is dependent on the completion of the one before it. 

# say we have 2 functions func1 and func2. Now suppose func1 does something useful and then waits for some info from database or just sleeps for some time. So we dont want to waste the CPU time , so we start executing another function func2 till func1 returns.

# await keyword tells the function to finish execution. it is more like synchronous programming in asynchronous.

# task =asyncio.create_task(fn) it schedules the task whenever CPU gets some idle time.

import asyncio

async def func1():
    task=asyncio.create_task(func2())
    print('A')
    await asyncio.sleep(1)                 #coroutine 'sleep' was never awaited-Error without await.
    print('B \n')
async def func2():
    print(1)
    await asyncio.sleep(2)   
    print(2)
    
asyncio.run(func1())
 
#  In this func1 starts executing and prints 'A' when it finds 1 sec of idle time it runs the scheduled task i.e. func2 and prints '1' then it has to wait so it continues with func1 and prints B and terminates skipping the second statement of func2 i.e. '2'. 

# So if you want to execute the whole func2 write await task and write it at the right place.


async def func1():
    task=asyncio.create_task(func2())
    print('A')
    await asyncio.sleep(1)
    print('B')
    value_Returned= await task
    print(f'return_value is {value_Returned}')
async def func2():
    print(1)
    await asyncio.sleep(2)   
    print(2)
    return 10                                   #Returns the value when we await task.
asyncio.run(func1())

async def func3():
    print("a")
    await asyncio.sleep(1)
    print('b')
async def func4():
    print(1)
    await asyncio.sleep(2)
    print(2)
    
# async def main():
#     await func3()
#     await func4() 


async def main():                               #If we don't write task = asyncio.create_task(function)
 X=await asyncio.gather(func3() , func4())        
 
 print(X)
 
asyncio.run(main())

# a
# 1
# b
# 2
# [None, None]    Nothing returned.