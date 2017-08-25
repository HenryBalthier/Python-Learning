import sys

if __name__ == '__main__':
    n = sys.stdin.readline().strip()
    while n:
        s = ''
        for i in n:
            if 'a' <= i <= 'z':
                s += i
            elif 'A' <= i <= 'Z':
                ss = ord(i) - ord('A') + ord('a')
                s += chr(ss)

        print(s)

        n = sys.stdin.readline().strip()
