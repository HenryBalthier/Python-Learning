class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        sum = 0
        for i in s:
            sum = sum * 26 + (ord(i)-64)
        return sum


if __name__ == '__main__':
    s = Solution()
    x = 'AA'
    print(s.titleToNumber(x))