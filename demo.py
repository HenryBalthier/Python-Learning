import sys
import re

def splitest():
    s = r'1    2   , 3   '
    #lst = re.split('\s+', s)
    lst = s.split(' ')
    lst = [item for item in filter(lambda x: x != '' and x != ',', lst)]
    print(lst)


if __name__ == '__main__':
    splitest()