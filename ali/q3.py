import sys

def func(n, m):
    lst = [[1] * n] * m
    try:
        for i in range(m):
            for j in range(n):
                if i > 0 and j > 0:
                    lst[i][j] = lst[i-1][j] + lst[i][j-1]
                elif i == 0 and j > 0:
                    lst[i][j] = lst[i][j-1]
                elif i > 0 and j == 0:
                    lst[i][j] = lst[i-1][j]
    except IndexError:
        print(i, j)
    print(lst[-1][-1])

if __name__ == '__main__':
    n = sys.stdin.readline().strip().split(' ')
    while n:
        func(int(n[0])+1, int(n[1])+1)
        n = sys.stdin.readline().strip().split(' ')
