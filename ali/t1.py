import sys

def func(a, b):
    if d.get(a, None) is None:
        d[a] = b
        dd[b] = 1
    else:
        if d[a] > b:
            d[a], dd[b] = b, dd[d[a]] + 1
        else:
            dd[d[a]] += 1

def result(d, dd):
    min = 0
    v = 0
    for i in dd:
        if dd[i] > min:
            min = dd[i]
            v = i
        elif dd[i] == min and i > v:
            min = dd[i]
            v = i

    for j in d:
        if d[j] == v:
            print('(%d, %d+%d, %d)' % (j, j, v, min))
            return


if __name__ == '__main__':
    n = sys.stdin.readline().strip()
    d = {}
    dd = {}
    while n:
        a = n.split('，')[0][1:]
        b = n.split('，')[1][:-1]
        #print(a, b)
        if 'KB' in b:
            b = int(b[:-2]) * 1024
        elif 'MB' in b:
            b = int(b[:-2]) * 1024 * 1024
        a = int(a)
        func(a, b)
        n = sys.stdin.readline().strip()
    result(d, dd)
