import sys

def Count(num):
    count = 0
    while num >= 5 and num % 5 == 0:
        num /= 5
        count += 1
    return count


def func(n):
    count = 0
    for i in range(1, n+1):
        if i % 5 == 0:
            count += Count(i)
    print(count)

if __name__ == '__main__':
    n = sys.stdin.readline().strip()
    while n:
        n = int(n)
        func(n)
        n = sys.stdin.readline().strip()