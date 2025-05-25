# manual way


import time
import threading
start = time.perf_counter()


def do_something():
    print('thread 1 runs')
    time.sleep(1)
    print('thread 1 terminates')


def do_something2():
    print('thread 2 runs')
    time.sleep(1)
    print('thread 2 terminates')


# give function name as argument not call function inside argument o/w it runs synchronously.
t1 = threading.Thread(target=do_something)
t2 = threading.Thread(target=do_something2)

t1.start()
t2.start()

t1.join()
t2.join()

finish = time.perf_counter()

print(f'Finished in {round(finish-start, 10)} second(s)')
