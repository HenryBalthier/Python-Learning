import sys

def decode(string):
    L = ['F','G','R','S','T','L','M','N','O','P','Q','W','X','Y','Z','U','A','G','H',
         'I','J','K','B','C','D','E','l','m','n','o','p','i','j','k','f','g','h','a',
         'b','c','d','e','q','r','w','x','y','z','s','t','u','v']
    l = len(L)
    lst = string.split('#')
    res = ''
    for i in lst:
        if i:
            s = ''
            for j in i:
                if j == '-':
                    s += '0'
                elif j == '.':
                    s += '1'
                else:
                    print('ERROR')
                    return
            ss = int(s, 2)
            if 0 <= ss < l:
                res += L[ss]
            else:
                print('ERROR')
                return
    print(res)
    return

if __name__ == '__main__':
    n = sys.stdin.readline().strip()
    while n:
        decode(n)
        n = sys.stdin.readline().strip()