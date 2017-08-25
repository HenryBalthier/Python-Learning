import sys

def search(d, f1, f2):
    lst = d[f1]
    for i in lst:
        if i in d:
            for j in d[i]:
                if j not in lst:
                    lst.append(j)
    if f2 in lst:
        return True
    else:
        return False

def func(n, s):
    d = {}
    A = s[-1].split()[0]
    B = s[-1].split()[1]
    #print(A, B)
    for i in range(n):
        f1 = s[i].split()[0]
        f2 = s[i].split()[1]
        d[f1] = d.get(f1, []) + [f2]
    #print(d)
    if A not in d or B not in d:
        print('F')
        return
    if search(d, A, B) and search(d, B, A):
        print('T')
    else:
        print('F')
    return

if __name__ == '__main__':
    n = sys.stdin.readline().strip()
    while n:
        s = []
        for i in range(int(n)+1):
            m = sys.stdin.readline().strip()
            s.append(m)
        #print(s)
        func(int(n), s)
        n = sys.stdin.readline().strip()