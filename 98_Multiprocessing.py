# Using the Older way
# using all cores of cpu parallelly for better performance of cpu bound tasks
# but here for understanding we will be using i/o bound task run parallelly
import multiprocessing
import time

t1 = time.perf_counter()


def do_something():
    print('process 1 started')
    time.sleep(2)
    print('process 1 terminated')


def do_something2():
    print('process 2 started')
    time.sleep(2)
    print('process 2 terminated')


if __name__ == '__main__':
    p1 = multiprocessing.Process(target=do_something)
    p2 = multiprocessing.Process(target=do_something2)

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    t2 = time.perf_counter()

    print(f'Time taken {round(t2-t1, 2)}')
    print('hello world')
print('it executes everytime a subprocess executes')

# in this main module code waits until complete execution of subprocesses, now subprocesses work by importing this main module again and ends up running every other code except included inside main . If name == main is not included  , main module would wait , then 1st subprocess would execute and import this module and again create 2 subprocesses further same 2nd one , and these 4 extra subprocesses would import module again and end up creating 16 subprocesses and this continues in a loop until your computer runs out of resources.
# Also anything outside the if name = main block will execute every time a subprocess execute as it imports the whole module. So it is better to protect your code by if name == main block to ensure this process spawning happens only once.
