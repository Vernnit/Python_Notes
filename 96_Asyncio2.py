import asyncio
import time
t1 = time.perf_counter()


async def do_something():
    print('task 1 started')
    await asyncio.sleep(2)
    print('task 1 terminated')


async def do_something2():
    print('task 2 started ')
    await asyncio.sleep(1)
    print('task 2 terminated ')


async def main():  # we need to create this func bcz we are compelled to await all coroutines and it can only be awaited within a async function
    await asyncio.gather(do_something(), do_something2())

asyncio.run(main())
t2 = time.perf_counter()

print(f'{round(t2-t1, 2)}')

# To actually run a coroutine, asyncio provides the following mechanisms:
# The asyncio.run() function to run the top-level entry point “main()” function

# firstly coroutine 1 executed prints task 1 starts and it paused its further execution until it is ready(2sec) , processor got freed , so it jumped to next coroutine and started it and then again paused its further execution until its ready(1s) , 1 sec elapsed now coroutine 2 was ready so it resumed and printed task2 terminated , then 2secs elapsed and 1st one also got resumed and printed task 1 terminated. overall time taken for complete execution ~ 2 sec.

# NOTE : while waiting for something means processor is not doing any work it is just waiting so no execution is taking place in background , .


# pausing a function means until it completes waiting , pause further execution , and once it is ready resume it , and in the mean time move on to another coroutine . And using await at last when running these coroutines i.e awaiting coroutines means wait until these gets executed and then only resume with further script i.e rest of the code here calculating time and printing it .

# await thing means "hey asyncio, wake me up when thing evaluates". In the meantime it may run other coroutines.
