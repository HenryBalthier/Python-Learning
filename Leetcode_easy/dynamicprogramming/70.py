class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """

        a = b = 1
        for _ in range(n):
            a, b = b, a+b
            print(a)
        return a



if __name__ == '__main__':
    s = Solution()
    n = 2
    print(s.climbStairs(n))