class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        s = bin(num)[2:]
        print(s)
        res = ''
        for i in s:
            res += '0' if int(i) else '1'
        return int('0b' + res, 2)

s = Solution()
x = 5
print(s.findComplement(x))