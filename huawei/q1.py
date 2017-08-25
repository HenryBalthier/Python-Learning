import sys


def stdinput(n, m):
    lst = sys.stdin.readline().strip().split()
    assert len(lst) == n
    lst = list(map(int, lst))
    for i in range(m):
        line = sys.stdin.readline().strip().split()
        if line[0] == 'Q':
            l = min(int(line[1]), int(line[2]))
            r = max(int(line[1]), int(line[2]))
            print(max(lst[l-1: r]))
        elif line[0] == 'U':
            lst[int(line[1])-1] = int(line[2])


if __name__ == '__main__':
    i = sys.stdin.readline().strip().split()
    while i:
        n, m = int(i[0]), int(i[1])
        stdinput(n, m)
        i = sys.stdin.readline().strip().split()

