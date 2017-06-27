class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 0 or n == 2:
            return False
        while n % 3 == 0:
            n = n // 3
            print(n)
        return n == 1


if __name__ == '__main__':
    s = Solution()
    x = 1
    print(s.isPowerOfThree(x))