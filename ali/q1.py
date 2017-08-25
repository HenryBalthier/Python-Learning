import sys

def func():
    pass


if __name__ == '__main__':
    n = sys.stdin.readline().strip()
    while n:
        n = int(n)
        a = sys.stdin.readline().strip().split(' ')
        b = sys.stdin.readline().strip().split(' ')
        c = []
        for i in range(n):
            c.append(int(a[i]) + int(b[i]) - 2)
        print(min(c))
        n = sys.stdin.readline().strip()