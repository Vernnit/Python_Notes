# using ProcessPoolExecutor
# better and efficient

import concurrent.futures as cf
import time

t1 = time.perf_counter()


def do_something(sec):
    print('Process 1 starts')
    time.sleep(sec)
    print(f'process 1 completed using {sec} as argument')
    return 'return statement of process 1'


def do_something2(sec):
    print('Process 2 starts')
    time.sleep(sec)
    print(f'process 2 completed using {sec} as argument')
    return 'return statement of process 2'


if __name__ == '__main__':
    with cf.ProcessPoolExecutor() as executor:
        f1 = executor.submit(do_something, 2)
        f2 = executor.submit(do_something2, 2)
        print(f1.result())
        print(f2.result())

    t2 = time.perf_counter()

    print(f'completed in {t2-t1: .3f} secs')

# both runs parallelly and finish in ~2secs
