class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """

        while n > 1:
            if n % 2 == 1:
                return False
            else:
                n = n // 2
        return n == 1

if __name__ == '__main__':
    s = Solution()
    x = 10
    print(s.isPowerOfTwo(x))