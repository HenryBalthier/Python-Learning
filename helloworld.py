def test():
    s1 = 72
    s2 = 85
    r = 100 * (s2 - s1) / s1
    print('%.1f%%' % r)


def inputio():
    s = input('your selection:')
    if isinstance(s, int):
        print('int!')
    else:
        print('no int!')


def move(n=3, a='A', b='B', c='C'):
    # 汉诺塔
    if n == 1:
        print(a, '-->', c)
        return
    move(n-1, a, c, b)
    move(1, a, b, c)
    move(n-1, b, a, c)


def log(func):
    import functools
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('begin call:')
        return func(*args, **kw), print('end call:')
    return wrapper


@log
def prtdate():
    print('2017-6-6')

if __name__ == '__main__':
    prtdate()
