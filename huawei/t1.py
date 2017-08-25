import sys

if __name__ == '__main__':
    count = 0
    res = 0
    for i in range(100, 1000):
        s = str(i)
        SUM = int(s[0]) ** 3 + int(s[1]) ** 3 + int(s[2]) ** 3
        if i == SUM:
            count += 1
            print('第%d个水仙花数: %d' % (count, i))
            res += i
    sys.stdout.write('水仙花数总和为: %d' % res)
