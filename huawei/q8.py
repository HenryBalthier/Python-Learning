import sys

s = 'F'
print(int(s, 16))

if __name__ == '__main__':
    sys.stdin.readline().strip()
    while s:
        print(int(s, 16))
        s = sys.stdin.readline().strip()
