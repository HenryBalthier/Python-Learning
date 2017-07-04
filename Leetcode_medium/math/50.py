class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0:
            return 1

        def f(x, n):
            if n == 1:
                return x
            elif n % 2 == 0:
                tmp = f(x, n//2)
                return tmp * tmp
            else:
                tmp = f(x, (n-1)//2)
                return tmp * tmp * x
        res = f(x, abs(n))
        if n < 0:
            res = 1 / res
        return res


s = Solution()
x = 2
n = 5
print(s.myPow(x, n))