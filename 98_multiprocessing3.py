# Using iterables

import concurrent.futures as cf
import time
t1 = time.perf_counter()


def do_something(sec):
    print(f'process starts for {sec} seconds')
    time.sleep(sec)
    return f'process terminated for {sec} seconds'


secs = [5, 4, 3, 2, 1]
if __name__ == '__main__':
    with cf.ProcessPoolExecutor() as executor:
        # results = [executor.submit(do_something, sec) for sec in secs]

        # for f in cf.as_completed(results):
        #     print(f.result())

        # t2 = time.perf_counter()
        # print(f'time taken is {t2-t1: .2f} secs')

        # or

        t3 = time.perf_counter()
        results2 = executor.map(do_something, secs)
        for f in results2:
            print(f)

        t4 = time.perf_counter()

        print(f'time taken is {t4-t3: .2f}')


# map does not wrap results in future objects. Also it returns the results in the order they were given to map. It just returns the values returned from function which operate on iterable in form of a list.

# while in case of using list comprehension for submit , it returns future object on which we can apply as_completed method and iterate over them.
