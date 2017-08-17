from multiprocessing import Process, Array

def test(a):
    for i in range(len(a)):
        a[i] = -a[i]

if __name__ == '__main__':
    arr = Array('i', range(10))
    p = Process(target=test, args=(arr, ))  #需要将arr对象传递给子进程
    p.start()
    p.join()
    print(arr[:])

