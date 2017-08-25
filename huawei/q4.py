import sys

def helper(string):
    s = ''
    for i in string:
        if i not in s:
            s += i
    print(s)

if __name__ == '__main__':
    i = sys.stdin.readline().strip()
    while i:
        helper(i)
        i = sys.stdin.readline().strip()
