from time import sleep, clock
import threading
import multiprocessing
import random
import os

def loop(number):
    print('start loop No.%d' % number)
    print('Parent process %s.' % os.getpid())
    sleep(number)
    print('end loop No,%d, sleep %d seconds' % (number, number))

def computer(number):
    print('start computer No.%d' % number)
    print('Parent process %s.' % os.getpid())
    res = sum([random.randint(1, 100) for i in range(1000000)])
    print('end computer No,%d, result = %d' % (number, res))

def Single(func, nums):
    start = clock()
    for i in range(nums):
        func(i)
    end = clock()
    print('Single run cost: %.2f s\n' % (end - start))

def Multithread(func, nums):
    start = clock()
    threads = []
    for i in range(nums):
        t = threading.Thread(target=func, args=(i, ))
        threads.append(t)
    for i in range(nums):
        threads[i].start()

    for i in range(nums):
        threads[i].join()
    end = clock()
    print('MultiThread run cost: %.2f s\n' % (end - start))

def Multiprocessing(func, nums):
    start = clock()
    pool = multiprocessing.Pool(nums)
    #pool.map(func, range(nums))
    for i in range(nums):
        pool.apply_async(func, args=(i, ))
    pool.close()
    pool.join()
    end = clock()
    print('MultiProcessing run cost: %.2f s\n' % (end - start))

if __name__ == '__main__':
    #f = loop
    f = computer
    #Single(f, 5)
    Multithread(f, 5)
    Multiprocessing(f, 5)
