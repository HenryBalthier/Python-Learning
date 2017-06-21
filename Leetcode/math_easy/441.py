class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        m = 1
        sum = 1
        if n == 1 or n == 0:
            return n
        while sum <= n:
            sum = (1 + m) * m / 2
            print(sum)
            m += 1
        return m - 2


if __name__ == '__main__':
    s = Solution()
    n = 3
    print(s.arrangeCoins(n))