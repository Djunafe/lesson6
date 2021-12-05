import time
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
import math


def fac_for(n):
    factorial = 1
    for i in range(2, n+1):
        factorial *= 1
    return factorial


def fac_while(n):
    factorial = 1
    while n > 1:
        factorial *= n
        n -= 1
    return factorial


def fac_math(n):
    return math.factorial(n)


def fan_executor1(executor_class, max_workers=4):
    executor = executor_class(max_workers=max_workers)
    started = time.time()
    executor.submit(fac_for(100000))
    print('Time for {executor}: {spent_time}'.format(
        executor=executor_class.__name__,
        spent_time=time.time() - started
    ))


def fan_executor2(executor_class, max_workers=4):
    executor = executor_class(max_workers=max_workers)
    started = time.time()
    executor.submit(fac_while(100000))
    print('Time for {executor}: {spent_time}'.format(
        executor=executor_class.__name__,
        spent_time=time.time() - started
    ))


def fan_executor3(executor_class, max_workers=4):
    executor = executor_class(max_workers=max_workers)
    started = time.time()
    executor.submit(fac_math(100000))
    print('Time for {executor}: {spent_time}'.format(
        executor=executor_class.__name__,
        spent_time=time.time() - started
    ))


if __name__ == '__main__':
    print('Factorial by using cycle ( for ) :')
    fan_executor1(ThreadPoolExecutor)
    fan_executor1(ProcessPoolExecutor)
    print('Factorial by using cycle ( while ) :')
    fan_executor2(ThreadPoolExecutor)
    fan_executor2(ProcessPoolExecutor)
    print('Factorial by using module ( math ) :')
    fan_executor3(ThreadPoolExecutor)
    fan_executor3(ProcessPoolExecutor)
