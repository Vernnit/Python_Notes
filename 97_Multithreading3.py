from concurrent.futures import ThreadPoolExecutor
import time

t1 = time.perf_counter()


def do_something(sec):
    print('started')
    time.sleep(sec)
    return 'terminated'


with ThreadPoolExecutor() as executor:
    # submit starts the execution of the function
    futureobject1 = executor.submit(do_something, 1)
    f2 = executor.submit(do_something, 2)
    f3 = executor.submit(do_something, 1)

# prints the return statement of the function , rest not printed .
print(f2.result())
# no need to write it though if there is no return statements , it waits until the all future objects are executed and returned (threads) and then continues further code. in short no need to write any kind of join() method in it .
t2 = time.perf_counter()

print(f'took {t2-t1} seconds')


# To loop over -
t3 = time.perf_counter()

secs = [5, 4, 3, 2, 1]
with ThreadPoolExecutor() as executor:
    results = [executor.submit(do_something, sec) for sec in secs]
for f in results:
    print(f.result())

t4 = time.perf_counter()

print(f'time taken is {t4-t3}')


# Use map
t5 = time.perf_counter()
with ThreadPoolExecutor() as executor:
    results = executor.map(do_something, secs)
    print(results)
for f in results:
    print(f)


t6 = time.perf_counter()

print({t6-t5})
# use concurrent.futures.as_completed(results) print f.result() to print results in the order they were completed.
