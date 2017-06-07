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


class Screen(object):
    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height

    @property
    def resolution(self):
        return self._width * self._height

    @width.setter
    def width(self, value):
        self._width = value

    @height.setter
    def height(self, value):
        self._height = value

if __name__ == '__main__':
    s = Screen()
    s.width = 1024
    s.height = 768
    print(s.resolution)
    assert s.resolution == 786432, '1024 * 768 = %d ?' % s.resolution
