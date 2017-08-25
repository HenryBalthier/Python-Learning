import sys

def func(Sum, a):
    a = [i for i in map(int, a)]
    a.sort()
    #print(a)
    count = []
    Sum = int(Sum)
    def search(Sum, a):
        #print(a)
        if a == []:
            return
        if Sum < a[0]:
            return
        for i, v in enumerate(a):
            if Sum == v:
                count.append(1)
            if Sum < v:
                break
            b = a[i:]
            b.remove(v)
            search(Sum-v, b)

    search(Sum, a)
    print(sum(count))

def func2(n, Sum, a):
    a = [i for i in map(int, a)]
    a.sort()
    count = 0
    Sum = int(Sum)
    n = int(n)
    d = [[0] * (Sum+1)]
    d[0][0] = 1

    for i in range(1, n+1):
        for j in range(Sum+1):
            if i >= len(d):
                d.append([0] * (Sum+1))
            d[i][j] = d[i-1][j]
            if j >=a[i-1]:
                d[i][j] += d[i-1][j-a[i-1]]
    print(d)
    print(d[n][Sum])



if __name__ == '__main__':
    n = sys.stdin.readline().strip().split(' ')
    while n:
        n = [i for i in filter(lambda x: x != '', n)]
        a = sys.stdin.readline().strip().split(' ')
        a = [i for i in filter(lambda x: x != '', a)]
        func2(n[0], n[1], a)

        n = sys.stdin.readline().strip()