class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        d = {}
        dd = {}
        for i in range(10):
            d[str(i)] = i * i
        flag = 2
        while(flag - 1):
            if dd.get(n, False):
                return False
            else:
                dd[n] = True

            sum = 0
            m = str(n)
            for i in m:
                sum += d[i]
            print(sum)
            flag = n = sum
        return True


if __name__ == '__main__':
    s = Solution()
    n = 20
    print(s.isHappy(n))