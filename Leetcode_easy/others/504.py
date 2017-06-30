class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        f = True
        if num == 0:
            return '0'
        if num < 0:
            num = abs(num)
            f = False
        s = ''
        while num:
            s = str(num % 7) + s
            num = num // 7
        return s if f else '-' + s

s = Solution()
x = -7
print(s.convertToBase7(x))