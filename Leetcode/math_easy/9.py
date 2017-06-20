class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x = str(x)
        return x == x[::-1]


if __name__ == '__main__':
    s = Solution()
    x = 12321
    print(s.isPalindrome(x))