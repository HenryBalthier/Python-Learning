class Solution(object):
    def rangeBitwiseAnd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        import math
        if m == 0:
            return 0

        if m == n:
            return n

        if int(math.log(m, 2)) < int(math.log(n, 2)):
            return 0
        res = m
        for i in range(m,n+1):
            res &= i
        return res


s = Solution()
m = 0
n = 0

print(s.rangeBitwiseAnd(m, n))