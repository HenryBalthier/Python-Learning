import sys

def Judge(s0, s1):
    l0, l1 = s0.split(), s1.split()
    if s0 == 'joker JOKER':
        return 0
    if s1 == 'joker JOKER':
        return 1
    len0 = len(l0)
    len1 = len(l1)
    if len0 == 4 and len1 != 4:
        return 0
    elif len1 == 4 and len0 != 4:
        return 1
    elif len1 != len0:
        return -1
    else:
        d = {
            '3':1,
            '4':2,
            '5':3,
            '6':4,
            '7':5,
            '8':6,
            '9':7,
            '10':8,
            'J':9,
            'Q':10,
            'K':11,
            'A':12,
            '2':13
        }
        if d[l0[0]] > d[l1[0]]:
            return 0
        else:
            return 1

if __name__ == '__main__':
    s = sys.stdin.readline().strip()
    while s:
        ss = s.split('-')
        ans = Judge(ss[0], ss[1])
        if ans == -1:
            print('ERROR')
        else:
            print(ss[ans])

        s = sys.stdin.readline().strip()