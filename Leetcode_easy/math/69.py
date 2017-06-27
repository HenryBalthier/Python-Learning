class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        return int(x ** 0.5)

if __name__ == '__main__':
    s = Solution()
    x = 4
    print(s.mySqrt(x))