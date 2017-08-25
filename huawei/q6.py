import sys

def helper(n, count):
    if n == 0 or n == 1:
        return count
    if n == 2:
        return count + 1
    if n >= 3:
        a = n // 3 + n % 3

        count = helper(a, count + n // 3)
    return count

if __name__ == '__main__':
    i = sys.stdin.readline().strip()
    while i != '0' and i:
        print(helper(int(i), 0))
        i = sys.stdin.readline().strip()
