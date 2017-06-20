class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = 0
        while n:
            m = n//5
            res += m
            n = m
        return res


if __name__ == '__main__':
    s = Solution()
    n = 25
    print(n//5)
    sum = 1
    for i in range(n):
        sum *= (i+1)
    print(sum)
    print(s.trailingZeroes(n))