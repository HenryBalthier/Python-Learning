import sys

if __name__ == '__main__':
    n = sys.stdin.readline().strip()
    while n:
        lst = []
        for i in range(int(n)):
            num = int(sys.stdin.readline().strip())
            if num not in lst:
                lst.append(num)
        l = sorted(lst)
        for i in l:
            print(i)

        n = sys.stdin.readline().strip()
