import sys

def dfs(row, col):
    for i in range(9):
        for j in range(9):
            pass

if __name__ == '__main__':
    lst = [[] for i in range(9)]
    print(lst)
    for i in range(9):
        lst[i] = sys.stdin.readline().strip().split()

    row = lst
    col = list(zip(*lst))
    print(row, '\n', col)