import sys

def log(lst):
    for i in lst:
        s = i[0].split(' ')
        if len(s[0]) <= 16:
            print(i[0] + ' ' + str(i[1][0]))
        else:
            s[0] = s[0][-16:]
            print(s[0] + ' ' + s[1] + ' ' + str(i[1][0]))

if __name__ == '__main__':
    i = sys.stdin.readline().strip().split()
    d = {}
    count = 99999
    while i:
        filename = i[0].split('\\')[-1]
        line = i[1]
        hashtag = filename + ' ' + line
        d[hashtag] = [d.get(hashtag, [0, 0])[0] + 1, d.get(hashtag, [0, count])[1]]
        i = sys.stdin.readline().strip().split()
        count -= 1
    lst = sorted(d.items(), key=lambda x: (x[1][0], x[1][1]), reverse=True)
    if len(lst) > 8:
        log(lst[:8])
    else:
        log(lst)

