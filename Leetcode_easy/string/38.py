class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 1:
            return '1'
        s = '1'
        res = ''
        pre = ''
        precount = 0
        while n > 1:
            for i in s:
                if pre == i:
                    precount += 1
                else:
                    if precount != 0:
                        res = res + str(precount) + pre
                        pre = i
                        precount = 1
                    else:
                        pre = i
                        precount += 1
            if precount != 0:
                res = res + str(precount) + pre
            n -= 1
            s = res
            print('s = %s' % s)
            res = ''
            pre = ''
            precount = 0
        return s


if __name__ == '__main__':
    s = Solution()
    x = 5
    print(s.countAndSay(x))