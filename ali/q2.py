import sys

def fib(n):
    lst = [0, 1, 1]
    fib = [0, 1, 1]
    i = 3
    Min = 0
    if n == 0 or n == 1 or n == 2:
        print(0)
        return
    while fib[-1] < n:
        lst[i%3] = lst[(i+1)%3] + lst[(i+2)%3]
        fib.append(lst[i%3])
        i += 1
        Min = n - fib[-2]
    Min = min(Min, fib[-1]-n)
    print(lst, fib)
    print(Min)

if __name__ == '__main__':
    n = sys.stdin.readline().strip()
    while n:
        n = int(n)
        fib(n)
        n = sys.stdin.readline().strip()