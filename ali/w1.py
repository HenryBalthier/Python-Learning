import sys
import re

def checklen(n, m):
    l = len(n)
    if l > 20-m:
        return 20-m - l
    if l < 8-m:
        return 8-m - l
    else:
        return 0

def checkupper(n):
    patten = re.compile(r'[A-Z]+')
    if patten.findall(n):
        return 0
    else:
        return 1

def checklower(n):
    patten = re.compile(r'[a-z]+')
    if patten.findall(n):
        return 0
    else:
        return 1

def checkdigit(n):
    patten = re.compile(r'[0-9]+')
    if patten.findall(n):
        return 0
    else:
        return 1

def checksim(n):
    count = 0
    d = {}
    for i in n:
        d[i] = d.get(i, 0) + 1
    for i in d:
        if d[i] >= 3:
            count += d[i] - 2
    return count * -1


def func(n):
    num = checkupper(n) + checklower(n) + checkdigit(n)
    sim = checksim(n)
    res = abs(sim) + num
    count = sim + num
    len = checklen(n, count)
    # print('len = %d, num = %d, sim = %d' % (len, num, sim))
    res += len
    return str(res)

if __name__ == '__main__':
    n = sys.stdin.readline().strip()
    while n:
        #print(func(n))
        sys.stdout.write(func(n)+'\n')
        n = sys.stdin.readline().strip()
