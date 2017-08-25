import sys

def count(a):
    l = len(a)
    p = 0
    c = 0
    while l > 1:
        if p < l:
            if c < 2:
                c += 1
                p += 1
                continue
            else: # c >=2
                c = 0
                a[p] = -1
                p += 1
        else: # p == l
            p = 0
            while -1 in a:
                a.remove(-1)
            l = len(a)
    return a[0]

if __name__ == '__main__':
    i = sys.stdin.readline().strip()
    if int(i) > 1000:
        i = '1000'
    while i:
        a = [x for x in range(int(i))]
        print(count(a))

        i = sys.stdin.readline().strip()
